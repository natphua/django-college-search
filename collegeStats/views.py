from django.shortcuts import render
from django.http import HttpResponseRedirect
from .config import api_key
import requests
import json

from .forms import collegeForm
from .models import College


def get_college(request):
    form = collegeForm()

    if request.method == 'POST':  # checks if form is populated with data (input)
        form = collegeForm(request.POST)

        if form.is_valid():
            College.objects.all().delete()
            form.save()
            return HttpResponseRedirect('/result/')

    context = {'form': form}
    return render(request, 'collegeStats/home.html', context)


def result(request):
    for i in College.objects.all():  # getting string items from query set (from College model)
        college_name = str(i)
    params_ = {     # for retrieving info from api
        'college_ids': college_name.replace(' ', '-'),
        'info_ids': 'location,out-of-state-tuition,acceptance-rate,is-private,colors,'
                    'rankings_best_colleges_for_computer_science,total-applicants,total_enrolled,campus_image'
    }
    r = requests.get('https://api.collegeai.com/v1/api/college/info?api_key=' + api_key, params_)
    college_data = json.loads(r.content)['colleges'][0]
    acceptance_rate = str(round(college_data['acceptanceRate'] * 100, 2)) + '%'
    ranking = f"{college_data['rankingsBestCollegesForComputerScience']['value']} out of {college_data['rankingsBestCollegesForComputerScience']['total']}"
    context = {
        'name': college_data['name'],
        'location': college_data['location'],
        'acceptance_rate': acceptance_rate,
        'tuition': college_data['outOfStateTuition'],
        'ranking': ranking,
        'private': college_data['isPrivate'],
        'appl': college_data['totalApplicants'],
        'enrolled': college_data['totalEnrolled'],
        'image_url': college_data['campusImage'],
    }
    return render(request, 'collegeStats/result.html', context)


def error_500(request):
    context = {}
    return render(request, 'collegeStats/500.html', context)


