from dataclasses import dataclass, field
from typing import Any

import reflex as rx

from portfolio.components.button import custom_button
from portfolio.components.section import section
from portfolio.components.styles.styles import GlobalThemeVariables, SectionStyle


@dataclass
class HeroStyle:
    container: dict[str, str | dict] = field(
        default_factory=lambda: {
            "display": "flex",
            "flex-direction": "row",
            "align-items": "center",
            "justify-content": "space-between",
            "gap": "1rem",
            # "@media (width <= 700px)": {
            #    "flex-direction": "column-reverse",
            # },
        },
    )

    info: dict[str, str | dict] = field(
        default_factory=lambda: {
            # "display": "flex",
            # "flex-direction": "column",
            "gap": "0.5rem",
            "padding-right": "32px",
            "@media (width <= 700px)": {
                "justify-content": "center",
                "align-items": "center",
                "padding-right": 0,
                "text-align": "center",
            },
        },
    )
    span: dict[str, str] = field(
        default_factory=lambda: {
            "color": "#666",
            "display": "flex",
            "align-items": "center",
            "gap": "0.25rem",
            "font-size": "0.85rem",
            "letter-spacing": " -0.05rem",
        },
    )
    hero_title: dict[str, str] = field(
        default_factory=lambda: {
            # "size": "7",
            # "background": rx.color_mode_cond(
            #    light=f"linear-gradient(to right, {GlobalThemeVariables.LIGHT.value['--primary']}, {GlobalThemeVariables.LIGHT.value['--secondary']})",
            #    dark=f"linear-gradient(to right, {GlobalThemeVariables.DARK.value['--primary']}, {GlobalThemeVariables.DARK.value['--secondary']})",
            # ),
            "font_size": "2rem",
            # "background_image": "linear-gradient(to right, #06B6D4, #3B82F6)",
            # "background_clip": "text",
            # "color": "transparent",
        },
    )

    hero_image: dict[str, str] = field(
        default_factory=lambda: {
            # "border-radius": "10%",
            # "border-radius": "0.5em",
            "box-shadow": rx.color_mode_cond(
                # light="0 0 30px rgba(8, 145, 178, 0.3)",
                # dark="0 0 30px rgba(6, 182, 212, 0.3)",
                light=f"0 0 30px {GlobalThemeVariables.LIGHT.value['--primary']}",
                dark=f"0 0 30px {GlobalThemeVariables.DARK.value['--primary']}",
            ),
            "height": "auto",
            # "size": "1",
            "border": f"1px solid {GlobalThemeVariables.LIGHT.value['--primary']}",
            "aspect-ratio": " 1 / 1",
            "object-fit": "cover",
            "width": "128px",
            "border-radius": "16px",
        },
    )
    hero_h2: dict[str, str] = field(
        default_factory=lambda: {
            # "color": rx.color_mode_cond(
            #    light=GlobalThemeVariables.LIGHT.value["--secondary"],
            #    dark=GlobalThemeVariables.DARK.value["--secondary"],
            # ),
            "color": "#444",
            "font-weight": "500",
            "font-size": "1.1rem",
            "text-wrap": "balance",
        },
    )


HeroStyle: HeroStyle = HeroStyle()


def hero_section() -> rx.Component:
    """Sección principal del hero."""
    return section(
        rx.hstack(
            rx.vstack(
                rx.avatar(
                    src="Designer.jpeg",
                    **HeroStyle.hero_image,
                ),
                rx.heading(
                    "Marcos Ferreto Estrada",
                    **HeroStyle.hero_title,
                ),
                rx.text(
                    "Especializado en desarrollo de software, modelación matemática y análisis de datos. "
                    "Creando soluciones innovadoras con un enfoque analítico y técnico.",
                    **HeroStyle.hero_h2,
                ),
                rx.vstack(
                    rx.icon(
                        "map-pinned",
                        # _as="span",
                    ),
                    rx.text(
                        "Buenos Aires de Puntarenas, Costa Rica",
                        # _as="span",
                    ),
                    _as="span",
                    **HeroStyle.span,
                ),
                rx.hstack(
                    rx.button(
                        "Ver Proyectos",
                        # background_color=rx.color_mode_cond(
                        #    light=GlobalThemeVariables.LIGHT.value["--primary"],
                        #    dark=GlobalThemeVariables.DARK.value["--primary"],
                        # ),
                        background_color=rx.Color("accent", 11),
                        color="white",
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                        margin_right="1rem",
                    ),
                    rx.button(
                        "Descargar CV",
                        background_color="transparent",
                        border=f"1px solid {GlobalThemeVariables.LIGHT.value['--primary']}",
                        color=rx.Color("accent", 11),
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                    ),
                ),
                # width="75%",
            ),
            width="100%",
            **HeroStyle.info,
        ),
        **HeroStyle.container,
    )
