import reflex as rx

from portfolio.components.section import section
from portfolio.components.styles.styles import SectionStyle, GlobalThemeVariables


def about_section(title: str = "Sobre mí") -> rx.Component:
    """Sección Sobre Mí."""
    return section(
        rx.heading(
            title,
            **SectionStyle.title_style,
        ),
        rx.hstack(
            rx.box(
                rx.text(
                    "Soy un desarrollador de software apasionado por la intersección entre matemáticas, "
                    "ciencia de datos y tecnología. Me especializo en crear soluciones innovadoras "
                    "que transforman datos complejos en información accionable.",
                    # color="#D1D5DB",
                    color=rx.color_mode_cond(
                        light=GlobalThemeVariables.LIGHT.value["--secondary"],
                        dark=GlobalThemeVariables.DARK.value["--secondary"],
                    ),
                ),
                rx.text(
                    "Mi enfoque se centra en combinar rigor matemático con implementaciones de software "
                    "eficientes y escalables, utilizando las últimas tecnologías en desarrollo y análisis de datos.",
                    color="#D1D5DB",
                ),
            ),
            width="100%",
        ),
    )
