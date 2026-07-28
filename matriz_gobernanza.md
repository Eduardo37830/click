# Matriz de gobernanza — click (pallets/click)

Verificación directa contra el repositorio y la organización GitHub `pallets`
(no inferido). Fuente por ítem, estado y observación de riesgo cuando aplica.

| Ítem | Estado | Evidencia | Observación |
|---|---|---|---|
| **CONTRIBUTING** | ✅ Presente | [docs/contributing.md](https://github.com/pallets/click/blob/main/docs/contributing.md) | Es una guía específica del repo que remite a la guía general de Pallets ([quick reference](https://palletsprojects.com/contributing/quick/)) — gobernanza **a nivel de organización**, no aislada por proyecto. |
| **SECURITY.md** | ✅ Presente (heredado) | [pallets/.github/SECURITY.md](https://github.com/pallets/.github/blob/main/SECURITY.md) | **No vive en el repo de `click`**, se hereda del repo especial `pallets/.github`. Política de divulgación privada vía GitHub Security Advisories o `security@palletsprojects.com`; CVE gestionado por los mantenedores. **Sin SLA comprometido** ("cannot guarantee any specific timeline") — riesgo a documentar en el dictamen si la plataforma pública tiene requisitos de tiempo de respuesta. |
| **Código de conducta** | ✅ Presente (heredado) | [pallets/.github/CODE_OF_CONDUCT.md](https://github.com/pallets/.github/blob/main/CODE_OF_CONDUCT.md) | Contributor Covenant estándar, aplicado a nivel de organización — GitHub lo reconoce automáticamente en el community profile de `click` (`community/profile` → `code_of_conduct`). |
| **Plantillas de Issues** | ✅ Presente | [.github/ISSUE_TEMPLATE/bug-report.md](.github/ISSUE_TEMPLATE/bug-report.md), [feature-request.md](.github/ISSUE_TEMPLATE/feature-request.md), [config.yml](.github/ISSUE_TEMPLATE/config.yml) | Diferenciadas por tipo (bug vs feature), con `config.yml` (probablemente enlaza a Discord/Discussions para preguntas generales, evitando ruido en el issue tracker). |
| **Plantilla de Pull Request** | ✅ Presente | [.github/pull_request_template.md](.github/pull_request_template.md) | — |
| **Versionado** | ✅ SemVer consistente | Tags recientes: `8.4.2`, `8.4.1`, `8.4.0`, `8.3.3`, `8.3.2`, `8.3.1`, `8.3.0` (`gh api repos/pallets/click/tags`) | Sigue `MAJOR.MINOR.PATCH` de forma estricta; los patches (`.1`, `.2`, `.3`) corresponden a fixes, confirmado en `CHANGES.md` (ver hallazgo de change-failure-rate en `lunes_entregables.md`). |
| **Cadencia de release** | ⚠️ Irregular | Ventana 8.3.0→8.4.2: 6 releases en 281 días (~1 cada 47 días); gap de 58 días entre 8.3.0 y 8.3.1 | No hay cadencia fija anunciada (no es "release train"); depende de acumulación de fixes y disponibilidad de mantenedores voluntarios. |
| **Bus factor** | 🔴 Riesgo alto | `git shortlog -sn upstream/main`: David Lord 876 commits (~18.7% del histórico de 469 contribuyentes), Armin Ronacher 593 (~12.6%) | Los 2 principales concentran ~31% de todo el historial de commits. Es voluntariado ("Maintainers are volunteers working in their free time" — texto literal de `SECURITY.md`), sin garantía de continuidad. **Hallazgo crítico para el dictamen de adopción.** |
| **Templates de release / changelog** | ✅ Presente y disciplinado | [CHANGES.md](CHANGES.md) | Cada entrada referencia `{issue}` y `{pr}` — trazabilidad casi total entre defecto reportado y fix mergeado (permitió construir la tabla de 19 issues de `lunes_entregables.md`). |
| **Revisión de código obligatoria** | ✅ De facto | Histórico de PRs mergeados vía `gh pr list --state merged` — no se observan commits directos a `main` fuera de merges de PR | No hay `CODEOWNERS` explícito; la revisión recae en el pool de mantenedores sin asignación automática por módulo. |
| **CI como gate de calidad** | ✅ Presente, robusto | `.github/workflows/tests.yaml` (9 combinaciones OS/Python + typing), `zizmor.yaml` (seguridad de workflows), regresión contra Flask | Ver detalle completo en `lunes_entregables.md` §2. No incluye gate de cobertura ni análisis estático de calidad nativo — vacío que este audit cubre con SonarCloud. |
| **Publicación segura a PyPI** | ✅ Buena práctica | `.github/workflows/publish.yaml` usa **OIDC trusted publishing** (`id-token: write`), sin token estático de PyPI en secrets | Reduce superficie de ataque de cadena de suministro (no hay token de larga vida que pueda filtrarse). |
| **Gestión de dependencias** | ✅ Automatizada | `uv-lock` en pre-commit + actividad de `dependabot[bot]`/`dependabot-preview[bot]` en el historial de commits | — |
| **Canal de comunicación de la comunidad** | ✅ Presente | Discord (`https://discord.gg/pallets`, en `pyproject.toml` → `project.urls.Chat`), GitHub Discussions habilitado (`has_discussions: true`) | — |
| **Licencia clara y OSI-aprobada** | ✅ BSD-3-Clause | [LICENSE.txt](LICENSE.txt), confirmado vía `gh api repos/pallets/click` → `license.spdx_id` | Sin restricciones para uso en plataforma pública. |
| **Health score de GitHub (community profile)** | ✅ 100% | `gh api repos/pallets/click/community/profile` → `health_percentage: 100` | Métrica agregada de GitHub; no sustituye el análisis cualitativo de esta matriz (p. ej. no penaliza el bus factor ni la ausencia de SLA de seguridad). |

## Lectura para el dictamen

**Fortalezas de gobernanza:** política de seguridad formal (aunque heredada),
trazabilidad issue↔PR↔changelog casi perfecta, CI robusto, publicación a PyPI
sin secretos estáticos.

**Riesgos a condicionar en la adopción:**
1. **Bus factor concentrado** (David Lord + Armin Ronacher ≈ 31% del historial) — la Secretaría TIC debería exigir un plan de contingencia o monitoreo de continuidad del proyecto antes de depender de él en producción crítica.
2. **Sin SLA de respuesta a vulnerabilidades** — el propio `SECURITY.md` renuncia explícitamente a comprometer tiempos. Si la plataforma pública tiene requisitos regulatorios de tiempo de remediación, esto debe compensarse con monitoreo propio (p. ej. Dependabot/CVE feeds del lado del consumidor).
3. **Cadencia de release irregular** — no apta para planificación de actualizaciones con fecha fija; se recomienda pinning de versión + revisión manual de `CHANGES.md` antes de actualizar.
