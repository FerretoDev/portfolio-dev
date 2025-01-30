from typing import Optional

import reflex as rx

# from portfolio.components.styles.theme import THEME_STYLES, ThemeState, Theme
from portfolio.components.ui.background import background
from portfolio.components.layout.hero_section import hero_section
from .footer import footer

# from .hero_section import hero_section
from .navbar import navbar
from portfolio.components.layout.project_section import project_section
from portfolio.components.styles.styles import LayoutStyle


def layout() -> rx.Component:
    """Layout of the application"""
    return rx.box(
        navbar(),
        rx.vstack(
            hero_section(),
            project_section(),
            background(),
        ),
        footer(),
        **LayoutStyle.base,
    )
