## Context

click (pallets/click) es una librería Python de interfaces CLI con 17.6k⭐ en GitHub, mantenida por la organización Pallets. El proyecto "La Interventoría" exige en su sección S3 un anexo normativo para gestión de IA. Actualmente click tiene:

- Matriz de gobernanza documentada (`matriz_gobernanza.md`) con riesgos de bus factor (31% en 2 mantenedores), sin SLA de seguridad, y cadencia de release irregular
- Flujo PR→release documentado en el diagrama as-is (`Diagrama_flujo_click.drawio`)
- Un agente QualityGate Auditor (QGA) especificado (Bloque C, Actividad 4.6) que audita PRs contra el Anexo de Calidad ISO 25010
- Ninguna política formal para contribuciones asistidas por IA, agentes de revisión automatizada, ni mapeo contra estándares internacionales de IA

El anexo debe ser un documento normativo autocontenido, no modifica código fuente ni configuración de CI/CD.

## Goals / Non-Goals

**Goals:**
- Crear `anexo_gobernanza_ia.md` en la raíz del proyecto
- Mapear ISO/IEC 42001 cláusulas 5, 6, 7, 9, 10 al contexto de click
- Aplicar el ciclo ISO/IEC 23894 (6 fases) al flujo PR→release con riesgos OWASP LLM Top 10
- Documentar la especificación del agente QGA y su alineación con estándares
- Definir protocolo de control humano (Custodio de Calidad)
- Establecer métricas de monitoreo y calibración del QGA

**Non-Goals:**
- Modificar código fuente, workflows CI/CD, configuración de GitHub, o dependencias
- Implementar el agente QGA (solo documentar su especificación)
- Cambiar el flujo as-is documentado en el diagrama swimlanes
- Definir la especificación del Anexo de Calidad ISO 25010 (es prerrequisito del QGA)
- Automatizar las métricas de monitoreo

## Decisions

1. **Documento único vs. múltiples archivos**: Se opta por un solo archivo `anexo_gobernanza_ia.md` en la raíz (co-located con `matriz_gobernanza.md`) en lugar de fragmentarlo en `openspec/specs/`. El anexo es un documento normativo de referencia, no una especificación técnica de software. Los specs de OpenSpec capturan requisitos implementables.

2. **Estructura basada en estándares**: El documento se organiza por norma (ISO 42001 → ISO 23894 → OWASP → QGA → control humano → métricas), no por componente del proyecto. Esto facilita la auditoría externa y la trazabilidad regulatoria.

3. **Tablas para mapeos normativos**: Se usan tablas Markdown para los mapeos ISO 42001, ISO 23894, y OWASP (cláusula/riesgo → aplicación → control). Esto sigue el mismo patrón de `matriz_gobernanza.md` y facilita la revisión.

4. **Sin código ejecutable**: El documento es puramente normativo. La implementación del QGA y las métricas se definen en otros artefactos (Bloque C, Anexo ISO 25010).

5. **Referencia cruzada explícita**: Cada sección enlaza a los archivos fuente relevantes (`matriz_gobernanza.md`, `entregable.md`, `Diagrama_flujo_click.drawio`, especificación del QGA) para mantener trazabilidad sin duplicar contenido.

## Risks / Trade-offs

- **[Riesgo] Desactualización del anexo**: Si el flujo PR→release cambia, el anexo debe actualizarse. → **Mitigación**: Incluir cláusula de revisión periódica (ISO 42001 cláusula 9.3).
- **[Riesgo] Solapamiento con matriz_gobernanza.md**: La matriz ya documenta riesgos de gobernanza tradicionales. → **Mitigación**: El anexo cubre exclusivamente riesgos de IA (agentes, prompts, OWASP), no duplica contenido.
- **[Riesgo] Dependencia externa del QGA**: El QGA está especificado pero no implementado. → **Mitigación**: El anexo documenta la especificación como referencia, no asume implementación.
- **[Riesgo] Extensión del documento**: Un anexo muy largo reduce su utilidad como referencia. → **Mitigación**: Estructura tabular concisa; detalles operativos van en documentos separados.
