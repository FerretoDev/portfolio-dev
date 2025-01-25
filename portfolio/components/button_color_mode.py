import reflex as rx

def button_color_mode() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
    )