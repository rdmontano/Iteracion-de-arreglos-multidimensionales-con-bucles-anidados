def calcular_temperatura_promedio(ciudades, dias_semana, semanas, temperaturas):
    """
    Calcula y muestra el promedio de temperaturas para cada ciudad durante un período de tiempo.

    Args:
    - ciudades (list): Lista de nombres de ciudades.
    - dias_semana (list): Lista de nombres de días de la semana.
    - semanas (int): Número de semanas.
    - temperaturas (list): Lista 3D que almacena las temperaturas por ciudad, semana y día.

    Returns:
    None
    """

    # Itera sobre cada ciudad
    for ciudad_idx, ciudad in enumerate(ciudades):
        print(f"Promedio de temperaturas para {ciudad}:")
        # Itera sobre cada semana
        for semana_idx in range(semanas):
            # Calcula el promedio de temperaturas para la semana actual de la ciudad actual
            promedio_semana = sum(temperaturas[ciudad_idx][semana_idx]) / len(temperaturas[ciudad_idx][semana_idx])
            print(f"Semana {semana_idx + 1}:")
            # Itera sobre cada día de la semana actual
            for dia_idx, dia in enumerate(dias_semana):
                # Imprime la temperatura del día actual
                print(f"{dia}: {temperaturas[ciudad_idx][semana_idx][dia_idx]}°C")
            # Imprime el promedio de la semana actual
            print(f"Promedio semana {semana_idx + 1}: {promedio_semana}°C")
        print()

# Definir las ciudades, días de la semana y semanas
ciudades = ["Esmeraldas", "Guayaquil", "Quito"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear la matriz 3D para almacenar las temperaturas
temperaturas = [
    [ # Esmeraldas
        [30, 32, 28, 29, 31, 30, 33], # Semana 1
        [31, 33, 29, 30, 32, 31, 34], # Semana 2
        [29, 31, 27, 28, 30, 29, 32], # Semana 3
        [32, 34, 30, 31, 33, 32, 35]  # Semana 4
    ],
    [ # Guayaquil
        [28, 30, 26, 27, 29, 28, 31], # Semana 1
        [29, 31, 27, 28, 30, 29, 32], # Semana 2
        [27, 29, 25, 26, 28, 27, 30], # Semana 3
        [30, 32, 28, 29, 31, 30, 33]  # Semana 4
    ],
    [ # Quito
        [25, 27, 23, 24, 26, 25, 28], # Semana 1
        [26, 28, 24, 25, 27, 26, 29], # Semana 2
        [24, 26, 22, 23, 25, 24, 27], # Semana 3
        [27, 29, 25, 26, 28, 27, 30]  # Semana 4
    ]
]

# Llamar a la función para calcular y mostrar los promedios de temperatura
calcular_temperatura_promedio(ciudades, dias_semana, semanas, temperaturas)
