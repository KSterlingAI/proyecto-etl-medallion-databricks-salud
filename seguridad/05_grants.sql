-- Paso 1: Otorgar uso en el Catálogo principal a todos los usuarios del espacio de trabajo
GRANT USAGE ON CATALOG `proyecto_salud_dev` TO `account users`;

-- Paso 2: Otorgar permisos de lectura (SELECT) en el esquema de destino definitivo (GOLD)
-- Esto permite que herramientas como Power BI puedan consultar las métricas analíticas
GRANT USAGE ON SCHEMA `proyecto_salud_dev`.`gold` TO `account users`;
GRANT SELECT ON SCHEMA `proyecto_salud_dev`.`gold` TO `account users`;

-- Paso 3: Permisos opcionales de auditoría para las capas operativas (BRONZE y SILVER)
GRANT USAGE ON SCHEMA `proyecto_salud_dev`.`bronze` TO `account users`;
GRANT SELECT ON TABLE `proyecto_salud_dev`.`bronze`.`telemedicina_raw` TO `account users`;
GRANT SELECT ON TABLE `proyecto_salud_dev`.`bronze`.`equipos_biomedicos_raw` TO `account users`;

GRANT USAGE ON SCHEMA `proyecto_salud_dev`.`silver` TO `account users`;
GRANT SELECT ON TABLE `proyecto_salud_dev`.`silver`.`telemedicina_clean` TO `account users`;
GRANT SELECT ON TABLE `proyecto_salud_dev`.`silver`.`equipos_biomedicos_clean` TO `account users`;
