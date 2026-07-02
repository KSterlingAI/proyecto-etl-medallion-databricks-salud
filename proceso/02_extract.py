%python
from pyspark.sql import SparkSession

# Inicializar la sesión de Spark
spark = SparkSession.builder.getOrCreate()

# Ruta raíz de tu contenedor Azure Data Lake Storage Gen2
base_url = "abfss://datalake@adlsaludproyectodev.dfs.core.windows.net"

print("Paso 1: Leyendo datos masivos desde la capa RAW...")

# 1. Leer Insumo de Telemedicina (JSON generado de forma masiva)
df_telemetria_raw = spark.read.format("json").load(f"{base_url}/raw/telemedicina_pacientes_bigdata")

# 2. Leer Insumo de Equipos Biomédicos (CSV generado con cabecera)
df_equipos_raw = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(f"{base_url}/raw/equipos_biomedicos_bigdata")

print("Paso 2: Escribiendo datos en formato Delta en la capa BRONZE...")

# Guardar las tablas crudas de forma segura dentro de tu Unity Catalog
df_telemetria_raw.write.format("delta").mode("overwrite").saveAsTable("proyecto_salud_dev.bronze.telemedicina_raw")
df_equipos_raw.write.format("delta").mode("overwrite").saveAsTable("proyecto_salud_dev.bronze.equipos_biomedicos_raw")

print("¡ÉXITO: Extracción a la capa Bronze completada sin errores!")
