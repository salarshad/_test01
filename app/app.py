import reflex as rx
from app.states.api_state import APIState
from app.components.sidebar import sidebar
from app.components.header import header
from app.pages.dashboard import dashboard
from app.pages.professionals import professionals_page
from app.pages.professional_detail import professional_detail_page


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            rx.el.main(dashboard(), class_name="p-6"),
            class_name="flex flex-col flex-1",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr] font-['Montserrat'] bg-gray-50",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(
    professionals_page, route="/professionals", on_load=APIState.fetch_professionals
)
app.add_page(
    professional_detail_page,
    route="/professionals/[id]",
    on_load=APIState.get_professional_by_id,
)