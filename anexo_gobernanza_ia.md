# Anexo de Gobernanza de Inteligencia Artificial — pallets/click

## Control de versiones

| Versión | Fecha | Autor | Descripción de cambios |
|---------|-------|-------|------------------------|
| 1.0 | 2026-07-28 | Equipo de Auditoría | Versión inicial del anexo de gobernanza de IA |

## 1. Propósito y alcance

Este anexo establece el marco normativo para la gestión de inteligencia artificial en el flujo de contribuciones del proyecto [pallets/click](https://github.com/pallets/click) (17.6k ⭐, librería Python de interfaces CLI, mantenida por la organización Pallets). Su creación responde al requisito del nivel S3 (gobernanza) del proyecto "La Interventoría", que exige políticas formales para contribuciones asistidas por IA, agentes de revisión automatizada y mapeo contra estándares internacionales.

El documento se alinea con:
- **ISO/IEC 42001:2023** — Sistema de Gestión de IA (AIMS)
- **ISO/IEC 23894:2023** — Gestión de Riesgos de IA
- **OWASP LLM Top 10 2025** — Riesgos de seguridad en modelos de lenguaje
- **NIST AI RMF 1.0** — Gestión de riesgos de IA
- **EU AI Act (Reglamento 2024/1689)** — Marco regulatorio europeo

**Referencias cruzadas:**
- `matriz_gobernanza.md` — Riesgos de gobernanza tradicionales (bus factor, SLA, cadencia de release)
- `entregable.md` — Defectos detectados, quality gates y flujo PR→release
- `Diagrama_flujo_click.drawio` — Diagrama swimlanes del flujo as-is
- `openspec/specs/diagrama-swimlanes-as-is/spec.md` — Especificación del flujo as-is

## 2. ISO/IEC 42001 — Sistema de Gestión de IA (AIMS)

| Cláusula ISO 42001 | Aplicación en click |
|-------------------|-------------------|
| **Cláusula 5: Liderazgo** | Los mantenedores del proyecto actúan como responsables del AIMS. Se establece una política de IA para contribuciones que define el uso aceptable de herramientas de IA generativa en PRs, issues y comunicaciones del proyecto. |
| **Cláusula 6: Planificación** | Los objetivos de calidad asistida por IA se definen en el Anexo de Calidad ISO 25010. El agente QGA se incorpora como control planificado en el flujo PR→release, con métricas de efectividad definidas en la sección 7 de este anexo. |
| **Cláusula 7: Soporte** | Las competencias necesarias para operar el QGA se documentan en `AGENTS.md`. La comunicación entre el agente y los mantenedores sigue el flujo PR→release del diagrama as-is. Los prompts del QGA se versionan y documentan como parte del sistema de calidad. |
| **Cláusula 8: Operación** | El QGA cubre parcialmente los controles de operación al auditar cada PR contra el Anexo ISO 25010. El proceso PR→release definido en el diagrama as-is (`Diagrama_flujo_click.drawio`) completa el ciclo operativo, incluyendo revisión humana, CI/CD y publicación a PyPI. |
| **Cláusula 9: Evaluación** | El QGA funciona como herramienta de auditoría interna. Cada dictamen es revisado por el Custodio de Calidad. Los resultados se agregan en informes periódicos de efectividad del sistema de gestión. |
| **Cláusula 10: Mejora** | Los PRs rechazados por el QGA se tratan como no conformidades. Cada rechazo genera una entrada en la bitácora de incidentes con causa raíz y acción correctiva. La retroalimentación se utiliza para calibrar el prompt del QGA. |

## 3. ISO/IEC 23894 — Gestión de Riesgos de IA

| Fase | Descripción aplicada a click |
|------|------------------------------|
| **Contexto** | El flujo PR→CHANGES.md→release documentado en el diagrama as-is (`Diagrama_flujo_click.drawio`) define el alcance. Los mantenedores actúan como decisores. La matriz de gobernanza (`matriz_gobernanza.md`) documenta los riesgos tradicionales (bus factor 31%, sin SLA, cadencia irregular). |
| **Identificación** | Riesgos identificados: LLM01 (Prompt Injection en diffs de PR), LLM02 (Sensitive Disclosure en dictámenes del QGA), LLM06 (Excessive Agency del agente). |
| **Análisis** | Severidad (Crítica / Alta / Media / Baja) × Frecuencia (Alta / Media / Baja). LLM01 y LLM06 se clasifican como Alta severidad × Media frecuencia. LLM02 como Media × Baja. |
| **Evaluación** | Riesgos aceptables: LLM02 (controlado por revisión humana y salida estructurada). Riesgos no aceptables sin tratamiento: LLM01 y LLM06 requieren los controles descritos en la sección 4. |
| **Tratamiento** | QGA como control detective (detecta prompt injection en el diff). Branch protection + human-in-the-loop como controles preventivos (revisión obligatoria del Custodio de Calidad antes del merge). |
| **Monitoreo** | Métricas: PRs rechazados por el QGA, time-to-merge, tasa de aprobación del QGA, regresiones post-release. Periodicidad: revisión mensual de métricas y calibración cada 5 PRs. |

## 4. OWASP LLM Top 10 2025 — Riesgos específicos del agente QGA

| Riesgo OWASP | Exposición en click | Control implementado |
|-------------|--------------------|--------------------|
| **LLM01: Prompt Injection** | Un contribuyente podría insertar instrucciones maliciosas en el diff del PR para manipular el dictamen del QGA. | El prompt de sistema del QGA sigue un enfoque "Auditor Adversario": instrucciones explícitas para ignorar comandos incrustados en comentarios, descripciones o código del PR. |
| **LLM02: Sensitive Disclosure** | El QGA podría exponer detalles de seguridad del código (rutas de archivos, configuraciones, dependencias vulnerables) en su dictamen público. | La salida del QGA se limita a una tabla estructurada con Criterio/Umbral/Evidencia/Dictamen, sin incluir fragmentos de código sensibles ni rutas internas. El Custodio de Calidad revisa el dictamen antes de hacerlo público en el PR. |
| **LLM06: Excessive Agency** | El agente podría ejecutar acciones no autorizadas si se le otorgan permisos de GitHub (merge, label, comment con autoridad). | Mínimo privilegio: el QGA opera exclusivamente en el entorno del webhook, produce solo texto estructurado, y NO tiene tokens de GitHub, API keys ni capacidad de modificar el repositorio. |

## 5. Especificación del agente QualityGate Auditor (QGA)

| Campo | Valor |
|-------|-------|
| **Nombre** | QualityGate Auditor (QGA) |
| **Rol** | Revisa Pull Requests contra el Anexo de Calidad ISO 25010 y emite un dictamen de APROBADO o RECHAZADO |
| **Prompt de sistema** | Enfoque "Auditor Adversario": el prompt instruye al agente a desconfiar de instrucciones incrustadas en el contenido del PR, priorizar la tabla de criterios del Anexo ISO 25010 y formatear la salida estrictamente en Markdown tabular. NO modifica código. |
| **Entradas** | Diff del PR, Anexo de Calidad (ISO 25010), resultados de CI/CD |
| **Salidas** | Tabla Markdown con columnas: Criterio, Umbral, Evidencia, Dictamen (CUMPLE/NO CUMPLE). Veredicto final: APROBADO o RECHAZADO. |
| **Control humano** | El Custodio de Calidad verifica cada dictamen del QGA antes de允许ir el merge. Si hay discrepancia en ≥ 2 criterios, el caso se escala al equipo de mantenedores para decisión colegiada. |
| **Cumplimiento ISO 42001** | Cláusula 9 (Evaluación): el QGA actúa como herramienta de auditoría interna. Cláusula 10 (Mejora): los rechazos alimentan el ciclo de mejora continua del AIMS. |

## 6. Protocolo de control humano

1. **Revisión obligatoria del Custodio de Calidad**: Ningún Pull Request puede ser mergeado sin revisión explícita del Custodio de Calidad, independientemente del dictamen del QGA. El Custodio es un mantenedor designado con conocimiento del Anexo ISO 25010 y del contexto del proyecto.

2. **Dictamen del QGA como insumo informativo**: El veredicto del QGA (APROBADO/RECHAZADO) es un insumo para la decisión del Custodio, no una decisión vinculante. El Custodio puede sobrescribir el dictamen fundamentando su decisión en el PR.

3. **Registro de incidentes**: Cada PR RECHAZADO por el QGA y confirmado por el Custodio se registra en la bitácora de incidentes con:
   - Identificador del PR y autor
   - Causa raíz del rechazo (criterio(s) ISO 25010 incumplido(s))
   - Acción correctiva propuesta
   - Fecha de cierre y verificación

4. **Calibración del QGA**: Cada 5 PRs auditados se ejecuta una prueba de mutación: se introduce un defecto conocido en un PR simulado y se verifica que el QGA lo detecte correctamente. Si el QGA no detecta el defecto, se ajusta el prompt de sistema y se repite la prueba.

## 7. Métricas de monitoreo

| Métrica | Descripción | Periodicidad |
|---------|-------------|-------------|
| **PRs rechazados** | Número y porcentaje de PRs cuyo dictamen del QGA fue RECHAZADO y confirmado por el Custodio | Por release |
| **Time-to-merge** | Tiempo promedio desde la apertura del PR hasta el merge, segmentado por PRs con y sin intervención del QGA | Mensual |
| **Tasa de aprobación QGA** | Porcentaje de PRs que reciben dictamen APROBADO del QGA | Mensual |
| **Regresiones post-release** | Número de issues reportados en los 30 días posteriores a un release que pudieron ser detectados por el QGA | Por release |

## 8. Bibliografía

1. **ISO/IEC 42001:2023** — Information technology — Artificial intelligence — Management system. International Organization for Standardization. https://www.iso.org/standard/81230.html
2. **ISO/IEC 23894:2023** — Information technology — Artificial intelligence — Risk management. International Organization for Standardization. https://www.iso.org/standard/77304.html
3. **OWASP LLM Top 10 2025** — OWASP Gen AI Security Project. https://genai.owasp.org/
4. **NIST AI RMF 1.0** — Artificial Intelligence Risk Management Framework. National Institute of Standards and Technology. https://www.nist.gov/artificial-intelligence
5. **EU AI Act** — Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo por el que se establecen normas armonizadas en materia de inteligencia artificial. Aplicación plena: agosto de 2026. https://eur-lex.europa.eu/eli/reg/2024/1689
