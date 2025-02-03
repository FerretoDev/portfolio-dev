import reflex as rx

from portfolio.components.styles.styles import GlobalThemeVariables


def button_color_mode() -> rx.Component:
    return rx.color_mode.button(
        color=rx.Color(GlobalThemeVariables.LIGHT.value["text_primary"]),
        variant="ghost",
    )

    # return rx.color_mode.button(position="top-right"),

    # return rx.color_mode.button(position="top-right"),
