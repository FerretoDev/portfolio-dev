import reflex as rx


def text(text: str) -> rx.Component:
    return rx.text(
        text,
        style={
            "color": "#555",
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
        },
    )
