"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# from portfolio.components.ui.starfield import starfield_page
from portfolio.pages.index import index  # noqa: F401

# Configuración del tema
config = rx.Config(
    app_name="portfolio",
)
app = rx.App(
    stylesheets=[
        "/styles/styles.css",  # Estilos globales desde CSS para compatibilidad con Reflex Cloud
    ],
    theme=rx.theme(
        # appearance="inherit",  # tema inicial
        appearance="light",  # tema inicial
    ),
)

# app.add_page(index(), "/", "Index Page")
# app.stylesheets(BackgroundDos.keyframes)
# app.add_page(index(), "/", "Index Page")
# app.stylesheets(BackgroundDos.keyframes)
