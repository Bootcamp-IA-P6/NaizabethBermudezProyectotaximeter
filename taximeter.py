import time

def calculate_fare(seconds_stopped, seconds_moving):
    """
    Calcular la tarifa total en euros.
    - Stopped: 0.02 €/s
    - Moving: 0.05 €/s
    """
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    print(f"Este es el total: {fare}")
    return fare

def taximeter():
    """
    Función para manejar y mostrar las opciones del taxímetro.
    """
    print("Welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")