from dataclasses import dataclass, field
from typing import Any, Optional

import reflex as rx

from portfolio.components.styles.styles import LayoutStyle, SectionStyle

from .footer import footer
from .header import header

# Estilos globales
global_styles = {}


@dataclass
class BaseStyle:
    # Estilos base para la sección
    base_style: dict[str, dict[str, str]] = field(
        default_factory=lambda: {
            "html": {
                "font_family": "Menlo, Monaco, Lucida Console, 'Courier New', Courier, monospace",
                "letter_spacing": "-0.025rem",
            },
            "body": {
                "margin": "0",
                "padding": "0",
            },
            "figure": {
                "margin": "0",
                "padding": "0",
            },
            "a": {
                "text_decoration": "none",
            },
            "ul": {
                "list_style": "none",
                "margin": "0",
                "padding": "0",
            },
            "*": {
                "box_sizing": "border-box",
            },
            "h1, h2, h3, h4": {
                "margin": "0",
                "font_family": """system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI',
            Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif""",
            },
            "p": {
                "color": "#666",
                "font_size": "0.9rem",
                "line_height": "1.5",
                "margin": "0",
                "text_wrap": "pretty",
            },
            ".print": {
                "display": "none",
            },
            "@media print": {
                ".no-print": {
                    "display": "none",
                },
                ".print": {
                    "display": "block",
                },
                "article": {
                    "break_inside": "avoid",
                },
            },
        }
    )
    style_index: dict[str, str] = field(
        default_factory=lambda: {
            "padding": "4rem",
            "margin": "auto",
            "width": "100 %",
        }
    )

    # Estilos responsive
    section_style_mobile: dict[str, dict[str, str]] = field(
        default_factory=lambda: {
            "@media (width <= 700px)": {
                "padding": "2rem",
            },
        }
    )


BaseStyle: BaseStyle = BaseStyle()


def layout(content: Optional[Any] = None) -> rx.Component:
    return (
        rx.vstack(
            rx.box(header(), width="100%"),  # Header
            rx.vstack(
                # rx.box(content, width="100%"),  # Contenido principal
                # rx.box(footer(), width="100%"),  # Footer
            ),
        ),
    )
