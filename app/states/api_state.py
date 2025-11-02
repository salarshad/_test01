import reflex as rx
from typing import TypedDict, Any
import asyncio
import random


class Location(TypedDict):
    address: str
    city: str
    state: str
    zip_code: str
    country: str


class ContactInfo(TypedDict):
    phone: str
    email: str
    website: str | None


class Review(TypedDict):
    reviewer_name: str
    rating: float
    comment: str


class Professional(TypedDict):
    id: str
    name: str
    category: str
    description: str
    services: list[str]
    location: Location
    rating: float
    reviews: list[Review]
    contact_info: ContactInfo
    image_urls: list[str]


MOCK_PROFESSIONALS: list[Professional] = [
    {
        "id": "pro_1",
        "name": "Dr. Emily Carter",
        "category": "Medical",
        "description": "Experienced general practitioner with a focus on preventative care.",
        "services": ["General Check-ups", "Vaccinations", "Health Screenings"],
        "location": {
            "address": "123 Health St",
            "city": "Wellnessville",
            "state": "CA",
            "zip_code": "90210",
            "country": "USA",
        },
        "rating": 4.8,
        "reviews": [
            {
                "reviewer_name": "John Doe",
                "rating": 5,
                "comment": "Very thorough and caring.",
            }
        ],
        "contact_info": {
            "phone": "123-456-7890",
            "email": "emily.carter@med.com",
            "website": "dremilycarter.com",
        },
        "image_urls": ["/placeholder.svg"],
    },
    {
        "id": "pro_2",
        "name": "Mike's Plumbing",
        "category": "Home Services",
        "description": "Reliable plumbing services for residential and commercial properties.",
        "services": ["Leak Repair", "Drain Cleaning", "Water Heater Installation"],
        "location": {
            "address": "456 Oak Ave",
            "city": "Springfield",
            "state": "IL",
            "zip_code": "62704",
            "country": "USA",
        },
        "rating": 4.5,
        "reviews": [
            {
                "reviewer_name": "Jane Smith",
                "rating": 4,
                "comment": "Fixed my leak quickly.",
            }
        ],
        "contact_info": {
            "phone": "987-654-3210",
            "email": "contact@mikesplumbing.com",
            "website": None,
        },
        "image_urls": ["/placeholder.svg"],
    },
    {
        "id": "pro_3",
        "name": "Innovate Web Solutions",
        "category": "Technology",
        "description": "Custom web development and digital marketing services.",
        "services": ["Website Design", "SEO Optimization", "Social Media Management"],
        "location": {
            "address": "789 Tech Park",
            "city": "Silicon Valley",
            "state": "CA",
            "zip_code": "94043",
            "country": "USA",
        },
        "rating": 5.0,
        "reviews": [
            {
                "reviewer_name": "Sam Wilson",
                "rating": 5,
                "comment": "Built an amazing website for my business!",
            }
        ],
        "contact_info": {
            "phone": "555-123-4567",
            "email": "hello@innovateweb.com",
            "website": "innovateweb.com",
        },
        "image_urls": ["/placeholder.svg"],
    },
]


class APIState(rx.State):
    professionals: list[Professional] = []
    chart_data: list[dict[str, str | int]] = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]
    loading: bool = False
    search_query: str = ""
    selected_category: str = ""
    current_page: int = 1
    items_per_page: int = 5
    show_edit_modal: bool = False
    show_add_modal: bool = False
    show_detail_modal: bool = False
    show_delete_dialog: bool = False
    detail_loading: bool = False
    sidebar_open: bool = False
    selected_professional_id: str | None = None
    edit_form: Professional = {}
    add_form: Professional = {
        "id": "",
        "name": "",
        "category": "",
        "description": "",
        "services": [],
        "location": {
            "address": "",
            "city": "",
            "state": "",
            "zip_code": "",
            "country": "",
        },
        "rating": 0.0,
        "reviews": [],
        "contact_info": {"phone": "", "email": "", "website": ""},
        "image_urls": [],
    }

    @rx.event(background=True)
    async def fetch_professionals(self):
        async with self:
            self.loading = True
        await asyncio.sleep(0.5)
        async with self:
            self.professionals = MOCK_PROFESSIONALS
            self.loading = False
            return rx.toast.info("Professionals list refreshed.")

    @rx.var
    def total_professionals(self) -> int:
        return len(self.professionals)

    @rx.var
    def total_categories(self) -> int:
        return len(set((p["category"] for p in self.professionals)))

    @rx.var
    def average_rating(self) -> float:
        if not self.professionals:
            return 0
        avg = sum((p["rating"] for p in self.professionals)) / len(self.professionals)
        return round(avg, 2)

    @rx.var
    def recent_updates(self) -> int:
        return random.randint(0, len(self.professionals))

    @rx.var
    def all_categories(self) -> list[str]:
        return sorted(list(set([p["category"] for p in MOCK_PROFESSIONALS] + ["All"])))

    @rx.var
    def filtered_professionals(self) -> list[Professional]:
        return [
            p
            for p in self.professionals
            if self.search_query.lower() in p["name"].lower()
            and (
                self.selected_category == ""
                or self.selected_category == "All"
                or p["category"] == self.selected_category
            )
        ]

    @rx.var
    def total_pages(self) -> int:
        return -(-len(self.filtered_professionals) // self.items_per_page)

    @rx.var
    def paginated_professionals(self) -> list[Professional]:
        start = (self.current_page - 1) * self.items_per_page
        end = start + self.items_per_page
        return self.filtered_professionals[start:end]

    @rx.var
    def selected_professional(self) -> Professional | None:
        if self.selected_professional_id is None:
            return None
        for p in self.professionals:
            if p["id"] == self.selected_professional_id:
                return p
        return None

    is_editing_detail: bool = False

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    @rx.event
    def toggle_edit_detail(self):
        self.is_editing_detail = not self.is_editing_detail

    @rx.event
    def cancel_edit_detail(self):
        self.is_editing_detail = False
        return APIState.get_professional_by_id

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query
        self.current_page = 1

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query
        self.current_page = 1

    @rx.event
    def set_selected_category(self, category: str):
        self.selected_category = category
        self.current_page = 1

    @rx.event
    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1

    @rx.event
    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1

    @rx.event
    def open_edit_modal(self, professional_id: str):
        for p in self.professionals:
            if p["id"] == professional_id:
                self.edit_form = p.copy()
                self.show_edit_modal = True
                return

    @rx.event
    def close_edit_modal(self):
        self.show_edit_modal = False
        self.edit_form = {}

    @rx.event
    def open_add_modal(self):
        self.add_form = {
            "id": f"pro_{len(self.professionals) + 1}",
            "name": "",
            "category": "",
            "description": "",
            "services": [],
            "location": {
                "address": "",
                "city": "",
                "state": "",
                "zip_code": "",
                "country": "USA",
            },
            "rating": 0.0,
            "reviews": [],
            "contact_info": {"phone": "", "email": "", "website": ""},
            "image_urls": [],
        }
        self.show_add_modal = True

    @rx.event
    def close_add_modal(self):
        self.show_add_modal = False
        self.add_form = {
            "id": "",
            "name": "",
            "category": "",
            "description": "",
            "services": [],
            "location": {
                "address": "",
                "city": "",
                "state": "",
                "zip_code": "",
                "country": "",
            },
            "rating": 0.0,
            "reviews": [],
            "contact_info": {"phone": "", "email": "", "website": ""},
            "image_urls": [],
        }

    @rx.event
    def update_edit_form(self, field: str, value: str | list[str]):
        if "." in field:
            parts = field.split(".")
            self.edit_form[parts[0]][parts[1]] = value
        else:
            self.edit_form[field] = value

    @rx.event
    def update_add_form(self, field: str, value: str | list[str]):
        if "." in field:
            parts = field.split(".")
            self.add_form[parts[0]][parts[1]] = value
        else:
            self.add_form[field] = value

    @rx.event
    def add_service_to_edit(self):
        self.edit_form["services"].append("")

    @rx.event
    def remove_service_from_edit(self, index: int):
        del self.edit_form["services"][index]

    @rx.event
    def add_image_url_to_edit(self):
        self.edit_form["image_urls"].append("")

    @rx.event
    def remove_image_url_from_edit(self, index: int):
        del self.edit_form["image_urls"][index]

    @rx.event
    def save_professional(self):
        for i, p in enumerate(self.professionals):
            if p["id"] == self.edit_form["id"]:
                self.professionals[i] = self.edit_form
                break
        self.show_edit_modal = False
        self.is_editing_detail = False
        return rx.toast.success("Professional updated!")

    @rx.event
    def add_professional(self):
        self.professionals.append(self.add_form)
        self.show_add_modal = False
        return rx.toast.success("Professional added!")

    @rx.event
    def reset_selected_professional(self):
        self.selected_professional_id = None

    @rx.event(background=True)
    async def get_professional_by_id(self):
        async with self:
            self.detail_loading = True
            self.edit_form = {}
        professional_id = self.router.page.params.get("id")
        async with self:
            self.is_editing_detail = False
            if not self.professionals:
                await self.fetch_professionals()
            for p in self.professionals:
                if p["id"] == professional_id:
                    self.selected_professional_id = professional_id
                    self.edit_form = p.copy()
                    self.detail_loading = False
                    return
            self.selected_professional_id = None
            self.detail_loading = False

    @rx.event
    def open_detail_modal(self, professional_id: str):
        self.selected_professional_id = professional_id
        self.show_detail_modal = True

    @rx.event
    def close_detail_modal(self):
        self.show_detail_modal = False
        self.selected_professional_id = None

    @rx.event
    def open_delete_dialog(self, professional_id: str):
        self.selected_professional_id = professional_id
        self.show_delete_dialog = True

    @rx.event
    def close_delete_dialog(self):
        self.show_delete_dialog = False
        self.selected_professional_id = None

    @rx.event
    def delete_professional(self):
        if self.selected_professional_id:
            self.professionals = [
                p
                for p in self.professionals
                if p["id"] != self.selected_professional_id
            ]
            self.show_delete_dialog = False
            self.selected_professional_id = None
            return rx.toast.error("Professional deleted.")