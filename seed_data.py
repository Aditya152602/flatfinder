import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flatfinder.settings')
django.setup()

from django.contrib.auth.models import User
from listings.models import Listing
from users.models import Profile

# Create superuser
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser('admin', 'admin@flatfinder.in', 'admin123')
    Profile.objects.get_or_create(user=admin)
    print("Created admin user: admin / admin123")

# Create a test user
if not User.objects.filter(username='testuser').exists():
    user = User.objects.create_user('testuser', 'test@flatfinder.in', 'test1234', first_name='Rahul', last_name='Sharma')
    Profile.objects.get_or_create(user=user)
    print("Created test user: testuser / test1234")
else:
    user = User.objects.get(username='testuser')

# Create sample listings
sample_listings = [
    {
        'title': 'Spacious 2BHK near Metro Station',
        'description': 'Beautiful fully furnished 2BHK apartment with modern amenities. Close to metro station, supermarkets, and schools. The apartment gets great natural light and has a lovely balcony view.',
        'property_type': 'apartment',
        'price': 18000,
        'location': 'Sector 17, Indirapuram',
        'city': 'Ghaziabad',
        'state': 'Uttar Pradesh',
        'pincode': '201014',
        'latitude': 28.6448,
        'longitude': 77.3669,
        'bedrooms': 2,
        'bathrooms': 2,
        'area_sqft': 1100,
        'furnishing': 'furnished',
        'floor': 4,
        'total_floors': 10,
        'parking': True,
        'balcony': True,
        'security': True,
        'owner_contact': '9876543210',
        'owner_email': 'owner1@example.com',
    },
    {
        'title': 'Cosy 1BHK Studio in City Centre',
        'description': 'Perfect for working professionals. Semi-furnished studio apartment in the heart of the city. Walking distance to offices, restaurants, and shopping malls.',
        'property_type': 'studio',
        'price': 8500,
        'location': 'Civil Lines',
        'city': 'Kanpur',
        'state': 'Uttar Pradesh',
        'pincode': '208001',
        'latitude': 26.4499,
        'longitude': 80.3319,
        'bedrooms': 1,
        'bathrooms': 1,
        'area_sqft': 550,
        'furnishing': 'semi',
        'floor': 2,
        'total_floors': 5,
        'parking': False,
        'balcony': False,
        'security': True,
        'owner_contact': '9898989898',
        'owner_email': 'owner2@example.com',
    },
    {
        'title': 'Luxury 3BHK with Pool & Gym',
        'description': 'Premium 3BHK apartment in a gated society. Features world-class amenities including swimming pool, fully-equipped gym, and 24/7 security. Ideal for families.',
        'property_type': 'apartment',
        'price': 45000,
        'location': 'Whitefield',
        'city': 'Bangalore',
        'state': 'Karnataka',
        'pincode': '560066',
        'latitude': 12.9716,
        'longitude': 77.7480,
        'bedrooms': 3,
        'bathrooms': 3,
        'area_sqft': 1800,
        'furnishing': 'furnished',
        'floor': 8,
        'total_floors': 15,
        'parking': True,
        'balcony': True,
        'gym': True,
        'swimming_pool': True,
        'security': True,
        'owner_contact': '9123456789',
        'owner_email': 'owner3@example.com',
    },
    {
        'title': 'Affordable 2BHK for Families',
        'description': 'Well-maintained 2BHK flat in a residential colony. Close to school and hospital. Great neighbourhood with parks nearby.',
        'property_type': 'flat',
        'price': 12000,
        'location': 'Gomti Nagar',
        'city': 'Lucknow',
        'state': 'Uttar Pradesh',
        'pincode': '226010',
        'latitude': 26.8467,
        'longitude': 80.9462,
        'bedrooms': 2,
        'bathrooms': 1,
        'area_sqft': 900,
        'furnishing': 'unfurnished',
        'floor': 1,
        'total_floors': 3,
        'parking': True,
        'balcony': True,
        'security': False,
        'owner_contact': '9000012345',
        'owner_email': 'owner4@example.com',
    },
    {
        'title': 'Modern 1BHK with Terrace Garden',
        'description': 'Unique 1BHK with a private terrace garden. Semi-furnished and pet-friendly. Located in a quiet gated community with round-the-clock security.',
        'property_type': 'flat',
        'price': 14000,
        'location': 'Baner',
        'city': 'Pune',
        'state': 'Maharashtra',
        'pincode': '411045',
        'latitude': 18.5204,
        'longitude': 73.8567,
        'bedrooms': 1,
        'bathrooms': 1,
        'area_sqft': 700,
        'furnishing': 'semi',
        'floor': 3,
        'total_floors': 4,
        'parking': True,
        'balcony': True,
        'security': True,
        'owner_contact': '9765432100',
        'owner_email': 'owner5@example.com',
    },
]

for data in sample_listings:
    if not Listing.objects.filter(title=data['title']).exists():
        Listing.objects.create(owner=user, **data)
        print(f"Created listing: {data['title']}")

print("\n✅ Sample data loaded successfully!")
print("Visit http://127.0.0.1:8000 to view the site")
print("Admin panel: http://127.0.0.1:8000/admin (admin / admin123)")
