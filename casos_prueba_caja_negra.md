# Casos de prueba de caja negra — Anexo V&V

Técnica: **partición en clases de equivalencia + análisis de valores límite**.
Objeto bajo prueba: `IntRange`, `Choice`, flags booleanos (`src/click/types.py`,
`src/click/core.py`). Ejecutado con `click.testing.CliRunner` — ver
[pruebas_caja_negra.py](pruebas_caja_negra.py) (código) y
[evidencia_pruebas_caja_negra.txt](evidencia_pruebas_caja_negra.txt) (resultado
real de la ejecución: **10/10 passed**).

| # | Tipo/objeto | Entrada | Clase de equivalencia / técnica | Resultado esperado | Resultado obtenido |
|---|---|---|---|---|---|
| TC1 | `IntRange(0, 10)` | `--n 5` | Partición válida — valor central del rango | `exit_code=0`, `n=5` | ✅ PASSED |
| TC2 | `IntRange(0, 10)` | `--n 0` | Valor límite — frontera inferior inclusiva | `exit_code=0`, `n=0` | ✅ PASSED |
| TC3 | `IntRange(0, 10)` | `--n 10` | Valor límite — frontera superior inclusiva | `exit_code=0`, `n=10` | ✅ PASSED |
| TC4 | `IntRange(0, 10)` | `--n -1` | Valor límite — justo bajo la frontera inferior (partición inválida) | `exit_code=2`, error "not in the range" | ✅ PASSED |
| TC5 | `IntRange(0, 10)` | `--n 11` | Valor límite — justo sobre la frontera superior (partición inválida) | `exit_code=2`, error "not in the range" | ✅ PASSED |
| TC6 | `IntRange(0, 10, clamp=True)` | `--n 15` | Partición inválida con `clamp=True` — debe ajustarse, no fallar | `exit_code=0`, `n=10` (clamped) | ✅ PASSED |
| TC7 | `Choice(["red","green","blue"])` | `--color green` | Partición válida — valor perteneciente al conjunto | `exit_code=0`, `color=green` | ✅ PASSED |
| TC8 | `Choice(["red","green","blue"])` | `--color purple` | Partición inválida — valor fuera del conjunto | `exit_code=2`, error "is not one of" | ✅ PASSED |
| TC9 | Flag booleano (`is_flag=True`) | *(sin `--verbose`)* | Partición — flag ausente, usa default | `exit_code=0`, `verbose=False` | ✅ PASSED |
| TC10 | Flag booleano (`is_flag=True`) | `--verbose` | Partición — flag presente explícitamente | `exit_code=0`, `verbose=True` | ✅ PASSED |

**Resultado global:** 10/10 casos superados (100%). No se encontraron defectos
en el comportamiento de `IntRange`, `Choice` ni en flags booleanos bajo estas
particiones — el comportamiento observado es consistente con lo documentado.
Esto es evidencia de **verificación positiva** (el código hace lo que dice
hacer); no reemplaza el hallazgo de defectos reales listado en
`lunes_entregables.md` (que provienen de bugs históricos ya corregidos, no de
comportamiento actual).

## Reproducción

```bash
python -m venv .venv_audit
.venv_audit/Scripts/pip install -e . pytest
.venv_audit/Scripts/python -m pytest pruebas_caja_negra.py -v
```
