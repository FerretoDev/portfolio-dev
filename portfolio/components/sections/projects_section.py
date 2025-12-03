import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import badge_style, card_style
from portfolio.constants import projects
from portfolio.utils.icons import github_icon


def project_item(project: dict) -> rx.Component:
    """
    Componente individual para cada proyecto
    """
    name = project["name"]
    url = project["url"]
    github = project.get("github")
    description = project["description"]
    is_active = project.get("isActive", False)
    highlights = project.get("highlights", [])

    # Construir el header del proyecto
    # El header debe ser una fila (hstack) de elementos
    header_elements = [
        rx.link(
            name,
            href=url,
            target="_blank",
            title=f"Ver el proyecto {name}",
            style={
                "color": "#111",
                "text_decoration": "none",
                "_hover": {"text_decoration": "underline"},
            },
        )
    ]

    # Indicador de proyecto activo
    if is_active:
        header_elements.append(
            rx.text(
                "•",
                class_name="active-indicator",
                style={
                    # "color": "rgb(0, 188, 47)",
                    "color": "rgb(29, 196, 71)",
                    "margin_left": "8px",
                },
            )
        )

    # Enlace al código fuente en GitHub
    if github:
        header_elements.append(
            rx.link(
                github_icon(),
                href=github,
                target="_blank",
                title=f"Ver código fuente del proyecto {name}",
                class_name="github-code-link",
                style={
                    "margin_left": "5px",
                    "color": "#111",
                    "text_decoration": "none",
                    "_hover": {"opacity": "0.7"},
                },
            )
        )

    return rx.list_item(
        rx.box(
            # Header con título, estado y enlace GitHub
            rx.box(
                rx.hstack(
                    *header_elements,
                    style={
                        "margin_bottom": "4px",
                        "margin": "0 0 4px 0",
                        "display": "flex",
                        "align_items": "center",
                        "flex_wrap": "wrap",
                    },
                ),
                rx.text(
                    description,
                    style={
                        "font_size": "0.75rem",
                        "line_height": "1.2rem",
                        "margin_bottom": "4px",
                        "color": "#666",
                    },
                ),
                style={"flex": "1"},
            ),
            # Footer con highlights/tecnologías
            rx.box(
                *[
                    rx.text(
                        highlight,
                        # tag="span",
                        style=highlight_style,
                    )
                    for highlight in highlights
                ],
                # tag="footer",
                style=footer_style,
            ),
            # tag="article",
            style=article_style,
        )
    )


def projects_section() -> rx.Component:
    """
    Sección completa de proyectos
    """
    return rx.fragment(
        section_component(
            title="Proyectos",
            children=[
                rx.unordered_list(
                    *[project_item(project) for project in projects],
                    style=projects_ul_style,
                )
            ],
        ),
        # Estilos CSS para animaciones y responsive
    )


# Estilos definidos como diccionarios
projects_ul_style = {
    "display": "grid",
    "grid_template_columns": "repeat(auto-fit, minmax(200px, 1fr))",
    "gap": "1rem",
    "margin_inline": "-16px",
    "list_style": "none",
    "margin": "0 -16px",
    "padding": "0",
}

article_style = card_style

footer_style = {
    "display": "flex",
    "flex_wrap": "wrap",
    "gap": "4px",
    "font_size": "0.6rem",
}

highlight_style = badge_style


# Versión alternativa con filtros por estado
def projects_section_with_filters() -> rx.Component:
    """
    Versión con filtros para proyectos activos/inactivos
    """
    active_projects = [p for p in projects if p.get("isActive", False)]
    inactive_projects = [p for p in projects if not p.get("isActive", False)]

    return section_component(
        title="Proyectos",
        children=[
            # Proyectos activos
            (
                rx.box(
                    rx.heading(
                        "🟢 Proyectos Activos",
                        level=3,
                        style={
                            "font_size": "1.1rem",
                            "margin_bottom": "12px",
                            "color": "#333",
                        },
                    ),
                    rx.unordered_list(
                        *[project_item(project) for project in active_projects],
                        style={
                            **projects_ul_style,
                            "margin_bottom": "32px",
                        },
                    ),
                )
                if active_projects
                else rx.fragment()
            ),
            # Proyectos archivados
            (
                rx.box(
                    rx.heading(
                        "📁 Proyectos Archivados",
                        level=3,
                        style={
                            "font_size": "1.1rem",
                            "margin_bottom": "12px",
                            "color": "#666",
                        },
                    ),
                    rx.unordered_list(
                        *[project_item(project) for project in inactive_projects],
                        style=projects_ul_style,
                    ),
                )
                if inactive_projects
                else rx.fragment()
            ),
        ],
    )


# Versión compacta para portfolios minimalistas
def project_item_compact(project: dict) -> rx.Component:
    """
    Versión compacta del item de proyecto
    """
    name = project["name"]
    url = project["url"]
    github = project.get("github")
    description = project["description"]
    is_active = project.get("isActive", False)

    return rx.box(
        rx.box(
            # Título con enlaces en línea
            rx.link(
                name,
                href=url,
                target="_blank",
                style={"font_weight": "600", "color": "#111"},
            ),
            (
                rx.text("•", style={"color": "rgb(0, 188, 47)", "margin": "0 8px"})
                if is_active
                else rx.fragment()
            ),
            (
                rx.link(
                    "GitHub",
                    href=github,
                    target="_blank",
                    style={"font_size": "0.8rem", "color": "#666"},
                )
                if github
                else rx.fragment()
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "gap": "8px",
                "margin_bottom": "4px",
            },
        ),
        rx.text(
            description,
            style={"font_size": "0.85rem", "color": "#666", "line_height": "1.3"},
        ),
        style={
            "margin_bottom": "16px",
            "padding_bottom": "16px",
            "border_bottom": "1px solid #f0f0f0",
        },
    )


def projects_section_compact() -> rx.Component:
    """
    Versión compacta de la sección de proyectos
    """
    return section_component(
        title="Proyectos",
        children=[rx.box(*[project_item_compact(project) for project in projects])],
    )
