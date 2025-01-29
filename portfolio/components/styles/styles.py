from dataclasses import dataclass, field

import reflex as rx
from reflex.constants.colors import Color
from portfolio.components.styles.theme import (
    THEME_STYLES,
    ThemeState,
    Theme,
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
            "mask": f"radial-gradient(100% 100% at 100% 100%, hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
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


link: dict[str, str] = field(
    default_factory=lambda: {
        "color": rx.color("slate", 11),
        "weight": "medium",
        "size": "2",
    },
)

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
            "position": "fixed",
            "width": "100%",
            "top": "0px",
            "z_index": "1000",
            "backdrop_filter": "blur(10px)",
            "background": rx.cond(
                ThemeState.theme == Theme.DARK,
                THEME_STYLES[Theme.LIGHT]["nav_bg"],
                THEME_STYLES[Theme.LIGHT]["nav_bg"],
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
