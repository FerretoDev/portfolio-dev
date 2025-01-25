import reflex as rx


def project_card(title: str, description: str) -> rx.Component:
    return rx.box(
        rx.heading(title),
        rx.text(description),
        border_radius="lg",
        box_shadow="lg",
        padding="1em",
    )
