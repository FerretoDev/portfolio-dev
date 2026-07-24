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

- **Colores con `rx.color(name, shade)`** — forma correcta según la documentación de Reflex. Genera variables CSS de Radix (`var(--slate-11)`) que funcionan en SSR sin problemas de hidratación. El shade va de 1 (más claro) a 12 (más oscuro). Ejemplos de uso:
  - Texto primario: `rx.color("slate", 12)`
  - Texto secundario/muted: `rx.color("slate", 11)`
  - Fondos sutiles/badges: `rx.color("slate", 3)`
  - Bordes: `rx.color("slate", 6)`
  - Color de acento (hover, links activos): `rx.color("accent", 10)` — hereda del `accent_color` del tema
- **NO usar `rx.color_mode_cond()` para nada** — genera expresiones JS (`resolvedColorMode`) que se evalúan en el cliente después de la hidratación SSR, causando que la página "se rompa" ~1 segundo después de cargar (hydration mismatch). La excepción es condicionales de componentes completos (no props de estilo).
- **NO usar `rx.color_mode_cond()` dentro de `global_style()`** — esa función compila a CSS estático en `theme.js` donde las expresiones JS no están disponibles. Usar `"var(--slate-11)"` directamente.
- **NO instanciar Vars de `rx.color_mode_cond()` a nivel de módulo** (ej. en `default_factory` de un `@dataclass` que se instancia al importar) — aunque el estilo no se use en ningún componente, el Var se crea al importar el módulo e inyecta lógica en el bundle.
- **NO usar `style=global_style()` en `rx.App` con selectores nativos** — aplicar CSS sobre `p`, `h1`, `h2`, `ul`, `a` etc. desde Python colisiona con las reglas que Radix UI inyecta en runtime. El servidor SSR renderiza sin esos estilos de Radix, el cliente los aplica → mismatch → `removeChild` crash. Usar CSS puro en `assets/` en su lugar.
- **`enable_state=False` en `rx.App`** cuando no hay `rx.State` activo — elimina el WebSocket, el overlay flotante de conexión, y el `useEffect` del `RadixThemesColorModeProvider` que manipula el DOM post-hidratación.
- Paleta del tema en `rx.App`: `theme=rx.theme(font_family="Inter", appearance="light", accent_color="cyan")`.
- Responsive breakpoints: `640px` (mobile), `768px` (tablet), `1024px` (desktop) — defined as `BREAKPOINTS` in `common_styles.py`.
- CSS media queries as nested dicts: `"@media (max-width: 640px)": {...}`.

### Reflex-Specific Patterns

- Pages registered via `@rx.page(route, title)` — no manual `app.add_page()` needed.
- `rx.cond()` y `rx.color_mode_cond()` para renderizado condicional (componentes o props no-color).
- Static assets in `assets/`, referenced by filename only (e.g., `src="Designer.jpg"`).

### Unused Scaffolding

- `state/auth.py`, `state/projects.py` — not actively used
- `translation/schemas.py`, `translation/es.py` — ES/EN translation scaffold, not wired up
- `components/styles/styles.py` — `NavbarStyle`, `HeaderStyle`, `LayoutStyle`, `PageStyle`, `SectionStyle`, `CardStyle` están definidos pero **no se usan** en el layout actual. Solo se usan `footer_style`, `text_style`, `section_box_style`, `section_title_style`, `layout_box_style`, `footer_copyright_style`.
- `components/ui/project_card.py` — componente alternativo de card, no está conectado a ninguna página.
- `components/button_color_mode.py` — botón de toggle de modo oscuro/claro, no está montado en ninguna página.
- `pages/projects/[id].py` — página de detalle de proyecto, actualmente **vacía**.

### Patrones de Componentización

- **`rx.unordered_list` / `rx.list_item` prohibidos** — generan `<ul><li>` con bullets del browser que Next.js/Radix no resetean consistentemente. Usar `rx.box` en su lugar.
- **`rx.avatar` prohibido para imágenes reales** — renderiza `<span>` + `<img>` interno; `object_fit` y `aspect_ratio` aplican al span, no al img. Usar `rx.image` directamente.
- **`rx.text` con `as_="span"`** para badges/indicadores inline — `rx.text` sin `as_` genera `<p>` (block-level) que rompe el flex layout. También usar `as_="span"` en `create_link_or_text` y subtítulos para evitar `<p>` dentro de elementos de bloque.
- **`rx.heading` usa `as_="h1"`/`"h2"`/etc., NO `level=N`** — `level` no es un prop válido en Radix y es ignorado, generando siempre `<h1>` → hydration mismatch.
- **No anidar componentes dentro de `rx.heading`** — si el título ya es un `rx.link` o `rx.text`, usarlo directamente sin envolverlo en `rx.heading`. `<h3><a>` es válido pero `<h3><p>` no lo es.
- **`rx.foreach` solo para State vars reactivos** — con listas Python estáticas de `constants.py`, usar comprehensions `*[fn(item) for item in items]`. `rx.foreach` convierte cada elemento a `Var[dict]` y hace que los `if url:`, `.get()` etc. fallen.

## Mejoras Pendientes

Refactorizaciones acordadas y en progreso, en orden:

1. ✅ **Datos de educación en `constants.py`** — resuelto.
2. ✅ **Duplicación de `section_component`** — resuelto.
3. ✅ **Inconsistencia de estilos** — resuelto, dicts en `common_styles.py`.
4. ✅ **`state/` sin usar** — resuelto.
5. ✅ **Colores con `rx.color()`** — resuelto, eliminado todo `rx.color_mode_cond` en props de estilo.
6. ✅ **`rx.unordered_list`/`rx.list_item` → `rx.box`** — resuelto en todas las secciones.
7. ✅ **`rx.avatar` → `rx.image`** — resuelto en hero_section.
8. ✅ **`not_found.py` vacío** — resuelto, página 404 creada e importada.
9. ✅ **`pages/projects/[id].py` vacío** — stub mínimo de página agregado con `@rx.page("/projects/[id]")`. No importada aún desde `portfolio.py` hasta implementar la página completa.
10. ✅ **`GlobalThemeVariables` enum en `styles.py`** — eliminado. Era código muerto con hex hardcodeados de paleta antigua.
11. ✅ **Dataclasses sin usar en `styles.py`** — `NavbarStyle`, `HeaderStyle`, `LayoutStyle`, `PageStyle`, `SectionStyle`, `CardStyle` eliminados. Solo quedan `FooterStyle` y `TextStyle` que sí se usan.
12. ✅ **Iconos cargados desde CDN externo** — SVGs descargados a `assets/icons/` (gmail, linkedin, twitter, github, html5, css3, javascript, git, python, postgresql). `map_pin_icon()` y `phone_icon()` usan `rx.icon()` (Lucide, bundled).
13. ⚠️ **`constants.py` referencias externas** — `BOOK_URL`, `BOOKS_URL`, `SETUP_URL`, `COFFEE_URL`, `MYPUBLICINBOX_URL` apuntan a `mouredev.com` (datos de ejemplo copiados). Actualizar con datos reales.
14. ✅ **`layout.py` tiene `basics` hardcodeado** — dict `basics` dummy y param `title` eliminados.

