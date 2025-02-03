import reflex as rx


def about_section():
    """Sección Sobre Mí."""
    return rx.box(
        rx.heading(
            "Sobre Mí",
            # style={"text-align": "center", "margin-bottom": "2rem"},
        ),
        rx.hstack(
            rx.avatar(src="/Designer.jpeg", size="2", border="4px solid #06B6D4"),
            rx.box(
                rx.text(
                    "Soy un desarrollador de software apasionado por la intersección entre matemáticas, "
                    "ciencia de datos y tecnología. Me especializo en crear soluciones innovadoras "
                    "que transforman datos complejos en información accionable.",
                    color="#D1D5DB",
                    margin_bottom="1rem",
                ),
                rx.text(
                    "Mi enfoque se centra en combinar rigor matemático con implementaciones de software "
                    "eficientes y escalables, utilizando las últimas tecnologías en desarrollo y análisis de datos.",
                    color="#D1D5DB",
                ),
                width="70%",
            ),
            width="100%",
            spacing="4",
        ),
    )
