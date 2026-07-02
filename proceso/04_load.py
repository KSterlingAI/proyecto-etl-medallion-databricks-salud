
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Inicializar la sesión de Spark
spark = SparkSession.builder.getOrCreate()

print("Paso 1: Leyendo datos limpios desde la capa SILVER...")
# Cargar la data procesada en el paso anterior
df_telemetria_silver = spark.read.table("proyecto_salud_dev.silver.telemetrina_clean")
df_equipos_silver = spark.read.table("proyecto_salud_dev.silver.equipos_biomedicos_clean")

print("Paso 2: Calculando métricas y KPIs agregados (Capa GOLD)...")

# 1. Filtrar pacientes que están en riesgo crítico
df_criticos = df_telemetria_silver.filter(col("estado_paciente") == "Riesgo Critico")

# 2. Generar el KPI definitivo de equipos biomédicos agrupados por área y su estado de alerta
# Esto le permite al hospital saber qué áreas críticas tienen equipos con mantenimiento urgente
df_kpi_final = df_equipos_silver.groupBy("area_hospital", "alerta_mantenimiento") \
    .agg(count("id_equipo").alias("total_equipos"))

print("Paso 3: Guardando el reporte analítico en el esquema GOLD...")
# Guardar la tabla final en la capa GOLD de Unity Catalog en formato Delta
df_kpi_final.write.format("delta").mode("overwrite").saveAsTable("proyecto_salud_dev.gold.kpi_disponibilidad_equipos")

print("¡ÉXITO: Carga a la capa Gold completada sin errores!")
