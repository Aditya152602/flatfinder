from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Listing, SavedListing, ContactInquiry, ListingImage
from .forms import ListingForm, ContactForm, ListingImageFormSet


def home(request):
    listings = Listing.objects.filter(is_available=True)
    featured = listings[:6]
    cities = Listing.objects.filter(is_available=True).values_list('city', flat=True).distinct()
    return render(request, 'listings/home.html', {
        'featured': featured,
        'cities': cities,
        'total_listings': listings.count(),
    })


def listing_list(request):
    listings = Listing.objects.filter(is_available=True)

    # Filters
    city = request.GET.get('city', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    bedrooms = request.GET.get('bedrooms', '')
    property_type = request.GET.get('property_type', '')
    furnishing = request.GET.get('furnishing', '')
    search = request.GET.get('search', '')

    if search:
        listings = listings.filter(
            Q(title__icontains=search) | Q(location__icontains=search) | Q(city__icontains=search)
        )
    if city:
        listings = listings.filter(city__icontains=city)
    if min_price:
        listings = listings.filter(price__gte=min_price)
    if max_price:
        listings = listings.filter(price__lte=max_price)
    if bedrooms:
        listings = listings.filter(bedrooms=bedrooms)
    if property_type:
        listings = listings.filter(property_type=property_type)
    if furnishing:
        listings = listings.filter(furnishing=furnishing)

    # Sorting
    sort = request.GET.get('sort', '-created_at')
    listings = listings.order_by(sort)

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    listings_page = paginator.get_page(page)

    cities = Listing.objects.filter(is_available=True).values_list('city', flat=True).distinct()

    return render(request, 'listings/listing_list.html', {
        'listings': listings_page,
        'cities': cities,
        'filters': {
            'city': city, 'min_price': min_price, 'max_price': max_price,
            'bedrooms': bedrooms, 'property_type': property_type,
            'furnishing': furnishing, 'search': search, 'sort': sort,
        },
    })


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedListing.objects.filter(user=request.user, listing=listing).exists()

    contact_form = ContactForm(initial={
        'name': request.user.get_full_name() if request.user.is_authenticated else '',
        'email': request.user.email if request.user.is_authenticated else '',
    })

    similar = Listing.objects.filter(
        city=listing.city, is_available=True
    ).exclude(pk=pk)[:3]

    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'is_saved': is_saved,
        'contact_form': contact_form,
        'similar': similar,
    })


def listing_map(request):
    listings = Listing.objects.filter(is_available=True, latitude__isnull=False, longitude__isnull=False)
    listings_data = [
        {
            'id': l.pk, 'title': l.title, 'price': str(l.price),
            'city': l.city, 'lat': l.latitude, 'lng': l.longitude,
            'bedrooms': l.bedrooms, 'property_type': l.property_type,
        }
        for l in listings
    ]
    return render(request, 'listings/listing_map.html', {'listings_data': listings_data})


@login_required
def save_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    saved, created = SavedListing.objects.get_or_create(user=request.user, listing=listing)
    if not created:
        saved.delete()
        messages.info(request, 'Listing removed from saved.')
    else:
        messages.success(request, 'Listing saved successfully!')
    return redirect('listing_detail', pk=pk)


@login_required
def saved_listings(request):
    saved = SavedListing.objects.filter(user=request.user).select_related('listing')
    return render(request, 'listings/saved_listings.html', {'saved': saved})


@login_required
def contact_owner(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.listing = listing
            inquiry.sender = request.user
            inquiry.save()
            messages.success(request, 'Your message has been sent to the owner!')
            return redirect('listing_detail', pk=pk)
    return redirect('listing_detail', pk=pk)


@login_required
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            # Handle images
            images = request.FILES.getlist('images')
            for i, img in enumerate(images):
                ListingImage.objects.create(listing=listing, image=img, is_primary=(i == 0))
            messages.success(request, 'Listing added successfully!')
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'listings/add_listing.html', {'form': form})


@login_required
def my_listings(request):
    listings = Listing.objects.filter(owner=request.user)
    return render(request, 'listings/my_listings.html', {'listings': listings})


@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Listing deleted.')
    return redirect('my_listings')
