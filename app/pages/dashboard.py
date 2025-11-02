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


def html_legend() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(class_name="w-3 h-3 rounded-full bg-[#8884d8]"),
            rx.el.p("Desktop", class_name="text-sm text-gray-600"),
            class_name="flex items-center gap-2",
        ),
        rx.el.div(
            rx.el.div(class_name="w-3 h-3 rounded-full bg-[#82ca9d]"),
            rx.el.p("Mobile", class_name="text-sm text-gray-600"),
            class_name="flex items-center gap-2",
        ),
        class_name="flex justify-center gap-6 mt-4",
    )


def line_chart() -> rx.Component:
    return rx.recharts.line_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.x_axis(data_key="month"),
        rx.recharts.y_axis(),
        rx.recharts.tooltip(),
        rx.recharts.line(
            data_key="desktop", stroke="#8884d8", type_="monotone", stroke_width=2
        ),
        rx.recharts.line(
            data_key="mobile", stroke="#82ca9d", type_="monotone", stroke_width=2
        ),
        data=APIState.chart_data,
        width="100%",
        height=300,
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
                rx.el.h2("User Activity", class_name="text-lg font-semibold mb-4"),
                line_chart(),
                html_legend(),
                class_name="rounded-xl border bg-white p-4 shadow-sm",
            ),
            class_name="mt-6",
        ),
        class_name="flex-1 p-6",
    )