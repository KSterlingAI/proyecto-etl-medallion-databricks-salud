# Pipeline ETL End-to-End con Arquitectura Medallion en Azure Databricks para el Sector Salud

## 📝 Descripción del Proyecto
Este proyecto soluciona un desafío crítico en la gestión hospitalaria: **la falta de visibilidad unificada sobre el estado de los pacientes y la operatividad de los equipos médicos.** Actualmente, muchas instituciones operan con información fragmentada. Esta solución integra dos fuentes de datos fundamentales en un único ecosistema inteligente:

1.  **Monitoreo de Telemedicina (Signos Vitales):** Centralizamos en tiempo real las constantes vitales de los pacientes, permitiendo al personal de salud detectar anomalías de manera oportuna y garantizar un seguimiento clínico ininterrumpido.
2.  **Gestión de Equipos Biomédicos:** Implementamos un sistema de analítica preventiva que monitorea el uso y estado de los equipos críticos. Esto nos permite identificar proactivamente qué dispositivos requieren mantenimiento antes de que fallen, evitando que un equipo esté fuera de servicio precisamente cuando un paciente más lo necesita.

**¿Qué logramos con esto?** La solución garantiza que, cuando un paciente llegue a urgencias o requiera soporte vital, la tecnología esté lista y operativa, y el seguimiento clínico sea preciso. Utilizamos una arquitectura moderna en **Azure Databricks** que procesa estos datos de forma automática, asegurando que la información sea confiable, segura y siempre disponible para los equipos médicos.

---

## 🏗️ Arquitectura de Datos (Medallion)
<p align="center">
  <img src="imagenes/arquitectura_medallion_salud.png" alt="Arquitectura Medallion Salud" width="100%">
</p>

El procesamiento se divide en tres capas lógicas dentro de **Unity Catalog**:
*   **Capa Bronze (Raw Data):** Ingesta directa de los datos crudos de telemedicina y sensores biomédicos en su formato original.
*   **Capa Silver (Cleansed & Conformed):** Procesos de limpieza, normalización de formatos y filtrado de anomalías operativas. Estructurado en tablas Delta optimizadas.
*   **Capa Gold (Business Level):** Agregación de métricas de negocio. KPIs clave como disponibilidad de equipos médicos y estados de pacientes por criticidad.

---

## 🛠️ Stack Tecnológico
* **Plataforma:** Azure Databricks.
* **Motor:** Apache Spark (PySpark & Spark SQL).
* **Almacenamiento:** Delta Lake.
* **Gobierno:** Unity Catalog.
* **Orquestación:** Databricks Workflows.
* **Automatización:** GitHub Actions (CI/CD).

---

## 📂 Estructura del Repositorio
* 📁 `.github/workflows/`: Pipeline de CI/CD automatizado.
* 📁 `proceso/`: Cuadernos de producción (Extracción, Transformación, Carga, Permisos).
* 📁 `PrepAmb/`: Configuración inicial del entorno.
* 📁 `dashboard/`: Visualizaciones de KPIs.
* 📁 `evidencias/`: Pruebas de ejecución exitosa.
* 📁 `certifications/`: Credenciales técnicas (Databricks Lakehouse Fundamentals).

---

## ✅ Evidencias de Ejecución
1. **Orquestación (Workflows):** Ejecución total del DAG con estado *Succeeded*. (`evidencias/01_workflow_exitoso_medallion.png`)
2. **Gobierno (Unity Catalog):** Estructura centralizada y auditada en esquemas bronze, silver y gold. (`evidencias/02_evidencia_unity_catalog.png`)
3. **CI/CD (GitHub Actions):** Despliegue automatizado directo a Databricks con cada commit en `main`. (`evidencias/03_evidencia_cicd_github.png`)

---

## 🎯 Conclusión y Resultados
La implementación de este pipeline bajo una arquitectura **Medallion** no solo estandariza el flujo de datos, sino que garantiza una alta disponibilidad de la información para la toma de decisiones clínicas. Gracias a la integración de **CI/CD**, hemos logrado un sistema ágil y seguro, capaz de reducir los tiempos de respuesta hospitalaria mediante la gestión proactiva de recursos biomédicos y el monitoreo constante del paciente.
