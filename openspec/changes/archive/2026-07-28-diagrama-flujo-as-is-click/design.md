## Context

El informe de interventoría para `pallets/click` requiere en su sección S2 un diagrama de proceso as-is modelado con carriles (swimlanes) que documente el flujo real de gestión de cambios desde el Pull Request hasta el Release publicado en PyPI. El archivo `entregable.md` ya contiene la descripción textual del flujo y los quality gates reales identificados. El diseño aquí documentado traduce esa evidencia a un diagrama draw.io (`Diagrama_flujo_click.drawio`) más su exportación PNG.

## Goals / Non-Goals

**Goals:**
- Crear un archivo `Diagrama_flujo_click.drawio` en la raíz del proyecto
- Modelar el flujo as-is con 4 carriles, actividades numeradas, gates bloqueantes, loops de corrección y notas de vacíos
- Exportar `Diagrama_flujo_click.png` con `drawio -x -f png`

**Non-Goals:**
- No rediseñar el proceso (es as-is, no to-be)
- No modificar código fuente, tests, pipelines, ni configuraciones existentes
- No generar documentación adicional más allá del diagrama

## Decisions

| Decisión | Opciones | Elegido | Razón |
|---|---|---|---|
| Formato de archivo | `.drawio` nativo vs. SVG vs. Mermaid | `.drawio` | La rúbrica del proyecto exige formato .drawio editable para la entrega |
| Herramienta de exportación | draw.io CLI vs. web export | `drawio -x -f png` | Se ejecuta en consola, idempotente, trazable en el pipeline |
| Número de carriles | 3 (sin Release) vs. 4 con Release separado | 4 carriles | El workflow `publish.yaml` es un proceso distinto con actor y gatillo diferentes |
| Notas de vacíos | En el diagrama vs. en texto aparte | Sticky notes dentro del diagrama | Visibilidad inmediata: el evaluador ve los vacíos sin buscar en otro lado |
| Subprocesos paralelos | Flechas separadas vs. pila bracket | Pila de rectángulos | Reduce ruido visual; los 4 workflows de CI se disparan en paralelo y no requieren secuencia |
| Representación del pre-commit | Rombo (gate) vs. rectángulo punteado | Rectángulo punteado + etiqueta "[OPCIONAL]" | El pre-commit no es bloqueante, el contribuyente puede saltárselo. Un gate con rombo implica decisión obligatoria, lo cual es incorrecto. |
| Tamaño de página draw.io | Por defecto vs. A4 apaisado (1169x827 px) | A4 apaisado | El diagrama tiene 4 carriles con subpilas; A4 apaisado evita truncamiento en la exportación PNG |

## Risks / Trade-offs

- [Riesgo] draw.io CLI (Electron) puede no estar instalado en el entorno actual → Mitigación: verificar con `which drawio` antes de la exportación
- [Riesgo] El PNG puede quedar truncado si el diagrama es muy grande → Mitigación: usar tamaño de página A4 apaisado en draw.io
- [Trade-off] Se prioriza fidelidad al proceso real sobre estética. Los colores de carril son los especificados para cumplir la rúbrica, no por preferencia visual
