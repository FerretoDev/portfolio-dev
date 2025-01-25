import reflex as rx

from portfolio.components.layout.layout import layout


def home() -> rx.Component:
    return layout(
        rx.text("Home: This is the home page. Marcos Ferreto"),
    )
