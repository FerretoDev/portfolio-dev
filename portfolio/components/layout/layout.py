from typing import List, Optional

import reflex as rx

from portfolio.components.button_color_mode import button_color_mode
from portfolio.components.styles.styles import layout_box_style


def layout(title: str = "Portfolio", children: Optional[List[rx.Component]] = None) -> rx.Component:
    """Componente principal de layout de la aplicación."""
    if children is None:
        children = []

    return rx.fragment(
        button_color_mode(),
        rx.box(
            *children,
            style=layout_box_style,
        ),
    )


