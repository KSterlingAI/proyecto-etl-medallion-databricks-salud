<h1 align="center">🏥 ETL Medallion Pipeline en Azure Databricks — Sector Salud</h1>
<p align="center">
  <b>Pipeline end-to-end de ingesta, transformación y gobernanza de datos clínicos y biomédicos,<br>
  construido sobre Lakehouse (Bronze → Silver → Gold) con CI/CD automatizado.</b>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white" />
  <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" />
  <img src="https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white" />
  <img src="https://img.shields.io/badge/Unity_Catalog-1A73E8?style=for-the-badge" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/status-en_desarrollo-yellow?style=for-the-badge" />
</p>
---
📑 Tabla de contenidos
Resumen ejecutivo
Problema de negocio
Arquitectura de datos
Modelo de datos por capa
Stack tecnológico
Estructura del repositorio
Cómo ejecutar el proyecto
Gobernanza y seguridad de datos
Evidencias de ejecución
Resultados y KPIs
Aprendizajes y roadmap
Licencia
---
🚀 Resumen ejecutivo
Este proyecto simula el entorno de datos de una institución de salud que necesita unificar dos fuentes críticas y hoy fragmentadas: el monitoreo de signos vitales de pacientes (telemedicina) y el estado operativo de equipos biomédicos. El pipeline ingiere, limpia, enriquece y expone estos datos como tablas analíticas listas para consumo (dashboards / BI), aplicando gobernanza de acceso por capa mediante Unity Catalog.
Por qué importa: un hospital que no correlaciona el estado clínico de un paciente con la disponibilidad real de sus equipos críticos corre el riesgo de que un dispositivo falle justo cuando más se necesita. Este pipeline convierte ese riesgo en una alerta accionable.
> 📌 *Nota de transparencia:* los datasets utilizados (`equipos_biomedicos_completo.csv`, `telemedicina_completo.json`) son **datos sintéticos generados para fines de aprendizaje y demostración técnica**, no información real de pacientes ni de instituciones de salud.
---
🎯 Problema de negocio
Situación actual	Consecuencia	Solución implementada
Signos vitales y estado de equipos viven en sistemas separados	El personal clínico no tiene visibilidad cruzada en tiempo útil	Un solo Lakehouse gobernado con ambas fuentes correlacionadas
Mantenimiento de equipos es reactivo (se atiende cuando falla)	Riesgo de indisponibilidad de equipos críticos en momentos de urgencia	Regla de negocio automática: equipos con `horas_uso > 1500` se marcan como `Requiere Mantenimiento Urgente`
Detección de pacientes en riesgo depende de revisión manual	Demora en la respuesta clínica	Regla automática: `frecuencia_cardiaca > 100` u `oxigenación < 92` → `Riesgo Crítico`
Acceso a los datos sin control por capa	Riesgo de exposición de información sensible	Permisos diferenciados por esquema (Bronze/Silver/Gold) vía Unity Catalog `GRANT`
---
🏗️ Arquitectura de datos (Medallion)
<p align="center">
  <img src="imagenes/arquitectura_medallion_salud.png" alt="Arquitectura Medallion Salud" width="100%">
</p>
El flujo completo, tal como está implementado en `proceso/`, sigue este recorrido:
```
Azure Data Lake Storage Gen2 (raw/)
   │  telemedicina_pacientes_bigdata (JSON)
   │  equipos_biomedicos_bigdata (CSV)
   ▼
🥉 BRONZE  →  Ingesta cruda a Delta, sin transformar (02_extract.py)
   ▼
🥈 SILVER  →  Tipado, limpieza y reglas de negocio/alertas (03_transform.py)
   ▼
🥇 GOLD    →  Agregaciones y KPIs listos para consumo BI (04_load.py)
   ▼
📊 Dashboard  →  Visualizaciones de KPIs clínicos y operativos
```
Cada capa vive como esquema independiente (`bronze`, `silver`, `gold`) dentro de un mismo catálogo de Unity Catalog (`proyecto_salud_dev`), lo que permite aplicar controles de acceso y linaje de datos de forma nativa.
---
🗃️ Modelo de datos por capa
Bronze — datos crudos, sin transformar
`bronze.telemedicina_raw` — ingesta 1:1 del JSON de telemedicina
`bronze.equipos_biomedicos_raw` — ingesta 1:1 del CSV de equipos
Silver — datos tipados, limpios y con reglas de negocio
`silver.telemedicina_clean` — signos vitales tipados + columna `estado_paciente` (`Riesgo Critico` / `Estable`)
`silver.equipos_biomedicos_clean` — datos de equipos tipados + columna `alerta_mantenimiento` (`Requiere Mantenimiento Urgente` / `Operativo Seguro`)
Gold — métricas de negocio agregadas
`gold.kpi_disponibilidad_equipos` — total de equipos agrupados por `area_hospital` y `alerta_mantenimiento`, listo para consumo directo en un dashboard
---
🛠️ Stack tecnológico
Categoría	Tecnología
Plataforma Lakehouse	Azure Databricks
Motor de procesamiento	Apache Spark (PySpark + Spark SQL)
Almacenamiento	Delta Lake sobre Azure Data Lake Storage Gen2
Gobierno de datos	Unity Catalog (catálogos, esquemas, `GRANT`/`REVOKE`)
Orquestación	Databricks Workflows
CI/CD	GitHub Actions
Lenguaje	Python (PySpark), SQL
---
📂 Estructura del repositorio
```
├── PrepAmb/                # Configuración inicial del entorno (catálogo y esquemas)
├── proceso/                 # Notebooks/scripts productivos del pipeline
│   ├── 01_prep_amb.py       # Crea catálogo y esquemas bronze/silver/gold
│   ├── 02_extract.py        # Ingesta RAW → Bronze
│   ├── 03_transform.py      # Limpieza y reglas de negocio Bronze → Silver
│   ├── 04_load.py           # Agregaciones y KPIs Silver → Gold
│   └── 05_grants.py         # Aplicación de permisos vía Unity Catalog
├── seguridad/
│   └── 05_grants.sql        # Script SQL de gobernanza (permisos por esquema/tabla)
├── reversion/
│   └── 06_reversion.sql     # Rollback ordenado del pipeline (drop de tablas/esquemas)
├── datasets/                 # Datasets sintéticos de origen (CSV/JSON)
├── dashboard/                 # KPIs visualizados (PNG)
├── evidencias/                 # Capturas de ejecución exitosa (Workflows, Unity Catalog, CI/CD)
├── .github/workflows/         # Pipeline de CI/CD automatizado
└── README.md
```
---
▶️ Cómo ejecutar el proyecto
Prerrequisitos
Workspace de Azure Databricks con Unity Catalog habilitado
Un contenedor de Azure Data Lake Storage Gen2 montado (`abfss://...`)
Permisos para crear catálogos externos gestionados
Pasos
```bash
# 1. Preparar el ambiente (catálogo + esquemas bronze/silver/gold)
databricks workspace run proceso/01_prep_amb.py

# 2. Extraer datos crudos hacia la capa Bronze
databricks workspace run proceso/02_extract.py

# 3. Limpiar y aplicar reglas de negocio hacia la capa Silver
databricks workspace run proceso/03_transform.py

# 4. Calcular KPIs y cargar la capa Gold
databricks workspace run proceso/04_load.py

# 5. Aplicar gobernanza de acceso (Unity Catalog)
databricks workspace run proceso/05_grants.py
```
> Para reiniciar el pipeline desde cero, ejecuta `reversion/06_reversion.sql`, que elimina tablas y esquemas de forma ordenada (Gold → Silver → Bronze) sin afectar la configuración del catálogo externo.
El pipeline también está automatizado end-to-end como un Job/Workflow de Databricks, desplegado automáticamente a cada `push` a `main` mediante GitHub Actions (ver `.github/workflows/`).
---
🔐 Gobernanza y seguridad de datos
La gobernanza se implementa con Unity Catalog aplicando el principio de mínimo privilegio por capa:
Gold → acceso de lectura (`SELECT`) abierto a todos los usuarios del workspace, pensado para consumo directo desde herramientas de BI.
Bronze y Silver → acceso de lectura auditado, pensado para trazabilidad y debugging, no para consumo de negocio.
Todos los permisos están declarados como código en `seguridad/05_grants.sql`, lo que permite versionar y auditar cambios de acceso igual que cualquier otro artefacto del pipeline.
---
✅ Evidencias de ejecución
Orquestación exitosa del DAG completo (Bronze → Silver → Gold)
<p align="center"><img src="evidencias/01_workflow_exitoso_medallion.png" alt="Workflow exitoso" width="85%"></p>
Gobernanza centralizada en Unity Catalog
<p align="center"><img src="evidencias/02_evidencia_unity_catalog.png" alt="Unity Catalog" width="85%"></p>
CI/CD: despliegue automatizado con cada commit a `main`
<p align="center"><img src="evidencias/03_evidencia_cicd_github.png" alt="CI/CD GitHub Actions" width="85%"></p>
---
📊 Resultados y KPIs
<p align="center">
  <img src="dashboard/kpi_mantenimiento_equipos_por_area.png" width="48%">
  <img src="dashboard/kpi_desgaste_horas_por_marca.png" width="48%">
</p>
<p align="center">
  <img src="dashboard/distribucion_edad_pacientes_criticos.png" width="48%">
  <img src="dashboard/proporcion_estado_salud_pacientes.png" width="48%">
</p>
Estos KPIs, calculados en la capa Gold, permiten al equipo hospitalario responder preguntas concretas como: ¿qué áreas concentran más equipos que requieren mantenimiento urgente?, ¿qué marcas de equipos presentan mayor desgaste? y ¿cómo se distribuye el riesgo clínico entre pacientes críticos?
---


📄 Licencia
Este proyecto se publica bajo licencia MIT. Los datasets incluidos son sintéticos y se distribuyen únicamente con fines educativos y de demostración técnica.
