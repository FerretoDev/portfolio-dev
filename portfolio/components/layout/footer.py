import reflex as rx
import datetime
from portfolio import constants
from portfolio.components.styles.styles import FooterStyle


def media(name: str, link: str) -> rx.Component:
    return rx.link(rx.text(name, **FooterStyle.link), href=link)


# Original
def footer2() -> rx.vstack:
    return rx.vstack(
        rx.divider(max_width="35em", color=rx.color("slate", 11)),
        rx.hstack(
            rx.text(
                f"© 2024-{datetime.date.today().year} Marcos Ferreto Estrada v1.",
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


def footer():
    """Pie de página."""
    current_year = datetime.date.today().year
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.link(rx.icon(tag="github"), href="https://github.com/username"),
                rx.link(
                    rx.icon(tag="linkedin"), href="https://linkedin.com/in/username"
                ),
                rx.link(rx.icon(tag="twitter"), href="https://twitter.com/username"),
                spacing="4",
            ),
            rx.text(
                f"© {current_year} Nombre Completo. Todos los derechos reservados.",
                color="#9CA3AF",
            ),
            width="100%",
            align_items="center",
            padding_y="2rem",
        ),
        background_color="rgba(31, 41, 55, 0.5)",
    )
