## Why

La Actividad 4.6 (Semana 4) exige una bitácora de auditoría de IA aplicando la rúbrica de la Tabla 4.4 a casos de prueba generados asistidamente. click ya tiene 10 casos de prueba de caja negra diseñados para IntRange, Choice y flags booleanos, ejecutados y verificados (10/10 PASSED). Falta documentar la auditoría formal de estos casos contra los 6 criterios de la rúbrica, replicando la estructura de trazabilidad del Bloque B (itsdangerous) adaptada a click.

## What Changes

- Crear `bitacora_auditoria_ia.md` en la raíz del proyecto click
- Auditar los 10 casos existentes (TC1–TC10) de `casos_prueba_caja_negra.md` contra la rúbrica Tabla 4.4 (6 criterios)
- Reutilizar la estructura de 7 secciones del Bloque B: Análisis, Prompt, Rúbrica, Decisiones, Conjunto final, Trazabilidad, Nivel alcanzado
- Incluir prompt adaptado a click (IntRange, Choice, is_flag) con regla de REQUISITO AMBIGUO
- Referencia cruzada a `anexo_gobernanza_ia.md` (ISO 42001) y `matriz_gobernanza.md`

## Capabilities

### New Capabilities
- `bitacora-ia-click`: Bitácora de auditoría de IA para click que documenta la evaluación de casos de prueba contra la rúbrica Tabla 4.4, con trazabilidad completa SGIA

### Modified Capabilities
<!-- Ninguna. No se modifican capacidades existentes. -->

## Impact

- Archivo único `bitacora_auditoria_ia.md` en raíz del proyecto — sin modificar código fuente, casos de prueba, ni configuraciones existentes
- Referencia cruzada con `casos_prueba_caja_negra.md` (10 casos a auditar)
- Referencia cruzada con `pruebas_caja_negra.py` (código ejecutado y verificado)
- Referencia cruzada con `anexo_gobernanza_ia.md` (requisito SGIA de trazabilidad)
- Referencia cruzada con `matriz_gobernanza.md` (contexto de gobernanza del proyecto)
