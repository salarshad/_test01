import reflex as rx
from app.states.api_state import APIState
from app.components.sidebar import sidebar
from app.components.header import header


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
        width=500,
        height=300,
    )


def charts_page() -> rx.Component:
    from app.app import page_layout

    return page_layout(
        rx.el.div(
            rx.el.h1("Charts", class_name="text-2xl font-semibold mb-6"),
            rx.el.div(
                rx.el.div(
                    rx.el.h2("User Activity", class_name="text-lg font-semibold mb-4"),
                    line_chart(),
                    html_legend(),
                    class_name="rounded-xl border bg-white p-4 shadow-sm",
                ),
                class_name="mt-6",
            ),
        )
    )