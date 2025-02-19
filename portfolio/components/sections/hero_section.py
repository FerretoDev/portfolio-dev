from dataclasses import dataclass, field

import reflex as rx

from portfolio.components.button import custom_button
from portfolio.components.section import section
from portfolio.components.styles.styles import GlobalThemeVariables, SectionStyle


@dataclass
class HeroStyle:
    hero_base: dict[str, str] = field(
        default_factory=lambda: {},
    )
    hero_title: dict[str, str] = field(
        default_factory=lambda: {
            "size": "7",
            "background": rx.color_mode_cond(
                light=f"linear-gradient(to right, {GlobalThemeVariables.LIGHT.value['--primary']}, {GlobalThemeVariables.LIGHT.value['--secondary']})",
                dark=f"linear-gradient(to right, {GlobalThemeVariables.DARK.value['--primary']}, {GlobalThemeVariables.DARK.value['--secondary']})",
            ),
            "font_size": "2rem",
            "background_image": "linear-gradient(to right, #06B6D4, #3B82F6)",
            "background_clip": "text",
            "color": "transparent",
        },
    )

    hero_image: dict[str, str] = field(
        default_factory=lambda: {
            # "border-radius": "10%",
            "border-radius": "0.5em",
            "box-shadow": rx.color_mode_cond(
                # light="0 0 30px rgba(8, 145, 178, 0.3)",
                # dark="0 0 30px rgba(6, 182, 212, 0.3)",
                light=f"0 0 30px {GlobalThemeVariables.LIGHT.value['--primary']}",
                dark=f"0 0 30px {GlobalThemeVariables.DARK.value['--primary']}",
            ),
            "width": "10%",
            # "max_width": "100%",
            "height": "auto",
            "size": "1",
            "border": f"1px solid {GlobalThemeVariables.LIGHT.value['--primary']}",
        },
    )
    hero_text: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--secondary"],
                dark=GlobalThemeVariables.DARK.value["--secondary"],
            ),
            # "font-size": "1.2em",
        },
    )


HeroStyle: HeroStyle = HeroStyle()


def hero_section() -> rx.Component:
    """Sección principal del hero."""
    return section(
        rx.hstack(
            rx.vstack(
                rx.text(
                    "Desarrollador de Software",
                    color=rx.color_mode_cond(
                        light=GlobalThemeVariables.LIGHT.value["--primary"],
                        dark=GlobalThemeVariables.DARK.value["--primary"],
                    ),
                    size="7",
                    # **HeroStyle.hero_text,
                    # color="#06B6D4",
                ),
                rx.heading(
                    "Transformando Ideas en Soluciones Tecnológicas",
                    **HeroStyle.hero_title,
                ),
                rx.text(
                    "Especializado en desarrollo de software, modelación matemática y análisis de datos. "
                    "Creando soluciones innovadoras con un enfoque analítico y técnico.",
                    # color="#D1D5DB",
                    color=rx.color_mode_cond(
                        light=GlobalThemeVariables.LIGHT.value["--secondary"],
                        dark=GlobalThemeVariables.DARK.value["--secondary"],
                    ),
                    margin_y="1rem",
                ),
                rx.hstack(
                    rx.button(
                        "Ver Proyectos",
                        background_color=rx.color_mode_cond(
                            light=GlobalThemeVariables.LIGHT.value["--primary"],
                            dark=GlobalThemeVariables.DARK.value["--primary"],
                        ),
                        color="white",
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                        margin_right="1rem",
                    ),
                    rx.button(
                        "Descargar CV",
                        background_color="transparent",
                        border=f"1px solid {GlobalThemeVariables.LIGHT.value['--primary']}",
                        color=rx.color_mode_cond(
                            light=GlobalThemeVariables.LIGHT.value["--primary"],
                            dark=GlobalThemeVariables.DARK.value["--primary"],
                        ),
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                    ),
                ),
                width="75%",
            ),
            rx.avatar(
                src="Designer.jpeg",
                **HeroStyle.hero_image,
            ),
            # width="100%",
            # align_items="center",
            # justify_content="space-between",
        ),
    )
