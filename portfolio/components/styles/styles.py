from dataclasses import dataclass, field
from enum import Enum

import reflex as rx
from reflex.constants.colors import Color


# VARIABLES GLOBALES
class GlobalThemeVariables(Enum):
    # Dark Theme
    DARK = {
        "primary": "#06B6D4",
        "primary_dark": "#0891B2",
        "secondary": "#3B82F6",
        "bg_dark": "#111827",
        "bg_darker": "#0F172A",
        "text_primary": "#F9FAFB",
        "text_secondary": "#D1D5DB",
        "surface_1": "#1F2937",
        "border_dark": "rgba(255,255,255,0.1)",
    }
    # Light Theme
    LIGHT: dict[str, str] = {
        "primary": "#0891B2",
        "bg_dark": "#F9FAFB",
        "text_primary": "#111827",
        "surface_1": "#FFFFFF",
        "border_dark": "rgba(0,0,0,0.05)",
        ###
        "primary_dark": "#0E7490",
        "secondary": "#2563EB",
        "bg_darker": "#F3F4F6",
        "text_secondary": "#374151",
        "text_muted": "#6B7280",
        "surface_2": "#F9FAFB",
        "shadow-color": "rgba(0,0,0,0.05)",
    }


# Estilos globales
def global_style() -> rx.style:
    return rx.style(
        {
            "body": {
                "background": GlobalThemeVariables.DARK.value["bg_dark"],
                # "background": "var(--bg-dark)",
                # "color": "var(--text-primary)",
                "color": GlobalThemeVariables.DARK.value["text_primary"],
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
    )


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
                light=GlobalThemeVariables.LIGHT.value["bg_dark"],
                dark=GlobalThemeVariables.DARK.value["bg_dark"],
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
The LayoutStyle
"""


@dataclass
class LayoutStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "background": rx.color_mode_cond(
                light="rgba(255, 255, 255, 0.8)",
                dark="rgba(0, 0, 0, 0.8)",
            ),
            "color": rx.color_mode_cond(
                light=rx.color("gray", 8),
                dark=rx.color("gray", 2),
            ),
            "transition": "background 0.3s ease, color 0.3s ease",
            "width": "100%",
            "justify": "between",
            "align": "center",
            "padding": "1em 0em",
        }
    )


LayoutStyle: LayoutStyle = LayoutStyle()
