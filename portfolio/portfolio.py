"""Aplicación principal de Portfolio en Reflex."""

import reflex as rx

from portfolio.pages.index import index  # noqa: F401

from portfolio.pages.not_found import not_found  # noqa: F401


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
        "animations.css",
    ],
    # enable_state=False,
)
