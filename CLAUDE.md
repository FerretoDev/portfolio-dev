# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run development server (hot reload)
reflex run

# Export static site
reflex export

# Type checking
mypy portfolio/

# Install dependencies
pip install -r requirements.txt
```

## Architecture

Personal portfolio built with **[Reflex](https://reflex.dev/)** (Python full-stack framework). Reflex compiles Python into React/Next.js with a FastAPI backend. Code comments, UI strings, and section titles are in **Spanish**.

### Entry Points

- `rxconfig.py` — Reflex config with `SitemapPlugin`
- `portfolio/portfolio.py` — `rx.App` init; applies `global_style()` and loads Inter font via Google Fonts stylesheet
- `portfolio/pages/index.py` — Main page (`@rx.page("/", "Portfolio")`), assembles all sections
- `portfolio/pages/projects/[id].py` — Dynamic project detail page

### Data Flow

All CV data lives in `portfolio/constants.py`: `basics`, `work`, `education`, `skills`, `projects`. Sections import directly from there — no database or reactive state needed for static content.

### Shared Utilities

- `portfolio/utils/date_utils.py` — `format_date_to_year(date_string)` converts `"YYYY-MM-DD"` → year string or `"Actual"`
- `portfolio/utils/icons.py` — `SOCIAL_ICONS` and `SKILLS_ICONS` dicts mapping names to icon functions; icons load from simple-icons CDN via `create_simple_icon(name)`

### Component Patterns

**Section wrapper** — `components/section.py` exports `section_component(title, children)`. This is the canonical wrapper for all page sections; it applies `section_box_style` and `section_title_style` from `styles.py`.

**Shared section styles** — `components/sections/common_styles.py` holds style dicts reused across sections: `list_vertical_style`, `item_header_style`, `time_display_style`, `badge_style`, `skill_badge_style`, `card_style`, hero styles, and project styles. Use these instead of defining new inline style dicts.

**Layout styles** — `components/styles/styles.py` defines `@dataclass` style objects (e.g., `header_style`, `footer_style`, `layout_style`) and flat style dicts (`section_box_style`, `section_title_style`, `layout_box_style`). Instances use lowercase names (e.g., `card_style`, not `CardStyle`).

### Styling Conventions

- Global theme tokens are in `GlobalThemeVariables` enum (`styles.py`); use `rx.color_mode_cond(light=..., dark=...)` for theme-aware values.
- Responsive breakpoints: `640px` (mobile), `768px` (tablet), `1024px` (desktop) — defined as `BREAKPOINTS` in `common_styles.py`.
- CSS media queries as nested dicts: `"@media (max-width: 640px)": {...}`.

### Reflex-Specific Patterns

- Pages registered via `@rx.page(route, title)` — no manual `app.add_page()` needed.
- `rx.cond()` and `rx.color_mode_cond()` for conditional rendering.
- Static assets in `assets/`, referenced by filename only (e.g., `src="Designer.jpg"`).

### Unused Scaffolding

- `state/auth.py`, `state/projects.py` — not actively used
- `translation/schemas.py`, `translation/es.py` — ES/EN translation scaffold, not wired up

## Mejoras Pendientes

Refactorizaciones acordadas y en progreso, en orden:

1. ✅ **Datos de educación en `constants.py`** — resuelto, `education_section.py` ya importa desde `constants`.
2. ✅ **Duplicación de `section_component`** — resuelto, todos los archivos importan desde `components/section.py`.
3. ✅ **Inconsistencia de estilos** — resuelto, todos los dicts inline movidos a `common_styles.py`.
4. ✅ **`state/` sin usar** — resuelto, `auth.py` y `projects.py` eliminados (estaban vacíos).
5. ~~**Patrón de impresión**~~ — descartado, no es prioritario.
6. ✅ **Idioma consistente** — resuelto, todos los comentarios están en español.
