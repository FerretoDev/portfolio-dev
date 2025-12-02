from dataclasses import dataclass, field
from typing import Any

import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.styles.styles import GlobalThemeVariables
from portfolio.constants import basics

SOCIAL_ICONS: dict[str, Any] = {
    "Email": rx.icon("mail"),
    "Phone": rx.icon("phone"),
    "GitHub": rx.icon("github"),
    "LinkedIn": rx.icon("linkedin"),
    "X": rx.icon("twitter"),
}


@dataclass
class HeroStyle:
    container: dict[str, str] = field(
        default_factory=lambda: {
            "display": "flex",
            "flex-direction": "row",
            "align-items": "center",
            "justify-content": "space-between",
            "gap": "1rem",
        },
    )

    info: dict[str, dict[str, int | str] | str] = field(
        default_factory=lambda: {
            "flexDirection": "row-reverse",  # Valor por defecto (PC) | Debería usar "direction": "row-reverse" pero no me funcionaba
            "align": "center",
            # "justify": "center",
            "gap": "0.5rem",
            "padding-right": "32px",
            "@media (width <= 700px)": {
                "justify-content": "center",
                "align-items": "center",
                "padding-right": 0,
                "text-align": "center",
                "flexDirection": "column",  # Para pantallas pequeñas (Móvil)
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

    hero_image: dict[str, Any] = field(
        default_factory=lambda: {
            "box-shadow": rx.color_mode_cond(
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


def hero_section1() -> rx.Component:
    """Sección principal del hero."""
    return section_component(
        children=[
            rx.box(
                rx.avatar(
                    src="Designer.jpeg",
                    **HeroStyle.hero_image,
                ),
                rx.vstack(
                    rx.heading(
                        "Marcos Ferreto Estrada",
                        **HeroStyle.hero_title,
                    ),
                    rx.text(
                        "Especializado en desarrollo de software, modelación matemática y análisis de datos. "
                        "Creando soluciones innovadoras con un enfoque analítico y técnico.",
                        **HeroStyle.hero_h2,
                    ),
                    rx.hstack(
                        rx.icon(
                            "map-pinned",
                            # _as="span",
                        ),
                        rx.text(
                            "Buenos Aires de Puntarenas, Costa Rica",
                            _as="span",
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
                # width="100%",
                **HeroStyle.info,
            ),
        ],
        **HeroStyle.container,
    )


def hero_section() -> rx.Component:
    """Sección principal del hero."""

    # Extraemos datos del basics
    name = basics["name"]
    label = basics["label"]
    image = basics["image"]
    location = basics["location"]
    profiles = basics["profiles"]
    phone = basics["phone"]
    mail = basics["email"]

    # Fix: handle location as list, dict, or str
    if isinstance(location, list) and location and isinstance(location[0], dict):
        city = location[0].get("city", "")
        region = location[0].get("region", "")
    elif isinstance(location, dict):
        city = location.get("city", "")
        region = location.get("region", "")
    elif isinstance(location, str):
        city = location
        region = ""
    else:
        city = ""
        region = ""

    return section_component(
        children=[
            rx.flex(
                # Sección de información
                rx.box(
                    rx.heading(name, level=1, style=h1_style),
                    rx.heading(
                        label,
                        level=2,
                        style=h2_style,
                    ),
                    rx.box(
                        rx.icon("map-pin"),
                        rx.text(
                            rx.text(f"{city}, {region}"),
                            style=location_style,
                        ),
                        _as="span",
                        style=location_style,
                    ),
                    rx.box(
                        rx.hstack(
                            *[
                                rx.link(
                                    SOCIAL_ICONS.get(
                                        profile.get("network", ""), rx.icon("link")
                                    ),
                                    href=profile.get("url", "#"),
                                    style=link_style,
                                    _as="a",
                                )
                                for profile in profiles
                                if isinstance(profile, dict)
                            ],
                        ),
                        style={"margin_top": "0.5rem"},
                    ),
                    class_name="info",
                    style=info_style,
                ),
                # Figura con imagen
                rx.box(
                    rx.avatar(
                        src="Designer.jpeg",
                        alt="Marcus",
                        style=img_style,
                    ),
                    style={"margin": "0"},
                ),
                style=container_style,
            ),
        ],
    )


# Estilos definidos como diccionarios
container_style: dict[str, str] = {
    "display": "flex",
    "flex_direction": "row",
    "align_items": "center",
    "justify_content": "space-between",
    "gap": "1rem",
    "padding_top": "4.5rem",
}

info_style: dict[str, str] = {
    "display": "flex",
    "flex_direction": "column",
    "gap": "0.5rem",
    "padding_right": "32px",
}

h1_style = {
    "font_size": "2rem",
    "margin": "0",
}

h2_style = {
    "color": "#444",
    "font_weight": "500",
    "font_size": "1.1rem",
    "text_wrap": "balance",
    "margin": "0",
}

img_style = {
    "aspect_ratio": "1 / 1",
    "object_fit": "cover",
    "width": "128px",
    "height": "auto",
    "border_radius": "16px",
}

location_style = {
    "color": "#666",
    "display": "flex",
    "align_items": "center",
    "gap": "0.25rem",
    "font_size": "0.85rem",
    "letter_spacing": "-0.05rem",
}

link_style = {
    "color": "#777",
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "border": "1px solid #eee",
    "padding": "4px",
    "height": "32px",
    "width": "32px",
    "border_radius": "6px",
    "transition": "all 0.3s ease",
    "text_decoration": "none",
    "_hover": {
        "background": "#eee",
        "border": "1px solid #ddd",
    },
}
