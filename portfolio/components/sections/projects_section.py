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
            rx.box(
                rx.hstack(
                    *header_elements,
                    style={
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
            rx.box(
                *[rx.text(highlight, style=badge_style) for highlight in highlights],
                style={
                    "display": "flex",
                    "flex_wrap": "wrap",
                    "gap": "4px",
                    "font_size": "0.6rem",
                },
            ),
            style=card_style,
        )
    )


def projects_section() -> rx.Component:
    """
    Sección completa de proyectos
    """
    return section_component(
        title="Proyectos",
        children=[
            rx.unordered_list(
                *[project_item(project) for project in projects],
                style={
                    "display": "grid",
                    "grid_template_columns": "repeat(auto-fit, minmax(200px, 1fr))",
                    "gap": "1rem",
                    "list_style": "none",
                    "margin": "0 -16px",
                    "padding": "0",
                },
            )
        ],
    )
