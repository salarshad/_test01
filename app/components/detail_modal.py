import reflex as rx
from app.states.api_state import APIState, Review


def detail_item(label: str, value: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.p(label, class_name="text-sm font-medium text-gray-500"),
        rx.el.p(value, class_name="text-sm text-gray-900"),
        class_name="py-2",
    )


def review_card(review: Review) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(review["reviewer_name"], class_name="font-semibold"),
            rx.el.div(
                rx.icon("star", class_name="h-4 w-4 text-yellow-400"),
                rx.el.span(review["rating"].to_string()),
                class_name="flex items-center gap-1 text-sm",
            ),
            class_name="flex justify-between items-center",
        ),
        rx.el.p(
            f'''"{review["comment"]}"''', class_name="text-sm text-gray-600 mt-1 italic"
        ),
        class_name="p-3 border rounded-lg bg-gray-50/50",
    )


def detail_modal() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title("Professional Details"),
            rx.el.div(
                rx.cond(
                    APIState.selected_professional,
                    rx.el.div(
                        detail_item("Name", APIState.selected_professional["name"]),
                        detail_item(
                            "Category", APIState.selected_professional["category"]
                        ),
                        detail_item(
                            "Description", APIState.selected_professional["description"]
                        ),
                        detail_item(
                            "Services",
                            APIState.selected_professional["services"].join(", "),
                        ),
                        detail_item(
                            "Location",
                            f"{APIState.selected_professional['location']['address']}, {APIState.selected_professional['location']['city']}, {APIState.selected_professional['location']['state']} {APIState.selected_professional['location']['zip_code']}",
                        ),
                        detail_item(
                            "Contact",
                            f"{APIState.selected_professional['contact_info']['phone']} | {APIState.selected_professional['contact_info']['email']}",
                        ),
                        rx.el.h4("Reviews", class_name="text-md font-medium mt-4 mb-2"),
                        rx.foreach(
                            APIState.selected_professional["reviews"], review_card
                        ),
                        class_name="max-h-[60vh] overflow-y-auto p-1",
                    ),
                    rx.el.p("No professional selected."),
                ),
                class_name="mt-4",
            ),
            rx.el.div(
                rx.el.button(
                    "Close",
                    on_click=APIState.close_detail_modal,
                    class_name="mt-4 px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50",
                ),
                class_name="flex justify-end",
            ),
        ),
        open=APIState.show_detail_modal,
    )