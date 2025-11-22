from typing import Any, cast

import reflex as rx

from portfolio.components.styles.styles import GlobalThemeVariables


def button_color_mode() -> rx.Component:
    return rx.color_mode.button(  # type: ignore
        color=cast(Any, GlobalThemeVariables.LIGHT.value["--primary"]),
        variant="ghost",
    )

    # return rx.color_mode_button(position="top-right"),

    # return rx.color_mode_button(position="top-right"),
