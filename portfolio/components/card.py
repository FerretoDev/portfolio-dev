import reflex as rx

from portfolio.components.styles.styles import CardStyle


def card(title: str, description: str, tag: str) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(title, style=CardStyle.title),
            rx.text(
                description,
                style=CardStyle.description,
            ),
            style=CardStyle.stack,
        ),
        rx.box(style=CardStyle.background),
        rx.icon(tag=tag, style=CardStyle.icon),  # type: ignore
        style=CardStyle.base,
    )
