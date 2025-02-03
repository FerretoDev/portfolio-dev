import reflex as rx

from portfolio.components.button_color_mode import button_color_mode
from portfolio.components.styles.styles import GlobalThemeVariables, HeaderStyle


def link(text: str, url: str) -> rx.Component:
    return rx.link(
        text,
        href=url,
        color=rx.color_mode_cond(
            light=GlobalThemeVariables.LIGHT.value["text_primary"],
            dark=GlobalThemeVariables.DARK.value["text_primary"],
        ),
    )


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("Portfolio", color=GlobalThemeVariables.DARK.value["primary"]),
            rx.spacer(),
            rx.hstack(
                link("Inicio", "#portfolio"),
                link("Contacto", "#contact"),
                button_color_mode(),
                spacing="2",
                display=["none", "none", "flex"],
            ),
            rx.spacer(),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        "Options",
                        variant="soft",
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Inicio"),
                    rx.menu.item("Proyectos"),
                    rx.menu.item("Contacto"),
                ),
                display=["flex", "flex", "none"],
            ),
            **HeaderStyle.content,
        ),
        **HeaderStyle.base,
    )
