## Why

El entregable del equipo auditor para la sección S2 del proyecto La Interventoría requiere un diagrama de proceso as-is (swimlanes) del flujo de gestión de cambios de `pallets/click`. Sin este diagrama, el informe de auditoría carece de la evidencia visual del proceso real que la rúbrica exige. El archivo `.drawio` debe generarse para poder editarlo en draw.io y exportarlo a PNG.

## What Changes

- Crear `Diagrama_flujo_click.drawio` en la raíz del proyecto con el diagrama de 4 carriles (Contribuyente, CI/CD, Mantenedor, Release)
- Exportar `Diagrama_flujo_click.png` desde el archivo `.drawio`
- El diagrama documenta el flujo as-is real extraído del archivo `entregable.md` (sección 2, Quality Gates) y de la evidencia del repositorio

## Capabilities

### New Capabilities
- `diagrama-swimlanes-as-is`: Diagrama de proceso con carriles que modela el flujo PR→release de pallets/click, incluyendo gates bloqueantes, loops de corrección, subprocesos paralelos de CI, y notas de vacíos de calidad.

### Modified Capabilities

## Impact

- Archivo nuevo `Diagrama_flujo_click.drawio` en la raíz del proyecto
- Archivo nuevo `Diagrama_flujo_click.png` (exportación PNG)
- No afecta código fuente, tests, ni pipelines existentes
