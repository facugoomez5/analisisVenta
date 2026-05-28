
import pandas as pd
import matplotlib.pyplot as plt

# Leer el dataset desde la carpeta datos
df = pd.read_csv('../datos/sales_sample_2024.csv')

# Convertir la columna de fecha a formato fecha
df['sales_date'] = pd.to_datetime(df['sales_date'])

# Calcular ventas totales
ventas_totales = df['sales_amount'].sum()

# Calcular venta promedio
venta_promedio = df['sales_amount'].mean()

# Calcular el día con mayor venta
dia_mayor_venta = df.loc[df['sales_amount'].idxmax()]

# Calcular ventas por mes
df['mes'] = df['sales_date'].dt.month
ventas_por_mes = df.groupby('mes')['sales_amount'].sum()

# Mostrar resultados
print('Ventas totales:', ventas_totales)
print('Venta promedio:', round(venta_promedio, 2))
print('Día con mayor venta:')
print(dia_mayor_venta)

print('\nVentas por mes:')
print(ventas_por_mes)

# Guardar resumen en resultados
with open('../resultados/resumen.txt', 'w', encoding='utf-8') as archivo:
    archivo.write('Resumen del análisis de ventas\n')
    archivo.write('--------------------------------\n')
    archivo.write(f'Ventas totales: {ventas_totales}\n')
    archivo.write(f'Venta promedio: {round(venta_promedio, 2)}\n')
    archivo.write(f'Día con mayor venta: {dia_mayor_venta["sales_date"]}\n')
    archivo.write(f'Monto del día con mayor venta: {dia_mayor_venta["sales_amount"]}\n')

# Generar gráfico
ventas_por_mes.plot(kind='bar')

plt.title('Ventas por mes - Año 2024')
plt.xlabel('Mes')
plt.ylabel('Monto de ventas')
plt.tight_layout()

plt.savefig('../resultados/grafico_ventas.png')

print('\nAnálisis finalizado correctamente.')
