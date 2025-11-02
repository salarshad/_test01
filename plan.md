# Service Professionals Admin Panel

## Overview
Build a modern admin panel to manage service professionals data using the Service Professionals API. The panel will feature a dashboard with data summaries and a comprehensive table view for browsing, editing, and adding professional profiles.

---

## Phase 1: Dashboard Layout and Data Fetching ✅
- [x] Set up base layout with sidebar navigation and header
- [x] Create state management for API data fetching
- [x] Implement dashboard page with summary statistics (total professionals, categories, average ratings, recent updates)
- [x] Add visual cards for key metrics with icons and gradients
- [x] Create professionals table page with search and filter functionality
- [x] Implement API integration to fetch professionals list with pagination

---

## Phase 2: Professionals Table with Edit & Add Features ✅
- [x] Build comprehensive data table displaying all professional profiles
- [x] Add column sorting, search filtering, and pagination controls
- [x] Create edit modal/drawer that opens when clicking an edit button on a row
- [x] Implement form fields for editing all professional attributes (name, category, description, services, location, contact info, etc.)
- [x] Add form validation and error handling for edit operations
- [x] Implement "Add New Professional" button and modal with full form
- [x] Handle image URL management (add/remove image URLs)

---

## Phase 3: API Integration for Save, Update, and Delete Operations
- [ ] Implement PUT/PATCH endpoint integration for updating existing professionals
- [ ] Add POST endpoint integration for creating new professionals
- [ ] Implement DELETE functionality for removing professionals (if API supports)
- [ ] Add loading states, success notifications, and error handling for all API operations
- [ ] Implement optimistic updates and data refresh after mutations
- [ ] Add confirmation dialogs for destructive actions
- [ ] Create detailed professional view modal showing all information including reviews

---

## Notes
- API Base URL: https://api.serviceprofessionals.com/v1
- Primary endpoints: GET /professionals/search, GET /professionals/{id}
- Professional schema includes: id, name, category, description, services, location, rating, reviews, contact_info, image_urls
- The API spec shows read endpoints; for edit/create/delete operations, we'll implement the structure and mock the endpoints (as they may need to be added to the API)
- Use Modern SaaS design with violet primary color, Montserrat font, and smooth interactions
