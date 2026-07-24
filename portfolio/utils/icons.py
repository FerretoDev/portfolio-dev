"""Utilidades para iconos del portfolio"""

from typing import Any, Callable, Dict

import reflex as rx

# Los SVGs locales se renderizan usando CSS mask para heredar 'currentColor'
def create_simple_icon(icon_name: str) -> rx.Component:
    """Crea un icono desde assets/icons/ usando máscaras para heredar el color."""
    return rx.box(
        width="20px",
        height="20px",
        background_color="currentColor",
        mask=f"url('/icons/{icon_name}.svg') no-repeat center / contain",
        WebkitMask=f"url('/icons/{icon_name}.svg') no-repeat center / contain",
    )


# Funciones de iconos de redes sociales y UI (usando Lucide nativo)
def email_icon() -> rx.Component:
    return rx.icon("mail", size=16)


def phone_icon() -> rx.Component:
    return create_simple_icon("phone")


def github_social_icon() -> rx.Component:
    return create_simple_icon("github")


def linkedin_icon() -> rx.Component:
    return create_simple_icon("linkedin")


def twitter_icon() -> rx.Component:
    return create_simple_icon("twitter")


def link_icon() -> rx.Component:
    return rx.icon("link", size=20)


def map_pin_icon() -> rx.Component:
    return rx.icon("map-pin", size=20)




# Diccionario de iconos de redes sociales
SOCIAL_ICONS: dict[str, Any] = {
    "Email": email_icon,
    "Phone": phone_icon,
    "GitHub": github_social_icon,
    "LinkedIn": linkedin_icon,
    "X": twitter_icon,
}


# Funciones de iconos de tecnologías (Simple Icons oficiales)
def html_icon() -> rx.Component:
    return create_simple_icon("html5")


def css_icon() -> rx.Component:
    return create_simple_icon("css3")


def javascript_icon() -> rx.Component:
    return create_simple_icon("javascript")


def typescript_icon() -> rx.Component:
    return create_simple_icon("typescript")


def react_icon() -> rx.Component:
    return create_simple_icon("react")


def node_icon() -> rx.Component:
    return create_simple_icon("nodedotjs")


def mysql_icon() -> rx.Component:
    return create_simple_icon("mysql")


def git_icon() -> rx.Component:
    return create_simple_icon("git")


def github_icon() -> rx.Component:
    return create_simple_icon("github")



def next_icon() -> rx.Component:
    return create_simple_icon("nextdotjs")


def tailwind_icon() -> rx.Component:
    return create_simple_icon("tailwindcss")


def swift_icon() -> rx.Component:
    return create_simple_icon("swift")


def swiftui_icon() -> rx.Component:
    return create_simple_icon("swiftui")


def kotlin_icon() -> rx.Component:
    return create_simple_icon("kotlin")


def flutter_icon() -> rx.Component:
    return create_simple_icon("flutter")


def python_icon() -> rx.Component:
    return create_simple_icon("python")


def postgresql_icon() -> rx.Component:
    return create_simple_icon("postgresql")


# Mapeo de nombres a funciones de iconos
SKILLS_ICONS: Dict[str, Callable[[], rx.Component]] = {
    "HTML": html_icon,
    "CSS": css_icon,
    "JavaScript": javascript_icon,
    "TypeScript": typescript_icon,
    "React": react_icon,
    "Node": node_icon,
    "MySQL": mysql_icon,
    "Git": git_icon,
    "GitHub": github_icon,
    "Next": next_icon,
    "Tailwind": tailwind_icon,
    "Swift": swift_icon,
    "SwiftUI": swiftui_icon,
    "Kotlin": kotlin_icon,
    "Flutter": flutter_icon,
    "Python": python_icon,
    "PostgreSQL": postgresql_icon,
}

