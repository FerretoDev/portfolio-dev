from typing import Any, Optional

import reflex as rx

from portfolio.components.styles.styles import LayoutStyle

from .about_section import about_section
from .education_section import education_section
from .footer import footer
from .header import header
from .hero_section import hero_section
from .navbar import navbar
from .project_section import project_section

# from portfolio.components.styles.theme import THEME_STYLES, ThemeState, Theme
# from portfolio.components.ui.background import background


def main_layout() -> rx.Component:
    """Layout of the application"""
    return rx.box(
        navbar(),
        rx.vstack(
            hero_section(),
            about_section(),
            project_section(),
            education_section(),
            # background(),
            align="center",
        ),
        footer(),
        **LayoutStyle.base,
    )


def layout(content: Optional[Any] = None) -> rx.Component:
    return rx.vstack(
        rx.box(header(), width="100%"),  # Header
        rx.box(content, width="100%"),  # Contenido principal
        rx.box(footer(), width="100%"),  # Footer
        min_height="100vh",
        spacing="0",
    )
