import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import (
    skill_badge_style,
    skill_text_style,
    skills_list_style,
)
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
            as_="span",
            style=skill_text_style,
        )
    )

    return rx.box(*item_content, style=skill_badge_style)


def skills_section() -> rx.Component:
    """
    Sección completa de habilidades
    """
    return section_component(
        title="Habilidades",
        children=[
            rx.box(
                *[skill_item(skill) for skill in skills],
                style=skills_list_style,
            )
        ],
    )
