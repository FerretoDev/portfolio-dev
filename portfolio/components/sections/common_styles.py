"""Estilos comunes para las secciones del portfolio"""

# Estilos para listas
list_vertical_style = {
    "display": "flex",
    "flex_direction": "column",
    "gap": "32px",
    "list_style": "none",
    "margin": "0",
    "padding": "0",
}

# Estilos para headers de items
item_header_style = {
    "display": "flex",
    "justify_content": "space-between",
    "align_items": "flex-start",
    "margin_bottom": "4px",
}

# Estilos para fechas/tiempo
time_display_style = {
    "color": "#555",
    "font_size": "0.85rem",
    "min_width": "102px",
}

# Estilos para badges/highlights
badge_style = {
    "border_radius": "6px",
    "background": "#eee",
    "color": "#444",
    "font_size": "0.6rem",
    "font_weight": "500",
    "padding": "0.2rem 0.6rem",
}

# Estilos para items de habilidades
skill_badge_style = {
    "align_items": "center",
    "background": "#eee",
    "border_radius": "6px",
    "color": "black",
    "display": "flex",
    "font_size": "0.8rem",
    "font_weight": "500",
    "gap": "4px",
    "padding": "0.2rem 0.6rem",
}

# Estilos para artículos/cards
card_style = {
    "border_radius": "8px",
    "border": "1px solid #f2f2f2",
    "gap": "16px",
    "display": "flex",
    "flex_direction": "column",
    "padding": "16px",
    "height": "100%",
}

# Estilos para Hero Section
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

container_style = {
    "display": "flex",
    "flex_direction": "row",
    "align_items": "center",
    "justify_content": "space-between",
    "gap": "1rem",
    "padding_top": "4.5rem",
}

info_style = {
    "display": "flex",
    "flex_direction": "column",
    "gap": "0.5rem",
    "padding_right": "32px",
}

# Estilos para Projects Section
project_link_style = {
    "color": "#111",
    "text_decoration": "none",
    "_hover": {"text_decoration": "underline"},
}

active_indicator_style = {
    "color": "rgb(29, 196, 71)",
    "margin_left": "8px",
}

github_link_style = {
    "margin_left": "5px",
    "color": "#111",
    "text_decoration": "none",
    "_hover": {"opacity": "0.7"},
}

project_header_style = {
    "margin": "0 0 4px 0",
    "display": "flex",
    "align_items": "center",
    "flex_wrap": "wrap",
}

project_description_style = {
    "font_size": "0.75rem",
    "line_height": "1.2rem",
    "margin_bottom": "4px",
    "color": "#666",
}

project_highlights_container_style = {
    "display": "flex",
    "flex_wrap": "wrap",
    "gap": "4px",
    "font_size": "0.6rem",
}

projects_grid_style = {
    "display": "grid",
    "grid_template_columns": "repeat(auto-fit, minmax(200px, 1fr))",
    "gap": "1rem",
    "list_style": "none",
    "margin": "0 -16px",
    "padding": "0",
}

# Estilos para Skills Section
skill_text_style = {
    "color": "black",
    "font_size": "0.8rem",
    "font_weight": "500",
}

skills_list_style = {
    "display": "inline-flex",
    "gap": "8px",
    "flex_wrap": "wrap",
    "list_style": "none",
    "margin": "0",
    "padding": "0",
}
