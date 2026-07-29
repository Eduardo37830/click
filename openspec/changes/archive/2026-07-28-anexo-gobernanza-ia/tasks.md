## 1. Estructura del documento

- [x] 1.1 Crear `anexo_gobernanza_ia.md` en la raíz del proyecto con encabezados jerarquicos y tabla de contenidos
- [x] 1.2 Redactar introducción con propósito, alcance y contexto del proyecto click
- [x] 1.3 Incluir referencias cruzadas a `matriz_gobernanza.md`, `entregable.md` y `Diagrama_flujo_click.drawio`

## 2. Sección ISO/IEC 42001 — Sistema de Gestión de IA

- [x] 2.1 Redactar tabla de mapeo para Cláusula 5 (Liderazgo): mantenedores como responsables del AIMS, política de IA para contribuciones
- [x] 2.2 Redactar tabla de mapeo para Cláusula 6 (Planificación): objetivos de calidad asistida por IA, QGA como control planificado
- [x] 2.3 Redactar tabla de mapeo para Cláusula 7 (Soporte): competencias (AGENTS.md), comunicación en flujo PR→release, documentación de prompts
- [x] 2.4 Redactar tabla de mapeo para Cláusula 9 (Evaluación): QGA como herramienta de auditoría interna, revisión por mantenedores
- [x] 2.5 Redactar tabla de mapeo para Cláusula 10 (Mejora): PRs rechazados como no conformidades, retroalimentación al prompt del QGA

## 3. Sección ISO/IEC 23894 — Gestión de Riesgos de IA

- [x] 3.1 Redactar tabla del ciclo de 6 fases: Contexto (flujo PR→release), Identificación (LLM01, LLM02, LLM06)
- [x] 3.2 Completar tabla con Análisis (severidad × frecuencia), Evaluación (riesgos aceptables vs no aceptables)
- [x] 3.3 Completar tabla con Tratamiento (QGA detective, branch protection + human-in-the-loop preventivos)
- [x] 3.4 Completar tabla con Monitoreo (PRs rechazados, time-to-merge, tasa aprobación QGA, regresiones)

## 4. Sección OWASP LLM Top 10 2025

- [x] 4.1 Redactar tabla con riesgo LLM01 (Prompt Injection): exposición en click (contribuyente inserta instrucciones en diff), control (prompt adversarial del QGA)
- [x] 4.2 Redactar tabla con riesgo LLM02 (Sensitive Disclosure): exposición (QGA podría exponer detalles de seguridad), control (salida estructurada sin datos sensibles + revisión humana)
- [x] 4.3 Redactar tabla con riesgo LLM06 (Excessive Agency): exposición (QGA opera solo en web, sin tokens de GitHub), control (mínimo privilegio, solo produce texto)

## 5. Sección Especificación del agente QGA

- [x] 5.1 Redactar tabla con campos: Nombre (QualityGate Auditor), Rol (revisa PRs contra ISO 25010), Prompt de sistema (Auditor Adversario)
- [x] 5.2 Completar tabla con: Entradas (diff del PR + Anexo de Calidad + resultados CI/CD), Salidas (tabla con Criterio/Umbral/Evidencia/Dictamen + veredicto)
- [x] 5.3 Completar tabla con: Control humano (Custodio de Calidad verifica cada dictamen), Cumplimiento ISO 42001 (Cláusulas 9 y 10)

## 6. Sección Protocolo de control humano

- [x] 6.1 Redactar regla: ningún PR sin revisión explícita del Custodio de Calidad
- [x] 6.2 Redactar regla: dictamen del QGA es insumo informativo, no decisión final
- [x] 6.3 Redactar procedimiento de registro de incidentes (PR rechazado → bitácora con causa y acción correctiva)
- [x] 6.4 Redactar protocolo de calibración cada 5 PRs con prueba de mutación

## 7. Sección Bibliografía

- [x] 7.1 Incluir referencia a ISO/IEC 42001:2023 con enlace
- [x] 7.2 Incluir referencia a ISO/IEC 23894:2023 con enlace
- [x] 7.3 Incluir referencia a OWASP LLM Top 10 2025 con enlace
- [x] 7.4 Incluir referencia a NIST AI RMF 1.0 con enlace
- [x] 7.5 Incluir referencia a EU AI Act (Reglamento 2024/1689) con enlace

## 8. Validación final

- [x] 8.1 Verificar que el archivo `anexo_gobernanza_ia.md` existe en la raíz del proyecto
- [x] 8.2 Verificar que todas las tablas de mapeo tienen el formato Markdown correcto
- [x] 8.3 Verificar que las referencias cruzadas a archivos existentes son correctas
- [x] 8.4 Verificar que el documento es autocontenido (no requiere archivos externos para su comprensión)
- [x] 8.5 Verificar que todos los enlaces de la bibliografía y referencias cruzadas sean accesibles (no 404)
- [x] 8.6 Verificar que la tabla de control de versiones está presente al inicio del documento
