-- =====================================================================
-- PREPARACIÓN DE AMBIENTE: CONFIGURACIÓN DE CATALOGO Y SCHEMAS (MEDALLION)
-- =====================================================================

-- 1. Crear el Catálogo apuntando directamente a tu ubicación externa validada
CREATE CATALOG IF NOT EXISTS `proyecto_salud_dev`
MANAGED LOCATION 'abfss://datalake@adlsaludproyectodev.dfs.core.windows.net/metastore/';

-- 2. Crear los tres esquemas de la arquitectura Medallion dentro del catálogo
CREATE SCHEMA IF NOT EXISTS `proyecto_salud_dev`.`bronze`;
CREATE SCHEMA IF NOT EXISTS `proyecto_salud_dev`.`silver`;
CREATE SCHEMA IF NOT EXISTS `proyecto_salud_dev`.`gold`;
