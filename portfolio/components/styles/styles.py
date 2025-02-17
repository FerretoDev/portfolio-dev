from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import reflex as rx
from reflex.constants.colors import Color


# VARIABLES GLOBALES
class GlobalThemeVariables(Enum):
    # Dark Theme
    DARK = {
        "--background": "#0a0a0a",  # Fondo principal oscuro
        "--foreground": "#ffffff",  # Color de texto principal oscuro
        "--primary": "#00b4d8",  # Mismo primario para consistencia
        "--secondary": "#0077b6",  # Mismo secundario para consistencia
        "--accent": "#90e0ef",  # Mismo acento para consistencia
        "--glass-background": "rgba(255, 255, 255, 0.05)",  # Fondo glass oscuro
        "--glass-border": "rgba(255, 255, 255, 0.1)",  # Borde glass oscuro
    }
    # Light Theme
    LIGHT: dict[str, str] = {
        "--background": "#f0f4f8",  # Fondo principal claro
        "--foreground": "#1a202c",  # Color de texto principal claro
        "--primary": "#00b4d8",  # Color primario (botones, acentos)
        "--secondary": "#0077b6",  # Color secundario (hover, detalles)
        "--accent": "#90e0ef",  # Color de acento complementario
        "--glass-background": "rgba(255, 255, 255, 0.1)",  # Fondo glass
        "--glass-border": "rgba(255, 255, 255, 0.2)",  # Borde glass
    }

    # Estilos base
    BASE_STYLE: dict[str, str] = {
        "font_family": "Inter, sans-serif",  # Fuente principal
        "transition": "all 0.3s ease",  # Transiciones suaves globales
    }

    # Estilos de vidrio (glassmorphism)
    GLASS_STYLE: dict[str, str] = {
        "backdrop_filter": "blur(10px)",  # Efecto de desenfoque
        "border_radius": "10px",  # Bordes redondeados
        "transition": "background-color 0.3s ease, border-color 0.3s ease",
    }


# Estilos globales
def global_style() -> Any:
    return {
        "body": {
            "background": GlobalThemeVariables.DARK.value["--background"],
            "color": GlobalThemeVariables.DARK.value["--background"],
            "transition": "all 0.3s ease",
        },
        ".section": {
            "padding": "6rem 0",
            "position": "relative",
        },
        ".split-section": {
            "display": "grid",
            "gap": "4rem",
            "alignItems": "center",
        },
    }


"""
The CardStyle
"""


def color(shade: int) -> Color:
    return rx.color("slate", shade)


TextShared: dict[str, str] = {"size": "2", "weight": "bold"}


@dataclass
class CardStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "align": "start",
            "justify": "start",
            "position": "relative",
            "width": "100%",
            "max_width": "320px",
            "height": "200px",
            "border": f"1px solid {rx.color('gray', 6)}",
            "bg": rx.color("gray", 3),
            "border_radius": "12px",
            "padding": "16px",
            "overflow": "hidden",
            "z_index": "30",
            "box_shadow": "0px 6px 12px 0px rgba(0, 0, 0, 0.05)",
        },
    )

    icon: dict[str, str] = field(
        default_factory=lambda: {
            "size": 21,
            "position": "absolute",
            "bottom": "16px",
            "right": "16px",
        },
    )

    stack: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "spacing": "1",
            "align": "start",
            "justify": "start",
            "text_align": "start",
        },
    )

    background: dict[str, str] = field(
        default_factory=lambda: {
            "background_size": "16px 16px",
            "background_image": f"radial-gradient(circle, {rx.color('gray', 12)} 1px, transparent 1px)",
            "mask": "radial-gradient(100% 100% at 100% 100%, hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
            "width": "100%",
            "height": "100%",
            "position": "absolute",
        },
    )

    title: dict[str, str] = field(
        default_factory=lambda: {"color": color(12), **TextShared},
    )

    description: dict[str, str] = field(
        default_factory=lambda: {"color": color(11), **TextShared},
    )


CardStyle: CardStyle = CardStyle()

"""
The FooterStyle
"""


active: Color = rx.color("slate", 12)
passive: Color = rx.color("slate", 10)


@dataclass
class FooterStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "20vh",
            "align": "center",
            "justify": "center",
            "padding": "0em 1em",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "35em",
            "justify": "between",
            "align": "center",
            "padding": "1em 0em",
        },
    )
    link: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "weight": "medium",
            "size": "2",
        },
    )
    brand: dict[str, str] = field(
        default_factory=lambda: {"color": active, "size": "2"},
    )


FooterStyle: FooterStyle = FooterStyle()

"""
The NavbarStyle
"""


@dataclass
class NavbarStyle:
    navigation: dict[str, str] = field(
        default_factory=lambda: {
            "display": "grid",
            "grid-template-columns": "repeat(auto - fit, minmax(300px, 1fr))",
            "gap": "1rem",
            "position": "fixed",
            "width": "100%",
            "top": "0px",
            "z_index": "1000",
            "backdrop_filter": "blur(10px)",
            "background": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--background"],
                dark=GlobalThemeVariables.DARK.value["--background"],
            ),
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "10em",
            "justify": "between",
            "align": "center",
            "padding": "1em 0em",
        },
    )
    link: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "weight": "medium",
            "size": "2",
        },
    )
    brand: dict[str, str] = field(
        default_factory=lambda: {"color": active, "size": "2"},
    )


NavbarStyle: NavbarStyle = NavbarStyle()


"""
The HeaderStyle
"""


@dataclass
class HeaderStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "position": "fixed",
            "width": "100%",
            "top": "0px",
            "z_index": "999",
            "backdrop_filter": "blur(10px)",  # Aplica desenfoque
            "border_bottom": rx.color_mode_cond(
                light="1px solid rgba(0,0,0,0.1)",
                dark="1px solid rgba(255,255,255,0.1)",
            ),
            "display": "flex",
            "flex_wrap": "wrap",
            "justify_content": "space-between",
            "align_items": "center",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "bg": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--glass-background"],
                dark=GlobalThemeVariables.DARK.value["--glass-background"],
            ),
            "padding": "1.5rem",
            "z_index": "1000",
            "width": "100%",
        },
    )


HeaderStyle: HeaderStyle = HeaderStyle()


"""
The LayoutStyle
"""


@dataclass
class LayoutStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            # "background": rx.color_mode_cond(
            #    # light="rgba(255, 255, 255, 0.8)",
            #    # dark="rgba(0, 0, 0, 0.8)",
            #   light=GlobalThemeVariables.LIGHT.value["--background"],
            #    dark=GlobalThemeVariables.DARK.value["--background"],
            # )
            "background": rx.color_mode_cond(
                light="linear-gradient(to bottom right, #E2E8F0, #CBD5E0)",
                dark="linear-gradient(to bottom right, #111827, #1F2937)",
            ),
            "color": rx.color_mode_cond(
                light=rx.color("gray", 8),
                dark=rx.color("gray", 2),
            ),
            "transition": "background 0.3s ease, color 0.3s ease",
            ###
            # "display": "flex",
            # "justify-content": "center",
            # "align-items": "center",
        }
    )
    # Estilos responsive
    section_style_mobile: dict[str, str] = field(
        default_factory=lambda: {
            "@media (width <= 700px)": {
                "padding": "2rem",
            },
        }
    )


LayoutStyle: LayoutStyle = LayoutStyle()


"""
The SectionStyle
"""


@dataclass
class SectionStyle:
    # Estilos base para la sección
    section_style: dict[str, str] = field(
        default_factory=lambda: {
            "max_width": "700px",
            "margin": "0 auto 48px",
        }
    )
    # Estilos para el título
    title_style: dict[str, str] = field(
        default_factory=lambda: {
            "margin_bottom": "8px",
            "font_weight": "700",
            "line_height": "1.5",
            "font_size": "1.5rem",
            "color": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--primary"],
                dark=GlobalThemeVariables.DARK.value["--primary"],
            ),
        }
    )
    # Estilos responsive
    section_style_mobile: dict[str, str] = field(
        default_factory=lambda: {
            "@media (width <= 700px)": {
                "margin_bottom": "38px",
            }
        }
    )


SectionStyle: SectionStyle = SectionStyle()
