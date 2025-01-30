from dataclasses import dataclass, field

import reflex as rx
from reflex.constants.colors import Color

from portfolio.components.button_color_mode import button_color_mode

# from portfolio.components.button_color_mode import button_color_mode
from portfolio.components.styles.styles import NavbarStyle
from portfolio.components.styles.theme import (
    THEME_STYLES,
    ThemeState,
    Theme,
    theme_toggle,
)


def media(name: str, link: str) -> rx.Component:
    return rx.link(rx.text(name, **NavbarStyle.link), href=link)


def navbar2() -> rx.Component:
    return rx.hstack(
        rx.heading("Portfolio( )", **NavbarStyle.brand),
        rx.spacer(),
        rx.hstack(
            *[
                rx.text(name, **NavbarStyle.brand)
                for name in [
                    media("Projects", "#Projects"),
                    media("About Me", "#about"),
                    media("Contact", "#contact"),
                ]
            ],
        ),
        **NavbarStyle.navigation,
    )


def navbar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.heading(
                "Portfolio()",
                color=rx.color("cyan", 5),
                font_family="mono",
            ),
            rx.spacer(),
            rx.hstack(
                rx.link("Proyectos", href="#proyectos"),
                rx.link("Sobre mí", href="#sobre-mi"),
                rx.link("Blog", href="#blog"),
                rx.link("Contacto", href="#contacto"),
                rx.button(
                    rx.color_mode_cond(
                        light=rx.icon("moon"),
                        dark=rx.icon("sun"),
                    ),
                    on_click=rx.toggle_color_mode,
                    variant="ghost",
                ),
                # button_color_mode(),
                spacing="2",
                color=rx.color_mode_cond(
                    light=rx.color("slate", 8),
                    dark=rx.color("slate", 2),
                ),
            ),
            width="100%",
            padding="1em",
            max_width="1200px",
            margin="0 auto",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="999",
        backdrop_filter="blur(10px)",
        background=rx.color_mode_cond(
            light="rgba(255, 255, 255, 0.8)",
            dark="rgba(0, 0, 0, 0.8)",
        ),
        border_bottom=rx.color_mode_cond(
            light="1px solid rgba(0,0,0,0.1)",
            dark="1px solid rgba(255,255,255,0.1)",
        ),
        display="flex",
        flex_wrap="wrap",
        justify_content="space-between",
        align_items="center",
    )
