# 📊 Datos Abiertos — Anuario Estadístico 2024, Jujuy

Repositorio de datos abiertos generados automáticamente a partir del **Anuario Estadístico 2024** de la Provincia de Jujuy (DiPEC).

Los datos se publican como **JSON y CSV** en **GitHub Pages** y se actualizan automáticamente mediante **GitHub Actions**.

---

## 🌐 GitHub Pages (datos publicados)

```
https://TU_USUARIO.github.io/jujuy-estadisticas/
```

| Dataset | JSON | CSV |
|---|---|---|
| Tasas laborales anuales | [tasas_laborales.json](data/json/tasas_laborales.json) | [tasas_laborales.csv](data/csv/tasas_laborales.csv) |
| Pobreza e indigencia | [pobreza_indigencia.json](data/json/pobreza_indigencia.json) | [pobreza_indigencia.csv](data/csv/pobreza_indigencia.csv) |
| Condición de actividad 2022 | [condicion_actividad_2022.json](data/json/condicion_actividad_2022.json) | [condicion_actividad_2022.csv](data/csv/condicion_actividad_2022.csv) |
| Ejecución presupuestaria | [sector_publico.json](data/json/sector_publico.json) | [sector_publico.csv](data/csv/sector_publico.csv) |
| Gasto corriente 2024 | [gasto_corriente_2024.json](data/json/gasto_corriente_2024.json) | [gasto_corriente_2024.csv](data/csv/gasto_corriente_2024.csv) |
| PBG constantes 2004–2024 | [pbg_constantes.json](data/json/pbg_constantes.json) | [pbg_constantes.csv](data/csv/pbg_constantes.csv) |
| Índice de Producción Industrial | [ipi.json](data/json/ipi.json) | [ipi.csv](data/csv/ipi.csv) |
| Sectores PBG 2024 | [sectores_pbg_2024.json](data/json/sectores_pbg_2024.json) | [sectores_pbg_2024.csv](data/csv/sectores_pbg_2024.csv) |

---

## 🚀 Cómo crear el repositorio desde cero (paso a paso)

### Paso 1 — Crear el repositorio en GitHub

1. Ir a [github.com/new](https://github.com/new)
2. Nombre del repositorio: `jujuy-estadisticas`
3. Visibilidad: **Public** ✅ (necesario para GitHub Pages gratuito)
4. Tildar **"Add a README file"**
5. Click en **"Create repository"**

---

### Paso 2 — Subir los archivos de este proyecto

```bash
# Clonar el repo recién creado
git clone https://github.com/TU_USUARIO/jujuy-estadisticas.git
cd jujuy-estadisticas

# Copiar todos los archivos de este proyecto al repositorio
# (copiar carpetas: scripts/, data/, docs/, .github/)

# Agregar, commitear y pushear
git add .
git commit -m "🎉 Setup inicial — datos Anuario 2024 Jujuy"
git push origin main
```

---

### Paso 3 — Activar GitHub Pages

1. Ir a tu repo → **Settings** → **Pages** (panel izquierdo)
2. En **"Source"** seleccionar: `Deploy from a branch`
3. En **"Branch"** seleccionar: `gh-pages` → carpeta `/` (root)
4. Click **Save**

> ⚠️ La primera vez que corra el workflow se creará la rama `gh-pages` automáticamente.

---

### Paso 4 — Dar permisos al workflow

1. Ir a **Settings** → **Actions** → **General**
2. Bajar hasta **"Workflow permissions"**
3. Seleccionar **"Read and write permissions"** ✅
4. Click **Save**

---

### Paso 5 — Correr el workflow manualmente (primera vez)

1. Ir a **Actions** → `Publicar datos en GitHub Pages`
2. Click en **"Run workflow"** → **"Run workflow"** (botón verde)
3. Esperar ~1 minuto
4. Verificar que en el repo aparezcan los archivos en `data/` y `docs/data/`

---

### Paso 6 — Reemplazar TU_USUARIO

Buscar y reemplazar `TU_USUARIO` en estos archivos:

- `README.md`
- `docs/index.html`
- `data/json/indice.json` (se genera automáticamente)
- `scripts/generar_datos.py` (línea del campo `repositorio`)

---

## 📁 Estructura del repositorio

```
jujuy-estadisticas/
│
├── .github/
│   └── workflows/
│       └── publicar_datos.yml     ← GitHub Actions (automatización)
│
├── scripts/
│   └── generar_datos.py           ← Script principal Python
│
├── data/
│   ├── json/                      ← Datos en formato JSON
│   └── csv/                       ← Datos en formato CSV
│
├── docs/                          ← GitHub Pages (sitio público)
│   ├── index.html                 ← Página de inicio con catálogo
│   └── data/                      ← Copia de data/ para Pages
│
└── README.md
```

---

## ⚙️ Cuándo se actualiza automáticamente

El workflow `publicar_datos.yml` se ejecuta:

| Trigger | Cuándo |
|---|---|
| `schedule` | El 1° de cada mes a las 06:00 UTC |
| `push` a `main` | Cada vez que modificás `scripts/` o `docs/` |
| `workflow_dispatch` | Manualmente desde la pestaña Actions |

---

## 🔧 Correr localmente

```bash
# Solo necesitás Python 3.8+ (sin dependencias externas)
python scripts/generar_datos.py
```

Los archivos se generan en `data/json/` y `data/csv/`.

---

## 📄 Fuentes

- **DiPEC** — Dirección Provincial de Estadística y Censos, Jujuy
- **INDEC** — Instituto Nacional de Estadística y Censos
- **EPH** — Encuesta Permanente de Hogares
- **Censo Nacional** 2022
- **Ministerio de Economía Argentina** — Ejecución presupuestaria

---

## 📜 Licencia

Datos: **CC BY 4.0** — Atribución requerida: DiPEC / Anuario Estadístico 2024, Jujuy  
Código: **MIT**
