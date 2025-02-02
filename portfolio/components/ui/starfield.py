import random
from dataclasses import dataclass, field
from typing import List

import reflex as rx

STAR_COLORS: List = ["#fff2", "#fff4", "#fff7", "#fffC"]


@dataclass
class SpaceLayerConfig:
    """Configuración para una capa de estrellas."""

    box_shadow: str
    size: str
    duration: str


def generate_space_layer(
    total_stars: int = 200, size: str = "2px", duration: str = "15s"
) -> SpaceLayerConfig:
    """Genera una capa de estrellas con configuración mejorada."""
    # Generamos las estrellas con posiciones aleatorias
    star_shadows = []
    for _ in range(total_stars):
        color = random.choice(STAR_COLORS)
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        star_shadows.append(f"{x}vw {y}vh white, {x}vw {y + 100}vh {color}")

    box_shadow = ", ".join(star_shadows)

    return SpaceLayerConfig(box_shadow=box_shadow, size=size, duration=duration)


@dataclass
class StarfieldBackground:
    """Clase para el fondo estrellado."""

    # Estilos para el contenedor principal
    container: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100vw",
            "height": "100vh",
            "position": "fixed",
            "top": "0",
            "left": "0",
            "background": "linear-gradient(#051327, #000)",
            "overflow": "hidden",
        }
    )

    # Configuraciones para las diferentes capas de estrellas
    stars_small: dict[str, str] = field(
        default_factory=lambda: {
            "position": "absolute",
            "width": "1px",
            "height": "1px",
            "background": "transparent",
            "box_shadow": generate_space_layer(
                total_stars=200, size="1px", duration="25s"
            ).box_shadow,
            "animation": "animateStarsSmall 20s linear infinite",
        }
    )

    stars_medium: dict[str, str] = field(
        default_factory=lambda: {
            "position": "absolute",
            "width": "2px",
            "height": "2px",
            "background": "transparent",
            "box_shadow": generate_space_layer(
                total_stars=100, size="2px", duration="20s"
            ).box_shadow,
            "animation": "animateStarsMedium 15s linear infinite",
        }
    )

    stars_large: dict[str, str] = field(
        default_factory=lambda: {
            "position": "absolute",
            "width": "3px",
            "height": "3px",
            "background": "transparent",
            "box_shadow": generate_space_layer(
                total_stars=25, size="4px", duration="15s"
            ).box_shadow,
            "animation": "animateStarsLarge 10s linear infinite",
        }
    )

    # Definición de las animaciones para cada capa
    keyframes: dict[str, dict[str, dict[str, str]]] = field(
        default_factory=lambda: {
            "@keyframes animateStarsSmall": {
                "from": {"transform": "translateY(0)"},
                "to": {"transform": "translateY(-100vh)"},
            },
            "@keyframes animateStarsMedium": {
                "from": {"transform": "translateY(0)"},
                "to": {"transform": "translateY(-100vh)"},
            },
            "@keyframes animateStarsLarge": {
                "from": {"transform": "translateY(0)"},
                "to": {"transform": "translateY(-100vh)"},
            },
        }
    )


# Instancia global
starfield_bg = StarfieldBackground()


def create_starfield() -> rx.Component:
    """Crea el componente de fondo estrellado con múltiples capas."""
    return rx.box(
        rx.box(
            rx.center(
                rx.text("🌟 Starfield"),
                size="5em",
                top="50%",
                left="50%",
            ),
            # Capa de estrellas pequeñas
            rx.box(
                **starfield_bg.stars_small,
            ),
            # Capa de estrellas medianas
            rx.box(
                **starfield_bg.stars_medium,
            ),
            # Capa de estrellas grandes
            rx.box(
                **starfield_bg.stars_large,
            ),
            **starfield_bg.container,
        ),
        **starfield_bg.keyframes,
        width="100%",
        height="100vh",
        background="#171717",
    )


@rx.page("/starfield")
def starfield_page() -> rx.Component:
    """Página de ejemplo con el fondo estrellado."""
    return create_starfield()
