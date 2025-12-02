import reflex as rx

from portfolio.components.section import section
from portfolio.components.text import text as text_component


def about_section() -> rx.Component:
    return rx.fragment(
        section(
            children=[
                rx.heading(
                    "Sobre mí",
                ),
                rx.vstack(
                    text_component(
                        "Soy un desarrollador de software apasionado por la intersección entre matemáticas, ciencia de datos y tecnología. Me especializo en crear soluciones innovadoras que transforman datos complejos en información accionable."
                    ),
                    text_component(
                        "Mi enfoque se centra en combinar rigor matemático con implementaciones de software eficientes y escalables, utilizando las últimas tecnologías en desarrollo y análisis de datos."
                    ),
                ),
            ]
        )
    )
