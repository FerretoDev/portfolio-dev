"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from portfolio.components.styles.styles import global_style

# from portfolio.components.ui.starfield import starfield_page
from portfolio.pages.index import index  # noqa: F401

# La configuración está en rxconfig.py
app = rx.App(
    style=global_style(),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    ],
)
