import reflex as rx


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.el.span(text),
        href=url,
        class_name="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("briefcase", class_name="h-6 w-6"),
                    rx.el.span("ServicePro Admin", class_name="sr-only"),
                    href="#",
                    class_name="flex h-16 items-center gap-2 font-semibold",
                ),
                class_name="flex items-center border-b p-4",
            ),
            rx.el.nav(
                sidebar_item("Dashboard", "layout-dashboard", "/"),
                sidebar_item("Professionals", "users", "/professionals"),
                sidebar_item("Charts", "bar-chart-3", "/charts"),
                class_name="grid items-start px-4 text-sm font-medium",
            ),
            class_name="flex-1 overflow-auto py-2",
        ),
        class_name="hidden border-r bg-gray-100/40 md:block",
    )