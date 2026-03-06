import reflex as rx


@rx.page("/404", "Página no encontrada")
def not_found() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("404", size="9"),
            rx.text("Página no encontrada"),
            rx.link("Volver al inicio", href="/"),
            align="center",
            spacing="4",
        ),
        height="100vh",
    )
