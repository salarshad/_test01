import reflex as rx
from app.states.api_state import APIState, Review
from app.components.sidebar import sidebar
from app.components.header import header


def detail_item_view(label: str, value: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.p(label, class_name="text-sm font-medium text-gray-500"),
        rx.el.p(value, class_name="text-base text-gray-900 mt-1"),
        class_name="py-3",
    )


def detail_item_edit(
    label: str, value: rx.Var, on_change: rx.event.EventHandler
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium text-gray-500"),
        rx.el.input(
            default_value=value,
            on_change=on_change,
            class_name="w-full mt-1 rounded-md border px-3 py-2 text-sm bg-white",
        ),
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
            f'"{{review["comment"]}}"', class_name="text-sm text-gray-600 mt-1 italic"
        ),
        class_name="p-3 border rounded-lg bg-gray-50/50",
    )


def professional_detail_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-4 w-4 mr-2"),
                "Back to Professionals",
                href="/professionals",
                class_name="inline-flex items-center text-sm font-medium text-blue-600 hover:underline",
            ),
            rx.cond(
                APIState.is_editing_detail,
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        on_click=APIState.cancel_edit_detail,
                        class_name="px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50",
                    ),
                    rx.el.button(
                        "Update Professional",
                        on_click=APIState.save_professional,
                        class_name="px-4 py-2 text-sm rounded-md bg-blue-600 text-white hover:bg-blue-700",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.button(
                    rx.icon("pencil", class_name="h-4 w-4 mr-2"),
                    "Edit Professional",
                    on_click=APIState.toggle_edit_detail,
                    class_name="inline-flex items-center px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50",
                ),
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.cond(
            APIState.detail_loading,
            rx.el.div(
                rx.el.p("Loading professional details..."),
                class_name="flex items-center justify-center h-64",
            ),
            rx.cond(
                APIState.edit_form.contains("id"),
                rx.el.div(
                    rx.cond(
                        APIState.is_editing_detail,
                        rx.el.div(
                            detail_item_edit(
                                "Name",
                                APIState.edit_form["name"],
                                lambda v: APIState.update_edit_form("name", v),
                            ),
                            detail_item_edit(
                                "Category",
                                APIState.edit_form["category"],
                                lambda v: APIState.update_edit_form("category", v),
                            ),
                            detail_item_edit(
                                "Description",
                                APIState.edit_form["description"],
                                lambda v: APIState.update_edit_form("description", v),
                            ),
                        ),
                        rx.el.div(
                            rx.el.h1(
                                APIState.edit_form["name"],
                                class_name="text-3xl font-bold mb-2",
                            ),
                            rx.el.p(
                                APIState.edit_form["category"],
                                class_name="text-md text-gray-500 mb-6",
                            ),
                        ),
                    ),
                    rx.cond(
                        APIState.is_editing_detail,
                        rx.el.div(),
                        rx.el.div(
                            detail_item_view(
                                "Description", APIState.edit_form["description"]
                            ),
                            detail_item_view(
                                "Services", APIState.edit_form["services"].join(", ")
                            ),
                            detail_item_view(
                                "Location",
                                f"{APIState.edit_form['location']['address']}, {APIState.edit_form['location']['city']}, {APIState.edit_form['location']['state']} {APIState.edit_form['location']['zip_code']}",
                            ),
                            detail_item_view(
                                "Contact",
                                f"{APIState.edit_form['contact_info']['phone']} | {APIState.edit_form['contact_info']['email']}",
                            ),
                            class_name="grid md:grid-cols-2 gap-x-8 gap-y-4 mt-6",
                        ),
                    ),
                    rx.el.h2("Reviews", class_name="text-2xl font-semibold mt-8 mb-4"),
                    rx.el.div(
                        rx.foreach(APIState.edit_form["reviews"], review_card),
                        class_name="space-y-4",
                    ),
                    class_name="bg-white p-8 rounded-xl border shadow-sm",
                ),
                rx.el.div(
                    rx.el.p("Professional not found."),
                    class_name="flex items-center justify-center h-64",
                ),
            ),
        ),
    )


def professional_detail_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            rx.el.main(professional_detail_content(), class_name="p-6"),
            class_name="flex flex-col flex-1",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr] font-['Montserrat'] bg-gray-50",
    )