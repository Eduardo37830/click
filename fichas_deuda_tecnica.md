# Fichas de deuda técnica — desde SonarCloud (Eduardo37830_click)

Metodología: se seleccionaron 3 hallazgos representativos de reglas distintas
(no instancias aisladas) para ilustrar clases de deuda diferentes, siguiendo
el cuadrante de Martin Fowler (Reckless/Prudent × Deliberate/Inadvertent).
El "esfuerzo Sonar" es el heurístico de remediación de SonarCloud (minutos
por instancia); el "esfuerzo real estimado" aplica un multiplicador propio
que contempla revisión de pares, pruebas de regresión y validación en la
matriz de 9 entornos de CI — no solo el cambio mecánico.

---

## Ficha 1 — Complejidad cognitiva excesiva en `core.py`

| Campo | Valor |
|---|---|
| **Regla** | `python:S3776` — Cognitive Complexity |
| **Instancias** | 6 funciones en `src/click/core.py` (líneas 340, 1477, 1701, 3228, 3331, 3376) |
| **Peor caso** | `core.py:3376` — complejidad 44 (límite permitido: 15) |
| **Esfuerzo Sonar** | 104 min (~1.7 h) para las 6 instancias de `core.py` |
| **Esfuerzo real estimado** | **12–16 h** — refactorizar funciones núcleo de `core.py` (`Context`, `Command.invoke`, parsing) exige pruebas de regresión exhaustivas porque son las rutas más ejercitadas del framework; cada extracción de función requiere validar en la matriz completa (9 combinaciones OS/Python) antes de mergear |
| **Cuadrante de Fowler** | **Prudente y Deliberado** — la complejidad es resultado de 10+ años de features acumuladas (opciones, flags, contextos anidados, shell completion) sobre una API que prioriza flexibilidad y retrocompatibilidad por encima de simplicidad interna. Es una decisión consciente y razonable en su momento, no negligencia. |
| **Por qué pagar ahora** | El bus factor identificado en la matriz de gobernanza (David Lord + Armin Ronacher ≈ 31% del historial) hace que la alta complejidad de `core.py` sea un riesgo de continuidad: un nuevo mantenedor tarda más en volverse productivo en el módulo más crítico y menos legible del proyecto. |
| **Evidencia** | [SonarCloud — regla S3776](https://sonarcloud.io/project/issues?id=Eduardo37830_click&resolved=false&rules=python%3AS3776) |

---

## Ficha 2 — Parámetro `delete` ignorado en `_AtomicFile.close()` (posible defecto funcional, no solo smell)

| Campo | Valor |
|---|---|
| **Regla** | `python:S1172` — Unused function parameters (detectada como code smell, pero el análisis manual revela algo más serio) |
| **Ubicación** | `src/click/_compat.py:466-471` |
| **Código** | ```python\ndef close(self, delete: bool = False) -> None:\n    if self.closed:\n        return\n    self._f.close()\n    os.replace(self._tmp_filename, self._real_filename)\n    self.closed = True\n``` invocado desde `__exit__` como `self.close(delete=exc_type is not None)` |
| **Esfuerzo Sonar** | 15 min |
| **Esfuerzo real estimado** | **3–5 h** — no es un simple "borrar parámetro": requiere entender la intención original (¿debía descartar el archivo temporal en caso de excepción?), escribir un caso de prueba que reproduzca escritura atómica fallida, y validar que no haya código downstream dependiendo del comportamiento actual (aunque sea incorrecto) |
| **Cuadrante de Fowler** | **Imprudente e Inadvertido** — a diferencia de la Ficha 1, aquí el nombre del parámetro (`delete`) y su uso en `__exit__` (`delete=exc_type is not None`) comunican una intención clara — descartar el archivo temporal si la escritura fue interrumpida por una excepción — que **el cuerpo de la función nunca implementa**: siempre ejecuta `os.replace()` incondicionalmente. Es deuda por inadvertencia, no por decisión consciente. |
| **Riesgo funcional** | Si `click.utils.LazyFile`/`atomic=True` se usa para escribir un archivo y ocurre una excepción a mitad de la escritura, el archivo temporal (parcial/corrupto) **reemplaza igualmente** al archivo real, contradiciendo la semántica de "escritura atómica" que el nombre de la clase promete. **Recomendación: verificar con un caso de prueba dedicado antes de radicar el hallazgo como confirmado** — no se ejecutó la reproducción end-to-end, esto es un hallazgo de inspección de código, pendiente de confirmar con un test. |
| **Evidencia** | [SonarCloud — regla S1172](https://sonarcloud.io/project/issues?id=Eduardo37830_click&resolved=false&rules=python%3AS1172) · código fuente `src/click/_compat.py:455-471` |

---

## Ficha 3 — Antipatrón de aserciones múltiples en pruebas de excepciones

| Campo | Valor |
|---|---|
| **Regla** | `python:S5778` — Only one method invocation is expected when testing runtime exceptions |
| **Instancias** | 12, concentradas en `tests/test_termui.py` (4), `tests/test_types.py` (4), `tests/test_utils/test_echo_via_pager.py` (2), `tests/test_context.py` (2) |
| **Esfuerzo Sonar** | 60 min (~1 h) |
| **Esfuerzo real estimado** | **2–3 h** — dividir cada bloque `pytest.raises(...)` que contiene múltiples llamadas en sub-tests independientes, sin cambiar la cobertura funcional |
| **Cuadrante de Fowler** | **Prudente e Inadvertido** — es deuda de la suite de pruebas (no de producción), típica de cuando el equipo escribe tests rápido para cubrir un caso y descubre después la buena práctica de una sola invocación por bloque `raises`. No compromete la corrección del software, solo la precisión diagnóstica de los tests (si dos llamadas dentro del bloque pueden lanzar la misma excepción, un test así no distingue cuál falló). |
| **Por qué es menor prioridad** | No afecta código de producción ni usuarios finales de `click`; es deuda interna de calidad de suite. Se incluye en esta ficha por ser el segundo hallazgo más frecuente (12 instancias, 16.4% del Pareto) — vale la pena una limpieza de bajo riesgo y alto retorno en precisión de diagnóstico de fallos futuros. |
| **Evidencia** | [SonarCloud — regla S5778](https://sonarcloud.io/project/issues?id=Eduardo37830_click&resolved=false&rules=python%3AS5778) |

---

## Resumen

| Ficha | Esfuerzo Sonar | Esfuerzo real estimado | Cuadrante Fowler | Prioridad |
|---|---|---|---|---|
| 1. Complejidad `core.py` | 1.7 h | 12–16 h | Prudente/Deliberado | Media (mitigar riesgo de bus factor) |
| 2. `_AtomicFile.close()` | 0.25 h | 3–5 h | **Imprudente/Inadvertido** | **Alta — verificar si es defecto real antes de radicar** |
| 3. Asserts múltiples en tests | 1 h | 2–3 h | Prudente/Inadvertido | Baja |

La Ficha 2 es la más relevante para el dictamen: es el único hallazgo de los
tres con riesgo de **comportamiento funcional incorrecto** (posible pérdida
de la garantía de escritura atómica), y su discrepancia entre lo que el
código promete (por nombre/uso) y lo que hace es la definición clásica de
deuda imprudente e inadvertida.
