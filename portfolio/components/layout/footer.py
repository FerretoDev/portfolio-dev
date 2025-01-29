import reflex as rx

from portfolio import constants
from portfolio.components.styles.styles import FooterStyle


def media(name: str, link: str) -> rx.Component:
    return rx.link(rx.text(name, **FooterStyle.link), href=link)


def footer() -> rx.vstack:
    return rx.vstack(
        rx.divider(max_width="35em", color=rx.color("slate", 11)),
        rx.hstack(
            rx.text("© 2025 Marcos Ferreto", **FooterStyle.brand),
            rx.hstack(
                media("Twitter", link=constants.TWITTER_X_URL),
                media("GitHub", link=constants.GITHUB_URL),
            ),
            **FooterStyle.content,
        ),
        **FooterStyle.base,
    )
