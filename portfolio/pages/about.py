import reflex as rx

from portfolio.components.layout.layout import layout


def about() -> rx.Component:
    return layout(
        rx.text("About: This is the about page. Marcos Ferreto"),
    )
