from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement.user = request.user
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
        url = reverse('adv-post')
        return redirect(url)
    else:
        form = AdvertisementForm()
        context = {'form': form}
        return render(request, 'app_advertisements/advertisement-post.html', context=context)


def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'advertisement': advertisement}
    return render(request, 'app_advertisements/advertisement.html', context=context)

# Create your views here.
