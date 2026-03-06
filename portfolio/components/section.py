from typing import Any, Dict, List, Optional

import reflex as rx

from portfolio.components.styles.styles import section_box_style, section_title_style


def section_component(
    title: Optional[str] = None,
    children: Optional[List[rx.Component]] = None,
    content_style: Optional[Dict[str, Any]] = None,
) -> rx.Component:
    """Componente base de sección.

    Args:
        title: Título de la sección (h2).
        children: Componentes hijos del contenido.
        content_style: Si se indica, envuelve los hijos en un rx.box con ese estilo.
                       Útil para listas, grids, etc. sin añadir una capa extra en cada sección.
    """
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

    if content_style is not None:
        section_content.append(rx.box(*children, style=content_style))
    else:
        section_content.extend(children)

    return rx.box(
        *section_content,
        as_="section",
        style=section_box_style,
    )
