from typing import Any

import reflex as rx


def container(*children: Any, **props: Any) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        max_width="1200px",
        margin_x="auto",
        padding_x=["1rem", "2rem", "3rem"],
        **props,
        # hola
    )
