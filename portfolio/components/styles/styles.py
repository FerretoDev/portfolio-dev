from dataclasses import dataclass, field
from typing import Any

import reflex as rx
from reflex.constants.colors import Color

"""
The FooterStyle
"""


active: Color = rx.color("slate", 12)


@dataclass
class FooterStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "20vh",
            "align": "center",
            "justify": "center",
            "padding": "0em 1em",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "35em",
            "justify": "between",
            "align": "center",
            "padding": "1em 0em",
        },
    )
    link: dict[str, str | Color] = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "weight": "medium",
            "size": "2",
        },
    )
    brand: dict[str, str | Color] = field(
        default_factory=lambda: {"color": active, "size": "2"},
    )


footer_style: FooterStyle = FooterStyle()


"""
Text Component Styles
"""


@dataclass
class TextStyle:
    # Estilos para texto de párrafo
    paragraph: dict[str, Any] = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "font_size": "1rem",
            "line_height": "1.6",
            "margin_bottom": "0.75rem",
            "@media (max-width: 768px)": {
                "font_size": "0.95rem",
                "line_height": "1.55",
            },
            "@media (max-width: 640px)": {
                "font_size": "0.9rem",
                "line_height": "1.5",
                "text_align": "left",
            },
        }
    )


text_style: TextStyle = TextStyle()


"""
Section Component Styles
"""


# Estilos para el componente section
section_box_style: dict[str, str | dict] = {
    "max_width": "800px",
    "margin": "0 auto 48px",
    "padding": "0 1rem",
    "scroll_margin_top": "80px",
    "@media (max-width: 768px)": {
        "margin_bottom": "38px",
        "padding": "0 0.5rem",
    },
    "@media (max-width: 640px)": {
        "margin_bottom": "28px",
        "padding": "0",
    },
}

section_title_style: dict[str, Any] = {
    "margin_bottom": "16px",
    "font_weight": "700",
    "line_height": "1.3",
    "font_size": "1.75rem",
    "@media (max-width: 768px)": {
        "font_size": "1.5rem",
        "margin_bottom": "12px",
    },
    "@media (max-width: 640px)": {
        "font_size": "1.35rem",
        "margin_bottom": "10px",
    },
}


"""
Layout Styles
"""


layout_box_style: dict[str, str | dict] = {
    "letter_spacing": "-0.025rem",
    "margin": "0 auto",
    "padding": "0 2rem",
    "max_width": "1200px",
    "width": "100%",
    "@media (max-width: 768px)": {
        "padding": "0 1.5rem",
    },
    "@media (max-width: 640px)": {
        "padding": "0 1rem",
    },
}


"""
Footer Styles
"""


footer_container_style: dict[str, str | dict] = {
    "@media (max-width: 640px)": {
        "padding_y": "2rem",
    },
}

footer_copyright_style: dict[str, Any] = {
    "font_size": "0.875rem",
    "color": rx.color("slate", 11),
    "@media (max-width: 640px)": {
        "font_size": "0.75rem",
        "text_align": "center",
    },
}
