import reflex as rx

from portfolio.components.styles.styles import GlobalThemeVariables


def header() -> rx.Component:
    return rx.hstack(
        rx.heading("Portafolio", color=GlobalThemeVariables.DARK.value["primary"]),
        rx.spacer(),
        rx.hstack(
            rx.link(
                "Inicio",
                href="/",
                color=GlobalThemeVariables.DARK.value["text_primary"],
            ),
            rx.link(
                "Proyectos",
                href="/projects",
                color=GlobalThemeVariables.DARK.value["text_primary"],
            ),
            rx.link(
                "Contacto",
                href="/contact",
                color=GlobalThemeVariables.DARK.value["text_primary"],
            ),
            spacing="2",
            display=["none", "none", "flex"],
        ),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Options", variant="soft"),
            ),
            rx.menu.content(
                rx.menu.item("Inicio"),
                rx.menu.item("Proyectos"),
                rx.menu.item("Contacto"),
            ),
            display=["flex", "flex", "none"],
        ),
        # rx.menu(
        #    rx.button(rx.icon(tag="trophy")),
        #    rx.menu_list(
        #        rx.menu_item("Inicio"),
        #        rx.menu_item("Proyectos"),
        #        rx.menu_item("Contacto"),
        #    ),
        #    display=["flex", "flex", "none"],
        # ),
        bg=GlobalThemeVariables.DARK.value["bg_darker"],
        padding="1.5rem",
        position="sticky",
        top="0",
        z_index="1000",
        width="100%",
    )
