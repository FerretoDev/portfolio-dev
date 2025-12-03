import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import (
    container_style,
    h1_style,
    h2_style,
    img_style,
    info_style,
    link_style,
    location_style,
)
from portfolio.constants import basics
from portfolio.utils.icons import SOCIAL_ICONS, map_pin_icon


def hero_section() -> rx.Component:
    """Sección principal del hero."""

    # Extraemos datos del basics
    name = basics["name"]
    label = basics["label"]
    location = basics["location"]
    profiles = basics["profiles"]

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
                        map_pin_icon(),
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
                                    icon_func(),
                                    href=profile.get("url", "#"),
                                    style=link_style,
                                    _as="a",
                                )
                                for profile in profiles
                                if isinstance(profile, dict)
                                and (
                                    icon_func := SOCIAL_ICONS.get(
                                        profile.get("network", "")
                                    )
                                )
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
