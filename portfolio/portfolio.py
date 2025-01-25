"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from portfolio.pages.about import about
from portfolio.pages.home import home


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text("Welcome to Reflex!"),
        ),
    )


app = rx.App()

app.add_page(index, route="/index")
app.add_page(home(), route="/")
app.add_page(about(), route="/about")
