from django import forms
from django.shortcuts import render

# Define the form inline here
class RouteForm(forms.Form):
    start = forms.CharField(label="Start Location", max_length=100)
    end = forms.CharField(label="End Location", max_length=100)

def map_view(request):
    start = end = None
    form = RouteForm()

    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']

    return render(request, 'location/map.html', {
        'form': form,
        'start': start,
        'end': end
    })
