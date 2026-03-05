from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Literal

import reflex as rx
from reflex.constants.colors import Color


# VARIABLES GLOBALES
class GlobalThemeVariables(Enum):
    # Dark Theme
    DARK = {
        "--background": "#0a0a0a",  # Fondo principal oscuro
        "--foreground": "#ffffff",  # Color de texto principal oscuro
        "--primary": "#00b4d8",  # Mismo primario para consistencia
        "--secondary": "#0077b6",  # Mismo secundario para consistencia
        "--accent": "#90e0ef",  # Mismo acento para consistencia
        "--glass-background": "rgba(255, 255, 255, 0.05)",  # Fondo glass oscuro
        "--glass-border": "rgba(255, 255, 255, 0.1)",  # Borde glass oscuro
    }
    # Light Theme
    LIGHT = {
        "--background": "#f0f4f8",  # Fondo principal claro
        "--foreground": "#1a202c",  # Color de texto principal claro
        "--primary": "#00b4d8",  # Color primario (botones, acentos)
        "--secondary": "#0077b6",  # Color secundario (hover, detalles)
        "--accent": "#90e0ef",  # Color de acento complementario
        "--glass-background": "rgba(255, 255, 255, 0.1)",  # Fondo glass
        "--glass-border": "rgba(255, 255, 255, 0.2)",  # Borde glass
    }

    # Estilos base
    BASE_STYLE = {
        "font_family": "Inter, sans-serif",  # Fuente principal
        "transition": "all 0.3s ease",  # Transiciones suaves globales
    }

    # Estilos de vidrio (glassmorphism)
    GLASS_STYLE = {
        "backdrop_filter": "blur(10px)",  # Efecto de desenfoque
        "border_radius": "10px",  # Bordes redondeados
        "transition": "background-color 0.3s ease, border-color 0.3s ease",
    }


# Estilos globales
def global_style() -> Any:
    return {
        # CSS Global como componente de estilo
        "html": {
            "scroll_behavior": "smooth",  # Scroll suave para navegación
        },
        "body": {
            "margin": "0",
            "padding": "0",
            "font_family": "Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        },
        "figure": {
            "margin": "0",
            "padding": "0",
        },
        "a": {
            "text_decoration": "none",
        },
        "ul": {
            "list_style": "none",
            "margin": "0",
            "padding": "0",
        },
        "*, *::before, *::after": {
            "box_sizing": "border_box",
        },
        "h1, h2, h3, h4": {
            "margin": "0",
            "font_family": "inherit",
        },
        "p": {
            "color": "#64748b",
            "font_size": "0.9rem",
            "line_height": "1.5",
            "margin": "0",
            "text_wrap": "pretty",
        },
        # Dark mode para p global (CSS puro, no acepta rx.color_mode_cond)
        ".dark p": {
            "color": "#94a3b8",
        },
        # Responsive typography
        "@media (max-width: 768px)": {
            "p": {
                "font_size": "0.85rem",
            },
            "h1": {
                "font_size": "1.75rem",
            },
            "h2": {
                "font_size": "1.5rem",
            },
        },
        "@media (max-width: 640px)": {
            "p": {
                "font_size": "0.8rem",
            },
            "h1": {
                "font_size": "1.5rem",
            },
            "h2": {
                "font_size": "1.25rem",
            },
        },
    }


"""
The CardStyle
"""


def color(shade: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) -> Color:
    return rx.color("slate", shade)


TextShared: dict[str, str] = {"size": "2", "weight": "bold"}


@dataclass
class CardStyle:
    base: dict[str, str | Color] = field(
        default_factory=lambda: {
            "align": "start",
            "justify": "start",
            "position": "relative",
            "width": "100%",
            "max_width": "320px",
            "height": "200px",
            "border": f"1px solid {rx.color('gray', 6)}",
            "bg": rx.color("gray", 3),
            "border_radius": "12px",
            "padding": "16px",
            "overflow": "hidden",
            "z_index": "30",
            "box_shadow": "0px 6px 12px 0px rgba(0, 0, 0, 0.05)",
        },
    )

    icon: dict[str, str | int] = field(
        default_factory=lambda: {
            "size": 21,
            "position": "absolute",
            "bottom": "16px",
            "right": "16px",
        },
    )

    stack: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "spacing": "1",
            "align": "start",
            "justify": "start",
            "text_align": "start",
        },
    )

    background: dict[str, str] = field(
        default_factory=lambda: {
            "background_size": "16px 16px",
            "background_image": f"radial-gradient(circle, {rx.color('gray', 12)} 1px, transparent 1px)",
            "mask": "radial-gradient(100% 100% at 100% 100%, hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
            "width": "100%",
            "height": "100%",
            "position": "absolute",
        },
    )

    title: dict[str, str | Color] = field(
        default_factory=lambda: {"color": color(12), **TextShared},
    )

    description: dict[str, str | Color] = field(
        default_factory=lambda: {"color": color(11), **TextShared},
    )


card_style: CardStyle = CardStyle()

"""
The FooterStyle
"""


active: Color = rx.color("slate", 12)
passive: Color = rx.color("slate", 10)


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
The NavbarStyle
"""


@dataclass
class NavbarStyle:
    navigation: dict[str, Any] = field(
        default_factory=lambda: {
            "display": "grid",
            "grid-template-columns": "repeat(auto - fit, minmax(300px, 1fr))",
            "gap": "1rem",
            "position": "fixed",
            "width": "100%",
            "top": "0px",
            "z_index": "1000",
            "backdrop_filter": "blur(10px)",
            "background": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--background"],
                dark=GlobalThemeVariables.DARK.value["--background"],
            ),
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "10em",
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


navbar_style: NavbarStyle = NavbarStyle()


"""
The HeaderStyle
"""


@dataclass
class HeaderStyle:
    base: dict[str, str | Any] = field(
        default_factory=lambda: {
            "position": "fixed",
            "width": "100%",
            "top": "0px",
            "z_index": "999",
            "backdrop_filter": "blur(10px)",  # Aplica desenfoque
            "border_bottom": rx.color_mode_cond(
                light="1px solid rgba(0,0,0,0.1)",
                dark="1px solid rgba(255,255,255,0.1)",
            ),
            "display": "flex",
            "flex_wrap": "wrap",
            "justify_content": "space-between",
            "align_items": "center",
        },
    )

    content: dict[str, str | Any] = field(
        default_factory=lambda: {
            "bg": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--glass-background"],
                dark=GlobalThemeVariables.DARK.value["--glass-background"],
            ),
            "padding": "0.8rem",
            "z_index": "1000",
            "width": "100%",
        },
    )


header_style: HeaderStyle = HeaderStyle()


"""
The LayoutStyle
"""


@dataclass
class LayoutStyle:
    base: dict[str, str | dict] = field(
        default_factory=lambda: {
            "padding": "4rem",
            "margin": "auto",
            "width": "100%",
            "max_width": "800px",
            "@media (max-width: 1024px)": {
                "padding": "3rem",
                "max_width": "100%",
            },
            "@media (max-width: 768px)": {
                "padding": "2rem",
            },
            "@media (max-width: 640px)": {
                "padding": "1rem",
            },
        }
    )


layout_style: LayoutStyle = LayoutStyle()

"""
The PageStyle
"""


@dataclass
class PageStyle:
    background: dict[str, Any] = field(
        default_factory=lambda: {
            "transition": "background 0.3s ease, color 0.3s ease",
            "background": rx.color_mode_cond(
                light="linear-gradient(to bottom right, #E2E8F0, #CBD5E0)",
                dark="linear-gradient(to bottom right, #111827, #1F2937)",
            ),
            # "width": "100%",
        }
    )


page_style: PageStyle = PageStyle()


"""
The SectionStyle
"""


@dataclass
class SectionStyle:
    # Estilos base para la sección
    section_style: dict[str, str | dict] = field(
        default_factory=lambda: {
            "max_width": "700px",
            "margin": "0 auto 48px",
            "@media (max-width: 768px)": {
                "margin": "0 auto 38px",
                "max_width": "100%",
            },
            "@media (max-width: 640px)": {
                "margin": "0 auto 28px",
            },
        }
    )
    # Estilos para el título
    title_style: dict[str, str | dict] = field(
        default_factory=lambda: {
            "level": "2",
            "margin_bottom": "8px",
            "font_weight": "700",
            "line_height": "1.5",
            "font_size": "1.5rem",
            "@media (max-width: 768px)": {
                "font_size": "1.35rem",
            },
            "@media (max-width: 640px)": {
                "font_size": "1.25rem",
                "margin_bottom": "6px",
            },
        }
    )


section_style: SectionStyle = SectionStyle()


"""
Text Component Styles
"""


@dataclass
class TextStyle:
    # Estilos para texto de párrafo
    paragraph: dict[str, Any] = field(
        default_factory=lambda: {
            "color": rx.color_mode_cond(light="#475569", dark="#94a3b8"),
            "font_size": "1rem",
            "line_height": "1.6",
            "margin_bottom": "0.75rem",
            "text_align": "justify",
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
    "color": rx.color_mode_cond(light="#64748b", dark="#94a3b8"),
    "@media (max-width: 640px)": {
        "font_size": "0.75rem",
        "text_align": "center",
    },
}
