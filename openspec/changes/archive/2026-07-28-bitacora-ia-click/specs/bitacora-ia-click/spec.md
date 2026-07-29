## ADDED Requirements

### Requirement: Documento bitácora de auditoría de IA
El sistema SHALL incluir un archivo `bitacora_auditoria_ia.md` en la raíz del proyecto que documente la auditoría de casos de prueba contra la rúbrica Tabla 4.4.

#### Scenario: La bitácora existe en la raíz del proyecto
- **WHEN** se inspecciona la raíz del proyecto
- **THEN** el archivo `bitacora_auditoria_ia.md` SHALL existir

### Requirement: Análisis del componente
La bitácora SHALL incluir una sección de análisis del componente que describa los tipos click bajo prueba (IntRange, Choice, is_flag) con las particiones de equivalencia y valores límite aplicados.

#### Scenario: Sección de análisis presente
- **WHEN** se lee la bitácora
- **THEN** DEBE contener una sección que describa los objetos bajo prueba y las técnicas de V&V aplicadas

### Requirement: Prompt registrado
La bitácora SHALL incluir el prompt ingresado al LLM adaptado a click, solicitando casos de prueba para IntRange, Choice e is_flag con la regla de REQUISITO AMBIGUO.

#### Scenario: Prompt documentado
- **WHEN** se lee la sección de prompt en la bitácora
- **THEN** DEBE contener el texto completo del prompt con instrucciones de partición de equivalencia, valores límite y regla de dominio

### Requirement: Salida del LLM documentada
La bitácora SHALL documentar la salida de 10 casos de prueba (TC1–TC10) con una nota aclaratoria sobre su origen.

#### Scenario: Tabla de 10 casos presente
- **WHEN** se lee la sección de salida del LLM
- **THEN** DEBE contener una tabla con los 10 casos (ID, Entrada, Resultado esperado, Técnica aplicada) y una nota de origen

### Requirement: Rúbrica de 6 criterios aplicada (Tabla 4.4)
La bitácora SHALL evaluar los casos de prueba contra los 6 criterios de la Tabla 4.4 (Funcionalidad, Seguridad, Calidad estructural, Dependencias, Calidad de las pruebas, Trazabilidad) con calificación y fundamento técnico cada uno.

#### Scenario: Tabla de rúbrica completa
- **WHEN** se lee la sección de auditoría
- **THEN** DEBE contener una tabla con 6 filas (una por criterio) incluyendo número, nombre del criterio, calificación (Nivel 1–3) y fundamento técnico

### Requirement: Decisiones por caso documentadas
La bitácora SHALL incluir una tabla de decisiones individuales para cada caso de prueba (TC1–TC10) con columna de decisión, justificación técnica y acción correctiva.

#### Scenario: Tabla de decisiones presente
- **WHEN** se lee la sección de toma de decisiones
- **THEN** DEBE contener una tabla con 10 filas (una por caso) con columnas ID, Decisión, Justificación técnica y Acción correctiva

### Requirement: Conjunto final de pruebas
La bitácora SHALL presentar el conjunto final de pruebas con marca de origen ("Equipo" o "Comité") y referencia a la ejecución verificada.

#### Scenario: Tabla de conjunto final presente
- **WHEN** se lee la sección de conjunto final de pruebas
- **THEN** DEBE contener una tabla que consolide los casos con resultado de ejecución y origen

### Requirement: Artefacto de trazabilidad completa
La bitácora SHALL incluir una sección de trazabilidad con: prompt exacto, salida original, rúbrica diligenciada, correcciones aplicadas, y decisión técnica final.

#### Scenario: Subsecciones de trazabilidad presentes
- **WHEN** se lee la sección de artefacto de trazabilidad
- **THEN** DEBE contener las 5 subsecciones (6.1 a 6.5) documentadas

### Requirement: Nivel de trazabilidad SGIA
La bitácora SHALL declarar el nivel de trazabilidad alcanzado según la Tabla 4.4 (criterio 6) y referenciar los requisitos SGIA del anexo de gobernanza de IA.

#### Scenario: Declaración de nivel presente
- **WHEN** se lee la sección final de la bitácora
- **THEN** DEBE declarar el nivel de trazabilidad alcanzado con referencia a `anexo_gobernanza_ia.md`

### Requirement: Referencias cruzadas a archivos existentes
La bitácora SHALL incluir referencias a `casos_prueba_caja_negra.md`, `pruebas_caja_negra.py`, `anexo_gobernanza_ia.md` y `matriz_gobernanza.md`.

#### Scenario: Enlaces a archivos presentes
- **WHEN** se lee la bitácora
- **THEN** DEBE contener enlaces a los 4 archivos de referencia listados
