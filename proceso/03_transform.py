
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Inicializar la sesión de Spark
spark = SparkSession.builder.getOrCreate()

print("Paso 1: Leyendo tablas estructuradas desde la capa BRONZE...")
# Leer las tablas Delta que creamos con éxito en el paso anterior
df_telemetria_bronze = spark.read.table("proyecto_salud_dev.bronze.telemedicina_raw")
df_equipos_bronze = spark.read.table("proyecto_salud_dev.bronze.equipos_biomedicos_raw")

print("Paso 2: Aplicando transformaciones y limpieza (Capa SILVER)...")

# 1. Transformación de Telemedicina:
# - Castear tipos de datos y asegurar consistencia
# - Crear columna de alerta: Si frecuencia > 100 o oxigenación < 92, es "Riesgo Crítico", de lo contrario "Estable"
df_telemetria_silver = df_telemetria_bronze \
    .withColumn("edad", col("edad").cast("int")) \
    .withColumn("frecuencia_cardiaca", col("frecuencia_cardiaca").cast("int")) \
    .withColumn("presion_sistolica", col("presion_sistolica").cast("int")) \
    .withColumn("presion_diastolica", col("presion_diastolica").cast("int")) \
    .withColumn("oxigenacion", col("oxigenacion").cast("int")) \
    .withColumn("fecha_registro", col("fecha_registro").cast("timestamp")) \
    .withColumn(
        "estado_paciente", 
        when((col("frecuencia_cardiaca") > 100) | (col("oxigenacion") < 92), "Riesgo Critico")
        .otherwise("Estable")
    )

# 2. Transformación de Equipos Biomédicos:
# - Castear tipos de datos numéricos y de fecha
# - Crear columna de alerta: Si horas_uso > 1500, marcar como "Requiere Mantenimiento Urgente"
df_equipos_silver = df_equipos_bronze \
    .withColumn("horas_uso", col("horas_uso").cast("double")) \
    .withColumn("ultimo_mantenimiento", col("ultimo_mantenimiento").cast("date")) \
    .withColumn(
        "alerta_mantenimiento",
        when(col("horas_uso") > 1500.0, "Requiere Mantenimiento Urgente")
        .otherwise("Operativo Seguro")
    )

print("Paso 3: Escribiendo datos limpios en el esquema SILVER...")
# Guardar en la capa SILVER de Unity Catalog en formato Delta
df_telemetria_silver.write.format("delta").mode("overwrite").saveAsTable("proyecto_salud_dev.silver.telemedicina_clean")
df_equipos_silver.write.format("delta").mode("overwrite").saveAsTable("proyecto_salud_dev.silver.equipos_biomedicos_clean")

print("¡ÉXITO: Transformación a la capa Silver completada sin errores!")
