import reflex as rx

from portfolio.components.styles.styles import text_style


def text(text: str) -> rx.Component:
    return rx.text(
        text,
        style=text_style.paragraph,
    )
