from dataclasses import dataclass, field

import reflex as rx
from reflex.constants.colors import Color

from portfolio.components.button_color_mode import button_color_mode

active: Color = rx.color("slate", 12)
passive: Color = rx.color("slate", 10)


@dataclass
class LayoutStyleSheet:
    navigation: dict[str, str] = field(
        default_factory=lambda: {
            # "top": "0",
            # "left": "0",
            # "width": "100%",
            # "align": "center",
            # "justify": "between",
            # "position": "sticky",
            # "padding": "1.25em 2em",
            # "background": rx.color("gray", 3),
            # "width": "100%",
            # "height": "20vh",
            # "align": "center",
            # "justify": "center",
            # "padding": "0em 1em",
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


LayoutStyleSheet: LayoutStyleSheet = LayoutStyleSheet()


def media(name: str, link: str) -> rx.Component:
    return rx.link(rx.text(name, **LayoutStyleSheet.link), href=link)


def navbar() -> rx.Component:
    return rx.hstack(
        rx.heading("Ferreto Dev", **LayoutStyleSheet.brand),
        rx.hstack(
            *[
                rx.text(name, **LayoutStyleSheet.brand)
                for name in [
                    media("Home", "/"),
                    media("Services", "/services"),
                    media("About Us", "/about"),
                    media("Contact", "/contact"),
                ]
            ],
            button_color_mode(),
        ),
        **LayoutStyleSheet.navigation,
    )
