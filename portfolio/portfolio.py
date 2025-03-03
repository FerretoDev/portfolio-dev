"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# from portfolio.components.ui.starfield import starfield_page
from portfolio.pages.index import index  # noqa: F401

# from portfolio.components.styles.styles import global_style

# Configuración del tema
config = rx.Config(
    app_name="portfolio",
)
app = rx.App(
    # style=global_style(),
    theme=rx.theme(
        appearance="dark",  # tema inicial
        has_background=True,
        radius="medium",
        accent_color="cyan",
        # gray_color="slate",
        panel_background="translucent",
        scaling="100%",
        font_family="Inter, sans-serif",
    ),
)

# app.add_page(index(), "/", "Index Page")
# app.stylesheets(BackgroundDos.keyframes)
# app.add_page(index(), "/", "Index Page")
# app.stylesheets(BackgroundDos.keyframes)
