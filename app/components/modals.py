import reflex as rx
from app.states.api_state import APIState, Review


def form_field(
    label: str,
    value: rx.Var,
    on_change: rx.event.EventHandler,
    placeholder: str = "",
    field_type: str = "text",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium"),
        rx.el.input(
            type=field_type,
            default_value=value,
            on_change=on_change,
            placeholder=placeholder,
            class_name="w-full rounded-md border px-3 py-2 text-sm mt-1 bg-white",
        ),
        class_name="mb-4",
    )


def list_manager(
    title: str,
    items: rx.Var,
    add_handler: rx.event.EventHandler,
    remove_handler_factory: rx.event.EventHandler,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(title, class_name="text-sm font-medium"),
        rx.foreach(
            items,
            lambda item, index: rx.el.div(
                rx.el.input(
                    placeholder=f"Enter {title.lower().rstrip('s')}...",
                    class_name="flex-1 rounded-md border px-3 py-2 text-sm bg-white",
                    default_value=item,
                    key=item,
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4"),
                    on_click=lambda: remove_handler_factory(index),
                    class_name="p-2 text-red-500 hover:bg-red-50 rounded-md",
                ),
                class_name="flex items-center gap-2 mt-2",
            ),
        ),
        rx.el.button(
            f"Add {title.rstrip('s')}",
            on_click=add_handler,
            class_name="mt-2 px-3 py-1 text-sm rounded-md border bg-gray-50 hover:bg-gray-100",
        ),
        class_name="mb-4 p-3 border rounded-lg bg-gray-50/50",
    )


def edit_modal() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title("Edit Professional"),
            rx.radix.primitives.dialog.description(
                "Update the professional's details below.", class_name="mb-4"
            ),
            form_field(
                "Name",
                APIState.edit_form["name"],
                lambda v: APIState.update_edit_form("name", v),
            ),
            form_field(
                "Category",
                APIState.edit_form["category"],
                lambda v: APIState.update_edit_form("category", v),
            ),
            form_field(
                "Description",
                APIState.edit_form["description"],
                lambda v: APIState.update_edit_form("description", v),
            ),
            list_manager(
                "Services",
                APIState.edit_form["services"],
                APIState.add_service_to_edit,
                APIState.remove_service_from_edit,
            ),
            list_manager(
                "Image URLs",
                APIState.edit_form["image_urls"],
                APIState.add_image_url_to_edit,
                APIState.remove_image_url_from_edit,
            ),
            rx.el.div(
                form_field(
                    "Address",
                    APIState.edit_form["location"]["address"],
                    lambda v: APIState.update_edit_form("location.address", v),
                ),
                form_field(
                    "City",
                    APIState.edit_form["location"]["city"],
                    lambda v: APIState.update_edit_form("location.city", v),
                ),
                form_field(
                    "State",
                    APIState.edit_form["location"]["state"],
                    lambda v: APIState.update_edit_form("location.state", v),
                ),
                form_field(
                    "Zip Code",
                    APIState.edit_form["location"]["zip_code"],
                    lambda v: APIState.update_edit_form("location.zip_code", v),
                ),
                class_name="grid grid-cols-2 gap-4",
            ),
            rx.el.div(
                rx.el.button(
                    "Cancel",
                    on_click=APIState.close_edit_modal,
                    class_name="px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50",
                ),
                rx.el.button(
                    "Save Changes",
                    on_click=APIState.save_professional,
                    class_name="px-4 py-2 text-sm rounded-md bg-blue-600 text-white hover:bg-blue-700",
                ),
                class_name="flex justify-end gap-3 mt-4",
            ),
        ),
        open=APIState.show_edit_modal,
    )


def add_modal() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title("Add New Professional"),
            rx.radix.primitives.dialog.description(
                "Fill in the details for the new professional below.", class_name="mb-4"
            ),
            form_field(
                "Name",
                APIState.add_form["name"],
                lambda v: APIState.update_add_form("name", v),
            ),
            form_field(
                "Category",
                APIState.add_form["category"],
                lambda v: APIState.update_add_form("category", v),
            ),
            rx.el.div(
                rx.el.button(
                    "Cancel",
                    on_click=APIState.close_add_modal,
                    class_name="px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50",
                ),
                rx.el.button(
                    "Add Professional",
                    on_click=APIState.add_professional,
                    class_name="px-4 py-2 text-sm rounded-md bg-blue-600 text-white hover:bg-blue-700",
                ),
                class_name="flex justify-end gap-3 mt-4",
            ),
        ),
        open=APIState.show_add_modal,
    )