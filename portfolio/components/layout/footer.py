import reflex as rx
import datetime
from portfolio import constants
from portfolio.components.styles.styles import FooterStyle


def media(name: str, link: str) -> rx.Component:
    return rx.link(rx.text(name, **FooterStyle.link), href=link)


def footer() -> rx.vstack:
    return rx.vstack(
        rx.divider(max_width="35em", color=rx.color("slate", 11)),
        rx.hstack(
            rx.text(
                f"© 2024-{datetime.date.today().year} Marcos Ferreto Estrada v5.",
                **FooterStyle.brand,
            ),
            rx.hstack(
                media("Twitter", link=constants.TWITTER_X_URL),
                media("GitHub", link=constants.GITHUB_URL),
            ),
            **FooterStyle.content,
        ),
        **FooterStyle.base,
    )
