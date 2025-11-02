import reflex as rx
from app.states.api_state import APIState


def stat_card(title: str, value: rx.Var, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(title, class_name="text-sm font-medium text-gray-500"),
                rx.el.p(value, class_name="text-2xl font-semibold text-gray-900"),
            ),
            rx.icon(icon, class_name="h-6 w-6 text-gray-400"),
            class_name="flex items-center justify-between",
        ),
        class_name="rounded-xl border bg-white p-4 shadow-sm",
    )


def dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Dashboard", class_name="text-2xl font-semibold mb-6"),
        rx.el.div(
            stat_card(
                "Total Professionals", APIState.total_professionals.to_string(), "users"
            ),
            stat_card(
                "Total Categories", APIState.total_categories.to_string(), "grip"
            ),
            stat_card("Average Rating", APIState.average_rating.to_string(), "star"),
            stat_card(
                "Recent Updates", APIState.recent_updates.to_string(), "activity"
            ),
            class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4",
        ),
        rx.el.div(
            rx.el.div(
                class_name="rounded-xl border bg-white p-4 shadow-sm mt-6 min-h-[300px] flex items-center justify-center text-gray-400"
            )
        ),
        class_name="flex-1 p-6",
    )