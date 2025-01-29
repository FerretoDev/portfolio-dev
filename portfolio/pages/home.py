import reflex as rx

from portfolio.components.layout.hero_section import hero_section
from portfolio.components.layout.layout import layout


@rx.page("/", "Home Page")
def home() -> rx.Component:
    return layout(
        hero_section(),
    )
