from pyspark.sql import SparkSession

# Inicializar la sesión de Spark
spark = SparkSession.builder.getOrCreate()

print("Iniciando la aplicación de Gobernanza con Unity Catalog...")

# Paso 1: Otorgar uso en el Catálogo principal a todos los usuarios
spark.sql("GRANT USAGE ON CATALOG `proyecto_salud_dev` TO `account users`;")

# Paso 2: Otorgar permisos de lectura (SELECT) en el esquema de destino definitivo (GOLD)
spark.sql("GRANT USAGE ON SCHEMA `proyecto_salud_dev`.`gold` TO `account users`;")
spark.sql("GRANT SELECT ON SCHEMA `proyecto_salud_dev`.`gold` TO `account users`;")

# Paso 3: Permisos opcionales de auditoría para las capas operativas (BRONZE y SILVER)
spark.sql("GRANT USAGE ON SCHEMA `proyecto_salud_dev`.`bronze` TO `account users`;")
spark.sql("GRANT SELECT ON TABLE `proyecto_salud_dev`.`bronze`.`telemedicina_raw` TO `account users`;")
spark.sql("GRANT SELECT ON TABLE `proyecto_salud_dev`.`bronze`.`equipos_biomedicos_raw` TO `account users`;")

spark.sql("GRANT USAGE ON SCHEMA `proyecto_salud_dev`.`silver` TO `account users`;")
spark.sql("GRANT SELECT ON TABLE `proyecto_salud_dev`.`silver`.`telemedicina_clean` TO `account users`;")
spark.sql("GRANT SELECT ON TABLE `proyecto_salud_dev`.`silver`.`equipos_biomedicos_clean` TO `account users`;")

print("¡ÉXITO: GRANTS aplicados correctamente desde PySpark!")
