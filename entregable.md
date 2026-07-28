# Entregables LUNES — Auditoría click (pallets/click → Eduardo37830/click)

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

### Pareto por regla (clásico 80/20 — confirma el principio)

| Regla | Nombre | Hallazgos | % | % acumulado |
|---|---|---|---|---|
| python:S3776 | Cognitive Complexity demasiado alta | 22 | 30.1% | 30.1% |
| python:S5778 | Un solo `assert`/invocación esperado al testear excepciones | 12 | 16.4% | 46.6% |
| python:S5806 | Builtins no deben ser sombreados por variables locales | 9 | 12.3% | 58.9% |
| python:S1172 | Parámetros de función no usados deben eliminarse | 8 | 11.0% | 69.9% |
| python:S107 | Demasiados parámetros en función/método | 5 | 6.8% | 76.7% |
| python:S8997 | Tests deben usar fixture `monkeypatch` | 2 | 2.7% | 79.5% |
| (14 reglas restantes, 1 hallazgo c/u) | — | 15 | 20.5% | 100% |

**Lectura:** el 30% de las reglas (6 de 20) explican el 80% de los hallazgos. La **complejidad cognitiva** por sí sola es el 30% de toda la deuda — señal clara de prioridad de refactorización, concentrada en `core.py` y `termui.py`.

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

| Módulo | Hallazgos | LOC | KLOC | Defectos/KLOC |
|---|---|---|---|---|
| `_compat.py` | 7 | 590 | 0.59 | **11.86** |
| `termui.py` | 8 | 1,003 | 1.00 | **7.98** |
| `_winconsole.py` | 2 | 297 | 0.30 | 6.73 |
| `_termui_impl.py` | 5 | 945 | 0.95 | 5.29 |
| `_textwrap.py` | 1 | 188 | 0.19 | 5.32 |
| `core.py` | 18 | 3,792 | 3.79 | 4.75 |
| `formatting.py` | 1 | 320 | 0.32 | 3.13 |
| `testing.py` | 3 | 798 | 0.80 | 3.76 |
| `parser.py` | 2 | 533 | 0.53 | 3.75 |
| `decorators.py` | 2 | 627 | 0.63 | 3.19 |
| `utils.py` | 2 | 688 | 0.69 | 2.91 |
| `exceptions.py` | 1 | 378 | 0.38 | 2.65 |
| `types.py` | 4 | 1,422 | 1.42 | 2.81 |
| `shell_completion.py` | 1 | 801 | 0.80 | 1.25 |
| **Total `src/click`** | **57** | **12,629** | **12.63** | **4.51** |

**Lectura:** `_compat.py` tiene la densidad más alta (11.86/KLOC) pese a ser un módulo pequeño — es el módulo de compatibilidad multiplataforma (Windows/Unix/terminal), consistente con su naturaleza de "código pegamento" con muchas ramas condicionales. `core.py` concentra el volumen absoluto (18 hallazgos) pero su densidad relativa (4.75) es media — es grande y complejo, pero no desproporcionadamente peor por línea que el resto.

---

## Resumen de fórmulas y supuestos usados (para la memoria de cálculo)

- **Lead time for changes** = timestamp de merge − timestamp de creación del PR. *Supuesto:* no se tuvo acceso al primer commit del branch, así que es una cota inferior del lead time real "code committed → deployed".
- **Frecuencia de despliegue** = # releases publicadas ÷ días entre la primera y última release de la ventana muestreada.
- **Change failure rate** = releases de parche que el propio `CHANGES.md` documenta como corrección de regresión introducida por la release anterior ÷ total de releases en la ventana.
- **MTTR** = fecha de release del fix − fecha de release que introdujo el defecto (proxy de exposición real del usuario, no fecha de commit).
- **Densidad de defectos** = hallazgos abiertos de SonarCloud (no resueltos) ÷ KLOC de código fuente, excluyendo tests.
- Todas las cifras son reproducibles con los comandos `gh` y las URLs de API citadas arriba — inclúyanlas como anexo de trazabilidad.
