import reflex as rx

from portfolio.components.section import section
from portfolio.components.styles.styles import GlobalThemeVariables, SectionStyle


def text_component(text: str) -> rx.Component:
    return rx.text(
        text,
        color=" #666",
        font_size="0.9rem",
        line_height="1.5",
        margin="0",
        text_wrap="pretty",
    )


def about_section(title: str = "Sobre mí") -> rx.Component:
    """Sección Sobre Mí."""
    return section(
        rx.heading(
            title,
            **SectionStyle.title_style,
        ),
        rx.vstack(
            text_component(
                "Soy un desarrollador de software apasionado por la intersección entre matemáticas, ciencia de datos y tecnología. Me especializo en crear soluciones innovadoras que transforman datos complejos en información accionable."
            ),
            text_component(
                "Mi enfoque se centra en combinar rigor matemático con implementaciones de software eficientes y escalables, utilizando las últimas tecnologías en desarrollo y análisis de datos."
            ),
        ),
    )
