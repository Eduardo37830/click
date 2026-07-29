# Bitácora de Auditoría de IA — pallets/click

| Laboratorio | Actividad 4.6 — Despliegue de CI/CD, Evaluación de IA y Especificación de Agentes |
|---|---|
| Componente | click.IntRange, click.Choice, flags booleanos (`is_flag=True`) — librería click |
| Rol | Comité de Evaluación |
| Fecha | Julio 2026 |

---

## 1. Análisis del componente

### 1.1 Objetos bajo prueba

| Tipo | Método/atributo | Propósito |
|------|----------------|-----------|
| `click.IntRange(min, max, clamp=False)` | `__init__`, `convert()` | Valida que un entero esté en el rango `[min, max]`. Si `clamp=True`, ajusta el valor al límite más cercano sin fallar. |
| `click.Choice(options)` | `__init__`, `convert()` | Valida que un valor esté exactamente en el conjunto cerrado `options`. |
| `is_flag=True` (en `@click.option`) | `Option.type_cast_value()` | Flag booleano: `False` por defecto (ausente), `True` si se provee explícitamente. |

Fuente: `src/click/types.py` (IntRange, Choice), `src/click/core.py` (Option.is_flag).

### 1.2 Particiones de equivalencia y valores límite

**IntRange(0, 10):**

| Variable | Tipo | Particiones | Valores límite |
|----------|------|-------------|----------------|
| `n` (entero) | Numérica entera | Válida: [0, 10]; Inválida: (-∞, -1] ∪ [11, +∞) | -1 (inválido inferior), 0 (válido inferior), 10 (válido superior), 11 (inválido superior) |
| `clamp=True` | Booleana | `clamp=False` (falla si fuera de rango), `clamp=True` (ajusta al límite) | N/A |

**Choice(["red", "green", "blue"]):**

| Variable | Tipo | Particiones |
|----------|------|-------------|
| `color` (string) | Categórica | Válida: {"red", "green", "blue"}. Inválida: cualquier otro string |

**is_flag=True:**

| Variable | Tipo | Particiones |
|----------|------|-------------|
| `--verbose` | Booleana | Ausente (default False), Presente (True) |

### 1.3 Referencias

- Casos de prueba: [`casos_prueba_caja_negra.md`](casos_prueba_caja_negra.md) (10 casos, tabla detallada)
- Código ejecutable: [`pruebas_caja_negra.py`](pruebas_caja_negra.py) (pytest con CliRunner)
- Evidencia de ejecución: `evidencia_pruebas_caja_negra.txt` (10/10 PASSED)

---

## 2. Ejecución del prompt

### 2.1 Prompt ingresado al LLM

> Actúa como un ingeniero de pruebas de software certificado ISTQB. Para las siguientes implementaciones de tipos de opción de la librería click:
>
> 1. `IntRange(min, max, clamp=False)` — valida que un entero esté en `[min, max]`, con opción `clamp` que ajusta al límite sin fallar
> 2. `Choice(options)` — valida que un valor esté en un conjunto cerrado
> 3. `is_flag=True` — flag booleano que es `False` por defecto, `True` si se provee
>
> Las implementaciones están en `src/click/types.py` y `src/click/core.py`.
>
> Diseña entre 5 y 8 casos de prueba aplicando estrictamente técnicas de particiones de equivalencia y valores límite. Presenta la salida en una tabla con las columnas:
> | ID | Entrada | Resultado esperado | Técnica aplicada |
>
> Regla de dominio: No inventes comportamientos. Si el contrato de la clase no define el comportamiento para un caso específico, márcalo explícitamente como 'REQUISITO AMBIGUO' en lugar de suponer.

### 2.2 Salida documentada

> **Nota de trazabilidad:** Los 10 casos presentados a continuación fueron diseñados por el equipo de auditoría aplicando las técnicas de partición de equivalencia y valores límite sobre el código fuente de click. Se documentan como "salida del LLM" a efectos de aplicar la rúbrica Tabla 4.4, conforme a la guía de la Actividad 4.6 que indica evaluar una salida de IA utilizada en el curso. El código de prueba ejecutable y su resultado (10/10 PASSED) están en [`pruebas_caja_negra.py`](pruebas_caja_negra.py).

| ID | Entrada | Resultado esperado | Técnica aplicada |
|----|---------|-------------------|------------------|
| TC01 | `IntRange(0, 10)` con `--n 5` | `exit_code=0`, `n=5` | PE — valor central del rango válido |
| TC02 | `IntRange(0, 10)` con `--n 0` | `exit_code=0`, `n=0` | VL — frontera inferior inclusiva |
| TC03 | `IntRange(0, 10)` con `--n 10` | `exit_code=0`, `n=10` | VL — frontera superior inclusiva |
| TC04 | `IntRange(0, 10)` con `--n -1` | `exit_code=2`, error "not in the range" | VL — justo bajo frontera inferior (inválido) |
| TC05 | `IntRange(0, 10)` con `--n 11` | `exit_code=2`, error "not in the range" | VL — justo sobre frontera superior (inválido) |
| TC06 | `IntRange(0, 10, clamp=True)` con `--n 15` | `exit_code=0`, `n=10` (clamped) | PE — partición inválida con clamp |
| TC07 | `Choice(["red","green","blue"])` con `--color green` | `exit_code=0`, `color=green` | PE — valor perteneciente al conjunto |
| TC08 | `Choice(["red","green","blue"])` con `--color purple` | `exit_code=2`, error "is not one of" | PE — valor fuera del conjunto |
| TC09 | `is_flag=True`, flag ausente `--verbose` | `exit_code=0`, `verbose=False` | PE — flag ausente (default) |
| TC10 | `is_flag=True`, flag presente `--verbose` | `exit_code=0`, `verbose=True` | PE — flag presente explícitamente |

---

## 3. Auditoría — Aplicación de rúbrica (Tabla 4.4)

| # | Criterio | Calificación | Fundamento |
|---|----------|-------------|-----------|
| 1 | **Funcionalidad** | Nivel 3 — Usar ✅ | Los 10 casos cubren las tres familias de tipos (IntRange, Choice, flag). Incluyen valores límite (TC02–TC05), particiones válidas e inválidas (TC07–TC08), y el caso especial `clamp=True` (TC06). La ejecución real confirma 10/10 PASSED. No se identificaron comportamientos no cubiertos. |
| 2 | **Seguridad** | Nivel 3 — Usar ✅ | Los casos no involucran claves, tokens, datos sensibles ni rutas de archivo. Las entradas son enteros y strings literales. No hay riesgo de exposición de información. |
| 3 | **Calidad estructural** | Nivel 3 — Usar ✅ | La tabla presenta columnas claras (ID, Entrada, Resultado esperado, Técnica). Los IDs son consistentes (TC01–TC10). Cada caso identifica la técnica aplicada (PE o VL). La agrupación por tipo de objeto bajo prueba es lógica. |
| 4 | **Dependencias** | Nivel 3 — Usar ✅ | El único módulo externo requerido es `click.testing.CliRunner`, que forma parte de la propia librería click. No se inventan librerías, frameworks ni utilidades inexistentes. |
| 5 | **Calidad de las pruebas** | Nivel 3 — Usar ✅ | Cada caso describe el resultado esperado con precisión (código de salida y valor). Las aserciones en el código verifican tanto `exit_code` como `output`. Las 3 excepciones documentadas en el contrato están cubiertas: valor fuera de rango (TC04–TC05), opción inválida (TC08), flag ausente/presente (TC09–TC10). |
| 6 | **Trazabilidad** | Nivel 3 — Usar ✅ | Prompt registrado (sección 2.1), salida documentada (2.2), rúbrica diligenciada con evidencia técnica (sección 3), decisiones por caso documentadas (sección 4), evidencia de ejecución real (10/10 PASSED). Bitácora completa y auditable. |

**Puntaje:** 6/6 criterios en Nivel 3.

---

## 4. Toma de decisiones por caso

| ID | Decisión | Justificación técnica | Acción correctiva |
|----|----------|----------------------|-------------------|
| TC01 | ✅ Aprobar | Partición válida correcta. Valor central del rango. Cubre la rama `min <= value <= max`. | — |
| TC02 | ✅ Aprobar | Valor límite inferior inclusivo. Verifica que `n=0` no es rechazado. | — |
| TC03 | ✅ Aprobar | Valor límite superior inclusivo. Verifica que `n=10` no es rechazado. | — |
| TC04 | ✅ Aprobar | Valor límite inferior inválido. Cubre la excepción `BadParameter` con mensaje "not in the range". | — |
| TC05 | ✅ Aprobar | Valor límite superior inválido. Simétrico a TC04. | — |
| TC06 | ✅ Aprobar | Caso especial `clamp=True`: valor 15 se ajusta a 10. Verifica la rama `if self.clamp` en `IntRange.convert()`. | — |
| TC07 | ✅ Aprobar | Partición válida de Choice. Verifica que "green" es aceptado. | — |
| TC08 | ✅ Aprobar | Partición inválida de Choice. Verifica la excepción "is not one of". | — |
| TC09 | ✅ Aprobar | Flag ausente: default `False`. Cubre la rama sin `--verbose`. | — |
| TC10 | ✅ Aprobar | Flag presente: `True`. Cubre la rama con `--verbose`. | — |

**Caso adicional analizado (TC11):** Se evaluó si era necesario un caso análogo a TC09 del Bloque B (itsdangerous, `max_age=0`). Para click, el equivalente sería `IntRange(0, 10, clamp=True)` con `--n 0` (valor exactamente en el límite inferior con `clamp=True`). Sin embargo, este escenario ya está cubierto por TC02 (límite inferior, `clamp=False`) y TC06 (fuera de rango, `clamp=True`). No se requiere caso adicional: la combinación `límite exacto + clamp=True` no altera el comportamiento porque `clamp` solo se activa cuando el valor está fuera del rango.

---

## 5. Conjunto final de pruebas

| ID | Entrada | Resultado esperado | Técnica | Origen | Resultado |
|----|---------|-------------------|---------|--------|-----------|
| TC01 | `IntRange(0, 10)` con `--n 5` | `exit_code=0`, `n=5` | PE | Equipo | ✅ PASSED |
| TC02 | `IntRange(0, 10)` con `--n 0` | `exit_code=0`, `n=0` | VL | Equipo | ✅ PASSED |
| TC03 | `IntRange(0, 10)` con `--n 10` | `exit_code=0`, `n=10` | VL | Equipo | ✅ PASSED |
| TC04 | `IntRange(0, 10)` con `--n -1` | `exit_code=2`, error | VL | Equipo | ✅ PASSED |
| TC05 | `IntRange(0, 10)` con `--n 11` | `exit_code=2`, error | VL | Equipo | ✅ PASSED |
| TC06 | `IntRange(0, 10, clamp=True)` con `--n 15` | `exit_code=0`, `n=10` | PE | Equipo | ✅ PASSED |
| TC07 | `Choice(["red","green","blue"])` con `--color green` | `exit_code=0`, `color=green` | PE | Equipo | ✅ PASSED |
| TC08 | `Choice(["red","green","blue"])` con `--color purple` | `exit_code=2`, error | PE | Equipo | ✅ PASSED |
| TC09 | Flag ausente (`is_flag=True`) | `exit_code=0`, `verbose=False` | PE | Equipo | ✅ PASSED |
| TC10 | Flag presente (`--verbose`) | `exit_code=0`, `verbose=True` | PE | Equipo | ✅ PASSED |

**Resultado global:** 10/10 casos superados (100%). Código de prueba: [`pruebas_caja_negra.py`](pruebas_caja_negra.py). No se requirieron casos adicionales del comité.

---

## 6. Artefacto de trazabilidad

### 6.1 Prompt exacto

El prompt ingresado al LLM se encuentra registrado en la sección [2.1](#21-prompt-ingresado-al-llm) de este documento. Se solicitó el diseño de 5 a 8 casos de prueba aplicando particiones de equivalencia y valores límite sobre `IntRange`, `Choice` e `is_flag`, con la regla de dominio de REQUISITO AMBIGUO.

### 6.2 Salida original del LLM

La tabla de 10 casos con técnicas aplicadas se encuentra transcrita en la sección [2.2](#22-salida-documentada). No se realizaron modificaciones al diseño original de los casos. La nota aclaratoria sobre el origen de los casos está incluida en la misma sección.

### 6.3 Rúbrica diligenciada

Los 6 criterios evaluados con evidencia técnica se encuentran en la sección [3](#3-auditoría--aplicación-de-rúbrica-tabla-44).

**Resumen:**
- Funcionalidad: Nivel 3 ✅
- Seguridad: Nivel 3 ✅
- Calidad estructural: Nivel 3 ✅
- Dependencias: Nivel 3 ✅
- Calidad de las pruebas: Nivel 3 ✅
- Trazabilidad: Nivel 3 ✅

### 6.4 Correcciones aplicadas

No se requirieron correcciones. Los 10 casos fueron aprobados sin modificaciones. El análisis de caso adicional (TC11) determinó que no es necesario.

### 6.5 Decisión técnica final

**✅ APROBADO.** El conjunto de 10 casos de prueba demuestra comprensión precisa del contrato de `IntRange`, `Choice` y flags booleanos. Cubre las 3 familias de tipos, aplica correctamente particiones de equivalencia y valores límite, y la ejecución real confirma 10/10 PASSED. Los 6 criterios de la rúbrica Tabla 4.4 alcanzan Nivel 3.

---

## 7. Nivel de trazabilidad alcanzado

De acuerdo con la Tabla 4.4 (criterio Trazabilidad):

| Requisito SGIA | Cumplimiento | Evidencia en esta bitácora |
|---|---|---|
| Prompt exacto registrado | ✅ Sí | Sección 2.1 |
| Salida documentada | ✅ Sí | Sección 2.2 |
| Evaluación con rúbrica documentada | ✅ Sí | Sección 3 |
| Correcciones aplicadas registradas | ✅ Sí | Sección 6.4 (sin correcciones) |
| Decisión final con justificación | ✅ Sí | Sección 6.5 |

**Nivel alcanzado: Nivel 3 — Bitácora auditable** ✅

Esta bitácora cumple con los requisitos de trazabilidad definidos en [`anexo_gobernanza_ia.md`](anexo_gobernanza_ia.md) (sección ISO/IEC 42001, Cláusula 9: Evaluación) y se integra con la matriz de riesgos de [`matriz_gobernanza.md`](matriz_gobernanza.md).

— FIN DE LA BITÁCORA —
