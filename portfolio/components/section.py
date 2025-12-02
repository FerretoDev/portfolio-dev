from typing import List, Optional

import reflex as rx


def section_component(
    title: Optional[str] = None, children: Optional[List[rx.Component]] = None
) -> rx.Component:
    """Componente Section"""
    if children is None:
        children = []

    section_content: List[rx.Component] = []

    if title:
        section_content.append(
            rx.heading(
                title,
                level=2,
                style={
                    "margin_bottom": "8px",
                    "font_weight": "700",
                    "line_height": "1.5",
                    "font_size": "1.5rem",
                },
            )
        )

    section_content.extend(children)

    return rx.box(
        *section_content,
        # tag="section",
        style={
            "max_width": "700px",
            "margin": "0 auto 48px",
            "@media (max-width: 700px)": {
                "margin_bottom": "38px",
            },
        },
    )
