import reflex as rx
from portfolio.components.section import section


def education_section():
    """Sección de educación."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "Educación",
                style=rx.Style(
                    {
                        "text-align": "center",
                        "margin-bottom": "2rem",
                    },
                ),
            ),
            rx.hstack(
                rx.box(
                    rx.heading("Maestría en Matemáticas Aplicadas", size="2"),
                    rx.text("Universidad Nacional Autónoma de México", color="#D1D5DB"),
                    rx.text("2018 - 2020", color="#9CA3AF"),
                    style=rx.Style(
                        {
                            "background": "rgba(31, 41, 55, 0.5)",
                            "border-radius": "0.75rem",
                            "padding": "1.5rem",
                            "transition": "transform 0.3s ease",
                            "hover": {"transform": "translateY(-10px)"},
                        },
                    ),
                    margin_bottom="1rem",
                ),
                rx.box(
                    rx.heading("Licenciatura en Ciencias de la Computación", size="2"),
                    rx.text(
                        "Instituto Tecnológico de Estudios Superiores", color="#D1D5DB"
                    ),
                    rx.text("2014 - 2018", color="#9CA3AF"),
                    style=rx.Style(
                        {
                            "background": "rgba(31, 41, 55, 0.5)",
                            "border-radius": "0.75rem",
                            "padding": "1.5rem",
                            "transition": "transform 0.3s ease",
                            "hover": {"transform": "translateY(-10px)"},
                        },
                    ),
                ),
                width="100%",
            ),
            align="center",
            padding="2rem",
        ),
        align_items="center",
        padding_x="10rem",
    )
