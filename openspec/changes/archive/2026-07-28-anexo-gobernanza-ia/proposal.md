## Why

El proyecto "La Interventoría" exige en su nivel S3 (gobernanza) un anexo normativo para gestión de inteligencia artificial. click carece de políticas formales para contribuciones asistidas por IA, agentes de revisión automatizada (QGA), y mapeo contra estándares internacionales (ISO 42001, ISO 23894, OWASP LLM Top 10, NIST AI RMF). Sin este anexo, no es posible auditar el uso de IA en el flujo PR→release ni certificar la calidad de los dictámenes del agente QualityGate Auditor.

## What Changes

- Crear `anexo_gobernanza_ia.md` en la raíz del proyecto click
- Mapear las cláusulas aplicables de ISO/IEC 42001 (AIMS) al contexto de click
- Aplicar el ciclo de 6 fases de ISO/IEC 23894 (gestión de riesgos de IA) al flujo PR→release
- Documentar los riesgos OWASP LLM Top 10 2025 específicos del agente QGA (LLM01, LLM02, LLM06)
- Especificar el protocolo de control humano (Custodio de Calidad) para validación de dictámenes del QGA
- Definir métricas de monitoreo: PRs rechazados, time-to-merge, tasa de aprobación QGA, regresiones
- Establecer protocolo de calibración del QGA cada 5 PRs con pruebas de mutación
- Incluir bibliografía con referencias a ISO, OWASP, NIST y EU AI Act

## Capabilities

### New Capabilities
- `anexo-gobernanza-ia`: Documento normativo que define políticas, riesgos, controles y métricas para la gestión de IA en el flujo de contribuciones y PRs de click

### Modified Capabilities
<!-- No se modifican capacidades existentes. El diagrama as-is (diagrama-swimlanes-as-is) describe el flujo actual y este anexo añade la capa de gobernanza de IA sin cambiar los requisitos del flujo. -->

## Impact

- Archivo único `anexo_gobernanza_ia.md` en raíz del proyecto — sin modificar código fuente existente
- Referencia cruzada con `matriz_gobernanza.md` (riesgos de gobernanza actuales: bus factor, SLA, cadencia)
- Referencia cruzada con `entregable.md` (defectos, quality gates, flujo PR→release)
- Referencia cruzada con `openspec/specs/diagrama-swimlanes-as-is/spec.md` (flujo as-is documentado)
- Dependencia del agente QGA especificado en el Bloque C de la Actividad 4.6
- Sin cambios en APIs, dependencias PyPI o configuración de CI/CD existente
