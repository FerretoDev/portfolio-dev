from typing import Any, List, Optional

import reflex as rx

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
            style={
                "font_family": "Menlo, Monaco, 'Lucida Console', 'Courier New', Courier, monospace",
                "letter_spacing": "-0.025rem",
                "margin": "0 auto",
                "padding": "0 2rem",
                "max_width": "1200px",
                "width": "100%",
                "@media (max-width: 768px)": {
                    "padding": "0 1.5rem",
                },
                "@media (max-width: 640px)": {
                    "padding": "0 1rem",
                },
            },
        ),
    )  # Como usar rx.fragment para envolver el layout completo en https://reflex.dev/docs/library/layout/fragment/
