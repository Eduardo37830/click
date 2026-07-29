## 1. Crear archivo .drawio

- [x] 1.1 Crear `Diagrama_flujo_click.drawio` en la raíz del proyecto con estructura XML de draw.io
- [x] 1.2 Agregar los 4 carriles con sus colores: Contribuyente (#E8F4FD), CI/CD (#FFF3E0), Mantenedor (#E8F5E9), Release (#F3E5F5)
- [x] 1.3 Agregar actividades del carril Contribuyente (pasos 1-4) con subpila de pre-commit como rectángulo punteado + etiqueta [OPCIONAL] (sin rombo)
- [x] 1.4 Configurar tamaño de página en A4 apaisado (1169 x 827 px) en las propiedades del diagrama
- [x] 1.5 Agregar actividades del carril CI/CD (pasos 5-6) con gate rombo y subpila de workflows paralelos
- [x] 1.6 Agregar actividades del carril Mantenedor (pasos 7-11) con gate rombo de review
- [x] 1.7 Agregar actividad del carril Release (paso 12) con subpila build→draft→PyPI
- [x] 1.8 Agregar flechas de conexión entre actividades y gates
- [x] 1.9 Agregar flechas punteadas rojas de loop de corrección (desde gates CI/Review hacia paso 2)
- [x] 1.10 Agregar sticky notes de vacíos de calidad (cobertura, Sonar/CodeQL, nota de Interventoría)

## 2. Exportar PNG

- [x] 2.1 Verificar que `drawio` CLI esté instalado (`which drawio`)
- [x] 2.2 Exportar `Diagrama_flujo_click.png` con `drawio -x -f png -o Diagrama_flujo_click.png Diagrama_flujo_click.drawio`

## 3. Verificar

- [x] 3.1 Confirmar que `Diagrama_flujo_click.drawio` existe y contiene XML válido
- [x] 3.2 Confirmar que `Diagrama_flujo_click.png` existe y es una imagen válida
