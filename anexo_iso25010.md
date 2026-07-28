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

**Pendiente de acción:** el proyecto usa actualmente el gate por defecto
**"Sonar way"**, que solo evalúa condiciones sobre *New Code* (código nuevo
desde la última versión), no *Overall Code*. Los umbrales de esta tabla están
pensados para un gate custom sobre **Overall Code** con, como mínimo:

- `reliability_rating` (Overall Code) ≤ A
- `security_rating` (Overall Code) ≤ A
- `sqale_rating` (Overall Code) ≤ A
- `coverage` (Overall Code) ≥ 80%
- `duplicated_lines_density` (Overall Code) ≤ 3%

Con los valores reales medidos hoy, **el proyecto NO pasaría** un gate así
sobre Overall Code (reliability y security están en C) — es exactamente el
tipo de brecha que sustenta un dictamen de "ADOPTAR CON CONDICIONES" en vez de
adopción sin reservas.
