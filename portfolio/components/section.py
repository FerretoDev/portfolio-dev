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
                    "margin_bottom": "16px",
                    "font_weight": "700",
                    "line_height": "1.3",
                    "font_size": "1.75rem",
                    "@media (max-width: 768px)": {
                        "font_size": "1.5rem",
                        "margin_bottom": "12px",
                    },
                    "@media (max-width: 640px)": {
                        "font_size": "1.35rem",
                        "margin_bottom": "10px",
                    },
                },
            )
        )

    section_content.extend(children)

    return rx.box(
        *section_content,
        as_="section",
        style={
            "max_width": "800px",
            "margin": "0 auto 48px",
            "padding": "0 1rem",
            "scroll_margin_top": "80px",  # Para navegación con scroll suave
            "@media (max-width: 768px)": {
                "margin_bottom": "38px",
                "padding": "0 0.5rem",
            },
            "@media (max-width: 640px)": {
                "margin_bottom": "28px",
                "padding": "0",
            },
        },
    )
