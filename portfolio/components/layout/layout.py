from typing import Any, List, Optional

import reflex as rx

from portfolio.components.styles.styles import layout_box_style


def layout(children: Optional[List[Any]] = None) -> rx.Component:
    if children is None:
        children = []

    return rx.fragment(
        rx.box(
            *children,
            style=layout_box_style,
        ),
    )
