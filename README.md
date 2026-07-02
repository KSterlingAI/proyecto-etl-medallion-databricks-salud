# Pipeline ETL End-to-End con Arquitectura Medallion en Azure Databricks para el Sector Salud

## 📝 Descripción del Proyecto
Este repositorio contiene la implementación de un pipeline de datos (ETL) automatizado de punta a punta, diseñado para procesar de forma segura y eficiente datos críticos del sector salud. Utilizando la **Arquitectura Medallion**, los datos crudos pasan por un proceso riguroso de extracción, limpieza, transformación y enriquecimiento hasta consolidarse en un repositorio analítico listo para la toma de decisiones estratégicas.

La solución está completamente desplegada sobre la plataforma **Azure Databricks**, gobernada bajo un modelo de datos estructurado en **Unity Catalog**, y automatizada mediante un pipeline de **Integración y Despliegue Continuo (CI/CD)** con **GitHub Actions**.

---

## 🏗️ Arquitectura de Datos (Medallion)
El procesamiento se divide en tres capas lógicas bien definidas dentro del entorno de **Unity Catalog** (`proyecto_salud_dev`):

1. **Capa Bronze (Raw Data):** Ingesta directa de los datos en su formato original. Almacenamiento histórico de los registros crudos de pacientes y disponibilidad de infraestructura médica.
2. **Capa Silver (Cleansed & Conformed):** Procesos de limpieza, normalización de formatos, manejo de valores nulos y filtrado de anomalías operativas. Los datos se tipifican y se estructuran en tablas Delta optimizadas.
3. **Capa Gold (Business Level):** Agregación de métricas de negocio y lógica analítica avanzada. Aquí se consolidan los KPIs clave como la tasa de disponibilidad de equipos médicos y los estados agregados de pacientes por criticidad.

---

## 🛠️ Stack Tecnológico Utilizado
* **Plataforma de Cloud Data:** Azure Databricks.
* **Motor de Procesamiento:** Apache Spark (PySpark & Spark SQL).
* **Formato de Almacenamiento:** Delta Lake.
* **Gobierno de Datos:** Unity Catalog.
* **Orquestación:** Databricks Workflows (DAG interactivo de notebooks).
* **Automatización (CI/CD):** GitHub Actions para el despliegue automático del código.

---

## 📂 Estructura del Repositorio
El repositorio sigue un orden jerárquico corporativo para facilitar la auditoría del proyecto:

* 📁 **`.github/workflows/`**: Contiene `deploy.yml`, el pipeline automatizado de CI/CD que compila y despliega el código en Databricks de manera segura usando credenciales cifradas (`Secrets`).
* 📁 **`proceso/`**: Cuadernos de producción numerados secuencialmente que ejecutan las fases de Extracción (`02_extract`), Transformación (`03_transform`), Carga de datos (`04_load`), asignación de permisos (`05_grants`) y reversiones (`06_reversion`).
* 📁 **`PrepAmb/`**: Cuadernos destinados a la configuración inicial del entorno, creación de catálogos y esquemas en Unity Catalog (`01_prep_amb`).
* 📁 **`dashboard/`**: Almacena las visualizaciones analíticas y tableros construidos a partir de las métricas agregadas de la capa Gold.
* 📁 **`evidencias/`**: Pruebas técnicas irrefutables del correcto funcionamiento del sistema.
* 📁 **`certifications/`**: Credenciales técnicas oficiales que respaldan el conocimiento arquitectónico aplicado en este desarrollo.

---

## ✅ Evidencias de Ejecución Exitosa

### 1. Orquestación del Pipeline (Workflows)
El flujo completo de notebooks se encuentra orquestado mediante un grafo dirigido acíclico (DAG) en Databricks Workflows, ejecutándose de inicio a fin con estado **Succeeded**.
*Ver evidencia en:* `evidencias/01_workflow_exitoso_medallion.png`

### 2. Gobierno de Datos (Unity Catalog)
Toda la estructura de datos está centralizada y auditada a través de Unity Catalog, garantizando la persistencia física de los esquemas `bronze`, `silver` y `gold`.
*Ver evidencia en:* `evidencias/02_evidencia_unity_catalog.png`

### 3. Integración Continua (GitHub Actions)
Cada cambio subido a la rama `main` dispara automáticamente un agente en la nube que valida el código e implementa los cuadernos directo en el espacio de trabajo de Azure Databricks mediante la API oficial.
*Ver evidencia en:* `evidencias/03_evidencia_cicd_github.png`
