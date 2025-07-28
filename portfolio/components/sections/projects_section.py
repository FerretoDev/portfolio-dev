from typing import List, Optional

import reflex as rx

from portfolio.components.card import card
from portfolio.components.section import section
from portfolio.components.styles.styles import GlobalThemeVariables, SectionStyle

# Simulamos la importación de datos de proyectos
# En tu caso real, importarías desde tu archivo de datos
projects = [
    # {
    #    "name": "Task Manager ",
    #    "url": "https://taskmanager-app.com",
    #    "github": "https://github.com/usuario/task-manager",
    #    "description": "Aplicación de gestión de tareas con funcionalidades de colaboración en tiempo real.",
    #    "isActive": True,
    #    "highlights": ["Vue.js", "Firebase", "PWA", "WebSockets"],
    # },
    {
        "name": "Portfolio",
        "url": "https://ferreto.dev",
        "github": None,
        "description": "Sitio web portfolio minimalista y diseño responsivo.",
        "isActive": True,
        "highlights": ["Python", "Reflex", "FastAPI", "CSS"],
    },
]


# Componente de icono GitHub (simulado)
def github_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/github.svg",
        style={"width": "16px", "height": "16px"},
    )


def section_component(
    title: Optional[str] = None, children: Optional[List[rx.Component]] = None
) -> rx.Component:
    """Componente Section (importado anteriormente)"""
    if children is None:
        children = []

    section_content = []

    if title:
        section_content.append(
            rx.heading(
                title,
                level=2,
                style={
                    "margin_bottom": "8px",
                    "font_weight": "700",
                    "line_height": "1.5",
                    "font_size": "1.5rem",
                },
            )
        )

    section_content.extend(children)

    return rx.box(
        *section_content,
        # tag="section",
        style={
            "max_width": "700px",
            "margin": "0 auto 48px",
            "@media (max-width: 700px)": {
                "margin_bottom": "38px",
            },
        },
    )


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

article_style = {
    "border_radius": "8px",
    "border": "1px solid #f2f2f2",
    "gap": "16px",
    "display": "flex",
    "flex_direction": "column",
    "padding": "16px",
    "height": "100%",
}

footer_style = {
    "display": "flex",
    "flex_wrap": "wrap",
    "gap": "4px",
    "font_size": "0.6rem",
}

highlight_style = {
    "border_radius": "6px",
    "background": "#eee",
    "color": "#444",
    "font_size": "0.6rem",
    "font_weight": "500",
    "padding": "0.2rem 0.6rem",
}


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
