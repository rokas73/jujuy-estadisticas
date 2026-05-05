"""
generar_datos.py
Extrae los datos del Anuario Estadístico 2024 - Jujuy
y genera archivos JSON y CSV listos para GitHub Pages.
"""

import json
import csv
import os
from pathlib import Path

# ── Rutas de salida ───────────────────────────────────────────────────
ROOT   = Path(__file__).parent.parent
DATA_J = ROOT / "data" / "json"
DATA_C = ROOT / "data" / "csv"
DATA_J.mkdir(parents=True, exist_ok=True)
DATA_C.mkdir(parents=True, exist_ok=True)


# ═══════════════════════════════════════════════════════════════════════
# 1. TRABAJO E INGRESOS
# ═══════════════════════════════════════════════════════════════════════

tasas_laborales = {
    "fuente": "DiPEC / EPH-INDEC",
    "unidad": "porcentaje",
    "nota": "Promedios anuales de los cuatro trimestres",
    "datos": [
        {"año": 2016, "region": "Jujuy-Palpalá", "actividad": 42.8, "empleo": 40.3, "desocupacion": 3.5, "subocupacion": 12.0},
        {"año": 2016, "region": "NOA",            "actividad": 43.5, "empleo": 41.0, "desocupacion": 5.7, "subocupacion": 10.0},
        {"año": 2016, "region": "Total País",     "actividad": 46.1, "empleo": 42.6, "desocupacion": 8.5, "subocupacion": 10.5},
        {"año": 2017, "region": "Jujuy-Palpalá", "actividad": 45.5, "empleo": 43.2, "desocupacion": 5.0, "subocupacion": 13.8},
        {"año": 2017, "region": "NOA",            "actividad": 44.7, "empleo": 41.9, "desocupacion": 6.3, "subocupacion": 11.0},
        {"año": 2017, "region": "Total País",     "actividad": 46.2, "empleo": 42.7, "desocupacion": 8.5, "subocupacion": 10.5},
        {"año": 2018, "region": "Jujuy-Palpalá", "actividad": 43.6, "empleo": 41.4, "desocupacion": 5.3, "subocupacion": 12.5},
        {"año": 2018, "region": "NOA",            "actividad": 43.9, "empleo": 41.1, "desocupacion": 6.5, "subocupacion": 11.0},
        {"año": 2018, "region": "Total País",     "actividad": 46.7, "empleo": 42.5, "desocupacion": 9.2, "subocupacion": 11.5},
        {"año": 2019, "region": "Jujuy-Palpalá", "actividad": 45.8, "empleo": 43.3, "desocupacion": 5.5, "subocupacion": 15.5},
        {"año": 2019, "region": "NOA",            "actividad": 45.4, "empleo": 42.8, "desocupacion": 6.2, "subocupacion": 13.1},
        {"año": 2019, "region": "Total País",     "actividad": 47.3, "empleo": 43.0, "desocupacion": 9.8, "subocupacion": 13.0},
        {"año": 2020, "region": "Jujuy-Palpalá", "actividad": 41.7, "empleo": 40.2, "desocupacion": 5.8, "subocupacion": 18.0},
        {"año": 2020, "region": "NOA",            "actividad": 41.5, "empleo": 38.9, "desocupacion": 6.1, "subocupacion": 12.9},
        {"año": 2020, "region": "Total País",     "actividad": 40.7, "empleo": 33.4, "desocupacion": 11.5, "subocupacion": 16.5},
        {"año": 2021, "region": "Jujuy-Palpalá", "actividad": 45.7, "empleo": 43.5, "desocupacion": 5.5, "subocupacion": 13.4},
        {"año": 2021, "region": "NOA",            "actividad": 44.1, "empleo": 41.9, "desocupacion": 5.7, "subocupacion": 12.5},
        {"año": 2021, "region": "Total País",     "actividad": 45.0, "empleo": 40.1, "desocupacion": 8.7, "subocupacion": 11.5},
        {"año": 2022, "region": "Jujuy-Palpalá", "actividad": 47.0, "empleo": 44.9, "desocupacion": 4.9, "subocupacion": 10.6},
        {"año": 2022, "region": "NOA",            "actividad": 46.1, "empleo": 43.7, "desocupacion": 5.2, "subocupacion": 12.4},
        {"año": 2022, "region": "Total País",     "actividad": 47.8, "empleo": 44.6, "desocupacion": 6.9, "subocupacion": 10.8},
        {"año": 2023, "region": "Jujuy-Palpalá", "actividad": 47.3, "empleo": 44.8, "desocupacion": 5.7, "subocupacion": 10.6},
        {"año": 2023, "region": "NOA",            "actividad": 45.9, "empleo": 43.4, "desocupacion": 5.3, "subocupacion": 12.6},
        {"año": 2023, "region": "Total País",     "actividad": 48.4, "empleo": 45.5, "desocupacion": 5.7, "subocupacion": 12.0},
        {"año": 2024, "region": "Jujuy-Palpalá", "actividad": 47.5, "empleo": 45.1, "desocupacion": 3.9, "subocupacion": 12.2},
        {"año": 2024, "region": "NOA",            "actividad": 46.1, "empleo": 43.5, "desocupacion": 5.8, "subocupacion": 9.7},
        {"año": 2024, "region": "Total País",     "actividad": 48.5, "empleo": 45.7, "desocupacion": 6.4, "subocupacion": 13.2},
    ]
}

pobreza_indigencia = {
    "fuente": "DiPEC / EPH-INDEC",
    "unidad": "porcentaje",
    "nota": "Datos semestrales. Jujuy-Palpalá",
    "datos": [
        {"semestre": "2S 2016", "pobreza_hogares": 20.1, "pobreza_personas": 25.7, "indigencia_hogares": 3.6,  "indigencia_personas": 4.5},
        {"semestre": "1S 2017", "pobreza_hogares": 17.8, "pobreza_personas": 23.8, "indigencia_hogares": 1.7,  "indigencia_personas": 1.7},
        {"semestre": "2S 2017", "pobreza_hogares": 18.7, "pobreza_personas": 24.2, "indigencia_hogares": 2.8,  "indigencia_personas": 4.0},
        {"semestre": "1S 2018", "pobreza_hogares": 23.0, "pobreza_personas": 30.3, "indigencia_hogares": 3.1,  "indigencia_personas": 4.3},
        {"semestre": "2S 2018", "pobreza_hogares": 24.7, "pobreza_personas": 31.7, "indigencia_hogares": 4.6,  "indigencia_personas": 6.4},
        {"semestre": "1S 2019", "pobreza_hogares": 26.2, "pobreza_personas": 35.7, "indigencia_hogares": 3.8,  "indigencia_personas": 6.4},
        {"semestre": "2S 2019", "pobreza_hogares": 28.2, "pobreza_personas": 37.8, "indigencia_hogares": 4.3,  "indigencia_personas": 5.7},
        {"semestre": "1S 2020", "pobreza_hogares": 28.6, "pobreza_personas": 38.0, "indigencia_hogares": 3.5,  "indigencia_personas": 4.8},
        {"semestre": "2S 2020", "pobreza_hogares": 27.4, "pobreza_personas": 37.7, "indigencia_hogares": 3.3,  "indigencia_personas": 4.7},
        {"semestre": "1S 2021", "pobreza_hogares": 33.4, "pobreza_personas": 42.5, "indigencia_hogares": 4.4,  "indigencia_personas": 5.7},
        {"semestre": "2S 2021", "pobreza_hogares": 29.4, "pobreza_personas": 36.2, "indigencia_hogares": 5.0,  "indigencia_personas": 6.3},
        {"semestre": "1S 2022", "pobreza_hogares": 28.2, "pobreza_personas": 33.8, "indigencia_hogares": 5.4,  "indigencia_personas": 6.4},
        {"semestre": "2S 2022", "pobreza_hogares": 32.5, "pobreza_personas": 41.8, "indigencia_hogares": 5.8,  "indigencia_personas": 8.5},
        {"semestre": "1S 2023", "pobreza_hogares": 34.0, "pobreza_personas": 42.2, "indigencia_hogares": 6.5,  "indigencia_personas": 8.7},
        {"semestre": "2S 2023", "pobreza_hogares": 33.8, "pobreza_personas": 43.6, "indigencia_hogares": 8.3,  "indigencia_personas": 11.1},
        {"semestre": "1S 2024", "pobreza_hogares": 46.3, "pobreza_personas": 55.7, "indigencia_hogares": 12.5, "indigencia_personas": 15.3},
        {"semestre": "2S 2024", "pobreza_hogares": 31.0, "pobreza_personas": 40.0, "indigencia_hogares": 6.8,  "indigencia_personas": 9.8},
    ]
}

condicion_actividad_2022 = {
    "fuente": "Censo Nacional de Población, Hogares y Viviendas 2022 — INDEC / DiPEC",
    "unidad": "personas",
    "nota": "Población de 14 años y más. Provincia de Jujuy",
    "datos": [
        {"grupo_edad": "Total",    "poblacion_14mas": 633222, "pea_total": 397889, "ocupados": 366361, "desocupados": 31528, "no_activos": 235333},
        {"grupo_edad": "14-19",    "poblacion_14mas":  79368, "pea_total":  17030, "ocupados":  13848, "desocupados":  3182, "no_activos":  62338},
        {"grupo_edad": "20-29",    "poblacion_14mas": 132868, "pea_total":  91937, "ocupados":  79487, "desocupados": 12450, "no_activos":  40931},
        {"grupo_edad": "30-44",    "poblacion_14mas": 180743, "pea_total": 149903, "ocupados": 140021, "desocupados":  9882, "no_activos":  30840},
        {"grupo_edad": "45-59",    "poblacion_14mas": 128556, "pea_total": 109893, "ocupados": 104254, "desocupados":  5639, "no_activos":  18663},
        {"grupo_edad": "60 y más", "poblacion_14mas": 111687, "pea_total":  29126, "ocupados":  28751, "desocupados":   375, "no_activos":  82561},
    ]
}


# ═══════════════════════════════════════════════════════════════════════
# 2. SECTOR PÚBLICO
# ═══════════════════════════════════════════════════════════════════════

sector_publico = {
    "fuente": "DiPEC — Ministerio de Economía Argentina",
    "unidad": "millones de pesos corrientes",
    "nota": "Administración Pública No Financiera. Ejecución presupuestaria provisoria. Cuarto trimestre acumulado",
    "datos": [
        {"año": 2005, "ingresos_corrientes": 1260,  "gastos_corrientes": 1146,  "ingresos_capital": 135,   "gastos_capital": 216,   "resultado_primario": 100,    "resultado_financiero": 33},
        {"año": 2006, "ingresos_corrientes": 1537,  "gastos_corrientes": 1403,  "ingresos_capital": 184,   "gastos_capital": 285,   "resultado_primario": 88,     "resultado_financiero": 32},
        {"año": 2007, "ingresos_corrientes": 2067,  "gastos_corrientes": 1941,  "ingresos_capital": 176,   "gastos_capital": 395,   "resultado_primario": -93,    "resultado_financiero": -17},
        {"año": 2008, "ingresos_corrientes": 2554,  "gastos_corrientes": 2479,  "ingresos_capital": 225,   "gastos_capital": 480,   "resultado_primario": -127,   "resultado_financiero": -180},
        {"año": 2009, "ingresos_corrientes": 3157,  "gastos_corrientes": 3078,  "ingresos_capital": 426,   "gastos_capital": 639,   "resultado_primario": -73,    "resultado_financiero": -135},
        {"año": 2010, "ingresos_corrientes": 4337,  "gastos_corrientes": 3876,  "ingresos_capital": 551,   "gastos_capital": 732,   "resultado_primario": 372,    "resultado_financiero": 281},
        {"año": 2011, "ingresos_corrientes": 5377,  "gastos_corrientes": 5244,  "ingresos_capital": 595,   "gastos_capital": 1016,  "resultado_primario": -280,   "resultado_financiero": -288},
        {"año": 2012, "ingresos_corrientes": 6939,  "gastos_corrientes": 6993,  "ingresos_capital": 767,   "gastos_capital": 1196,  "resultado_primario": -470,   "resultado_financiero": -484},
        {"año": 2013, "ingresos_corrientes": 8667,  "gastos_corrientes": 9380,  "ingresos_capital": 1161,  "gastos_capital": 1641,  "resultado_primario": -1140,  "resultado_financiero": -1193},
        {"año": 2014, "ingresos_corrientes": 12548, "gastos_corrientes": 12875, "ingresos_capital": 1755,  "gastos_capital": 2559,  "resultado_primario": -1125,  "resultado_financiero": -1132},
        {"año": 2015, "ingresos_corrientes": 17436, "gastos_corrientes": 17639, "ingresos_capital": 2212,  "gastos_capital": 3678,  "resultado_primario": -1649,  "resultado_financiero": -1669},
        {"año": 2016, "ingresos_corrientes": 21329, "gastos_corrientes": 24275, "ingresos_capital": 1615,  "gastos_capital": 3660,  "resultado_primario": -4518,  "resultado_financiero": -4991},
        {"año": 2017, "ingresos_corrientes": 29395, "gastos_corrientes": 31710, "ingresos_capital": 2380,  "gastos_capital": 5470,  "resultado_primario": -4465,  "resultado_financiero": -5405},
        {"año": 2018, "ingresos_corrientes": 38952, "gastos_corrientes": 39299, "ingresos_capital": 2174,  "gastos_capital": 7668,  "resultado_primario": -3361,  "resultado_financiero": -5841},
        {"año": 2019, "ingresos_corrientes": 54640, "gastos_corrientes": 53895, "ingresos_capital": 1901,  "gastos_capital": 7890,  "resultado_primario": -2525,  "resultado_financiero": -5244},
        {"año": 2020, "ingresos_corrientes": 76340, "gastos_corrientes": 68527, "ingresos_capital": 1974,  "gastos_capital": 10098, "resultado_primario": 2794,   "resultado_financiero": -311},
        {"año": 2021, "ingresos_corrientes": 125888,"gastos_corrientes": 106111,"ingresos_capital": 2800,  "gastos_capital": 17724, "resultado_primario": 9928,   "resultado_financiero": 4854},
        {"año": 2022, "ingresos_corrientes": 225879,"gastos_corrientes": 175317,"ingresos_capital": 1796,  "gastos_capital": 40924, "resultado_primario": 20035,  "resultado_financiero": 11435},
        {"año": 2023, "ingresos_corrientes": 517806,"gastos_corrientes": 442970,"ingresos_capital": 21360, "gastos_capital": 103168,"resultado_primario": 7599,   "resultado_financiero": -6991},
        {"año": 2024, "ingresos_corrientes": 1591672,"gastos_corrientes":1161179,"ingresos_capital": 39550,"gastos_capital": 250519,"resultado_primario": 248375, "resultado_financiero": 219524},
    ]
}

gasto_corriente_2024 = {
    "fuente": "DiPEC — Ministerio de Economía Argentina",
    "unidad": "millones de pesos corrientes",
    "año": 2024,
    "datos": [
        {"concepto": "Gastos de consumo",            "monto": 845386, "detalle": "Personal + Bienes + Servicios"},
        {"concepto": "Personal",                      "monto": 735657, "detalle": "Remuneraciones al personal del Estado"},
        {"concepto": "Bienes de consumo",             "monto": 47579,  "detalle": ""},
        {"concepto": "Servicios",                     "monto": 62150,  "detalle": ""},
        {"concepto": "Rentas de la propiedad",        "monto": 28851,  "detalle": "Intereses de deuda"},
        {"concepto": "Transferencias corrientes",     "monto": 286942, "detalle": "Sector privado + Sector público"},
        {"concepto": "Al sector privado",             "monto": 103688, "detalle": ""},
        {"concepto": "Al sector público",             "monto": 183254, "detalle": ""},
        {"concepto": "TOTAL gastos corrientes",       "monto": 1161179,"detalle": ""},
    ]
}


# ═══════════════════════════════════════════════════════════════════════
# 3. ACTIVIDAD ECONÓMICA
# ═══════════════════════════════════════════════════════════════════════

pbg_constantes = {
    "fuente": "DiPEC — Departamento de Cuentas Provinciales",
    "unidad": "miles de pesos a precios constantes de 2004",
    "nota": "Datos del año 2024 de carácter provisorio",
    "datos": [
        {"año": 2004, "pbg_total": 3696464, "sector_bienes": 1406328, "sector_servicios": 2290136},
        {"año": 2005, "pbg_total": 4010107, "sector_bienes": 1551111, "sector_servicios": 2458996},
        {"año": 2006, "pbg_total": 4225402, "sector_bienes": 1588584, "sector_servicios": 2636819},
        {"año": 2007, "pbg_total": 4548294, "sector_bienes": 1652959, "sector_servicios": 2895334},
        {"año": 2008, "pbg_total": 4707750, "sector_bienes": 1721856, "sector_servicios": 2985894},
        {"año": 2009, "pbg_total": 4844307, "sector_bienes": 1712335, "sector_servicios": 3131972},
        {"año": 2010, "pbg_total": 5053614, "sector_bienes": 1808899, "sector_servicios": 3244715},
        {"año": 2011, "pbg_total": 5375231, "sector_bienes": 1863567, "sector_servicios": 3511664},
        {"año": 2012, "pbg_total": 5545932, "sector_bienes": 1886583, "sector_servicios": 3659349},
        {"año": 2013, "pbg_total": 5667284, "sector_bienes": 1821385, "sector_servicios": 3845899},
        {"año": 2014, "pbg_total": 5830365, "sector_bienes": 1903255, "sector_servicios": 3927110},
        {"año": 2015, "pbg_total": 6063316, "sector_bienes": 1955459, "sector_servicios": 4107857},
        {"año": 2016, "pbg_total": 5994338, "sector_bienes": 1851721, "sector_servicios": 4142617},
        {"año": 2017, "pbg_total": 6206366, "sector_bienes": 1927690, "sector_servicios": 4278676},
        {"año": 2018, "pbg_total": 6172768, "sector_bienes": 1898931, "sector_servicios": 4273837},
        {"año": 2019, "pbg_total": 6018466, "sector_bienes": 1835815, "sector_servicios": 4182651},
        {"año": 2020, "pbg_total": 5776501, "sector_bienes": 1674270, "sector_servicios": 4102231},
        {"año": 2021, "pbg_total": 6296518, "sector_bienes": 1889245, "sector_servicios": 4407273},
        {"año": 2022, "pbg_total": 6891750, "sector_bienes": 2117284, "sector_servicios": 4774466},
        {"año": 2023, "pbg_total": 6858376, "sector_bienes": 2047740, "sector_servicios": 4810635},
        {"año": 2024, "pbg_total": 6465553, "sector_bienes": 1825367, "sector_servicios": 4640186},
    ]
}

ipi = {
    "fuente": "DiPEC — Departamento de Cuentas Provinciales",
    "unidad": "índice base 2004=100 y variación porcentual anual",
    "datos": [
        {"año": 2004, "indice": 100.0, "variacion_anual_pct": None},
        {"año": 2005, "indice": 111.2, "variacion_anual_pct": 11.2},
        {"año": 2006, "indice": 115.5, "variacion_anual_pct": 3.9},
        {"año": 2007, "indice": 120.2, "variacion_anual_pct": 4.1},
        {"año": 2008, "indice": 125.2, "variacion_anual_pct": 4.1},
        {"año": 2009, "indice": 115.2, "variacion_anual_pct": -7.9},
        {"año": 2010, "indice": 118.8, "variacion_anual_pct": 3.1},
        {"año": 2011, "indice": 121.5, "variacion_anual_pct": 2.2},
        {"año": 2012, "indice": 118.4, "variacion_anual_pct": -2.5},
        {"año": 2013, "indice": 116.2, "variacion_anual_pct": -1.8},
        {"año": 2014, "indice": 122.0, "variacion_anual_pct": 5.0},
        {"año": 2015, "indice": 127.0, "variacion_anual_pct": 4.1},
        {"año": 2016, "indice": 120.5, "variacion_anual_pct": -5.1},
        {"año": 2017, "indice": 122.1, "variacion_anual_pct": 1.4},
        {"año": 2018, "indice": 117.1, "variacion_anual_pct": -4.2},
        {"año": 2019, "indice": 123.7, "variacion_anual_pct": 5.7},
        {"año": 2020, "indice": 118.2, "variacion_anual_pct": -4.5},
        {"año": 2021, "indice": 131.3, "variacion_anual_pct": 11.1},
        {"año": 2022, "indice": 130.9, "variacion_anual_pct": -0.3},
        {"año": 2023, "indice": 126.0, "variacion_anual_pct": -3.8},
        {"año": 2024, "indice": 113.3, "variacion_anual_pct": -10.0},
    ]
}

sectores_pbg_2024 = {
    "fuente": "DiPEC — Departamento de Cuentas Provinciales",
    "unidad": "miles de pesos constantes 2004 y participación porcentual",
    "año": 2024,
    "nota": "Datos provisorios",
    "datos": [
        {"sector": "G - Comercio al por mayor y menor",             "monto": 1122476, "participacion_pct": 16.1},
        {"sector": "K - Actividades inmobiliarias y empresariales", "monto": 1061083, "participacion_pct": 15.2},
        {"sector": "L - Administración pública y defensa",          "monto":  993128, "participacion_pct": 14.2},
        {"sector": "D - Industria manufacturera",                   "monto":  829367, "participacion_pct": 11.9},
        {"sector": "I - Transporte, almac. y comunicaciones",       "monto":  709172, "participacion_pct": 10.2},
        {"sector": "F - Construcción",                              "monto":  389840, "participacion_pct":  5.6},
        {"sector": "C - Minas y canteras",                          "monto":  376965, "participacion_pct":  5.4},
        {"sector": "A - Agricultura y ganadería",                   "monto":  342293, "participacion_pct":  4.9},
        {"sector": "M - Enseñanza",                                 "monto":  313347, "participacion_pct":  4.5},
        {"sector": "N - Servicios sociales y de salud",             "monto":  295582, "participacion_pct":  4.2},
        {"sector": "O - Otras actividades comunitarias",            "monto":  159366, "participacion_pct":  2.3},
        {"sector": "J - Intermediación financiera",                 "monto":  130504, "participacion_pct":  1.9},
        {"sector": "E - Electricidad, gas y agua",                  "monto":  123994, "participacion_pct":  1.8},
        {"sector": "H - Hoteles y restaurantes",                    "monto":  120138, "participacion_pct":  1.7},
        {"sector": "P - Servicio doméstico",                        "monto":   15972, "participacion_pct":  0.2},
    ]
}


# ═══════════════════════════════════════════════════════════════════════
# FUNCIONES DE ESCRITURA
# ═══════════════════════════════════════════════════════════════════════

def guardar_json(nombre, data):
    path = DATA_J / f"{nombre}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✓ JSON → {path.relative_to(ROOT)}")


def guardar_csv(nombre, datos, campos=None):
    if not datos:
        return
    path = DATA_C / f"{nombre}.csv"
    campos = campos or list(datos[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(datos)
    print(f"  ✓ CSV  → {path.relative_to(ROOT)}")


def generar_indice():
    """Genera data/json/indice.json con metadatos de todos los datasets."""
    indice = {
        "titulo": "Anuario Estadístico 2024 — Provincia de Jujuy",
        "generado": "2024",
        "fuente_general": "DiPEC — Dirección Provincial de Estadística y Censos",
        "repositorio": "https://github.com/TU_USUARIO/jujuy-estadisticas",
        "datasets": [
            {"id": "tasas_laborales",        "descripcion": "Tasas laborales anuales (actividad, empleo, desocupación, subocupación)", "archivos": {"json": "data/json/tasas_laborales.json",       "csv": "data/csv/tasas_laborales.csv"}},
            {"id": "pobreza_indigencia",     "descripcion": "Pobreza e indigencia semestrales (hogares y personas)",                    "archivos": {"json": "data/json/pobreza_indigencia.json",     "csv": "data/csv/pobreza_indigencia.csv"}},
            {"id": "condicion_actividad",    "descripcion": "Condición de actividad económica por grupo de edad — Censo 2022",         "archivos": {"json": "data/json/condicion_actividad_2022.json","csv": "data/csv/condicion_actividad_2022.csv"}},
            {"id": "sector_publico",         "descripcion": "Ejecución presupuestaria 2005–2024",                                       "archivos": {"json": "data/json/sector_publico.json",         "csv": "data/csv/sector_publico.csv"}},
            {"id": "gasto_corriente_2024",   "descripcion": "Estructura del gasto corriente 2024",                                     "archivos": {"json": "data/json/gasto_corriente_2024.json",   "csv": "data/csv/gasto_corriente_2024.csv"}},
            {"id": "pbg_constantes",         "descripcion": "PBG a precios constantes 2004–2024",                                      "archivos": {"json": "data/json/pbg_constantes.json",         "csv": "data/csv/pbg_constantes.csv"}},
            {"id": "ipi",                    "descripcion": "Índice de Producción Industrial 2004–2024",                                "archivos": {"json": "data/json/ipi.json",                    "csv": "data/csv/ipi.csv"}},
            {"id": "sectores_pbg_2024",      "descripcion": "Composición sectorial del PBG 2024",                                      "archivos": {"json": "data/json/sectores_pbg_2024.json",      "csv": "data/csv/sectores_pbg_2024.csv"}},
        ]
    }
    guardar_json("indice", indice)


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n🗂  Generando datos — Anuario Estadístico 2024, Jujuy\n")

    print("📋 Trabajo e Ingresos")
    guardar_json("tasas_laborales",     tasas_laborales)
    guardar_csv ("tasas_laborales",     tasas_laborales["datos"])
    guardar_json("pobreza_indigencia",  pobreza_indigencia)
    guardar_csv ("pobreza_indigencia",  pobreza_indigencia["datos"])
    guardar_json("condicion_actividad_2022", condicion_actividad_2022)
    guardar_csv ("condicion_actividad_2022", condicion_actividad_2022["datos"])

    print("\n🏛  Sector Público")
    guardar_json("sector_publico",      sector_publico)
    guardar_csv ("sector_publico",      sector_publico["datos"])
    guardar_json("gasto_corriente_2024",gasto_corriente_2024)
    guardar_csv ("gasto_corriente_2024",gasto_corriente_2024["datos"])

    print("\n📈 Actividad Económica")
    guardar_json("pbg_constantes",      pbg_constantes)
    guardar_csv ("pbg_constantes",      pbg_constantes["datos"])
    guardar_json("ipi",                 ipi)
    guardar_csv ("ipi",                 ipi["datos"])
    guardar_json("sectores_pbg_2024",   sectores_pbg_2024)
    guardar_csv ("sectores_pbg_2024",   sectores_pbg_2024["datos"])

    print("\n📑 Índice general")
    generar_indice()

    print("\n✅ Listo. Archivos generados en data/json/ y data/csv/\n")
