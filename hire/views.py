from django.shortcuts import render, redirect
from hire.models import Job

# Create your views here.

def index(request):
    return render(request, 'index.html')


def job_post(request):
    if request.method == 'POST':
        title = request.POST.get('job_title')
        description = request.POST.get('description')

        new_job = Job.objects.create(title = title, description = description)
        new_job.save()
        return redirect('home')

    return render(request, 'job_post.html')


def jobs(request):
    jobs = Job.objects.all()

    context = {
        'jobs': jobs,
    }
    return render(request, 'jobs.html', context)