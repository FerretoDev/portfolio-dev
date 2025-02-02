from typing import Any

import reflex as rx


def section(*children: Any, **props: Any) -> rx.Component:
    return rx.box(
        *children,
        class_name="section",
        width="100%",
        **props,
    )
