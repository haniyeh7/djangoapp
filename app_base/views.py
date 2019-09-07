from django.shortcuts import render
from app_base.models import sampleBot,otherSampleBot


def home(request):
    ctx={}
    ctx['sampleBotes'] = sampleBot.objects.all()
    return render(request,'home.html',ctx)

def sample_details(request):
    ctx={}
    ctx['other_sample'] = otherSampleBot.objects.all()
    return render(request,'sample-details.html',ctx)
