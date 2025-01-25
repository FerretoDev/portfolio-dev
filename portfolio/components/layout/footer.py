from dataclasses import dataclass, field

import reflex as rx
from reflex.constants.colors import Color

from portfolio import constants

active: Color = rx.color("slate", 12)
passive: Color = rx.color("slate", 10)


@dataclass
class FooterV2Style:
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


FooterV2Style: FooterV2Style = FooterV2Style()


def media(name: str, link: str) -> rx.Component:
    return rx.link(rx.text(name, **FooterV2Style.link), href=link)


def footer() -> rx.vstack:
    return rx.vstack(
        rx.divider(max_width="35em", color=rx.color("slate", 11)),
        rx.hstack(
            rx.text("© 2025 Marcos Ferreto", **FooterV2Style.brand),
            rx.hstack(
                media("Twitter", link=constants.TWITTER_X_URL),
                media("GitHub", link=constants.GITHUB_URL),
            ),
            **FooterV2Style.content,
        ),
        **FooterV2Style.base,
    )
