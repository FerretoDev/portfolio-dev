import reflex as rx

def social_link(social_title: str, link:str)-> rx.Component:
    return rx.hstack(
        rx.link(social_title,href=link),
    )