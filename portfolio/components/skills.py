import reflex as rx


def skills(text: str, text_heading: str = "Habilidades") -> rx.Component:
    return rx.vstack(
        rx.heading(
            text_heading,
            size="4",
        ),
        rx.text(text),
    )
