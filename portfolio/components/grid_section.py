from typing import Any

import reflex as rx


def grid_section(*children: Any, columns: int = 3) -> rx.Component:
    return rx.grid(
        *children,
        template_columns=f"repeat({columns}, 1fr)",
        gap=4,
        width="100%",
        padding_y="2rem",
        responsive=True,
    )
