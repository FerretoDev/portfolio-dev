"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from portfolio.components.styles.theme import ThemeState
from portfolio.pages.about import about
from portfolio.pages.home import home

app = rx.App()


app.add_page(home(), route="/")
app.add_page(about(), route="/about")
