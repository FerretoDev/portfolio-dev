import reflex as rx

from portfolio.components.button_color_mode import button_color_mode
from portfolio.components.ui.background import background

from .footer import footer
from .navbar import navbar


def layout(content: rx.Component) -> rx.Component:
    """Layout of the application"""
    return rx.vstack(
        button_color_mode(),
        navbar(),
        content,
        background(),
        footer(),
        witdh="100%",
        height="100%",
        spacing="4",
        align="center",
        padding="2rem",
    )
