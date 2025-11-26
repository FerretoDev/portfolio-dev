import datetime

import reflex as rx

from portfolio import constants
from portfolio.components.styles.styles import FooterStyle

# from portfolio.constants import basics


def media(name: str, link: str) -> rx.Component:
    return rx.link(rx.text(name, **FooterStyle.link), href=link)


def footer():
    # Extraemos datos del basics
    """Pie de página."""
    current_year = datetime.date.today().year
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.icon(tag="github"),
                href="https://github.com/FerretoDev",
                style=link_style,
            ),
            rx.link(
                rx.icon(tag="linkedin"),
                href="https://linkedin.com/in/marcos-ferreto/",
                style=link_style,
            ),
            rx.link(
                rx.icon(tag="twitter"),
                href="https://x.com/MarcosFerretoE",
                style=link_style,
            ),
        ),
        rx.text(
            f"© 2024-{current_year} Marcos Eduardo Ferreto Estrada v1.",
        ),
        width="100%",
        align_items="center",
        padding_y="2rem",
    )


link_style: dict[str, dict[str, str] | str] = {
    "color": "#777",
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "border": "1px solid #eee",
    "padding": "4px",
    "height": "32px",
    "width": "32px",
    "border_radius": "6px",
    "transition": "all 0.3s ease",
    "text_decoration": "none",
    "_hover": {
        "background": "#eee",
        "border": "1px solid #ddd",
    },
}
