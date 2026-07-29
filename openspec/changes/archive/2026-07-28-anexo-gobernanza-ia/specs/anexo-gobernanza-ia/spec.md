## ADDED Requirements

### Requirement: Documento anexo de gobernanza de IA
El sistema SHALL incluir un archivo `anexo_gobernanza_ia.md` en la raíz del proyecto que documento la política de gestión de inteligencia artificial para el flujo de contribuciones.

#### Scenario: El anexo existe en la raíz del proyecto
- **WHEN** se inspecciona la raíz del proyecto
- **THEN** el archivo `anexo_gobernanza_ia.md` SHALL existir

### Requirement: Mapeo ISO/IEC 42001
El anexo SHALL mapear las cláusulas 5 (Liderazgo), 6 (Planificación), 7 (Soporte), 8 (Operación), 9 (Evaluación) y 10 (Mejora) de ISO/IEC 42001 al contexto del proyecto click.

#### Scenario: Tabla de mapeo ISO 42001 presente
- **WHEN** se lee el anexo
- **THEN** DEBE contener una tabla que asigne cada cláusula ISO 42001 (5, 6, 7, 8, 9, 10) a su aplicación en click

#### Scenario: Cláusula 8 (Operación) documentada
- **WHEN** se lee la tabla de mapeo ISO 42001
- **THEN** DEBE incluir una fila para Cláusula 8 (Operación) explicando que el QGA cubre parcialmente los controles de operación, y que el proceso PR→release definido en el diagrama as-is completa el ciclo operativo

### Requirement: Gestión de riesgos ISO/IEC 23894
El anexo SHALL aplicar el ciclo de 6 fases de ISO/IEC 23894 (Contexto, Identificación, Análisis, Evaluación, Tratamiento, Monitoreo) al flujo PR→release de click.

#### Scenario: Tabla de ciclo de riesgos presente
- **WHEN** se lee la sección de ISO 23894 en el anexo
- **THEN** DEBE contener una tabla con las 6 fases del ciclo, cada una con su descripción aplicada a click

### Requirement: Riesgos OWASP LLM Top 10 2025
El anexo SHALL documentar los riesgos LLM01 (Prompt Injection), LLM02 (Sensitive Disclosure) y LLM06 (Excessive Agency) de OWASP LLM Top 10 2025, específicos del agente QualityGate Auditor.

#### Scenario: Tabla OWASP con controles
- **WHEN** se lee la sección de OWASP en el anexo
- **THEN** DEBE contener una tabla que asocie cada riesgo OWASP (LLM01, LLM02, LLM06) con su exposición en click y el control implementado

### Requirement: Especificación del agente QualityGate Auditor
El anexo SHALL documentar la especificación del agente QGA incluyendo: nombre, rol, prompt de sistema, entradas, salidas, y control humano requerido.

#### Scenario: Tabla de especificación QGA presente
- **WHEN** se lee la sección del agente QGA en el anexo
- **THEN** DEBE contener una tabla con los campos Nombre, Rol, Prompt de sistema, Entradas, Salidas, Control humano, y Cumplimiento ISO 42001

### Requirement: Protocolo de control humano
El anexo SHALL definir que ningún PR puede ser mergeado sin revisión explícita del Custodio de Calidad, y que el dictamen del QGA es insumo informativo no decisión final.

#### Scenario: Protocolo de control humano documentado
- **WHEN** se lee la sección de control humano en el anexo
- **THEN** DEBE especificar que el Custodio de Calidad verifica cada dictamen del QGA antes del merge

### Requirement: Métricas de monitoreo
El anexo SHALL definir métricas para monitorear la efectividad del QGA: PRs rechazados, time-to-merge, tasa de aprobación QGA, y regresiones post-release.

#### Scenario: Tabla de métricas presente
- **WHEN** se lee la sección de monitoreo en el anexo
- **THEN** DEBE contener al menos 4 métricas con su descripción y periodicidad

### Requirement: Protocolo de calibración del QGA
El anexo SHALL establecer un protocolo de calibración del QGA cada 5 PRs mediante pruebas de mutación con defectos conocidos.

#### Scenario: Calibración documentada
- **WHEN** se lee la sección de calibración en el anexo
- **THEN** DEBE especificar la frecuencia (cada 5 PRs) y el método (prueba de mutación con defecto conocido)

### Requirement: Control de versiones del documento
El archivo `anexo_gobernanza_ia.md` SHALL incluir al inicio una tabla de control de versiones con las columnas: Versión, Fecha, Autor, Descripción de cambios.

#### Scenario: Tabla de versiones presente
- **WHEN** se lee el anexo
- **THEN** DEBE contener una tabla de control de versiones al inicio del documento

### Requirement: Bibliografía normativa
El anexo SHALL incluir una sección de bibliografía con referencias a ISO/IEC 42001:2023, ISO/IEC 23894:2023, OWASP LLM Top 10 2025, NIST AI RMF 1.0, y EU AI Act 2024/1689.

#### Scenario: Bibliografía completa
- **WHEN** se lee la sección de bibliografía en el anexo
- **THEN** DEBE contener referencias a los 5 estándares/normativas listados
