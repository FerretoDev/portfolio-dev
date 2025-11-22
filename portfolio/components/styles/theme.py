from dataclasses import dataclass, field
from enum import Enum

import reflex as rx


# Definición de temas
class Theme(Enum):
    LIGHT = "light"
    DARK = "dark"


# Estado para el tema
class ThemeState(rx.State):
    theme: Theme = Theme.DARK
    theme_loaded: bool = False

    def handle_theme_change(self):
        """Toggle entre temas."""
        self.theme = Theme.LIGHT if self.theme == Theme.DARK else Theme.DARK

    def set_theme(self, theme: Theme):
        """Establecer un tema específico."""
        self.theme = theme

    def hydrate(self):
        """Marca el estado como hidratado después de la carga inicial."""
        self.theme_loaded = True


# Estilos base para cada tema
@dataclass
class THEME_STYLESS:
    base: dict[Theme, dict[str, str]] = field(
        default_factory=lambda: {
            Theme.LIGHT: {
                "background": "radial-gradient(circle at 10% 20%, rgb(255, 255, 255) 0%, rgb(240, 240, 240) 90.1%)",
                "text_color": "gray.800",
                "nav_bg": "rgba(255, 255, 255, 0.7)",
                "card_bg": "rgba(255, 255, 255, 0.5)",
                "border_color": "rgba(0, 0, 0, 0.1)",
                "hover_color": "cyan.600",
            },
            Theme.DARK: {
                "background": "radial-gradient(circle at 10% 20%, rgb(0, 0, 0) 0%, rgb(17, 24, 39) 90.1%)",
                "text_color": "white",
                "nav_bg": "rgba(17, 24, 39, 0.7)",
                "card_bg": "rgba(31, 41, 55, 0.5)",
                "border_color": "rgba(255, 255, 255, 0.1)",
                "hover_color": "cyan.400",
            },
        }
    )


THEME_STYLESS: THEME_STYLESS = THEME_STYLESS()  # type: ignore

THEME_STYLES = {
    Theme.LIGHT: {
        "background": "radial-gradient(circle at 10% 20%, rgb(255, 255, 255) 0%, rgb(240, 240, 240) 90.1%)",
        "text_color": "gray.800",
        "nav_bg": "rgba(255, 255, 255, 0.7)",
        "card_bg": "rgba(255, 255, 255, 0.5)",
        "border_color": "rgba(0, 0, 0, 0.1)",
        "hover_color": "cyan.600",
    },
    Theme.DARK: {
        "background": "radial-gradient(circle at 10% 20%, rgb(0, 0, 0) 0%, rgb(17, 24, 39) 90.1%)",
        "text_color": "white",
        "nav_bg": "rgba(17, 24, 39, 0.7)",
        "card_bg": "rgba(31, 41, 55, 0.5)",
        "border_color": "rgba(255, 255, 255, 0.1)",
        "hover_color": "cyan.400",
    },
}


# Componente para el toggle de tema
def theme_toggle() -> rx.Component:
    return rx.box(
        rx.button(
            rx.cond(ThemeState.theme == Theme.DARK, rx.icon("sun"), rx.icon("moon")),
            on_click=ThemeState.handle_theme_change,  # Type: ignore
            bg="transparent",
            _hover={"color": "cyan.400"},
        ),
    )
