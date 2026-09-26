# Business Intelligence para un e-commerce en Looker Studio

Proyecto integrador de un curso de Business Intelligence: calidad de datos, preparación en Google Sheets, dashboard en Looker Studio y storytelling sobre las ventas 2024 de un e-commerce. Después de terminarlo audité el dashboard con Python y encontré dos KPIs mal calculados; en este README están los números corregidos.

**Herramientas:** Google Sheets · Looker Studio · Python (pandas) para la verificación

**[Ver el dashboard en Looker Studio](https://lookerstudio.google.com/reporting/495f1084-597b-4651-9dfc-7c9f955bd3ed)**

## Problema

Un e-commerce quería entender cómo le fue en 2024: cuánto vendió, a cuántos clientes, qué productos salen más y cómo pagan sus clientes. El trabajo iba desde revisar la calidad de los datos hasta presentar los resultados en un dashboard.

## Datos

- Registro de ventas de 2024 provisto por el curso: 3.000 ventas después de la limpieza, del 31/01/2024 al 30/12/2024.
- Columnas: ID de venta, fecha, cliente, producto, cantidad, medio de pago y estado (completa, pendiente o cancelada), más una tabla auxiliar con los 5 medios de pago.
- El dataset no tiene precios, así que se mide en ventas (transacciones) y unidades, no en montos.
- `data/ventas_2024.csv` es la hoja `ventas` del Excel de la Etapa 2, exportada para poder reproducir los KPIs con código.

## Método

El proyecto se hizo en cuatro etapas; cada entregable está en `docs/`.

1. **Fundamentos y calidad de datos.** Armé un checklist de calidad en Google Forms y lo apliqué al dataset: había IDs de venta vacíos, filas duplicadas y fechas con formatos distintos (4/12/2024 y 04/12/2024). También incluye un caso de estudio sobre ética de datos en e-commerce y tres fuentes públicas de datos del sector (CACE, Statista, Wuala).
2. **Preparación y análisis.** En Google Sheets normalicé las fechas, crucé los medios de pago con `VLOOKUP` y calculé ventas por mes, media, mediana, moda y desvío de unidades, y compras por cliente.
3. **Dashboard.** Elegí cada gráfico según la pregunta: líneas para la evolución mensual, torta para los medios de pago, tabla para los productos más vendidos. Además hice una versión optimizada: reemplacé el treemap de compra promedio por cliente por un top 10, que se lee mejor.
4. **Storytelling.** Presentación de los hallazgos a partir del dashboard.
5. **Verificación.** Con `verificar_kpis.py` recalculo en pandas cada KPI desde el CSV.

## Resultados

| Indicador | Valor |
|---|---|
| Ventas (transacciones) | 3.000 |
| Unidades vendidas | 10.441 |
| Unidades promedio por venta | 3,48 |
| Clientes distintos | 326 |
| Productos distintos | 38 |

- **Estado:** el 84 % de las ventas está completa (2.523), el 15,6 % pendiente (467) y 10 fueron canceladas.
- **Evolución mensual:** de febrero a diciembre las ventas se mueven entre 249 y 309 por mes. Junio es el mes con más actividad: 309 ventas y 1.077 unidades. Enero aparece muy bajo solo porque los datos arrancan el 31 de enero; no es una caída de ventas.
- **Medios de pago:** Mercado Pago 29 %, transferencia 26,3 %, efectivo 18,3 %, tarjeta de débito 17,8 % y tarjeta de crédito 8,6 %.
- **Productos:** los que más unidades venden son el 26 (375), el 27 (357) y el 29 (350).

<img src="https://github.com/user-attachments/assets/6679d4a2-30f1-4ceb-9ffc-83238b43a680" alt="Dashboard del proyecto en Looker Studio" width="700"/>

### Errores que encontré en el dashboard

Al recalcular los KPIs con Python, dos no coincidían con los datos:

- **"Ventas totales: 10.441"** en realidad suma las unidades vendidas. Las ventas son 3.000.
- **"Productos vendidos: 59.006"** suma los ID de producto, un número sin significado. Hay 38 productos distintos.

Además, el tablero muestra 307 clientes y los datos tienen 326 clientes distintos.

La lección que me llevo: todo KPI de un dashboard tiene que poder reproducirse desde los datos crudos.

## Cómo ejecutarlo

Para ver el dashboard alcanza con el link de arriba. Para reproducir los KPIs:

```bash
git clone https://github.com/EmiiFernandez/proyecto-bi-ecommerce-looker-studio.git
cd proyecto-bi-ecommerce-looker-studio
pip install -r requirements.txt
python verificar_kpis.py
```

## Estructura del repo

```
proyecto-bi-ecommerce-looker-studio/
├── data/
│   └── ventas_2024.csv                          # ventas limpias (3.000 filas)
├── docs/
│   ├── etapa1_fundamentos_calidad_datos.pdf     # checklist de calidad, ética y fuentes
│   ├── etapa2_preparacion_analisis_datos.xlsx   # preparación y análisis en Sheets
│   ├── etapa3_dashboards_visualizacion.pdf      # elección de gráficos
│   └── etapa4_storytelling.pdf                  # presentación final
├── verificar_kpis.py                            # recalcula los KPIs del dashboard
├── requirements.txt
└── LICENSE
```

## Próximos pasos

- Corregir los KPIs en el dashboard y agregar un indicador de ventas pendientes.
- Hacer la limpieza de la Etapa 2 en SQL o pandas para que todo el proceso sea reproducible, no solo la verificación.
- Si se suman precios al dataset, medir facturación y ticket promedio.

---

Emilia Fernández · [LinkedIn](https://www.linkedin.com/in/emiliafernandez) · Licencia MIT
