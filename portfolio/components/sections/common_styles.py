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
    "color": rx.color("slate", 11),
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
    "display": "inline-flex",
    "align_items": "center",
    "border_radius": "6px",
    "background": rx.color("slate", 3),
    "color": rx.color("slate", 11),
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
    "background": rx.color("slate", 3),
    "border_radius": "6px",
    "color": rx.color("slate", 12),
    "display": "flex",
    "flex_direction": "row",
    "font_size": "0.85rem",
    "font_weight": "500",
    "gap": "6px",
    "padding": "0.4rem 0.8rem",
    "@media (max-width: 640px)": {
        "font_size": "0.75rem",
        "padding": "0.3rem 0.6rem",
    },
}

# Estilos para artículos/cards
card_style = {
    "border_radius": "8px",
    "background": rx.color("slate", 1),
    "border": f"1px solid {rx.color('slate', 4)}",
    "box_shadow": f"0 1px 4px {rx.color('slate', 4, True)}",
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
    "color": rx.color("slate", 12),
    "margin": "0",
    "transition": "color 0.2s ease",
    "_hover": {
        "color": rx.color("accent", 10),
    },
}

item_subtitle_style = {
    "color": rx.color("slate", 11),
    "display": "block",
    "font_weight": "400",
    "margin": "0",
}

date_box_style = {
    "display": "flex",
    "align_items": "center",
    "color": rx.color("slate", 11),
}

item_link_style = {
    "color": rx.color("slate", 12),
    "text_decoration": "none",
    "_hover": {
        "text_decoration": "underline",
        "color": rx.color("accent", 10),
    },
}

item_text_style = {
    "color": rx.color("slate", 12),
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
    "color": rx.color("slate", 12),
    "font_weight": "500",
    "font_size": "1.2rem",
    "text_wrap": "balance",
    "margin": "0",
    "margin_bottom": "0.25rem",
    "@media (max-width: 768px)": {
        "font_size": "1.1rem",
    },
    "@media (max-width: 640px)": {
        "font_size": "1rem",
        "text_align": "center",
    },
}

hero_des_style = {
    "color": rx.color("slate", 11),
    "font_weight": "400",
    "font_size": "1rem",
    "text_wrap": "balance",
    "line_height": "1.5",
    "margin": "0",
    "@media (max-width: 768px)": {
        "font_size": "0.95rem",
    },
    "@media (max-width: 640px)": {
        "font_size": "0.9rem",
        "text_align": "center",
    },
}

img_style = {
    "aspect_ratio": "1 / 1",
    "object_fit": "cover",
    "width": "220px",
    "height": "auto",
    "border_radius": "16px",
    "background_color": "white",
    "box_shadow": f"0 4px 14px {rx.color('slate', 6, True)}",
    "padding": "4px",
    "@media (max-width: 768px)": {
        "width": "180px",
    },
    "@media (max-width: 640px)": {
        "width": "120px",
    },
}

location_style = {
    "color": rx.color("slate", 11),
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
    "color": rx.color("slate", 11),
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "border": f"1px solid {rx.color('slate', 6)}",
    "padding": "6px",
    "height": "38px",
    "width": "38px",
    "border_radius": "8px",
    "transition": "all 0.3s ease",
    "text_decoration": "none",
    "_hover": {
        "background": rx.color("slate", 3),
        "border": f"1px solid {rx.color('slate', 7)}",
        "color": rx.color("accent", 10),
        "transform": "translateY(-2px)",
    },
    "@media (max-width: 640px)": {
        "height": "42px",  # Más grande para táctil
        "width": "42px",
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
    "flex": "1",
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
    "flex_shrink": "0",
}

# Estilos para Projects Section
project_link_style = {
    "color": rx.color("slate", 12),
    "font_weight": "500",
    "text_decoration": "none",
    "transition": "color 0.2s ease",
    "_hover": {
        "text_decoration": "underline",
        "color": rx.color("accent", 10),
    },
    "@media (max-width: 640px)": {
        "font_size": "0.95rem",
    },
}


github_link_style = {
    "margin_left": "5px",
    "color": rx.color("slate", 11),
    "text_decoration": "none",
    "transition": "color 0.2s ease",
    "_hover": {
        "color": rx.color("accent", 10),
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
    "color": rx.color("slate", 11),
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
    "color": rx.color("slate", 12),
    "font_size": "0.8rem",
    "font_weight": "500",
    "@media (max-width: 640px)": {
        "font_size": "0.7rem",
    },
}

skills_list_style = {
    "display": "flex",
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

skills_container_style = {
    "display": "flex",
    "flex_direction": "column",
    "gap": "20px",
    "width": "100%",
    "@media (max-width: 640px)": {
        "gap": "16px",
    },
}

skill_category_style = {
    "display": "flex",
    "flex_direction": "column",
    "gap": "10px",
    "@media (max-width: 640px)": {
        "gap": "8px",
        "align_items": "center",
    },
}

skill_category_title_style = {
    "color": rx.color("slate", 11),
    "font_size": "1rem",
    "font_weight": "600",
    "margin": "0",
    "@media (max-width: 640px)": {
        "font_size": "0.9rem",
        "text_align": "center",
    },
}
