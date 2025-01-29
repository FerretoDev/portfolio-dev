import reflex as rx

def custom_button(text: str, link: str)-> rx.Component:
    return rx.link(
        rx.button(text, bg="blue.500", color="white", border_radius="2"),
        href=link,
    )