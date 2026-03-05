import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import (
    active_indicator_style,
    badge_style,
    card_style,
    github_link_style,
    project_content_style,
    project_description_style,
    project_header_style,
    project_highlights_container_style,
    project_link_style,
    projects_grid_style,
)
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

    return rx.list_item(
        rx.box(
            rx.box(
                # Header con título, indicador activo y enlace a GitHub
                rx.box(
                    rx.link(
                        name,
                        href=url,
                        target="_blank",
                        title=f"Ver el proyecto {name}",
                        style=project_link_style,
                    ),
                    (
                        rx.text(
                            "•",
                            class_name="active-indicator",
                            style=active_indicator_style,
                        )
                        if is_active
                        else None
                    ),
                    (
                        rx.link(
                            github_icon(),
                            href=github,
                            target="_blank",
                            title=f"Ver código fuente del proyecto {name}",
                            class_name="github-code-link",
                            style=github_link_style,
                        )
                        if github
                        else None
                    ),
                    style=project_header_style,
                ),
                rx.text(
                    description,
                    style=project_description_style,
                ),
                style=project_content_style,
            ),
            rx.box(
                *[rx.text(highlight, style=badge_style) for highlight in highlights],
                style=project_highlights_container_style,
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
                style=projects_grid_style,
            )
        ],
    )
