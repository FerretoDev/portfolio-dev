import reflex as rx
from portfolio.components.section import section
from portfolio.components.styles.styles import SectionStyle


def experience_section(title: str = "Experiencia Profesional") -> rx.Component:
    """Sección de experiencia laboral."""
    return section(
        rx.heading(
            title,
            **SectionStyle.title_style,
        ),
        rx.vstack(
            rx.box(
                rx.heading("Científico de Datos Senior", size="2"),
                rx.text("Empresa Tech Innovadora", color="#D1D5DB"),
                rx.text("2020 - Presente", color="#9CA3AF"),
                rx.text(
                    "Desarrollo de modelos predictivos y soluciones de machine learning para optimización de procesos.",
                    color="#D1D5DB",
                    # margin_top="0.5rem",
                ),
                # style=section_styles["card"],
                # margin_bottom="1rem",
            ),
            rx.box(
                rx.heading("Desarrollador de Software", size="2"),
                rx.text("Startup de Análisis de Datos", color="#D1D5DB"),
                rx.text("2018 - 2020", color="#9CA3AF"),
                rx.text(
                    "Implementación de APIs y servicios backend para análisis de grandes volúmenes de datos.",
                    color="#D1D5DB",
                    # margin_top="0.5rem",
                ),
                # style=section_styles["card"],
            ),
            # width="100%",
        ),
    )
