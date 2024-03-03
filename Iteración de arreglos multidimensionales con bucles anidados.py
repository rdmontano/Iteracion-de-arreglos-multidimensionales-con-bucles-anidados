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

# Calcular el promedio de temperaturas para cada ciudad por semana
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for semana_idx in range(semanas):
        promedio_semana = sum(temperaturas[ciudad_idx][semana_idx]) / len(temperaturas[ciudad_idx][semana_idx])
        print(f"Semana {semana_idx + 1}:")
        for dia_idx, dia in enumerate(dias_semana):
            print(f"{dia}: {temperaturas[ciudad_idx][semana_idx][dia_idx]}°C")
        print(f"Promedio semana {semana_idx + 1}: {promedio_semana}°C")
    print()
