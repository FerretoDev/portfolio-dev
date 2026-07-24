import reflex as rx


def button_color_mode() -> rx.Component:
    """Botón para alternar entre modo claro y oscuro."""
    return rx.box(
        rx.color_mode.button(),
        style={
            "position": "fixed",
            "top": "1.25rem",
            "right": "1.25rem",
            "z_index": "1000",
        },
    )


