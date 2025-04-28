from django import template
from asset.models import JobsApplication
from registeration.models import Profile

register = template.Library()

@register.simple_tag
def any_function(jobId,UserId):
    joblist = JobsApplication.objects.all().filter(Job = jobId).filter(Applicant = UserId)
    if(len(joblist)!=0 ):
            return 'Applied'
    return 'Apply'

@register.simple_tag
def getuserprofile(UserId):
    user_data = Profile.objects.all().filter(pk = UserId)
    return(user_data[0].category)
