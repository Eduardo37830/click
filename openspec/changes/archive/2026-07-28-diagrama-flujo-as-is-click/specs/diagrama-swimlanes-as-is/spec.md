## ADDED Requirements

### Requirement: Diagrama de proceso as-is con 4 carriles
El sistema SHALL generar un diagrama draw.io con exactamente 4 carriles horizontales swimlane que modelen el flujo PR→release de `pallets/click`.

#### Scenario: Creación de archivo .drawio
- **WHEN** se ejecuta la implementación
- **THEN** se crea `Diagrama_flujo_click.drawio` en la raíz del proyecto

#### Scenario: Exportación a PNG
- **WHEN** se ejecuta `drawio -x -f png -o Diagrama_flujo_click.png`
- **THEN** se genera `Diagrama_flujo_click.png` con el mismo contenido que el .drawio

### Requirement: Carril Contribuyente
El carril Contribuyente SHALL contener 4 actividades secuenciales y usar color de fondo azul claro `#E8F4FD`. La actividad 3 (pre-commit local) SHALL representarse como rectángulo redondeado con borde punteado (dashed) y etiqueta `[OPCIONAL]`, NO como gate con rombo.

#### Scenario: Actividades del carril Contribuyente
- **WHEN** se inspecciona el carril Contribuyente
- **THEN** DEBE contener: (1) Hacer fork del repo, (2) Desarrollar fix/feature en rama, (3) [OPCIONAL] Pre-commit local con los 8 hooks listados (rectángulo punteado, sin rombo), (4) Abrir Pull Request

#### Scenario: Pre-commit no es gate
- **WHEN** se revisa el elemento visual del paso 3
- **THEN** DEBE ser un rectángulo redondeado con borde punteado (dashed)
- **THEN** NO DEBE ser un rombo (diamond shape)
- **THEN** DEBE tener la etiqueta "[OPCIONAL]" visible

### Requirement: Carril CI/CD
El carril CI/CD SHALL contener 2 actividades con un gate y usar color de fondo naranja claro `#FFF3E0`.

#### Scenario: Actividades del carril CI/CD
- **WHEN** se inspecciona el carril CI/CD
- **THEN** DEBE contener: (5) Disparar workflows en paralelo (Tests matrix 9 combos, Typing mypy, Zizmor, Flask regression), (6) [GATE - ROMBO] ¿Todos los checks pasan?

#### Scenario: Gate CI
- **WHEN** el gate "¿Todos los checks pasan?" es Sí
- **THEN** DEBE tener flecha verde hacia carril Mantenedor
- **WHEN** el gate es No
- **THEN** DEBE tener flecha punteada roja de vuelta al paso 2 de Contribuyente

### Requirement: Carril Mantenedor
El carril Mantenedor SHALL contener 4 actividades con un gate y usar color de fondo verde claro `#E8F5E9`.

#### Scenario: Actividades del carril Mantenedor
- **WHEN** se inspecciona el carril Mantenedor
- **THEN** DEBE contener: (7) Recibe PR con checks verdes, (8) Review humano, (9) [GATE] ¿Review aprobado?, (10) Verificar/Actualizar CHANGES.md, (11) Crear tag de versión

#### Scenario: Gate Review
- **WHEN** el gate "¿Review aprobado?" es Sí
- **THEN** DEBE continuar a Merge a main
- **WHEN** el gate es No
- **THEN** DEBE tener flecha punteada roja de vuelta al paso 2 de Contribuyente

### Requirement: Carril Release
El carril Release SHALL contener 1 actividad y usar color de fondo morado claro `#F3E5F5`.

#### Scenario: Actividad del carril Release
- **WHEN** se inspecciona el carril Release
- **THEN** DEBE contener: (12) Ejecutar publish.yaml con pila (uv build → Draft GitHub Release → PyPI OIDC)

### Requirement: Notas de vacíos de calidad
El diagrama SHALL incluir una leyenda tipo sticky note que identifique los quality gates ausentes en el proceso as-is.

#### Scenario: Sticky notes visibles
- **WHEN** se visualiza el diagrama
- **THEN** DEBE mostrar 3 etiquetas: "AUSENTE: gate de cobertura de código", "AUSENTE: análisis estático de calidad (Sonar/CodeQL)", "Vacíos cubiertos por la Interventoría con SonarCloud"

### Requirement: Tamaño de página A4 apaisado
El archivo `.drawio` SHALL tener configurado el tamaño de página en A4 apaisado (1169 x 827 px) para garantizar que el PNG exportado no trunque actividades ni gates.

#### Scenario: Configuración de página en draw.io
- **WHEN** se abre `Diagrama_flujo_click.drawio` en draw.io
- **THEN** el tamaño de página DEBE ser A4 apaisado (1169 x 827 px)
- **WHEN** se exporta a PNG con `drawio -x -f png`
- **THEN** el PNG DEBE mostrar el diagrama completo sin recortes
