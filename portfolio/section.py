import reflex as rx

def section(title: str, content:rx.Component)->rx.Component:
    return rx.vstack(
        rx.heading(title, size="4"),
        content,
        spacing="4",
        align="center",
        padding="2rem",
    )