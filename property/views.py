from django.shortcuts import render

def property_list(request):
	return render(request, 'property/property_list.html', {})
