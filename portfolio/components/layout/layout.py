from typing import Any, Optional

import reflex as rx

from portfolio.components.styles.styles import LayoutStyle


from .footer import footer
from .header import header


def layout(content: Optional[Any] = None) -> rx.Component:
    return rx.vstack(
        rx.box(header(), width="100%"),  # Header
        rx.box(content, width="100%"),  # Contenido principal
        rx.box(footer(), width="100%"),  # Footer
        **LayoutStyle.base,  # Estilos base
    )
