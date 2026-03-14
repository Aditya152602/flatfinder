from django.contrib import admin
from .models import Listing, ListingImage, SavedListing, ContactInquiry


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1


class InquiryInline(admin.TabularInline):
    model = ContactInquiry
    extra = 0
    readonly_fields = ['sender', 'name', 'email', 'phone', 'message', 'sent_at']


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'price', 'bedrooms', 'property_type', 'is_available', 'created_at']
    list_filter = ['city', 'property_type', 'furnishing', 'is_available', 'bedrooms']
    search_fields = ['title', 'location', 'city', 'owner__username']
    list_editable = ['is_available']
    inlines = [ListingImageInline, InquiryInline]
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'description', 'property_type', 'is_available')}),
        ('Pricing', {'fields': ('price',)}),
        ('Location', {'fields': ('location', 'city', 'state', 'pincode', 'latitude', 'longitude')}),
        ('Details', {'fields': ('bedrooms', 'bathrooms', 'area_sqft', 'furnishing', 'floor', 'total_floors')}),
        ('Amenities', {'fields': ('parking', 'balcony', 'gym', 'swimming_pool', 'security')}),
        ('Contact', {'fields': ('owner', 'owner_contact', 'owner_email')}),
    )


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'listing', 'sent_at', 'is_read']
    list_filter = ['is_read', 'sent_at']
    list_editable = ['is_read']


admin.site.register(SavedListing)
