"""Aplicación principal de Portfolio en Reflex."""

import reflex as rx

from portfolio.components.styles.styles import global_style
from portfolio.pages.index import index  # noqa: F401

app = rx.App(
    style=global_style(),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    ],
)

