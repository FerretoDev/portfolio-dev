import reflex as rx


def education_section():
    """Sección de educación."""
    return rx.box(
        rx.heading(
            "Educación",
            # style={"text-align": "center", "margin-bottom": "2rem"},
        ),
        rx.vstack(
            rx.box(
                rx.heading("Maestría en Matemáticas Aplicadas", size="2"),
                rx.text("Universidad Nacional Autónoma de México", color="#D1D5DB"),
                rx.text("2018 - 2020", color="#9CA3AF"),
                # style=section_styles["card"],
                margin_bottom="1rem",
            ),
            rx.box(
                rx.heading("Licenciatura en Ciencias de la Computación", size="2"),
                rx.text(
                    "Instituto Tecnológico de Estudios Superiores", color="#D1D5DB"
                ),
                rx.text("2014 - 2018", color="#9CA3AF"),
                # style=section_styles["card"],
            ),
            width="100%",
        ),
    )
