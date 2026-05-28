
# ANÁLISIS DE VENTAS - TP ORGANIZACIÓN EMPRESARIAL

## UNIVERSIDAD TECNOLÓGICA NACIONAL

Trabajo Práctico:
Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

---

## Alumno

- Facundo Gomez

---

## Materia

Organización Empresarial

---

## Año Lectivo

2026

---

## Escenario Seleccionado

Escenario B – Análisis de Ventas de una Pequeña Empresa :contentReference[oaicite:0]{index=0}

---

## Descripción del Proyecto

El presente proyecto tiene como objetivo aplicar conceptos de:

- Gestión colaborativa
- Control de versiones
- Organización empresarial
- Trazabilidad de tareas
- Documentación técnica

Para ello, se desarrolló un sistema simple de análisis de ventas utilizando Python y Google Colab, implementando un flujo de trabajo profesional mediante Git, GitHub y Jira.

---

## Dataset Utilizado

Se utilizó un dataset público de ventas comerciales en formato CSV recomendado por la consigna del trabajo práctico.

### Dataset utilizado:
`sales_sample_2024.csv`

### Columnas principales:

- `id`
- `sales_date`
- `sales_amount`

### Fuente del dataset

Dataset público de ventas simuladas recomendado por la cátedra

---

## Objetivos del Análisis

El script desarrollado permite:

- Calcular ventas totales
- Obtener el promedio de ventas
- Identificar el día con mayor venta
- Analizar ventas agrupadas por mes
- Generar gráficos estadísticos
- Exportar resultados automáticamente

---

## Tecnologías Utilizadas

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Jira
- Google Colab

---

## Herramientas de Gestión

### Jira

Se utilizó Jira para la planificación y trazabilidad de tareas mediante Issues.

### Git y GitHub

Se implementó un flujo de trabajo basado en:

- ramas (`branches`)
- commits descriptivos
- pull requests
- control de versiones distribuido

---

## Estructura del Proyecto

```text
analisisVenta/
│
├── datos/
│   └── sales_sample_2024.csv
│
├── scripts/
│   └── analisis_ventas.py
│
├── resultados/
│   ├── grafico_ventas.png
│   └── resumen.txt
│
├── README.md
│
└── .gitignore
```

---

## Flujo de Trabajo Implementado

1. Creación del proyecto en Jira
2. Creación del repositorio en GitHub
3. Clonado del repositorio en Google Colab
4. Creación de ramas
5. Desarrollo del script de análisis
6. Realización de commits trazables
7. Push mediante Personal Access Token (PAT)
8. Creación de Pull Request
9. Revisión y merge final

---

## Commits Realizados



PROY-1: Crear estructura inicial del proyecto
PROY-2: Agregar dataset de ventas
PROY-2: Desarrollar script de análisis de ventas
PROY-2: Crear gitIgnore
PROY-3: Mejorar documentación y revisión QA


---

## Archivo .gitignore

Se configuró un archivo `.gitignore` para excluir:

- archivos temporales
- checkpoints de notebooks
- caché de Python
- datasets pesados

Contenido utilizado:

```text
__pycache__/
.ipynb_checkpoints/
*.log
datos/sales_sample_2024.csv
```

---

## Ejecución del Proyecto

Desde Google Colab o terminal:

```bash
python analisis_ventas.py
```

---

## Resultados Generados

El proyecto genera automáticamente:

- `resumen.txt`
- `grafico_ventas.png`

Los resultados son almacenados dentro de la carpeta:

```text
/resultados
```

---

## Buenas Prácticas Aplicadas

- Uso de ramas de desarrollo
- Conventional Commits
- Uso de Pull Requests
- Separación modular de carpetas
- Uso de rutas relativas
- Exclusión de archivos sensibles mediante `.gitignore`
- Documentación técnica del proyecto

---

## Conclusión

El trabajo permitió aplicar conceptos fundamentales de organización empresarial y desarrollo colaborativo utilizando herramientas ampliamente utilizadas en la industria del software.

La utilización de Git, GitHub, Jira y Google Colab permitió implementar un flujo de trabajo profesional basado en trazabilidad, control de versiones y documentación técnica reproducible.
