"""Estilos comunes para las secciones del portfolio"""

import reflex as rx

# Breakpoints para responsive design
BREAKPOINTS = {
    "mobile": "640px",  # Smartphones
    "tablet": "768px",  # Tablets
    "desktop": "1024px",  # Laptops/Desktop
}

# Estilos para listas
list_vertical_style = {
    "display": "flex",
    "flex_direction": "column",
    "gap": "32px",
    "list_style": "none",
    "margin": "0",
    "padding": "0",
    "@media (max-width: 640px)": {
        "gap": "24px",  # Menos espacio en móvil
    },
}

# Estilos para headers de items
item_header_style = {
    "display": "flex",
    "justify_content": "space-between",
    "align_items": "flex-start",
    "margin_bottom": "4px",
    "gap": "8px",
    "@media (max-width: 640px)": {
        "flex_direction": "column",
        "gap": "4px",
    },
}

# Estilos para fechas/tiempo
time_display_style = {
    "color": rx.color_mode_cond(light="#64748b", dark="#94a3b8"),
    "cursor": "default",
    "font_size": "0.85rem",
    "min_width": "102px",
    "@media (max-width: 640px)": {
        "font_size": "0.75rem",
        "min_width": "auto",
    },
}

# Estilos para badges/highlights
badge_style = {
    "border_radius": "6px",
    "background": rx.color_mode_cond(light="#f3f4f6", dark="#1f2937"),
    "color": rx.color_mode_cond(light="#475569", dark="#94a3b8"),
    "font_size": "0.6rem",
    "font_weight": "500",
    "padding": "0.2rem 0.6rem",
    "@media (max-width: 640px)": {
        "font_size": "0.55rem",
        "padding": "0.15rem 0.5rem",
    },
}

# Estilos para items de habilidades
skill_badge_style = {
    "align_items": "center",
    "background": rx.color_mode_cond(light="#f3f4f6", dark="#1f2937"),
    "border_radius": "6px",
    "color": rx.color_mode_cond(light="#111111", dark="#f9fafb"),
    "display": "flex",
    "font_size": "0.8rem",
    "font_weight": "500",
    "gap": "4px",
    "padding": "0.2rem 0.6rem",
    "@media (max-width: 640px)": {
        "font_size": "0.7rem",
        "padding": "0.15rem 0.5rem",
    },
}

# Estilos para artículos/cards
card_style = {
    "border_radius": "8px",
    "background": rx.color_mode_cond(light="#ffffff", dark="#0f172a"),
    "border": rx.color_mode_cond(light="1px solid #f3f4f6", dark="1px solid #1f2937"),
    "box_shadow": rx.color_mode_cond(light="0 1px 4px rgba(0,0,0,0.06)", dark="none"),
    "gap": "16px",
    "display": "flex",
    "flex_direction": "column",
    "padding": "16px",
    "height": "100%",
    "@media (max-width: 640px)": {
        "padding": "12px",
        "gap": "12px",
    },
}

# Estilos para componentes helpers
item_title_style = {
    "font_weight": "600",
    "color": rx.color_mode_cond(light="#111111", dark="#f9fafb"),
    "margin": "0",
    "transition": "color 0.2s ease",
    "_hover": {
        "color": rx.color_mode_cond(light="#0096c7", dark="#48cae4"),
    },
}

item_subtitle_style = {
    "color": rx.color_mode_cond(light="#475569", dark="#94a3b8"),
    "font_weight": "400",
    "margin": "0",
}

date_box_style = {
    "display": "flex",
    "align_items": "center",
    "color": rx.color_mode_cond(light="#718096", dark="#94a3b8"),
}

item_link_style = {
    "color": rx.color_mode_cond(light="#111111", dark="#f9fafb"),
    "text_decoration": "none",
    "_hover": {
        "text_decoration": "underline",
        "color": rx.color_mode_cond(light="#0096c7", dark="#48cae4"),
    },
}

item_text_style = {
    "color": rx.color_mode_cond(light="#111111", dark="#f9fafb"),
}

# Estilos para Hero Section
h1_style = {
    "font_size": "2rem",
    "margin": "0",
    "@media (max-width: 768px)": {
        "font_size": "1.75rem",
    },
    "@media (max-width: 640px)": {
        "font_size": "1.5rem",
        "text_align": "center",
    },
}

h2_style = {
    "color": rx.color_mode_cond(light="#475569", dark="#94a3b8"),
    "font_weight": "500",
    "font_size": "1.1rem",
    "text_wrap": "balance",
    "margin": "0",
    "@media (max-width: 768px)": {
        "font_size": "1rem",
    },
    "@media (max-width: 640px)": {
        "font_size": "0.9rem",
        "text_align": "center",
    },
}

img_style = {
    "aspect_ratio": "1 / 1",
    "object_fit": "cover",
    "width": "128px",
    "height": "auto",
    "border_radius": "16px",
    "@media (max-width: 768px)": {
        "width": "112px",
    },
    "@media (max-width: 640px)": {
        "width": "96px",
    },
}

location_style = {
    "color": rx.color_mode_cond(light="#64748b", dark="#94a3b8"),
    "display": "flex",
    "align_items": "center",
    "gap": "0.25rem",
    "font_size": "0.85rem",
    "letter_spacing": "-0.05rem",
    "@media (max-width: 640px)": {
        "font_size": "0.75rem",
        "justify_content": "center",
    },
}

link_style = {
    "color": rx.color_mode_cond(light="#64748b", dark="#94a3b8"),
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "border": rx.color_mode_cond(light="1px solid #e5e7eb", dark="1px solid #374151"),
    "padding": "4px",
    "height": "32px",
    "width": "32px",
    "border_radius": "6px",
    "transition": "all 0.3s ease",
    "text_decoration": "none",
    "_hover": {
        "background": rx.color_mode_cond(light="#f3f4f6", dark="#1f2937"),
        "border": rx.color_mode_cond(
            light="1px solid #d1d5db", dark="1px solid #374151"
        ),
        "color": rx.color_mode_cond(light="#0096c7", dark="#48cae4"),
        "transform": "translateY(-2px)",
    },
    "@media (max-width: 640px)": {
        "height": "36px",  # Más grande para táctil
        "width": "36px",
    },
}

container_style = {
    "display": "flex",
    "flex_direction": "row",
    "align_items": "center",
    "justify_content": "space-between",
    "gap": "1rem",
    "padding_top": "4.5rem",
    "@media (max-width: 768px)": {
        "padding_top": "3.5rem",
        "gap": "0.75rem",
    },
    "@media (max-width: 640px)": {
        "flex_direction": "column-reverse",
        "padding_top": "2.5rem",
        "gap": "1rem",
        "text_align": "center",
    },
}

info_style = {
    "display": "flex",
    "flex_direction": "column",
    "gap": "0.5rem",
    "padding_right": "32px",
    "@media (max-width: 768px)": {
        "padding_right": "16px",
    },
    "@media (max-width: 640px)": {
        "padding_right": "0",
        "align_items": "center",
        "width": "100%",
    },
}

social_links_wrapper_style = {
    "margin_top": "0.5rem",
}

avatar_wrapper_style = {
    "margin": "0",
}

# Estilos para Projects Section
project_link_style = {
    "color": rx.color_mode_cond(light="#111111", dark="#f9fafb"),
    "font_weight": "500",
    "text_decoration": "none",
    "transition": "color 0.2s ease",
    "_hover": {
        "text_decoration": "underline",
        "color": rx.color_mode_cond(light="#0096c7", dark="#48cae4"),
    },
    "@media (max-width: 640px)": {
        "font_size": "0.95rem",
    },
}

active_indicator_style = {
    "color": "rgb(29, 196, 71)",
    "margin_left": "8px",
    "font_size": "1rem",
}

github_link_style = {
    "margin_left": "5px",
    "color": rx.color_mode_cond(light="#64748b", dark="#94a3b8"),
    "text_decoration": "none",
    "transition": "color 0.2s ease",
    "_hover": {
        "color": rx.color_mode_cond(light="#0096c7", dark="#48cae4"),
        "opacity": "1",
    },
    # Área táctil más grande en móvil
    "@media (max-width: 640px)": {
        "padding": "4px",
        "margin_left": "8px",
    },
}

project_header_style = {
    "margin": "0 0 8px 0",
    "display": "flex",
    "align_items": "center",
    "flex_wrap": "wrap",
    "gap": "4px",
    "@media (max-width: 640px)": {
        "margin": "0 0 6px 0",
    },
}

project_description_style = {
    "font_size": "0.75rem",
    "line_height": "1.2rem",
    "margin_bottom": "4px",
    "color": rx.color_mode_cond(light="#64748b", dark="#94a3b8"),
    "@media (max-width: 640px)": {
        "font_size": "0.7rem",
        "line_height": "1.1rem",
    },
}

project_highlights_container_style = {
    "display": "flex",
    "flex_wrap": "wrap",
    "gap": "4px",
    "font_size": "0.6rem",
}

project_content_style = {
    "flex": "1",
}

projects_grid_style = {
    "display": "grid",
    "grid_template_columns": "repeat(auto-fit, minmax(200px, 1fr))",
    "gap": "1rem",
    "list_style": "none",
    "margin": "0 -16px",
    "padding": "0",
    "@media (max-width: 768px)": {
        "grid_template_columns": "repeat(auto-fit, minmax(180px, 1fr))",
        "margin": "0 -8px",
        "gap": "0.75rem",
    },
    "@media (max-width: 640px)": {
        "grid_template_columns": "1fr",
        "margin": "0",
        "gap": "0.5rem",
    },
}

# Estilos para Skills Section
skill_text_style = {
    "color": rx.color_mode_cond(light="#111111", dark="#f9fafb"),
    "font_size": "0.8rem",
    "font_weight": "500",
    "@media (max-width: 640px)": {
        "font_size": "0.7rem",
    },
}

skills_list_style = {
    "display": "inline-flex",
    "gap": "8px",
    "flex_wrap": "wrap",
    "list_style": "none",
    "margin": "0",
    "padding": "0",
    "@media (max-width: 640px)": {
        "gap": "6px",
        "justify_content": "center",
    },
}
