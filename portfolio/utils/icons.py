"""Utilidades para iconos"""

from typing import Any, Callable, Dict

import reflex as rx

# Estilo estándar para iconos
ICON_STYLE: dict[str, str] = {"width": "16px", "height": "16px"}


def create_simple_icon(icon_name: str) -> rx.Component:
    """Crea un icono desde assets/icons/ (SVGs locales de simple-icons)."""
    return rx.image(
        src=f"/icons/{icon_name}.svg",
        style=ICON_STYLE,
    )


# Funciones de iconos de redes sociales
def email_icon() -> rx.Component:
    return create_simple_icon("gmail")


def phone_icon() -> rx.Component:
    return rx.icon(tag="phone", width="16px", height="16px")


def github_social_icon() -> rx.Component:
    return create_simple_icon("github")


def linkedin_icon() -> rx.Component:
    return create_simple_icon("linkedin")


def twitter_icon() -> rx.Component:
    return create_simple_icon("twitter")


def link_icon() -> rx.Component:
    return rx.icon(tag="link", width="16px", height="16px")


def map_pin_icon() -> rx.Component:
    return rx.icon(tag="map-pin", width="16px", height="16px")


# Diccionario de iconos de redes sociales
SOCIAL_ICONS: dict[str, Any] = {
    "Email": email_icon,
    "Phone": phone_icon,
    "GitHub": github_social_icon,
    "LinkedIn": linkedin_icon,
    "X": twitter_icon,
}


# Funciones de iconos individuales
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
    "Next": next_icon,
    "Tailwind": tailwind_icon,
    "Swift": swift_icon,
    "SwiftUI": swiftui_icon,
    "Kotlin": kotlin_icon,
    "Flutter": flutter_icon,
    "Python": python_icon,
    "PostgreSQL": postgresql_icon,
}
