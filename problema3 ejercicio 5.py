
# CURSO: Fundamentos de Programación
# FASE 5: Evaluación Final POA
# Estudiante: Brayan Steven Lopez Porras
# PROBLEMA 3: Auditoría de Inventario

# función para calcular cuánto pedir de cada articulo
def calcular_pedido(actual, minimo):
    if actual < minimo:
        resultado = minimo - actual
        return resultado
    else:
        return 0

# Matriz con los datos de los 5 articulos
inventario = [
    ["A001", "Cuadernos", 15, 50],
    ["A002", "Bolígrafos", 120, 100],
    ["A003", "Marcadores", 8, 30],
    ["A004", "Resaltadores", 45, 40],
    ["A005", "Borradores", 5, 25]
]

# Imprimir el titulo del reporte
print("========================================")
print("   INFORME DE AUDITORIA DE INVENTARIO")
print("========================================")
print("PRODUCTOS             | CANTIDAD A SOLICITAR")
print("----------------------------------------")

# Ciclo para revisar la matriz y mostrar los resultados
for fila in inventario:
    nombre_producto = fila[1]
    stock_actual = fila[2]
    stock_minimo = fila[3]
    
    # Llamamos a la funcion para el calculo
    cantidad_final = calcular_pedido(stock_actual, stock_minimo)
    
    # Mostramos los datos organizados
    print(f"{nombre_producto:<20} | {cantidad_final}")

print("========================================")