from typing import List, Optional

import reflex as rx

from portfolio.components.styles.styles import section_box_style, section_title_style


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
                as_="h2",
                style=section_title_style,
            )
        )

    section_content.extend(children)

    return rx.box(
        *section_content,
        as_="section",
        style=section_box_style,
    )
