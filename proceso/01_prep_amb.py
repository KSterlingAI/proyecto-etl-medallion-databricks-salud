from pyspark.sql import SparkSession

# Inicializar la sesión de Spark
spark = SparkSession.builder.appName("PrepAmbiente").getOrCreate()

# 1. Crear el Catálogo apuntando directamente a tu ubicación externa validada
spark.sql("""
CREATE CATALOG IF NOT EXISTS `proyecto_salud_dev`
MANAGED LOCATION 'abfss://datalake@adlsaludproyectodev.dfs.core.windows.net/metastore/';
""")

# 2. Crear los tres esquemas de la arquitectura Medallion dentro del catálogo
spark.sql("CREATE SCHEMA IF NOT EXISTS `proyecto_salud_dev`.`bronze`;")
spark.sql("CREATE SCHEMA IF NOT EXISTS `proyecto_salud_dev`.`silver`;")
spark.sql("CREATE SCHEMA IF NOT EXISTS `proyecto_salud_dev`.`gold`;")

print("Ambiente preparado desde PySpark con éxito.")
