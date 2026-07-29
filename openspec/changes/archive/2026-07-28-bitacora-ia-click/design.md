## Context

El Bloque B (Actividad 4.6, Semana 4) define un artefacto de trazabilidad de 7 secciones para auditar casos de prueba generados por IA contra la rúbrica Tabla 4.4. click ya cuenta con:

- 10 casos de prueba de caja negra en `casos_prueba_caja_negra.md` (IntRange, Choice, flags)
- Código ejecutable en `pruebas_caja_negra.py` con resultado 10/10 PASSED
- Evidencia de ejecución en `evidencia_pruebas_caja_negra.txt`
- Anexo de gobernanza de IA en `anexo_gobernanza_ia.md` (ISO 42001, ISO 23894, QGA)

La bitácora replica fielmente la estructura del Bloque B pero adaptando:
- El componente analizado: TimestampSigner.unsign() → click.IntRange/Choice/is_flag
- El conjunto de pruebas: 8 casos LLM + 1 comité → 10 casos existentes del equipo
- La fuente del código: timed.py → types.py + core.py

## Goals / Non-Goals

**Goals:**
- Crear `bitacora_auditoria_ia.md` en la raíz del proyecto
- Documentar el análisis del componente (tipos click) con particiones y valores límite
- Registrar el prompt adaptado a click con regla de REQUISITO AMBIGUO
- Evaluar los 10 casos contra los 6 criterios de la Tabla 4.4 con evidencia técnica
- Documentar decisiones por caso y conjunto final de pruebas
- Alcanzar Nivel 3 de trazabilidad (bitácora auditable SGIA)

**Non-Goals:**
- Modificar los casos de prueba existentes o su código
- Ejecutar un nuevo prompt contra un LLM (se auditan los casos como salida generada asistidamente)
- Modificar `anexo_gobernanza_ia.md` o `matriz_gobernanza.md`
- Agregar nuevos casos de prueba (solo documentar si se identifica la necesidad)

## Decisions

1. **Opción B — Auditar datos existentes**: Se auditan los 10 casos ya diseñados como si fueran salida de IA, en lugar de regenerar un prompt contra un LLM. Justificación: los casos están ejecutados y verificados, la guía permite aplicar la rúbrica a salidas existentes, y es más eficiente (50 min vs 80 min).

2. **Estructura idéntica al Bloque B**: Se replica exactamente la estructura de 7 secciones del Bloque B para mantener consistencia con el artefacto de itsdangerous y facilitar la comparación entre ambas auditorías.

3. **Nota aclaratoria en la salida**: La sección 2.2 incluye una nota explícita de que los 10 casos fueron diseñados por el equipo (no generados por LLM en este momento), pero se auditan contra la misma rúbrica para fines de trazabilidad.

4. **TC11 opcional — clamp=True en límite exacto**: Si la auditoría revela que falta un caso para `clamp=True` con valor exactamente en el límite inferior (análogo a TC09 del Bloque B con `max_age=0`), se documenta como caso adicional recomendado.

5. **Calificación única para todos los criterios**: Dado que los 10 casos están ejecutados y pasan, la calificación esperada es Nivel 3 en los 6 criterios, con fundamento técnico específico para cada uno.

## Risks / Trade-offs

- **[Riesgo] Percepción de "auto-auditoría"**: Al auditar casos que ya sabemos que funcionan, la calificación es predecible (todo Nivel 3). → **Mitigación**: El valor está en documentar el *fundamento técnico* de cada criterio, no en descubrir defectos. La evidencia de ejecución (10/10 PASSED) es objetiva.
- **[Riesgo] Sin caso LLM real**: No se ejecutó un prompt contra un LLM para esta bitácora. → **Mitigación**: La nota aclaratoria en 2.2 establece explícitamente el origen de los casos; la trazabilidad es honesta sobre la fuente.
- **[Riesgo] Duplicación con anexo_gobernanza_ia.md**: Ambos documentos referencian ISO 42001. → **Mitigación**: La bitácora es el artefacto operativo (audita casos); el anexo es el marco normativo (define políticas). No hay solapamiento de contenido.
