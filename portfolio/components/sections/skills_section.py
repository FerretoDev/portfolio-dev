import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import skill_badge_style
from portfolio.constants import skills
from portfolio.utils.icons import SKILLS_ICONS


def skill_item(skill: dict) -> rx.Component:
    """
    Componente individual para cada habilidad
    """
    name = skill["name"]

    # Manejo especial para Next.js
    icon_name = "Next" if name == "Next.js" else name

    # Obtener el icono correspondiente
    icon_func = SKILLS_ICONS.get(icon_name)

    # Crear el contenido del item
    item_content = []

    # Agregar icono si existe
    if icon_func:
        item_content.append(icon_func())

    # Agregar el nombre de la habilidad
    item_content.append(
        rx.text(
            name,
            style={
                "color": "black",
                "font_size": "0.8rem",
                "font_weight": "500",
            },
        )
    )

    return rx.list_item(*item_content, style=skill_badge_style)


def skills_section() -> rx.Component:
    """
    Sección completa de habilidades
    """
    return section_component(
        title="Habilidades",
        children=[
            rx.unordered_list(
                *[skill_item(skill) for skill in skills],
                style={
                    "display": "inline-flex",
                    "gap": "8px",
                    "flex_wrap": "wrap",
                    "list_style": "none",
                    "margin": "0",
                    "padding": "0",
                },
            )
        ],
    )
