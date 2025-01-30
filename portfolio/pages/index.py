import reflex as rx


from portfolio.components.layout.layout import layout


@rx.page("/", "Portfolio")
def index() -> rx.Component:
    return layout()
