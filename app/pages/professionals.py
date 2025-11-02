import reflex as rx
from app.states.api_state import APIState, Professional
from app.components.sidebar import sidebar
from app.components.header import header
from app.components.modals import edit_modal, add_modal
from app.components.detail_modal import detail_modal
from app.components.delete_dialog import delete_dialog


def table_header() -> rx.Component:
    return rx.el.thead(
        rx.el.tr(
            rx.el.th(
                "Name", class_name="p-3 text-left text-sm font-semibold text-gray-600"
            ),
            rx.el.th(
                "Category",
                class_name="p-3 text-left text-sm font-semibold text-gray-600",
            ),
            rx.el.th(
                "Services",
                class_name="p-3 text-left text-sm font-semibold text-gray-600",
            ),
            rx.el.th(
                "Location",
                class_name="p-3 text-left text-sm font-semibold text-gray-600",
            ),
            rx.el.th(
                "Rating", class_name="p-3 text-left text-sm font-semibold text-gray-600"
            ),
            rx.el.th(
                "Actions",
                class_name="p-3 text-left text-sm font-semibold text-gray-600",
            ),
            class_name="border-b bg-gray-50",
        )
    )


def table_row(professional: Professional) -> rx.Component:
    return rx.el.tr(
        rx.el.td(professional["name"], class_name="p-3 border-t"),
        rx.el.td(
            rx.el.span(
                professional["category"],
                class_name="px-2 py-1 text-xs font-medium rounded-full bg-blue-100 text-blue-800",
            ),
            class_name="p-3 border-t",
        ),
        rx.el.td(
            professional["services"].join(", "),
            class_name="p-3 border-t text-sm text-gray-600 max-w-xs truncate",
        ),
        rx.el.td(
            f"{professional['location']['city']}, {professional['location']['state']}",
            class_name="p-3 border-t",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon("star", class_name="h-4 w-4 text-yellow-400"),
                rx.el.span(professional["rating"].to_string()),
                class_name="flex items-center gap-1",
            ),
            class_name="p-3 border-t",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.a(
                    rx.icon("copy", class_name="h-4 w-4"),
                    href=f"/professionals/{professional['id']}",
                    class_name="p-2 text-blue-600 hover:bg-blue-50 rounded-md",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4"),
                    on_click=lambda: APIState.open_delete_dialog(professional["id"]),
                    class_name="p-2 text-red-500 hover:bg-red-50 rounded-md",
                ),
                class_name="flex items-center gap-1",
            ),
            class_name="p-3 border-t",
        ),
        class_name="hover:bg-gray-50",
    )


def professionals_table() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            table_header(),
            rx.el.tbody(rx.foreach(APIState.paginated_professionals, table_row)),
            class_name="w-full table-auto",
        ),
        class_name="rounded-xl border bg-white shadow-sm overflow-hidden",
    )


def pagination_controls() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            f"Page {APIState.current_page} of {APIState.total_pages}",
            class_name="text-sm text-gray-600",
        ),
        rx.el.div(
            rx.el.button(
                "Previous",
                on_click=APIState.prev_page,
                disabled=APIState.current_page <= 1,
                class_name="px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50 disabled:opacity-50",
            ),
            rx.el.button(
                "Next",
                on_click=APIState.next_page,
                disabled=APIState.current_page >= APIState.total_pages,
                class_name="px-4 py-2 text-sm rounded-md border bg-white hover:bg-gray-50 disabled:opacity-50",
            ),
            class_name="flex gap-2",
        ),
        class_name="flex justify-between items-center mt-4",
    )


def professionals_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            rx.el.main(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1("Professionals", class_name="text-2xl font-semibold"),
                        rx.el.div(
                            rx.el.input(
                                placeholder="Search by name...",
                                on_change=APIState.set_search_query,
                                class_name="w-full md:w-64 rounded-md border px-3 py-2 text-sm",
                                default_value=APIState.search_query,
                            ),
                            rx.el.select(
                                rx.foreach(
                                    APIState.all_categories,
                                    lambda c: rx.el.option(c, value=c),
                                ),
                                on_change=APIState.set_selected_category,
                                value=APIState.selected_category,
                                placeholder="Filter by category",
                                class_name="rounded-md border px-3 py-2 text-sm",
                            ),
                            rx.el.button(
                                rx.icon("refresh-cw", class_name="h-4 w-4"),
                                on_click=APIState.fetch_professionals,
                                class_name="p-2 text-sm rounded-md border bg-white hover:bg-gray-50",
                            ),
                            rx.el.button(
                                "Add New Professional",
                                on_click=APIState.open_add_modal,
                                class_name="px-4 py-2 text-sm rounded-md bg-blue-600 text-white hover:bg-blue-700",
                            ),
                            class_name="flex items-center gap-4",
                        ),
                        class_name="flex justify-between items-center mb-6",
                    ),
                    professionals_table(),
                    pagination_controls(),
                    edit_modal(),
                    add_modal(),
                    detail_modal(),
                    delete_dialog(),
                ),
                class_name="p-6",
            ),
            class_name="flex flex-col flex-1",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr] font-['Montserrat'] bg-gray-50",
    )