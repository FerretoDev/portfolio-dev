from dataclasses import dataclass, field

import reflex as rx

from portfolio.components.button import custom_button
from portfolio.components.styles.styles import GlobalThemeVariables


@dataclass
class HeroStyle:
    hero_title: dict[str, str] = field(
        default_factory=lambda: {
            "size": "9",
            "font_size": "2.5em",
            "background": rx.color_mode_cond(
                light=f"linear-gradient(to right, {GlobalThemeVariables.LIGHT.value["--primary"]}, {GlobalThemeVariables.LIGHT.value["--secondary"]})",
                dark=f"linear-gradient(to right, {GlobalThemeVariables.DARK.value["--primary"]}, {GlobalThemeVariables.DARK.value["--secondary"]})",
            ),
            "background_clip": "text",
            "color": "transparent",
        },
    )

    hero_image: dict[str, str] = field(
        default_factory=lambda: {
            "border-radius": "10%",
            "box-shadow": rx.color_mode_cond(
                light="0 0 30px rgba(8, 145, 178, 0.3)",
                dark="0 0 30px rgba(6, 182, 212, 0.3)",
            ),
            "width": "10%",
            # "max_width": "100%",
            "height": "auto",
        },
    )
    hero_text: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--secondary"],
                dark=GlobalThemeVariables.DARK.value["--secondary"],
            ),
            "font-size": "1.2em",
        },
    )


HeroStyle: HeroStyle = HeroStyle()


def hero_section2() -> rx.Component:
    """Hero section of the application"""
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.heading(
                    "Software Development + Mathematical Modeling",
                    **HeroStyle.hero_title,
                ),
                rx.text(
                    "Transformando datos y algoritmos en soluciones innovadoras.",
                    color="whiteAlpha.800",
                    font_size="1.2em",
                ),
                rx.hstack(
                    rx.button(
                        "Ver Proyectos",
                        bg="cyan.500",
                        _hover={"bg": "cyan.600"},
                    ),
                    rx.button(
                        "Contactar",
                        variant="outline",
                        border_color="cyan.500",
                        color="cyan.500",
                        _hover={"bg": "rgba(6, 182, 212, 0.1)"},
                    ),
                    padding_top="1em",
                ),
                align_items="start",
                spacing="1",
                width="100%",
            ),
            rx.image(
                src="/Designer.jpeg",
                border_radius="1em",
                width="10%",
                box_shadow="0 0 30px rgba(6, 182, 212, 0.3)",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_top="8em",
            padding="2em",
            align_items="center",
            justify_content="space-between",
        )
    )


def hero_section1_3() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Software Development + Mathematical Modeling",
                **HeroStyle.hero_title,
            ),
            rx.text(
                "Transformando datos y algoritmos en soluciones innovadoras.",
                **HeroStyle.hero_text,
            ),
            rx.hstack(
                rx.button(
                    "Ver Proyectos",
                    size="2",
                    color_scheme="cyan",
                ),
                rx.button(
                    "Contactar",
                    size="2",
                    variant="outline",
                    color_scheme="cyan",
                ),
                rx.spacer(),
                rx.image(
                    src="/Designer.jpeg",
                    **HeroStyle.hero_image,
                ),
                padding_top="1em",
                align="center",
            ),
            align="center",
            spacing="6",
            padding_y="20",
        ),
        max_width="1200px",
        margin="0 auto",
        padding_top="8em",
        padding_x="2em",
        align_items="center",
        justify_content="space-between",
    )


def hero_section():
    """Sección principal del hero."""
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Desarrollador de Software", color="#06B6D4"),
                rx.heading(
                    "Transformando Ideas en Soluciones Tecnológicas",
                    font_size="3rem",
                    background_image="linear-gradient(to right, #06B6D4, #3B82F6)",
                    background_clip="text",
                    color="transparent",
                ),
                rx.text(
                    "Especializado en desarrollo de software, modelación matemática y análisis de datos. "
                    "Creando soluciones innovadoras con un enfoque analítico y técnico.",
                    color="#D1D5DB",
                    margin_y="1rem",
                ),
                rx.hstack(
                    rx.button(
                        "Ver Proyectos",
                        background_color="#06B6D4",
                        color="white",
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                        margin_right="1rem",
                    ),
                    rx.button(
                        "Descargar CV",
                        background_color="transparent",
                        border="1px solid #06B6D4",
                        color="#06B6D4",
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                    ),
                ),
                width="50%",
            ),
            rx.avatar(src="Designer.jpeg", size="2", border="4px solid #06B6D4"),
            width="100%",
            align_items="center",
            justify_content="space-between",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        min_height="100vh",
        # padding="0 2rem",
    )
