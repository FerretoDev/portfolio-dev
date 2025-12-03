from typing import Any, List, Optional

import reflex as rx

from portfolio.components.styles.styles import layout_box_style

# Simulamos la importación de datos del CV
# En tu caso real, importarías desde tu archivo de datos
basics: dict = {
    "image": "/path/to/image.jpg",
    "summary": "Descripción del CV",
    "url": "https://tu-dominio.com",
}


def layout(title="Mi CV", children: Optional[List[Any]] = None) -> rx.Component:
    if children is None:
        children = []

    return rx.fragment(
        # Layout base
        rx.box(
            *children,
            style=layout_box_style,
        ),
    )  # Como usar rx.fragment para envolver el layout completo en https://reflex.dev/docs/library/layout/fragment/
