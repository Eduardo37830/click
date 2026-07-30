# Entregables LUNES — Auditoría click (pallets/click → Eduardo37830/click)

Hola

Fuentes: `gh` CLI sobre `pallets/click`, API pública de SonarCloud
(`Eduardo37830_click`), conteo de líneas local. Todo verificable con las URLs citadas.

---

## 1. Diagnóstico de defectos — 19 issues cerrados con commit/PR asociado

| # Issue | Error (síntoma reportado) | Defecto (causa raíz) | Falla (efecto) | Severidad* | Módulo | PR/commit |
|---|---|---|---|---|---|---|
| [#3572](https://github.com/pallets/click/issues/3572) | Códigos ANSI no se limpian en `confirm()` tras actualizar a 8.4 | `strip_ansi` no se aplicaba en el nuevo flujo de streams | Salida con caracteres de escape visibles en terminales sin color | Media | `termui.py` | [PR #3653](https://github.com/pallets/click/pull/3653) |
| [#3502](https://github.com/pallets/click/issues/3502) | Completado fish roto en 8.4.1 | Newlines/tabs en help text no se escapaban | Autocompletado fish generaba script inválido | Alta (regresión de release) | `shell_completion.py` | [PR #3504](https://github.com/pallets/click/pull/3504) |
| [#3501](https://github.com/pallets/click/issues/3501) | `isolated_filesystem()` no es thread-safe | Uso de `os.chdir` global sin lock | Condición de carrera en tests paralelos | Media | `testing.py` | [PR #3704](https://github.com/pallets/click/pull/3704) |
| [#3489](https://github.com/pallets/click/issues/3489) | Ejemplo "Advanced Patterns" usa `urllib.urlopen` (Python 2) | Documentación no migrada a `urllib` API actual | Ejemplo de docs no ejecuta en Python 3 | Baja | `docs/advanced.md` | [PR #3503](https://github.com/pallets/click/pull/3503) |
| [#3487](https://github.com/pallets/click/issues/3487) | `echo()` con bytes/bytearray vacío lanza `TypeError` | Falta manejo del caso "cadena vacía" en la rama de bytes | Crash al hacer `echo(b"")` | Alta | `utils.py` | [PR #3493](https://github.com/pallets/click/pull/3493) |
| [#3481](https://github.com/pallets/click/issues/3481) | Utilidades Python 2 y poco usadas siguen en el código | Deuda técnica acumulada, sin deprecación formal | Superficie de mantenimiento innecesaria | Baja | `core.py`, `utils.py`, `types.py` | [PR #3695](https://github.com/pallets/click/pull/3695) |
| [#3476](https://github.com/pallets/click/issues/3476) | Test depende de `-Werror` para pasar | Test no usa context manager idiomático para capturar warning | Falso negativo/positivo según flags del intérprete | Baja | `tests/test_options.py` | [PR #3591](https://github.com/pallets/click/pull/3591) |
| [#3458](https://github.com/pallets/click/issues/3458) | `get_parameter_source()` retorna `None` en 8.4.0 | Regresión: la fuente no se registra durante conversión/eager callbacks | Lógica que depende del origen del parámetro falla silenciosamente | Alta (regresión de release) | `core.py` | [PR #3484](https://github.com/pallets/click/pull/3484) |
| [#3449](https://github.com/pallets/click/issues/3449) | "I/O operation on closed file" con `CliRunner` + `echo_via_pager` | GC cierra un `stdout` prestado | Excepción intermitente en tests que usan pager | Alta | `_termui_impl.py` | [PR #3482](https://github.com/pallets/click/pull/3482) — *fix parcial, completado en PR #3533 / v8.4.2* |
| [#3403](https://github.com/pallets/click/issues/3403) | Comportamiento de `default` en pares de flags enable/disable cambia entre versiones | Lógica de resolución de default no distinguía el par de flags | Valor por defecto incorrecto en flags booleanos combinados | Media | `core.py` | [PR #3404](https://github.com/pallets/click/pull/3404) |
| [#3384](https://github.com/pallets/click/issues/3384) | Click 8.3.3 rompe `pytest` cuando el fd del stream está duplicado | Cambio en manejo de `fileno` sin considerar streams duplicados | `pytest` no captura output / crashea en algunos entornos | Crítica (rompe herramienta externa ampliamente usada) | `testing.py` | [PR #3391](https://github.com/pallets/click/pull/3391) |
| [#3360](https://github.com/pallets/click/issues/3360) | `HelpFormatter.write_usage` produce caracteres espurios sin argumentos | Formateo de usage no maneja el caso de comando sin args | Help text con salida corrupta | Media | `formatting.py` | [PR #3434](https://github.com/pallets/click/pull/3434) |
| [#3298](https://github.com/pallets/click/issues/3298) | `semver.Version` como default causa error | Chequeo de "string vacío" mal implementado (especulativo/duplicado) | Excepción al usar objetos no-str como valor por defecto | Media | `core.py` | [PR #3299](https://github.com/pallets/click/pull/3299) |
| [#3277](https://github.com/pallets/click/issues/3277) | Completado zsh falla con "parse error near elif" en Windows | Script de completado zsh generado con sintaxis no portable | Autocompletado zsh no funciona en Windows | Media | `shell_completion.py` | [PR #3466](https://github.com/pallets/click/pull/3466) |
| [#3242](https://github.com/pallets/click/issues/3242) | `stdin` no se limpia (flush) al escribir a un pager | Falta `flush()` tras escritura en `echo_via_pager` con generador | Salida no se transmite hasta llenar el buffer (percibido como "colgado") | Media | `termui.py` | [PR #3534](https://github.com/pallets/click/pull/3534) |
| [#3164](https://github.com/pallets/click/issues/3164) | `click.launch()` no funciona con URLs no locales en Windows | Manejo de rutas/URLs no diferenciado en `_winconsole`/`_termui_impl` | Comando `launch` falla silenciosamente en Windows | Media | `_termui_impl.py` | [PR #3186](https://github.com/pallets/click/pull/3186) |
| [#3136](https://github.com/pallets/click/issues/3136) | `Sentinel` no disponible en contexto durante callbacks de opciones | `Context` no exponía el sentinel usado internamente | Callbacks no pueden distinguir "no provisto" de valores reales | Baja | `core.py` | [PR #3137](https://github.com/pallets/click/pull/3137) |
| [#3128](https://github.com/pallets/click/issues/3128) | `test_edit` falla con BSD sed | Test asume sintaxis GNU sed | Falso negativo de CI en macOS/BSD | Baja | `tests/test_termui.py` | [PR #3129](https://github.com/pallets/click/pull/3129) |
| [#3125](https://github.com/pallets/click/issues/3125) | `version_option` ignora `package_name` | Resolución de distribución no consideraba nombre de paquete top-level distinto al de distribución | `--version` reporta versión incorrecta o falla para paquetes como `Pillow`/`PyJWT` | Media | `decorators.py` | [PR #3582](https://github.com/pallets/click/pull/3582) |

\* Severidad estimada por el equipo auditor según impacto funcional (crash/regresión pública = Alta-Crítica; comportamiento incorrecto acotado = Media; cosmético/docs/test-only = Baja). Ajustar según el criterio de severidad que definan en el Anexo 25010.

**Candidato para CoNQ:** [#3384](https://github.com/pallets/click/issues/3384) — rompe `pytest` en entornos con fd duplicado. Es el de mayor blast radius (afecta a *cualquier* proyecto downstream que use `CliRunner` bajo pytest), tiene fecha de introducción (release 8.3.3) y fecha de fix (PR #3391) bien acotadas para memoria de cálculo de costo de no-calidad.

## Memoria de cálculo — CoNQ (Costo de No Calidad) del incidente #3384

### 1. Línea de tiempo verificada (fuente: `gh issue view`/`gh pr view`/`CHANGES.md`)

| Hito | Fecha | Fuente |
|---|---|---|
| Release que introduce la regresión (`8.3.3`) | 2026-04-22 | `gh release list` |
| Issue reportado por un usuario (`#3384`) | 2026-04-27 (5 días después del release) | `gh issue view 3384` |
| PR de fix abierto (`#3391`) | 2026-04-29 (2 días después del reporte) | `gh pr view 3391` |
| PR de fix mergeado | 2026-05-16 (17 días de revisión) | `gh pr view 3391` |
| Release con el fix (`8.4.0`) | 2026-05-17 | `CHANGES.md` línea 110, `gh release list` |
| **Ventana de exposición del defecto** | **25 días** (8.3.3 → 8.4.0) | calculado |

El PR de fix (`#3391`, "Add capture mode to `CliRunner` and revert default
`fileno` exposure") tiene **391 líneas agregadas, 98 eliminadas, 4 archivos
modificados, 2 commits** — no es un one-liner: introduce un concepto nuevo
(`capture=` mode en `CliRunner`) para poder revertir el comportamiento
problemático de 8.3.3 sin romper el caso de uso que esa versión intentaba
habilitar. El issue acumuló 7 comentarios de discusión antes de cerrarse.

### 2. Tarifa/hora declarada

Se declara una tarifa de **$60.000 COP/hora** (≈ USD 15/hora al cambio de
referencia), correspondiente al costo totalmente cargado (salario +
prestaciones + overhead) de un desarrollador Python senior en Colombia según
bandas salariales de mercado 2025-2026 para perfiles de mantenimiento
open-source / backend senior. Se aplica la **misma tarifa a todos los roles**
(mantenedor, revisor, equipos downstream) como simplificación metodológica
explícita — en la práctica el costo real de un mantenedor voluntario
internacional de Pallets puede diferir, pero no hay forma de observarlo
objetivamente desde el historial público, así que se usa una tarifa de
referencia única y se declara como supuesto.

### 3. Desglose de horas por actividad

| Actividad | Horas estimadas | Justificación |
|---|---|---|
| **Diagnóstico** (mantenedor lee el issue, reproduce el fallo, identifica la causa raíz en el manejo de `fileno`/`fd`) | 3.0 h | Brecha de 2 días calendario entre reporte y PR abierto; para un mantenedor voluntario con otras responsabilidades, se estima que el trabajo efectivo de diagnóstico (no el tiempo calendario) fue de medio día laboral |
| **Fix** (implementación del PR #3391: revertir comportamiento de 8.3.3 + diseñar el nuevo modo `capture=`) | 6.0 h | 391 líneas agregadas / 98 eliminadas en 4 archivos, 2 commits; el fix no es trivial porque debe preservar el caso de uso original de 8.3.3 sin romper la compatibilidad con pytest |
| **Revisión de código** (aprobación del PR, discusión en 7 comentarios del issue) | 2.0 h | 17 días de brecha calendario entre apertura y merge sugieren idas y vueltas de revisión, no bloqueo continuo; se estima el tiempo efectivo de revisión, no el calendario |
| **Release** (changelog, build, tag, publicación a PyPI vía `publish.yaml`) | 0.5 h | Costo marginal atribuible a este fix específico dentro de una release (8.4.0) que agrupa múltiples cambios; el proceso de release en sí (`uv build` → draft release → OIDC publish) está automatizado |
| **Subtotal interno (mantenedores)** | **11.5 h** | — |
| **Impacto downstream** (equipos que actualizaron a 8.3.3 y sufrieron fallos de CI/pytest durante la ventana de 25 días, antes de que 8.4.0 estuviera disponible) | 50 h | Supuesto explícito: se estima que ~50 proyectos downstream (de los miles que dependen de `click`) actualizaron a `8.3.3` durante la ventana de 25 días y usan `CliRunner` bajo `pytest` con captura a nivel de `fd` (el caso específico que rompe). Cada equipo afectado invierte en promedio ~1 hora en diagnosticar un fallo de CI intermitente/confuso antes de identificar que la causa es la librería y no su propio código (buscar en logs, hacer bisect de dependencias, encontrar el issue de GitHub). **Esta es la cifra más especulativa del cálculo** — no hay telemetría pública de adopción de versión ni de uso de `capture="fd"`; se declara como supuesto conservador (50 equipos es una fracción muy pequeña de la base de instalación de `click`, que solo en PyPI tiene millones de descargas/mes) |
| **Total horas** | **61.5 h** | 11.5 h internas + 50 h downstream |

### 4. Costo total de no calidad (CoNQ)

```text
CoNQ = Total horas × Tarifa/hora
     = 61.5 h × $60.000 COP/h
     = $3.690.000 COP (≈ USD 925)
```

**Desglose:**

- Costo interno (Pallets, diagnóstico+fix+revisión+release): 11.5 h × $60.000 = **$690.000 COP** (≈ USD 173)
- Costo downstream (equipos consumidores afectados): 50 h × $60.000 = **$3.000.000 COP** (≈ USD 750)
- **El 81% del CoNQ de este incidente lo pagan los consumidores de la librería, no Pallets** — es la naturaleza de un defecto en una dependencia transitiva ampliamente usada: el costo de diagnóstico se externaliza a cientos de equipos que no tienen forma de saber que el problema no es su código.

### 5. Supuestos explícitos (para defender el número ante réplicas)

1. Tarifa única de $60.000 COP/h para todos los roles — simplificación declarada, no observación real de costos de mantenedores voluntarios internacionales.
2. Horas de diagnóstico/fix/revisión estimadas a partir de brechas calendario entre eventos de GitHub (issue→PR→merge), **no** de tiempo efectivo medido (no existe telemetría de tiempo real de los mantenedores).
3. El número de equipos downstream afectados (50) es una **estimación conservadora no verificable con datos públicos** — se declara explícitamente como el supuesto más débil del cálculo, y el CoNQ total escala linealmente con este número si el equipo evaluador quiere ajustarlo (p. ej., 500 equipos → CoNQ ≈ $30.7M COP).
4. No se incluye el costo de reputación/confianza (usuarios que consideran migrar a otra librería de CLI tras el incidente) por no ser cuantificable de forma objetiva — se documenta como riesgo cualitativo adicional, no como parte del CoNQ numérico.

---

## 2. Quality Gates reales del proceso as-is

Evidencia extraída directamente del repo (no inferida):

| Etapa | Gate real | Evidencia |
|---|---|---|
| Pre-commit local | `ruff-check` + `ruff-format` (lint/estilo), `uv-lock` (lockfile consistency), `codespell` (typos, auto-fix), `check-merge-conflict`, `debug-statements`, `fix-byte-order-marker`, `trailing-whitespace`, `end-of-file-fixer` | [.pre-commit-config.yaml](.pre-commit-config.yaml) |
| CI — matriz de pruebas | 9 combinaciones: Python 3.10–3.14, 3.14 free-threaded (`3.14t`), Windows, macOS, PyPy 3.11 — vía `tox` | [.github/workflows/tests.yaml](.github/workflows/tests.yaml) |
| CI — tipado estático | Job `typing` separado, ejecuta `tox -e typing` (mypy) | [.github/workflows/tests.yaml](.github/workflows/tests.yaml) |
| CI — seguridad de workflows | `zizmor` analiza los propios workflows de GitHub Actions | [.github/workflows/zizmor.yaml](.github/workflows/zizmor.yaml) |
| CI — regresión downstream | Workflow dedicado corre el test suite de Flask contra Click (detecta breaking changes en un consumidor real) | mencionado en `docs/contributing.md`, `.github/workflows/test-flask.yaml` |
| Revisión humana | Merge a `main` requiere PR (no hay push directo evidenciado en el historial de PRs revisado) | histórico de PRs en GitHub |
| Registro de cambios | Cada entrada relevante de `CHANGES.md` referencia `{issue}` y `{pr}` — trazabilidad obligatoria de facto | [CHANGES.md](CHANGES.md) |
| Release → PyPI | Workflow `publish.yaml`: build con `uv build` → draft GitHub Release → publish a PyPI vía **OIDC trusted publishing** (`id-token: write`, sin token estático) | [.github/workflows/publish.yaml](.github/workflows/publish.yaml) |
| Gate de dependencias | `uv-lock` hook + Dependabot (evidenciado en top-contributors: `dependabot[bot]`, `dependabot-preview[bot]`) | pre-commit config + `git shortlog` |

**Nota para el diagrama `.drawio`:** el flujo real es
`Contribuyente (fork+PR)` → `pre-commit (local, opcional)` → `CI: tests matrix + typing + zizmor + flask-regression` → `Mantenedor (review humana)` → `merge a main` → `CHANGES.md actualizado` → `tag de versión` → `publish.yaml: build → draft release → PyPI (OIDC)`.
No hay gate de cobertura de código ni de análisis estático de calidad (Sonar/CodeQL) integrado nativamente — es exactamente el vacío que ustedes están llenando con la integración de SonarCloud.

---

## 3. Métricas DORA — muestra: últimos 10 PRs mergeados a `main`

Rango: PR #3676 (2026-07-08) a PR #3721 (2026-07-23).

**Fórmula lead time for changes** = `mergedAt − createdAt` por PR (aproximación: no se midió tiempo de primer commit, solo apertura de PR, por limitación de datos disponibles vía `gh`).

| PR | Título | Creado | Merged | Lead time |
|---|---|---|---|---|
| [#3676](https://github.com/pallets/click/pull/3676) | Restore `test_echo_color_flag` | 07-08 10:42 | 07-08 15:57 | 5.3 h |
| [#3677](https://github.com/pallets/click/pull/3677) | Validate `style()` color arguments | 07-08 11:21 | 07-08 16:05 | 4.7 h |
| [#3678](https://github.com/pallets/click/pull/3678) | Fix parsing when a parameter is named `help` | 07-08 12:19 | 07-10 03:24 | 39.1 h |
| [#3681](https://github.com/pallets/click/pull/3681) | Strip all ANSI sequences | 07-09 14:07 | 07-10 03:14 | 13.1 h |
| [#3685](https://github.com/pallets/click/pull/3685) | Fix `sdist` include (CHANGES.md) | 07-12 16:59 | 07-23 11:45 | 258.8 h |
| [#3695](https://github.com/pallets/click/pull/3695) | Mark private functions, deprecate Py2 utils | 07-16 20:33 | 07-17 19:25 | 22.9 h |
| [#3697](https://github.com/pallets/click/pull/3697) | Pre-8.5.0 changelog/doc fixes | 07-17 09:36 | 07-24 20:27 | 178.8 h |
| [#3704](https://github.com/pallets/click/pull/3704) | Deprecate `isolated_filesystem()` | 07-17 21:39 | 07-20 17:43 | 68.1 h |
| [#3715](https://github.com/pallets/click/pull/3715) | Parametrize deprecation tests | 07-22 18:51 | 07-22 22:29 | 3.6 h |
| [#3721](https://github.com/pallets/click/pull/3721) | Update all GitHub actions | 07-23 11:39 | 07-23 18:58 | 7.3 h |

- **Lead time promedio:** 60.2 h (~2.5 días)
- **Lead time mediano:** 18.0 h (~0.75 días) — la media está sesgada por 2 PRs de documentación/housekeeping que tardaron 7–11 días en mergear; los fixes de código real mergean en horas.
- **Clasificación DORA:** Alto rendimiento (mediana < 1 día; la media se degrada por PRs no urgentes).

**Frecuencia de despliegue** (fórmula: releases ÷ días entre la primera y última release de la muestra):
Ventana 8.3.0 (2025-09-18) → 8.4.2 (2026-06-26) = 6 releases en 281 días → **1 release cada ~47 días (~6.7 semanas)**.
Supuesto: se cuentan solo tags publicados (no drafts); cadencia irregular (8.3.0→8.3.1 tomó 58 días, 8.4.1→8.4.2 tomó 35 días).
**Clasificación DORA:** Media (entre 1/semana y 1/mes-6meses).

**Change failure rate** (fórmula: releases de parche que corrigen regresiones introducidas por la release inmediatamente anterior ÷ total de releases de la muestra, según texto de `CHANGES.md`):
De 3 releases de la línea 8.4.x, **2 de 3 (66.7%)** fueron parches motivados por regresiones de la release previa:
- 8.4.1 (4 días después de 8.4.0) corrige 6 regresiones/bugs de 8.4.0, incl. `get_parameter_source()` roto (#3458).
- 8.4.2 (34 días después) corrige fish completion roto por 8.4.0 (#3502) y **completa** un fix parcial de 8.4.1 (#3449, "completing the partial fix from #3482").
**Clasificación DORA:** Alta/Elevada (>15% se considera señal de alerta; aquí el patrón es sistemático en esta línea de versión) — dato fuerte para el dictamen.

**MTTR** (fórmula: fecha de release del fix − fecha de reporte del issue):
- #3458 (`get_parameter_source` roto) reportado en release 8.4.0 (2026-05-17), corregido en 8.4.1 (2026-05-21) → **4 días**.
- #3449 (I/O on closed file) reportado antes de 8.4.0, fix parcial en 8.4.1 (2026-05-21), fix completo en 8.4.2 (2026-06-24) → **fix completo tardó ~34+ días desde el primer intento**, evidencia de que el primer fix fue incompleto.
Supuesto: se usa la fecha de release pública como proxy de "restauración", no la fecha del merge del PR (más conservador, refleja tiempo real que el usuario final estuvo afectado).

---

## 4. Pareto de hallazgos y densidad de defectos/KLOC (datos reales de SonarCloud)

Fuente: `GET sonarcloud.io/api/issues/search?componentKeys=Eduardo37830_click&resolved=false` — **73 issues abiertos** al [27-jul-2026], [tablero](https://sonarcloud.io/project/issues?id=Eduardo37830_click&resolved=false).

**Por tipo:** 70 Code Smells, 2 Vulnerabilities, 1 Bug → el 96% de la deuda es de mantenibilidad, no de fiabilidad/seguridad (contexto relevante para el CoNQ y el dictamen).

**Por severidad:** MAJOR 43, CRITICAL 25, MINOR 4, BLOCKER 1.

### Pareto por regla — separado producción vs. test (corrección 29-jul-2026)

**Corrección:** la versión anterior mezclaba en una sola tabla reglas de
producción (`S3776`, complejidad cognitiva) con reglas exclusivas de código
de test (`S5778`, `S8997` — patrones de `pytest`), lo cual conflacionaba dos
perfiles de riesgo distintos. `sonar.tests=tests` ya separa correctamente
ambos conjuntos en SonarCloud (57 issues en `src/click`, 16 en `tests/`); lo
que faltaba era reflejar esa separación en el Pareto de este documento, no
corregir la configuración (que ya estaba bien).

**Pareto por regla — SOLO código de producción (`src/click`, 57 issues):**

| Regla | Nombre | Hallazgos | % | % acumulado |
|---|---|---|---|---|
| python:S3776 | Cognitive Complexity demasiado alta | 22 | 38.6% | 38.6% |
| python:S5806 | Builtins no deben ser sombreados por variables locales | 9 | 15.8% | 54.4% |
| python:S1172 | Parámetros de función no usados deben eliminarse | 8 | 14.0% | 68.4% |
| python:S107 | Demasiados parámetros en función/método | 5 | 8.8% | 77.2% |
| (12 reglas restantes, 1 hallazgo c/u) | — | 13 | 22.8% | 100% |

**Lectura:** en producción, el Pareto es aún más pronunciado que en la
versión mezclada: **el 7% de las reglas (4 de 17) explican el 77% de los
hallazgos de producción**, y la complejidad cognitiva (`S3776`) sube de
30.1% a **38.6%** al aislarla del ruido de las reglas de test — confirma con
más fuerza que la refactorización de complejidad es la prioridad número uno.

**Reglas exclusivas de `tests/` (16 issues, no compiten por prioridad de
refactorización de producción):**

| Regla | Nombre | Hallazgos | % de issues de test |
|---|---|---|---|
| python:S5778 | Un solo `assert`/invocación esperado al testear excepciones | 12 | 75.0% |
| python:S8997 | Tests deben usar fixture `monkeypatch` | 2 | 12.5% |
| python:S9000 | `pytest.raises` debe usarse como context manager | 1 | 6.2% |
| python:S9001 | Fallos de test esperados deben incluir una razón | 1 | 6.2% |

**Nota:** `S9000` es el único hallazgo tipo `BUG` de todo el proyecto (ver
Anexo ISO/IEC 5055) — está en `tests/test_utils/test_echo_via_pager.py:165`,
confirmando que es deuda de calidad de test, no un defecto de fiabilidad en
producción.

### Pareto por módulo

| Módulo | Hallazgos | % | % acumulado |
|---|---|---|---|
| `src/click/core.py` | 18 | 24.7% | 24.7% |
| `src/click/termui.py` | 8 | 11.0% | 35.6% |
| `src/click/_compat.py` | 7 | 9.6% | 45.2% |
| `src/click/_termui_impl.py` | 5 | 6.8% | 52.1% |
| `src/click/types.py` | 4 | 5.5% | 57.5% |
| (resto de `src/click`, 8 archivos) | 15 | 20.5% | 78.1% |
| (archivos de `tests/`) | 16 | 21.9% | 100% |

### Densidad de defectos por KLOC (solo `src/click`, producción)

**Corrección 29-jul-2026:** la versión anterior de esta tabla usaba `wc -l`
(líneas físicas totales, incl. blancos/comentarios/docstrings) como
denominador. Se reemplaza por `ncloc` (líneas de código ejecutable,
excluyendo blancos y comentarios), obtenido directamente de SonarCloud vía
`GET /api/measures/component_tree?component=Eduardo37830_click&metricKeys=ncloc&qualifiers=FIL`
— es la métrica que SonarCloud usa internamente y la que corresponde
correctamente a un cálculo de densidad de defectos. `sonar.tests=tests` ya
estaba correctamente configurado desde el primer commit (verificado: los 17
archivos de `ncloc` son exclusivamente de `src/click`, ningún archivo de
`tests/` se cuenta ahí) — no había un defecto de configuración que corregir,
solo un error en el denominador usado en este documento.

| Módulo | Hallazgos | `ncloc` | KLOC | Defectos/KLOC |
|---|---|---|---|---|
| `termui.py` | 8 | 440 | 0.440 | **18.18** |
| `_compat.py` | 7 | 411 | 0.411 | **17.03** |
| `core.py` | 18 | 1,892 | 1.892 | 9.51 |
| `_winconsole.py` | 2 | 227 | 0.227 | 8.81 |
| `_termui_impl.py` | 5 | 617 | 0.617 | 8.10 |
| `_textwrap.py` | 1 | 131 | 0.131 | 7.63 |
| `decorators.py` | 2 | 300 | 0.300 | 6.67 |
| `testing.py` | 3 | 451 | 0.451 | 6.65 |
| `utils.py` | 2 | 327 | 0.327 | 6.12 |
| `parser.py` | 2 | 331 | 0.331 | 6.04 |
| `formatting.py` | 1 | 197 | 0.197 | 5.08 |
| `types.py` | 4 | 826 | 0.826 | 4.84 |
| `exceptions.py` | 1 | 229 | 0.229 | 4.37 |
| `shell_completion.py` | 1 | 482 | 0.482 | 2.07 |
| `__init__.py` | 0 | 121 | 0.121 | 0.00 |
| `globals.py` | 0 | 28 | 0.028 | 0.00 |
| `_utils.py` | 0 | 20 | 0.020 | 0.00 |
| **Total `src/click`** | **57** | **7,030** | **7.030** | **8.11** |

**Lectura corregida:** con el denominador correcto, **`termui.py` (18.18) y
`_compat.py` (17.03) son, por un margen amplio, los módulos con mayor
densidad de defectos** — más del doble que `core.py` (9.51), pese a que
`core.py` concentra el mayor volumen absoluto (18 hallazgos). Esto **invierte
la lectura anterior** (que señalaba a `_compat.py` como único módulo crítico
con `core.py` en un nivel "medio"): ahora `termui.py` y `_compat.py` destacan
juntos como los dos módulos con la deuda más concentrada por línea de código,
y `core.py`, aunque voluminoso, es proporcionalmente menos denso que ambos.
La densidad global del proyecto también sube de 4.51 a **8.11
defectos/KLOC** al usar el denominador correcto (7.03 KLOC reales de
producción, no 12.63 KLOC de líneas físicas totales).

---

## Resumen de fórmulas y supuestos usados (para la memoria de cálculo)

- **Lead time for changes** = timestamp de merge − timestamp de creación del PR. *Supuesto:* no se tuvo acceso al primer commit del branch, así que es una cota inferior del lead time real "code committed → deployed".
- **Frecuencia de despliegue** = # releases publicadas ÷ días entre la primera y última release de la ventana muestreada.
- **Change failure rate** = releases de parche que el propio `CHANGES.md` documenta como corrección de regresión introducida por la release anterior ÷ total de releases en la ventana.
- **MTTR** = fecha de release del fix − fecha de release que introdujo el defecto (proxy de exposición real del usuario, no fecha de commit).
- **Densidad de defectos** = hallazgos abiertos de SonarCloud (no resueltos) ÷ `ncloc` (líneas de código ejecutable medidas por SonarCloud, no `wc -l`), excluyendo tests. *Corrección 29-jul-2026: la versión inicial de este cálculo usó `wc -l` por error; ver nota en la sección 4.*
- Todas las cifras son reproducibles con los comandos `gh` y las URLs de API citadas arriba — inclúyanlas como anexo de trazabilidad.
