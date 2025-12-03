"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from portfolio.components.styles.styles import global_style

# from portfolio.components.ui.starfield import starfield_page
from portfolio.pages.index import index  # noqa: F401

# Configuración del tema
config = rx.Config(
    app_name="portfolio",
)
app = rx.App(
    style=global_style(),
    # Sin theme personalizado para evitar sobrescritura de estilos
)
