from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView , ListView
from asset.models import Job , JobsApplication
from registeration.models import Profile


@login_required()
def candidate(request):
    return redirect('/alljobs')

@login_required()
def recruiter(request):
    return redirect('/addjob')

@login_required
def applyforjob(request,job_id):
    if request.method == "POST":
        print(job_id)
        j = JobsApplication()
        j.Job = Job.objects.all().get(pk=job_id)
        j.Applicant = Profile.objects.get(pk=request.user.id).user
        j.postedby = Job.objects.all().get(pk=job_id).createdBy
        j.save()
        return redirect('/alljobs')
    elif(request.method == "GET"):
        return redirect('/alljobs')

class AllJobsApplied(LoginRequiredMixin,ListView):
    model = JobsApplication
    template_name = 'appliedjobs.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        data = JobsApplication.objects.all().filter(Applicant = self.request.user.id)
        return data


class AllJobsPostedRecruiter(LoginRequiredMixin,ListView):
    model = Job
    template_name = 'myjobs.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        data = Job.objects.all().filter(createdBy = self.request.user)
        return data

class AllJobsView(LoginRequiredMixin,ListView):
    model = Job
    template_name = 'alljobs.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        data = Job.objects.filter(~Q(createdBy = self.request.user.id))
        #print(data,self.request.user)
        return data

class PostAJob(LoginRequiredMixin,CreateView):
    model = Job
    fields = ['title' , 'description' ,'location']
    template_name = 'createjob.html'
    success_url = '/recruiter'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.createdBy = self.request.user
        obj.save()
        return redirect('/allpostedjobs')

@login_required
def showAllApplicants(request):
    all_posted_jobs = Job.objects.all().filter(createdBy = request.user.id)
    #print(all_posted_jobs)
    all_applicants = []
    for job in all_posted_jobs:
        allJobApplication = JobsApplication.objects.filter(postedby = request.user.id).filter(Job = job.id)
        if(len(allJobApplication) > 0):
            all_applicants.extend(allJobApplication)
    return render(request,"showapplicants.html",{'all_applicants': all_applicants})

@login_required
def withDrawApplication(request,job_id,userid):
    #print(job_id,userid)
    JobsApplication.objects.filter(Applicant = userid).filter(Job = job_id).delete()
    return redirect('/alljobs')
