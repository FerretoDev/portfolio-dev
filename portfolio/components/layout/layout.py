from dataclasses import dataclass, field

import reflex as rx

from portfolio.components.styles.theme import THEME_STYLES, ThemeState, Theme
from portfolio.components.ui.background import background

from .footer import footer

# from .hero_section import hero_section
from .navbar import navbar


@dataclass
class LayoutStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "background": rx.cond(
                ThemeState.theme == Theme.DARK,
                THEME_STYLES[Theme.DARK]["nav_bg"],
                THEME_STYLES[Theme.LIGHT]["nav_bg"],
            ),
            "min_height": "130vh",
            "color": rx.cond(
                ThemeState.theme == Theme.DARK,
                THEME_STYLES[Theme.DARK]["text_color"],
                THEME_STYLES[Theme.LIGHT]["text_color"],
            ),
            "transition": "background 0.3s ease, color 0.3s ease",
            "width": "100%",
            "align": "center",
            "justify": "center",
            "padding": "0em 1em",
        }
    )


LayoutStyle: LayoutStyle = LayoutStyle()


def layout(content: rx.Component) -> rx.Component:
    """Layout of the application"""
    return rx.vstack(
        navbar(),
        content,
        background(),
        footer(),
        **LayoutStyle.base,
    )
