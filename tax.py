import tkinter as tk
from tkinter import messagebox
import time
import sqlite3

# ==============================================
# Trip Model
# ==============================================
class Trip:
    def __init__(self, stopped_rate=0.02, moving_rate=0.05):
        self.stopped_rate = stopped_rate
        self.moving_rate = moving_rate
        self.start_time = time.time()
        self.stopped_time = 0.0
        self.moving_time = 0.0
        self.state = "stopped"
        self.state_start_time = time.time()

    def change_state(self, new_state):
        now = time.time()
        elapsed = now - self.state_start_time
        if self.state == "stopped":
            self.stopped_time += elapsed
        else:
            self.moving_time += elapsed
        self.state = new_state
        self.state_start_time = now
        return elapsed

    def finish(self):
        now = time.time()
        elapsed = now - self.state_start_time
        if self.state == "stopped":
            self.stopped_time += elapsed
        else:
            self.moving_time += elapsed
        return self.calculate_fare()

    def calculate_fare(self):
        return self.stopped_time * self.stopped_rate + self.moving_time * self.moving_rate

    def to_dict(self):
        return {
            "start_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start_time)),
            "stopped_time": self.stopped_time,
            "moving_time": self.moving_time,
            "total_fare": self.calculate_fare()
        }

# ==============================================
# SQLite DB
# ==============================================
class TripDB:
    def __init__(self, db_name="trips.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time TEXT,
                stopped_time REAL,
                moving_time REAL,
                total_fare REAL
            )
        """)
        self.conn.commit()

    def save_trip(self, trip):
        data = trip.to_dict()
        self.cursor.execute("""
            INSERT INTO trips (start_time, stopped_time, moving_time, total_fare)
            VALUES (?, ?, ?, ?)
        """, (data['start_time'], data['stopped_time'], data['moving_time'], data['total_fare']))
        self.conn.commit()

    def get_all_trips(self):
        self.cursor.execute("SELECT start_time, total_fare FROM trips ORDER BY id DESC")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# ==============================================
# Taximeter GUI
# ==============================================
class TaximeterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxímetro F5")
        self.root.geometry("520x600")
        self.root.configure(bg="#f0f2f5")

        self.trip = None
        self.db = TripDB()  # Conexión a SQLite

        # Widgets principales
        self.title_label = tk.Label(root, text="Taxímetro F5", font=("Helvetica", 20, "bold"), bg="#f0f2f5", fg="#333")
        self.title_label.pack(pady=15)

        self.state_label = tk.Label(root, text="Estado: (sin viaje)", font=("Helvetica", 14), bg="#f0f2f5")
        self.state_label.pack(pady=5)

        self.fare_label = tk.Label(root, text="Tarifa total: €0.00", font=("Helvetica", 14), bg="#f0f2f5")
        self.fare_label.pack(pady=5)

        self.time_label = tk.Label(root, text="Tiempo detenido: 0s | Movimiento: 0s", font=("Helvetica", 12), bg="#f0f2f5")
        self.time_label.pack(pady=5)

        # Botones estilizados
        button_color = "#4a90e2"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")

        self.start_button = tk.Button(root, text="Start Trip", width=12, bg=button_color, fg=button_fg,
                                      font=button_font, relief="ridge", command=self.start_trip)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(root, text="Stop", width=12, bg=button_color, fg=button_fg,
                                     font=button_font, relief="ridge", state="disabled", command=self.set_stopped)
        self.stop_button.pack(pady=5)
        self.move_button = tk.Button(root, text="Move", width=12, bg=button_color, fg=button_fg,
                                     font=button_font, relief="ridge", state="disabled", command=self.set_moving)
        self.move_button.pack(pady=5)
        self.finish_button = tk.Button(root, text="Finish Trip", width=12, bg=button_color, fg=button_fg,
                                       font=button_font, relief="ridge", state="disabled", command=self.finish_trip)
        self.finish_button.pack(pady=5)

        # Botón para cerrar y volver al login
        self.close_button = tk.Button(root, text="Cerrar programa", width=15, bg="#e74c3c", fg="white",
                                      font=("Helvetica", 12, "bold"), relief="ridge", command=self.close_program)
        self.close_button.pack(pady=10)

        # -----------------------------------------------
        # Listbox para mostrar viajes con scroll
        # -----------------------------------------------
        self.trips_frame = tk.Frame(root, bd=2, relief="groove", bg="#ffffff")
        self.trips_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título dentro del frame
        self.trips_title_label = tk.Label(self.trips_frame, text="Registro de viajes", font=("Helvetica", 14, "bold"), bg="#ffffff")
        self.trips_title_label.pack(pady=(10, 5))

        # Frame interno para Listbox + Scrollbar
        self.listbox_frame = tk.Frame(self.trips_frame, bg="#ffffff")
        self.listbox_frame.pack(pady=(0, 10), padx=10, fill="both", expand=True)

        # Listbox
        self.trips_listbox = tk.Listbox(
            self.listbox_frame,
            font=("Helvetica", 12),
            bg="#f9f9f9",
            fg="#333",
            selectbackground="#4a90e2",
            selectforeground="white",
            borderwidth=0,
            highlightthickness=0
        )
        self.trips_listbox.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical", command=self.trips_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.trips_listbox.config(yscrollcommand=self.scrollbar.set)

        # Cargar datos iniciales
        self.load_trips_listbox()

        # Loop de actualización
        self.update_loop()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ------------------------------------------------------
    # Funciones del taxímetro
    # ------------------------------------------------------
    def start_trip(self):
        if self.trip:
            messagebox.showerror("Error", "Ya hay un viaje en curso.")
            return
        self.trip = Trip()
        self.state_label.config(text="Estado: detenido")
        self.stop_button.config(state="normal")
        self.move_button.config(state="normal")
        self.finish_button.config(state="normal")

    def set_stopped(self):
        if self.trip:
            self.trip.change_state("stopped")
            self.state_label.config(text="Estado: detenido")

    def set_moving(self):
        if self.trip:
            self.trip.change_state("moving")
            self.state_label.config(text="Estado: en movimiento")

    def finish_trip(self):
        if not self.trip:
            return
        total_fare = self.trip.finish()
        self.db.save_trip(self.trip)
        self.trip = None
        self.state_label.config(text="Estado: (sin viaje)")
        self.fare_label.config(text="Tarifa total: €0.00")
        self.time_label.config(text="Tiempo detenido: 0s | Movimiento: 0s")
        self.stop_button.config(state="disabled")
        self.move_button.config(state="disabled")
        self.finish_button.config(state="disabled")
        self.load_trips_listbox()

    def update_loop(self):
        if self.trip:
            fare = self.trip.calculate_fare()
            self.fare_label.config(text=f"Tarifa total: €{fare:.2f}")
            self.time_label.config(
                text=f"Tiempo detenido: {int(self.trip.stopped_time)}s | "
                     f"Movimiento: {int(self.trip.moving_time)}s"
            )
        self.root.after(1000, self.update_loop)

    def load_trips_listbox(self):
        self.trips_listbox.delete(0, tk.END)
        trips = self.db.get_all_trips()
        for t in trips:
            self.trips_listbox.insert(tk.END, f"{t[0]} -> €{t[1]:.2f}")

    def close_program(self):
        """Cierra el taxímetro y vuelve al login"""
        self.db.close()
        self.root.destroy()
        login_root.deiconify()

    def on_closing(self):
        self.db.close()
        self.root.destroy()
        login_root.destroy()

# ==============================================
# Login GUI
# ==============================================
class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login - Taxímetro F5")
        self.master.geometry("450x300")
        self.master.configure(bg="#d0e6f5")

        tk.Label(master, text="Bienvenido al Taxímetro F5", font=("Helvetica", 14, "bold"), bg="#d0e6f5").pack(pady=10)
        tk.Label(master, text="Usuario:", bg="#d0e6f5").pack()
        self.user_entry = tk.Entry(master)
        self.user_entry.pack(pady=5)

        tk.Label(master, text="Contraseña:", bg="#d0e6f5").pack()
        self.pass_entry = tk.Entry(master, show="*")
        self.pass_entry.pack(pady=5)

        self.login_button = tk.Button(master, text="Iniciar sesión", bg="#4a90e2", fg="white",
                                      font=("Helvetica", 12, "bold"), width=15, command=self.authenticate)
        self.login_button.pack(pady=10)

        self.master.bind('<Return>', lambda event: self.authenticate())

    def authenticate(self):
        USER = "admin"
        PASSWORD = "1234"
        username = self.user_entry.get()
        password = self.pass_entry.get()
        if username == USER and password == PASSWORD:
            open_taximeter_window(self.master)
            self.master.withdraw()
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")

def open_taximeter_window(master):
    taximeter_window = tk.Toplevel(master)
    app = TaximeterGUI(taximeter_window)

# ==============================================
# Main
# ==============================================
if __name__ == "__main__":
    login_root = tk.Tk()
    login_app = LoginWindow(login_root)
    login_root.mainloop()
