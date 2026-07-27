from typing import Union

import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import (
    skill_badge_style,
    skill_category_style,
    skill_category_title_style,
    skill_text_style,
    skills_container_style,
    skills_list_style,
)
from portfolio.constants import skills, skills_categorized
from portfolio.utils.icons import SKILLS_ICONS


def skill_item(skill: Union[dict, str]) -> rx.Component:
    """
    Componente individual para cada habilidad.
    Soporta tanto dict (ej: {"name": "Python"}) como str (ej: "Python").
    """
    name = skill["name"] if isinstance(skill, dict) else skill

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


def skill_category(category: str, items: list[str]) -> rx.Component:
    """
    Componente para una categoría de habilidades (estilo alternativo)
    """
    return rx.box(
        rx.heading(
            category,
            as_="h3",
            style=skill_category_title_style,
        ),
        rx.box(
            *[skill_item(item) for item in items],
            style=skills_list_style,
        ),
        style=skill_category_style,
    )


def skills_section() -> rx.Component:
    """
    Sección completa de habilidades (estilo anterior: lista plana)
    """
    return section_component(
        title="Habilidades",
        children=[skill_item(skill) for skill in skills],
        content_style=skills_list_style,
    )


def categorized_skills_section() -> rx.Component:
    """
    Sección completa de habilidades por categorías (guardada para uso futuro).
    Para activarla, reemplace skills_section por categorized_skills_section en pages/index.py
    """
    return section_component(
        title="Habilidades",
        children=[
            skill_category(category, items)
            for category, items in skills_categorized.items()
        ],
        content_style=skills_container_style,
    )
