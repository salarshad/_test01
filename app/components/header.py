import reflex as rx
from app.states.api_state import APIState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon("menu", class_name="h-6 w-6"),
                on_click=APIState.toggle_sidebar,
                class_name="md:hidden",
            ),
            class_name="flex items-center gap-4 md:ml-auto md:gap-2 lg:gap-4",
        ),
        rx.el.div(class_name="w-full flex-1"),
        rx.el.div(
            rx.image(
                src=f"https://api.dicebear.com/9.x/notionists/svg?seed=Admin",
                class_name="h-8 w-8 rounded-full",
            )
        ),
        class_name="flex items-center h-16 border-b px-4 md:px-6 bg-white gap-4",
    )