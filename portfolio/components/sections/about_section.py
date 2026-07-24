import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.text import text as text_component
from portfolio.constants import basics


def about_section() -> rx.Component:
    return section_component(
        title="Sobre mí",
        children=[
            rx.vstack(
                *[text_component(p) for p in basics["summary"]],
                spacing="3",
                align_items="start",
                width="100%",
            ),
        ],
    )
