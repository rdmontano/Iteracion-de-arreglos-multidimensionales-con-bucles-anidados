class RegistroTemperaturas:
    def __init__(self):
        self.registro = {}

    def agregar_temperatura(self, ciudad, fecha, temperatura):
        if ciudad not in self.registro:
            self.registro[ciudad] = {}

        if fecha not in self.registro[ciudad]:
            self.registro[ciudad][fecha] = []

        self.registro[ciudad][fecha].append(temperatura)

    def obtener_temperaturas_ciudad_fecha(self, ciudad, fecha):
        if ciudad in self.registro and fecha in self.registro[ciudad]:
            return self.registro[ciudad][fecha]
        else:
            return None


# Ejemplo de uso
registro_temperaturas = RegistroTemperaturas()

# Agregar temperaturas
registro_temperaturas.agregar_temperatura('Ciudad A', '2024-03-01', 25)
registro_temperaturas.agregar_temperatura('Ciudad A', '2024-03-01', 28)
registro_temperaturas.agregar_temperatura('Ciudad A', '2024-03-02', 26)
registro_temperaturas.agregar_temperatura('Ciudad B', '2024-03-01', 22)
registro_temperaturas.agregar_temperatura('Ciudad B', '2024-03-01', 24)

# Obtener temperaturas para una ciudad y fecha específica
print("Temperaturas de Ciudad A el 2024-03-01:", registro_temperaturas.obtener_temperaturas_ciudad_fecha('Ciudad A', '2024-03-01'))
print("Temperaturas de Ciudad B el 2024-03-01:", registro_temperaturas.obtener_temperaturas_ciudad_fecha('Ciudad B', '2024-03-01'))
