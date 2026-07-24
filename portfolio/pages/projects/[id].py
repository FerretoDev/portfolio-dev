import reflex as rx


@rx.page("/projects/[id]", "Proyecto")
def project_detail() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Proyecto", size="5"),
            rx.link("← Volver al inicio", href="/"),
            align="center",
            spacing="4",
        ),
        height="100vh",
    )
