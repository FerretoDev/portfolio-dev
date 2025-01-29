from dataclasses import dataclass, field

import reflex as rx
from reflex.constants.colors import Color

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


def navbar():
    return rx.box(
        rx.hstack(
            rx.heading("Portfolio()", color="cyan.500", font_family="monospace"),
            rx.spacer(),
            rx.hstack(
                rx.link("Proyectos", href="#proyectos"),
                rx.link("Sobre mí", href="#sobre-mi"),
                rx.link("Blog", href="#blog"),
                rx.link("Contacto", href="#contacto"),
                theme_toggle(),  # Toggle de tema
                spacing="2",
                color=rx.cond(
                    ThemeState.theme == Theme.DARK,
                    THEME_STYLES[Theme.DARK]["text_color"],
                    THEME_STYLES[Theme.LIGHT]["text_color"],
                ),
            ),
            padding="1em",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        **NavbarStyle.navigation,
        # background=rx.cond(
        #    State.theme == Theme.DARK,
        #    THEME_STYLES[Theme.DARK]["nav_bg"],
        #    THEME_STYLES[Theme.LIGHT]["nav_bg"],
        # ),
    )
