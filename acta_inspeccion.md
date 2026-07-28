# Acta de inspección formal — `src/click/core.py`

**[IA]** Este documento fue elaborado con asistencia de un modelo de lenguaje
(Claude, Anthropic) bajo supervisión del equipo auditor. La inspección de
código (lectura línea a línea y hallazgos técnicos) fue ejecutada por la IA
actuando como Lector/Inspector; **los campos de participantes humanos deben
completarse con los nombres reales del equipo antes de radicar**, y la sesión
debe repetirse o al menos validarse en conjunto para que el acta refleje una
inspección real de equipo, no solo asistida.

---

## 1. Datos generales

| Campo | Valor |
|---|---|
| **Fecha** | 2026-07-28 |
| **Duración** | ~45 min (sesión única, asistida por IA) |
| **Módulo inspeccionado** | `src/click/core.py` |
| **Alcance específico** | `Option.get_help_record()` (líneas 3331–3374) y `Option.get_help_extra()` (líneas 3376–3458) — 128 líneas |
| **Motivo de selección del alcance** | `get_help_extra` es la función de mayor complejidad cognitiva de todo el repositorio (44, sobre el límite de 15 — regla `python:S3776`, ver Ficha de deuda técnica #1). La inspección manual complementa el análisis estático: SonarCloud mide complejidad, no corrección lógica. |
| **Técnica** | Inspección formal tipo Fagan simplificada (preparación individual + reunión de hallazgos), con checklist de defectos guiado por las categorías del Anexo ISO/IEC 25010 |
| **Participantes** | Moderador: _(completar)_ · Autor/a (representa el código, no presente — proyecto externo): N/A (código de terceros, pallets/click) · Lector: IA (Claude) bajo supervisión de _(completar)_ · Inspector/Tester: _(completar)_ |
| **Documento de entrada** | `src/click/core.py` @ commit `00e592c` (HEAD de `pallets/click` al momento del fork), Ficha de deuda técnica #1 (`fichas_deuda_tecnica.md`), Anexo ISO/IEC 25010 (`anexo_iso25010.md`) |

---

## 2. Checklist de inspección utilizado

Basado en las características de ISO/IEC 25010 priorizadas en el Anexo:

- [ ] **Adecuación funcional** — ¿la función hace lo que su nombre/docstring promete en todos los casos de entrada, incluyendo tipos no estándar?
- [ ] **Fiabilidad** — ¿hay rutas que puedan lanzar excepciones no documentadas/no manejadas?
- [ ] **Mantenibilidad** — ¿la complejidad ciclomática/cognitiva dificulta razonar sobre todas las ramas?
- [ ] **Consistencia** — ¿el comportamiento es simétrico entre casos análogos (p. ej. flags True/False, con/sin `secondary_opts`)?

---

## 3. Hallazgos (trazados al Anexo 25010)

| # | Línea(s) | Hallazgo | Característica 25010 afectada | Severidad | Tipo (Fowler) |
|---|---|---|---|---|---|
| H1 | `core.py:3418-3420` | `default_value not in (None, UNSET)` usa el operador `in`, que internamente invoca `__eq__` del objeto. Si un usuario define `default=` con un objeto cuyo `__eq__` no retorna un `bool` simple (p. ej. arrays de NumPy, `pandas.Series`, que lanzan `ValueError: truth value of an array is ambiguous`), `get_help_extra()` puede **lanzar una excepción al generar el texto de ayuda** (`--help`), no al usar la opción. | Fiabilidad | Media — caso de borde no cubierto por los 10 casos de caja negra ejecutados (que usan `int`/`str`/`bool`), no confirmado con reproducción, requiere test dedicado con un tipo `__eq__`-hostil antes de radicarse como defecto confirmado | Imprudente/Inadvertido — el uso de `in` sobre una tupla es idiomático y no evidencia mala intención, pero no contempla objetos con `__eq__` no booleano |
| H2 | `core.py:3376-3458` | La función mezcla 4 responsabilidades en un solo cuerpo: (a) resolver env var, (b) resolver y formatear el valor por defecto, (c) resolver metadatos de rango numérico, (d) resolver bandera de "required". Esto explica la complejidad cognitiva 44/15 medida por SonarCloud (Ficha de deuda técnica #1). | Mantenibilidad | Baja (ya identificado y cuantificado por análisis estático; la inspección confirma que la causa raíz es cohesión baja, no un algoritmo intrínsecamente complejo) | Prudente/Deliberado (deuda de acumulación incremental de features, ver Ficha #1) |
| H3 | `core.py:3429-3434` | Para flags booleanos con `secondary_opts` (pares `--flag/--no-flag`), el string de default se calcula indexando `[0]` del primer elemento de `self.opts` o `self.secondary_opts` sin validar que la lista no esté vacía. Si `secondary_opts` fuese una lista vacía (en vez de `None`) el acceso `[0]` lanzaría `IndexError`. **No se encontró una ruta de código que produzca `secondary_opts=[]` en vez de `None`/lista no vacía** tras revisar el constructor de `Option`, por lo que se clasifica como defensivo, no como defecto confirmado. | Fiabilidad | Baja (no explotable con la API pública actual; queda como nota de robustez) | N/A — hallazgo defensivo, no deuda confirmada |
| H4 | `core.py:3345-3348` | Comportamiento correctamente simétrico: `_write_opts` omite el metavar para flags (`is_flag`) y contadores (`count`), consistente con `get_help_extra` que también trata ambos casos de forma especial (línea 3448). **Verificado como correcto, no es un hallazgo de defecto** — se documenta para dejar constancia de que el ítem del checklist "Consistencia" fue revisado explícitamente. | Adecuación funcional | — (conformidad verificada) | — |

---

## 4. Veredicto de la inspección

**Aprobado con observaciones.** No se encontraron defectos funcionales
confirmados dentro del alcance inspeccionado. El hallazgo **H1** es el más
relevante: es un caso de borde legítimo (tipos de `default` con `__eq__` no
booleano) que los 10 casos de prueba de caja negra ya ejecutados no cubren,
porque todos usan tipos primitivos. Se recomienda:

1. Agregar un caso de prueba de caja negra adicional: `Option(default=<objeto con __eq__ que lanza ValueError>)` + invocación de `--help`, para confirmar o descartar H1 como defecto real.
2. Registrar H2 como respaldo cualitativo de la Ficha de deuda técnica #1 (la inspección manual confirma la causa raíz de baja cohesión, no solo el síntoma de complejidad).
3. Repetir esta inspección con el equipo humano completo (roles Moderador/Lector/Inspector reales) para que el acta cumpla el requisito de trazabilidad de autoría de la rúbrica — la sesión actual es un insumo, no un reemplazo, de la inspección de equipo.

---

## 5. Trazabilidad

- Ficha de deuda técnica relacionada: `fichas_deuda_tecnica.md` — Ficha 1 (complejidad cognitiva `core.py`)
- Anexo normativo: `anexo_iso25010.md` — características Fiabilidad, Mantenibilidad, Adecuación funcional
- Evidencia de casos de prueba existentes: `casos_prueba_caja_negra.md` (no cubre H1; ver recomendación #1)
