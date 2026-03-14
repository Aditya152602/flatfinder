# FlatFinder 🏠

A full-stack Django web app to browse and list flats/apartments with filters, map view, user auth, and more.

## Tech Stack
- **Backend:** Django 4.2
- **Database:** SQLite (dev) — switchable to PostgreSQL
- **Frontend:** Django Templates + Bootstrap 5 + Leaflet.js maps
- **Auth:** Django built-in auth

## Features
- 🔍 Filter listings by city, budget, BHK, furnishing, property type
- 🗺️ Interactive map view (Leaflet.js + OpenStreetMap)
- 👤 User registration, login, profile
- ❤️ Save/unsave listings
- 📩 Contact owner form
- ➕ Post your own listings with photos
- ⚙️ Full Django Admin panel

## Setup Instructions

### 1. Clone / Extract the project
```bash
cd flatfinder
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Load sample data (optional but recommended)
```bash
python seed_data.py
```
This creates:
- Admin user: `admin` / `admin123`
- Test user: `testuser` / `test1234`
- 5 sample listings across Indian cities

### 6. Run the development server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

### 7. Admin Panel
Visit: http://127.0.0.1:8000/admin
Login with `admin` / `admin123`

## Project Structure
```
flatfinder/
├── flatfinder/         # Project settings & URLs
├── listings/           # Main app (models, views, forms)
├── users/              # Auth & profiles
├── templates/          # All HTML templates
│   ├── base.html
│   ├── listings/
│   └── users/
├── static/             # CSS, JS, images
├── media/              # User-uploaded files
├── manage.py
├── seed_data.py        # Sample data loader
└── requirements.txt
```

## Adding Map Coordinates
When posting a listing, add latitude and longitude to make it appear on the map view.
You can get coordinates from Google Maps by right-clicking any location.

## Customization
- Change colors in `templates/base.html` (CSS variables in `:root`)
- Add more cities in the filter dropdowns
- Switch to PostgreSQL in `settings.py` for production
