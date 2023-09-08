from django.http import JsonResponse


# Create your views here.
def endpointview(request):
    data = {
        'slack_name': 'Amon Kibet',
        'current_date':'',
        'utc_time':'',
        'track':'',
        'github_file_url':'',
        'github_file_repo':'https://github.com/kibetAmon/HNGxEndpoint',


    }
