# Anexo ISO/IEC 25010 — click (plataforma pública de referencia)

Contexto de aplicación: `click` es una librería fundacional (17.6k ⭐, 1.9k forks,
usada por Flask/pip/etc.), análoga en criticidad a un componente base de
plataforma pública — de ahí que se prioricen **Fiabilidad**, **Seguridad** y
**Mantenibilidad** sobre características de UX (que no aplican a una librería).

Valores de "Fuente" tomados de `Overall Code` en SonarCloud
(`sonarcloud.io/api/measures/component?component=Eduardo37830_click`), estado
al [27-jul-2026], y del run de `pytest --cov` local.

| Característica (25010) | Métrica | Umbral propuesto | Valor actual medido | Fuente | Peso |
|---|---|---|---|---|---|
| Adecuación funcional | % de casos de prueba de caja negra que pasan (Anexo V&V) | ≥ 95% | Pendiente hasta ejecutar las 5–8 pruebas del martes | `CliRunner` (V&V martes) | 10% |
| Fiabilidad | Reliability Rating (Sonar) | A (rating 1) en Overall Code | **C (rating 3)** — 1 bug abierto | SonarCloud `reliability_rating` | 20% |
| Fiabilidad | Bugs abiertos (Overall Code) | 0 bugs bloqueantes/críticos | 1 bug (CODE_SMELL dominante, 1 BUG real) | SonarCloud `bugs` | 10% |
| Fiabilidad | % de tests que pasan en la matriz CI (9 combinaciones OS/Python) | 100% | 100% (evidenciado en `tests.yaml` verde) | GitHub Actions | 10% |
| Seguridad | Security Rating (Sonar) | A (rating 1) en Overall Code | **C (rating 3)** — 2 vulnerabilities abiertas | SonarCloud `security_rating` | 15% |
| Seguridad | Security Hotspots revisados | 100% | 100% (0 hotspots pendientes) | SonarCloud `security_hotspots` | 5% |
| Mantenibilidad | Maintainability Rating (Sonar) | A (rating 1) | A (rating 1) — cumple | SonarCloud `sqale_rating` | 10% |
| Mantenibilidad | Deuda técnica (SQALE debt ratio) | ≤ 5% | 0.3% — cumple ampliamente | SonarCloud `sqale_debt_ratio` | 5% |
| Mantenibilidad | Complejidad cognitiva por función | ≤ 15 (umbral de regla S3776) | 22 funciones superan el umbral (30% de toda la deuda, ver Pareto) | SonarCloud `python:S3776` | 10% |
| Mantenibilidad | Duplicación de código | ≤ 3% | 0.3% — cumple ampliamente | SonarCloud `duplicated_lines_density` | 5% |
| Compatibilidad / Portabilidad | Cobertura de matriz de entornos (versiones Python × SO) | ≥ 8 combinaciones | 9 combinaciones (3.10–3.14, 3.14t, Win, Mac, PyPy) | `.github/workflows/tests.yaml` | 5% |
| Verificabilidad (test coverage, subcaract. de Mantenibilidad) | % cobertura de línea (pytest-cov) | ≥ 80% | 84.2% — cumple | `coverage.xml` / SonarCloud `coverage` | 10% |

**Justificación de pesos:** Fiabilidad + Seguridad concentran el 35% del puntaje
porque `click` es dependencia transitiva de miles de proyectos (incl.
infraestructura pública) — una falla o vulnerabilidad se propaga aguas abajo
sin que el equipo consumidor lo note. Mantenibilidad pesa 30% porque el bus
factor identificado (David Lord ~18% de los commits históricos, ver metadatos
de HOY) hace que la legibilidad/complejidad del código sea crítica para la
continuidad del proyecto ante ausencia de mantenedores clave. Adecuación
funcional se mantiene con peso menor (10%) porque la funcionalidad ya está
madura (8.x, producción estable); Portabilidad y Verificabilidad se ponderan
con base en evidencia objetiva y reproducible (matriz CI, cobertura).

## Verificación de coherencia con el Quality Gate de SonarCloud

**Actualizado 28-jul-2026:** el Quality Gate custom sobre *Overall Code* ya
fue creado y aplicado al proyecto (reemplaza al gate por defecto "Sonar way",
que solo evaluaba *New Code*). Verificado en vivo vía
`GET /api/qualitygates/project_status?projectKey=Eduardo37830_click`:

```text
status: ERROR
  reliability_rating   > A   -> actual C   ❌ ERROR
  security_rating      > A   -> actual C   ❌ ERROR
  sqale_rating         > A   -> actual A   ✅ OK
  coverage             ≥ 80% -> actual 84.2% ✅ OK
  duplicated_lines_density ≤ 3% -> actual 0.3% ✅ OK
  security_hotspots_reviewed = 100% -> actual 100% ✅ OK
  sqale_debt_ratio     ≤ 5%  -> actual 0.3% ✅ OK
```

**El proyecto falla el gate sobre Overall Code**, confirmado con datos reales,
no proyectados — el tablero de SonarCloud muestra el veredicto en rojo. Esto
sustenta directamente el dictamen "ADOPTAR CON CONDICIONES" en vez de adopción
sin reservas.

**Matiz importante para el dictamen:** el único hallazgo tipo `BUG` que hace
fallar `reliability_rating` (regla `python:S9000`, "pytest.raises should be
used as a context manager") está en **`tests/test_utils/test_echo_via_pager.py:165`**
— es un defecto de estilo en un test, no un defecto funcional en código de
producción. El rating C es real y el gate debe seguir fallando (así está
definido el umbral), pero el dictamen debe ser preciso: no hay un bug de
producción confirmado detrás de esta calificación, lo cual matiza la severidad
real del hallazgo sin invalidar el resultado del gate.

---

## Anexo ISO/IEC 5055 — Análisis estático mapeado a las 4 características automatizables

El brief exige explícitamente, a nivel de producto: *"Análisis estático del
código (vía SonarCloud) aplicando los estándares de ISO/IEC 5055"*. A
diferencia de ISO/IEC 25010 (calidad de producto en general, con
características subjetivas como Usabilidad), **ISO/IEC 5055 define 4
características medibles automáticamente por herramientas de análisis
estático de código fuente**: Fiabilidad, Eficiencia de Desempeño, Seguridad y
Mantenibilidad. El mapeo siguiente agrupa los **73 issues abiertos** de
SonarCloud (`Eduardo37830_click`, resolved=false) por esas 4 categorías,
usando el campo `type` de cada issue (no una clasificación manual/subjetiva).

| Característica ISO/IEC 5055 | Tipo SonarCloud | # Issues | % del total | Reglas principales | Severidad (SonarCloud) |
|---|---|---|---|---|---|
| **Seguridad** | `VULNERABILITY` | 2 | 2.7% | `python:S2245` (PRNG en contexto "sensible"), `python:S5332` (protocolo HTTP) | 1 MAJOR, 1 MINOR |
| **Fiabilidad** | `BUG` | 1 | 1.4% | `python:S9000` (`pytest.raises` sin context manager) | 1 MAJOR — **en código de test, no de producción** (ver nota abajo) |
| **Eficiencia de Desempeño** | *(sin issues activos en esta categoría)* | 0 | 0% | El ruleset Python activo en este proyecto no tiene reglas de rendimiento (`tag:performance`) disparadas — no se detectaron bucles ineficientes, complejidad algorítmica excesiva ni uso indebido de estructuras de datos en el código analizado | — |
| **Mantenibilidad** | `CODE_SMELL` | 70 | 95.9% | `python:S3776` (complejidad cognitiva, 22), `python:S5778` (asserts múltiples en tests, 12), `python:S5806` (builtins sombreados, 9), `python:S1172` (parámetros no usados, 8), `python:S107` (demasiados parámetros, 5), `python:S8997` (fixture monkeypatch, 2), + 14 reglas con 1 hallazgo c/u | 43 MAJOR, 25 CRITICAL, 4 MINOR, 1 BLOCKER (agregado sobre las 4 categorías) |
| **Total** | — | **73** | **100%** | — | — |

**Lectura para el dictamen:**

1. **95.9% de la deuda es de Mantenibilidad**, no de Fiabilidad ni Seguridad —
   `click` es funcionalmente sólido y no tiene vulnerabilidades de alto
   impacto; su deuda es de legibilidad/complejidad interna (coherente con la
   Ficha de deuda técnica #1 y el hallazgo de bus factor de la matriz de
   gobernanza).
2. **Cero hallazgos de Eficiencia de Desempeño** es una observación honesta,
   no una omisión: se documenta explícitamente porque ISO/IEC 5055 exige
   evaluar la característica, y la ausencia de hallazgos es en sí un dato (no
   se puede "inflar" esta fila con hallazgos que no existen).
3. **Las 2 vulnerabilidades de Seguridad son de riesgo bajo, verificado
   manualmente:**
   - `_compat.py:432` (`S2245`) — `random.randrange()` se usa únicamente para
     generar un nombre de archivo temporal único en la escritura atómica
     (`_AtomicFile`), no para tokens ni claves criptográficas. Es un
     **falso positivo probable** de la regla (que dispara ante cualquier uso
     de `random`, sin poder inferir la intención).
   - `_termui_impl.py:834` (`S5332`) — el string `"http://"` se usa solo para
     comparar el *esquema* de una URL (`url.startswith(("http://",
     "https://"))`) antes de delegar a `webbrowser.open()`, no para
     transmitir datos por HTTP sin cifrar. También es un **falso positivo
     probable**.
   - Se recomienda documentar ambos como "revisados, sin acción" en
     SonarCloud (marcarlos como *Won't Fix* con justificación) en vez de
     dejarlos abiertos indefinidamente — así el Security Rating podría subir
     de C a A sin cambiar una sola línea de código, solo con triage.
4. **El único Bug (Fiabilidad) está en un test, no en producción** — ver nota
   en la sección de Quality Gate arriba. Si SonarCloud permitiera excluir
   `tests/` del cómputo de `bugs`/`vulnerabilities` (actualmente solo excluye
   `tests/` del cómputo de `ncloc`), el Reliability Rating real de
   *producción* sería A, no C. Esto no invalida el resultado del gate (que
   evalúa el proyecto tal como está configurado), pero es una precisión
   necesaria para no sobrestimar el riesgo de fiabilidad en el dictamen.

**Fuente de los datos:** `GET sonarcloud.io/api/issues/search?componentKeys=Eduardo37830_click&resolved=false&facets=rules,severities,types` +
`GET sonarcloud.io/api/rules/show?key=<regla>&organization=eduardo37830` (para tags/tipo de cada regla), consultado 2026-07-29.
