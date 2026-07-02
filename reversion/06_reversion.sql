-- Romper y limpiar de forma ordenada los objetos lógicos de Unity Catalog si es necesario reiniciar el pipeline
DROP TABLE IF EXISTS `proyecto_salud_dev`.`gold`.`kpi_disponibilidad_equipos`;
DROP SCHEMA IF EXISTS `proyecto_salud_dev`.`gold` RESTRICT;

DROP TABLE IF EXISTS `proyecto_salud_dev`.`silver`.`telemedicina_clean`;
DROP TABLE IF EXISTS `proyecto_salud_dev`.`silver`.`equipos_biomedicos_clean`;
DROP SCHEMA IF EXISTS `proyecto_salud_dev`.`silver` RESTRICT;

DROP TABLE IF EXISTS `proyecto_salud_dev`.`bronze`.`telemedicina_raw`;
DROP TABLE IF EXISTS `proyecto_salud_dev`.`bronze`.`equipos_biomedicos_raw`;
DROP SCHEMA IF EXISTS `proyecto_salud_dev`.`bronze` RESTRICT;

-- NOTA: El catálogo no lo eliminamos para preservar la configuración de la ubicación externa gestionada
