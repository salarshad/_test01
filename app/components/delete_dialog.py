import reflex as rx
from app.states.api_state import APIState


def delete_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title("Confirm Deletion"),
            rx.radix.primitives.dialog.description(
                "Are you sure you want to delete this professional? This action cannot be undone.",
                class_name="my-4",
            ),
            rx.el.div(
                rx.el.button(
                    "Cancel",
                    on_click=APIState.close_delete_dialog,
                    class_name="px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50",
                ),
                rx.el.button(
                    "Delete",
                    on_click=APIState.delete_professional,
                    class_name="px-4 py-2 text-sm rounded-md bg-red-600 text-white hover:bg-red-700",
                ),
                class_name="flex justify-end gap-3",
            ),
        ),
        open=APIState.show_delete_dialog,
    )