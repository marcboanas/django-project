from django.shortcuts import render
from django.utils import timezone
from .models import Listing

def property_list(request):
	listings = Listing.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'property/property_list.html', {'listings': listings})
