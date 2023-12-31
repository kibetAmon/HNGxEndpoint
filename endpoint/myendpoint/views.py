from django.http import JsonResponse
from datetime import datetime, timezone, date

import calendar


# Create your views here.
def endpointview(request):
    today = date.today()
    data = {
        'slack_name': 'amonkibet',
        'current_day': calendar.day_name[today.weekday()],
        'utc_time': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': 'backend',
        'github_file_url': 'https://github.com/kibetAmon/HNGxEndpoint/blob/master/endpoint/myendpoint/views.py',
        'github_repo_url': 'https://github.com/kibetAmon/HNGxEndpoint',
        'status_code': 200
    }
    response = JsonResponse(data, status=200)
    return response
