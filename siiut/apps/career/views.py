from django.shortcuts import redirect, render
from .models import Quarter
from .forms import QuarterForm
# CRUD  Views para Quarter
def quarter_list(request):
    quarters = Quarter.objects.all()
    context = {
        "quarters": quarters
    }
    return render(request, 'career/quarter/index.html', context)

def quarter_create(request):
    if request.method == 'POST':
        form = QuarterForm(request.POST)
        if form.is_valid():
            quarter = Quarter(
                quarter = form.cleaned_data['quarter'],
                quarter_name = form.cleaned_data['quarter_name']
            )
            quarter.save()
            return redirect('career:quarter_list')
    else:
        form = QuarterForm()
        return render(request, 'career/quarter/create.html', {'form': form})

    return render(request, 'career/quarter/create.html',{'form': form})

def quarter_details(request, q_id):
    quarter = Quarter.objects.get(pk=q_id)
    return render(request, 'career/quarter/details.html', {'quarter': quarter})

def quarter_update(request, q_id):
    return render(request, 'career/quarter/update.html')

def quarter_delete(request, q_id):
    pass
