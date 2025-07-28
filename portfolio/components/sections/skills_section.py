from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

import reflex as rx

from portfolio.components.section import section
from portfolio.components.styles.styles import GlobalThemeVariables, SectionStyle


@dataclass
class SkillsStyle:
    skills_base: dict[str, str] = field(
        default_factory=lambda: {
            "display": "flex",
            "align_items": "center",
            "justify_content": "space-between",
        },
    )
    hero_title: dict[str, str] = field(
        default_factory=lambda: {
            "background": rx.color_mode_cond(
                light=f"linear-gradient(to right, {GlobalThemeVariables.LIGHT.value['--primary']}, {GlobalThemeVariables.LIGHT.value['--secondary']})",
                dark=f"linear-gradient(to right, {GlobalThemeVariables.DARK.value['--primary']}, {GlobalThemeVariables.DARK.value['--secondary']})",
            ),
            # "font_size": "3rem",
            "background_image": "linear-gradient(to right, #06B6D4, #3B82F6)",
            "background_clip": "text",
            "color": "transparent",
            ########################################################################
            "size": "2",
            "margin_bottom": "1rem",
        },
    )

    hero_text: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--secondary"],
                dark=GlobalThemeVariables.DARK.value["--secondary"],
            ),
            "font-size": "1.2em",
        },
    )


SkillsStyle: SkillsStyle = SkillsStyle()


# Simulamos la importación de datos de habilidades
# En tu caso real, importarías desde tu archivo de datos
skills = [
    {"name": "HTML"},
    {"name": "CSS"},
    {"name": "JavaScript"},
    # {"name": "TypeScript"},
    # {"name": "React"},
    # {"name": "Node"},
    # {"name": "MySQL"},
    {"name": "Git"},
    {"name": "GitHub"},
    # {"name": "Next.js"},
    # {"name": "Tailwind"},
    # {"name": "Swift"},
    # {"name": "SwiftUI"},
    # {"name": "Kotlin"},
    # {"name": "Flutter"},
    {"name": "Python"},
    {"name": "PostgreSQL"},
]


# Componentes de iconos (simulados con emojis)
# En tu implementación real, usarías SVGs o iconos reales
def html_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/html5.svg",
        style={"width": "16px", "height": "16px"},
    )


def css_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/css3.svg",
        style={"width": "16px", "height": "16px"},
    )


def javascript_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/javascript.svg",
        style={"width": "16px", "height": "16px"},
    )


def typescript_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/typescript.svg",
        style={"width": "16px", "height": "16px"},
    )


def react_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/react.svg",
        style={"width": "16px", "height": "16px"},
    )


def node_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/nodedotjs.svg",
        style={"width": "16px", "height": "16px"},
    )


def mysql_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/mysql.svg",
        style={"width": "16px", "height": "16px"},
    )


def git_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/git.svg",
        style={"width": "16px", "height": "16px"},
    )


def github_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/github.svg",
        style={"width": "16px", "height": "16px"},
    )


def next_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/nextdotjs.svg",
        style={"width": "16px", "height": "16px"},
    )


def tailwind_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/tailwindcss.svg",
        style={"width": "16px", "height": "16px"},
    )


def swift_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/swift.svg",
        style={"width": "16px", "height": "16px"},
    )


def swiftui_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/swiftui.svg",
        style={"width": "16px", "height": "16px"},
    )


def kotlin_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/kotlin.svg",
        style={"width": "16px", "height": "16px"},
    )


def flutter_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/flutter.svg",
        style={"width": "16px", "height": "16px"},
    )


def python_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/python.svg",
        style={"width": "16px", "height": "16px"},
    )


def postgresql_icon():
    return rx.image(
        src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/postgresql.svg",
        style={"width": "16px", "height": "16px"},
    )


# Mapeo de iconos de habilidades
SKILLS_ICONS: Dict[str, Callable] = {
    "HTML": html_icon,
    "CSS": css_icon,
    "JavaScript": javascript_icon,
    "TypeScript": typescript_icon,
    "React": react_icon,
    "Node": node_icon,
    "MySQL": mysql_icon,
    "Git": git_icon,
    "GitHub": github_icon,
    "Next": next_icon,  # Mapeo especial para Next.js
    "Tailwind": tailwind_icon,
    "Swift": swift_icon,
    "SwiftUI": swiftui_icon,
    "Kotlin": kotlin_icon,
    "Flutter": flutter_icon,
    "Python": python_icon,
    "PostgreSQL": postgresql_icon,
}


def section_component(
    title: Optional[str] = None, children: Optional[List[rx.Component]] = None
) -> rx.Component:
    """Componente Section (importado anteriormente)"""
    if children is None:
        children = []

    section_content: List[rx.Component] = []

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

    section_content.extend(list(children))

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


def skill_item(skill: dict) -> rx.Component:
    """
    Componente individual para cada habilidad
    """
    name = skill["name"]

    # Manejo especial para Next.js (como en el código original)
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
            # tag="span",
            style={
                "color": "black",
                "font_size": "0.8rem",
                "font_weight": "500",
            },
        )
    )

    return rx.list_item(*item_content, style=skill_item_style)


def skills_section() -> rx.Component:
    """
    Sección completa de habilidades
    """
    return rx.fragment(
        section_component(
            title="Habilidades",
            children=[
                rx.unordered_list(
                    *[skill_item(skill) for skill in skills], style=skills_ul_style
                )
            ],
        ),
    )


# Estilos definidos como diccionarios
skills_ul_style = {
    "display": "inline-flex",
    "gap": "8px",
    "flex_wrap": "wrap",
    "list_style": "none",
    "margin": "0",
    "padding": "0",
}

skill_item_style = {
    "align_items": "center",
    "background": "#eee",
    "border_radius": "6px",
    "color": "black",
    "display": "flex",
    "font_size": "0.8rem",
    "font_weight": "500",
    "gap": "4px",
    "padding": "0.2rem 0.6rem",
}

# Versión alternativa con niveles de competencia
skills_with_levels = [
    {"name": "HTML", "level": "Avanzado"},
    {"name": "CSS", "level": "Avanzado"},
    {"name": "JavaScript", "level": "Avanzado"},
    {"name": "TypeScript", "level": "Intermedio"},
    {"name": "React", "level": "Avanzado"},
    {"name": "Node", "level": "Intermedio"},
    {"name": "MySQL", "level": "Intermedio"},
    {"name": "Git", "level": "Avanzado"},
    {"name": "GitHub", "level": "Avanzado"},
    {"name": "Next.js", "level": "Intermedio"},
    {"name": "Tailwind", "level": "Avanzado"},
    {"name": "Python", "level": "Avanzado"},
]


def skill_item_with_level(skill: dict) -> rx.Component:
    """
    Versión alternativa que incluye nivel de competencia
    """
    name = skill["name"]
    level = skill.get("level", "")

    icon_name = "Next" if name == "Next.js" else name
    icon_func = SKILLS_ICONS.get(icon_name)

    # Colores según nivel
    level_colors = {
        "Básico": "#fef3c7",  # amarillo claro
        "Intermedio": "#dbeafe",  # azul claro
        "Avanzado": "#d1fae5",  # verde claro
        "Experto": "#fce7f3",  # rosa claro
    }

    background_color = level_colors.get(level, "#eee")

    item_content = []

    if icon_func:
        item_content.append(icon_func())

    item_content.extend(
        [
            rx.text(
                name,
                # tag="span",
                style={"font_weight": "500"},
            ),
            (
                rx.text(
                    level,
                    # tag="span",
                    style={
                        "font_size": "0.7rem",
                        "opacity": "0.7",
                        "font_style": "italic",
                    },
                )
                if level
                else rx.fragment()
            ),
        ]
    )

    return rx.list_item(
        *item_content,
        style={
            **skill_item_style,
            "background": background_color,
            "flex_direction": "column" if level else "row",
            "text_align": "center" if level else "left",
            "min_width": "80px" if level else "auto",
        },
    )


def skills_section_with_levels() -> rx.Component:
    """
    Versión con niveles de competencia
    """
    return section_component(
        title="Habilidades",
        children=[
            rx.unordered_list(
                *[skill_item_with_level(skill) for skill in skills_with_levels],
                style=skills_ul_style,
            )
        ],
    )


# Versión agrupada por categorías
skills_by_category = {
    "Frontend": [
        {"name": "HTML"},
        {"name": "CSS"},
        {"name": "JavaScript"},
        {"name": "TypeScript"},
        {"name": "React"},
        {"name": "Next.js"},
        {"name": "Tailwind"},
    ],
    "Backend": [
        {"name": "Node"},
        {"name": "Python"},
        {"name": "MySQL"},
        {"name": "PostgreSQL"},
    ],
    "Mobile": [
        {"name": "Swift"},
        {"name": "SwiftUI"},
        {"name": "Kotlin"},
        {"name": "Flutter"},
    ],
    "Herramientas": [
        {"name": "Git"},
        {"name": "GitHub"},
    ],
}


def skills_category(category: str, category_skills: List[dict]) -> rx.Component:
    """
    Componente para una categoría de habilidades
    """
    return rx.box(
        rx.heading(
            category,
            level=3,
            style={
                "font_size": "1rem",
                "font_weight": "600",
                "margin_bottom": "8px",
                "color": "#333",
            },
        ),
        rx.unordered_list(
            *[skill_item(skill) for skill in category_skills],
            style={
                **skills_ul_style,
                "margin_bottom": "16px",
            },
        ),
        style={"margin_bottom": "24px"},
    )


def skills_section_by_categories() -> rx.Component:
    """
    Versión agrupada por categorías
    """
    return section_component(
        title="Habilidades",
        children=[
            skills_category(category, category_skills)
            for category, category_skills in skills_by_category.items()
        ],
    )
