import reflex as rx
from app.states.api_state import APIState, Review
from app.components.sidebar import sidebar
from app.components.header import header


def detail_item(label: str, value: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.p(label, class_name="text-sm font-medium text-gray-500"),
        rx.el.p(value, class_name="text-base text-gray-900"),
        class_name="py-3",
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
        rx.el.a(
            rx.icon("arrow-left", class_name="h-4 w-4 mr-2"),
            "Back to Professionals",
            href="/professionals",
            class_name="inline-flex items-center text-sm font-medium text-blue-600 hover:underline mb-6",
        ),
        rx.cond(
            APIState.selected_professional,
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        APIState.selected_professional["name"],
                        class_name="text-3xl font-bold mb-2",
                    ),
                    rx.el.p(
                        APIState.selected_professional["category"],
                        class_name="text-md text-gray-500 mb-6",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
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
                    class_name="grid md:grid-cols-2 gap-x-8 gap-y-4",
                ),
                rx.el.h2("Reviews", class_name="text-2xl font-semibold mt-8 mb-4"),
                rx.el.div(
                    rx.foreach(APIState.selected_professional["reviews"], review_card),
                    class_name="space-y-4",
                ),
                class_name="bg-white p-8 rounded-xl border shadow-sm",
            ),
            rx.el.div(
                rx.el.p("Loading professional details..."),
                class_name="flex items-center justify-center h-64",
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