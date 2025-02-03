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
            rx.heading("Portafolio", color=GlobalThemeVariables.DARK.value["primary"]),
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
            bg=rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["bg_dark"],
                dark=GlobalThemeVariables.DARK.value["bg_dark"],
            ),
            padding="1.5rem",
            position="sticky",
            top="0",
            z_index="1000",
            width="100%",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="999",
        backdrop_filter="blur(10px)",
        # background=rx.color_mode_cond(
        #    light="rgba(255, 255, 255, 0.8)",
        #    dark="rgba(0, 0, 0, 0.8)",
        # ),
        border_bottom=rx.color_mode_cond(  # Linea de separación
            light="1px solid rgba(0,0,0,0.1)",
            dark="1px solid rgba(255,255,255,0.1)",
        ),
        display="flex",
        flex_wrap="wrap",
        justify_content="space-between",
        align_items="center",
    )
