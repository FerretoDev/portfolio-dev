"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from portfolio.components.styles.styles import global_style

# from portfolio.components.ui.starfield import starfield_page
from portfolio.pages.index import index  # noqa: F401
from portfolio.pages.not_found import not_found  # noqa: F401

# La configuración está en rxconfig.py
app = rx.App(
    theme=rx.theme(font_family="Inter", appearance="light", accent_color="cyan"),
    style=global_style(),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
        "animations.css",
    ],
)
