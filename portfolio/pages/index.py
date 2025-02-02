import reflex as rx

from portfolio.components.layout.hero_section import hero_section
from portfolio.components.layout.layout import layout
from portfolio.components.layout.project_section import project_section


@rx.page("/", "Portfolio")  # type: ignore
def index() -> rx.Component:
    return layout(
        rx.vstack(
            hero_section(),
            project_section(),
        )
    )
