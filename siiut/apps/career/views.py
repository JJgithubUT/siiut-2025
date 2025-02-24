from django.shortcuts import render
from .models import Quarter
# CRUD  Views para Quarter
def quarter_list(request):
    quarters = Quarter.objects.all()
    context = {
        "quarters": quarters
    }
    return render(request, 'career/quarter/index.html', context)

def quarter_create(request, q_id):
    return render(request, 'career/quarter/create.html')

def quarter_details(request, q_id):
    return render(request, 'career/quarter/details.html')

def quarter_update(request, q_id):
    return render(request, 'career/quarter/update.html')

def quarter_delete(request, q_id):
    return render(request, 'career/quarter/delete.html')
