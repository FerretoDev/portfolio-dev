import datetime

import reflex as rx

from portfolio import constants
from portfolio.components.sections.common_styles import link_style
from portfolio.components.styles.styles import (
    FooterStyle,
    footer_container_style,
    footer_copyright_style,
)


def media(name: str, link: str) -> rx.Component:
    return rx.link(
        rx.text(name),
        href=link,
        style=FooterStyle.link,
    )


def footer():
    # Extraemos datos del basics
    """Pie de página."""
    current_year = datetime.date.today().year
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.icon(tag="github"),
                href=constants.GITHUB_URL,
                style=link_style,
            ),
            rx.link(
                rx.icon(tag="linkedin"),
                href=constants.LINKEDIN_URL,
                style=link_style,
            ),
            rx.link(
                rx.icon(tag="twitter"),
                href=constants.TWITTER_X_URL,
                style=link_style,
            ),
            spacing="3",
        ),
        rx.text(
            f"© 2024-{current_year} Marcos Eduardo Ferreto Estrada v1.",
            style=footer_copyright_style,
        ),
        width="100%",
        align_items="center",
        padding_y="3rem",
        spacing="4",
        style=footer_container_style,
    )
