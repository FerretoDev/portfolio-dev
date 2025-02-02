import reflex as rx


def about_section() -> rx.Component:
    return rx.box(
        rx.text("About: This is the about page. Marcos Ferreto"),
    )
