from django.shortcuts import render, get_object_or_404
from .models import Loch

# Create your views here.
def loch_list(request):
    lochs = Loch.objects.all()
    return render(request, 'lochs/loch_list.html', {'lochs' : lochs})

def loch_detail(request, id):
    loch = get_object_or_404(Loch, id=id)
    return render(request, 'lochs/loch_detail.html', {'loch' : loch})