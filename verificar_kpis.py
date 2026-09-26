"""Recalcula los KPIs del dashboard a partir de data/ventas_2024.csv.

Lo escribí para auditar el dashboard de Looker Studio: cada número del
tablero tiene que poder reproducirse desde los datos.

Uso (desde la raíz del repo):
    python verificar_kpis.py
"""

import pandas as pd

ventas = pd.read_csv("data/ventas_2024.csv", parse_dates=["fecha"])

# Controles de calidad sobre los datos ya limpios
print("--- Calidad de datos ---")
print(f"Filas: {len(ventas)}")
print(f"IDs de venta nulos: {ventas['id_venta'].isna().sum()}")
print(f"IDs de venta duplicados: {ventas['id_venta'].duplicated().sum()}")
print(f"Período: {ventas['fecha'].min():%d/%m/%Y} a {ventas['fecha'].max():%d/%m/%Y}")

# KPIs principales
total_ventas = ventas["id_venta"].nunique()
unidades = ventas["cantidad"].sum()
clientes = ventas["id_cliente"].nunique()
productos = ventas["id_producto"].nunique()

print("\n--- KPIs ---")
print(f"Ventas (transacciones): {total_ventas:,}".replace(",", "."))
print(f"Unidades vendidas: {unidades:,}".replace(",", "."))
print(f"Clientes distintos: {clientes}")
print(f"Productos distintos: {productos}")
print(f"Unidades promedio por venta: {unidades / total_ventas:.2f}")

# Estado de las ventas
print("\n--- Ventas por estado ---")
print(ventas["estado"].value_counts().to_string())

# Evolución mensual
mensual = ventas.groupby(ventas["fecha"].dt.to_period("M")).agg(
    ventas=("id_venta", "nunique"),
    unidades=("cantidad", "sum"),
    dias_con_datos=("fecha", "nunique"),
)
print("\n--- Evolución mensual ---")
print(mensual.to_string())
mes_top = mensual["unidades"].idxmax()
print(f"\nMes con más unidades vendidas: {mes_top} ({mensual.loc[mes_top, 'unidades']} unidades)")

# Medios de pago
print("\n--- Medios de pago (% de ventas) ---")
print((ventas["metodo_pago"].value_counts(normalize=True) * 100).round(1).to_string())

# Productos con más unidades vendidas
print("\n--- Top 5 productos por unidades ---")
print(ventas.groupby("id_producto")["cantidad"].sum().nlargest(5).to_string())

# Errores detectados en el dashboard original
print("\n--- Contraste con el dashboard original ---")
print(f"'Ventas totales' mostraba 10.441: coincide con las unidades ({unidades}), no con las ventas ({total_ventas}).")
print(f"'Productos vendidos' mostraba 59.006: coincide con la suma de los ID de producto ({ventas['id_producto'].sum()}).")
