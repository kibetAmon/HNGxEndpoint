from django.http import JsonResponse
from datetime import datetime, timezone, date

import calendar


# Create your views here.
def endpointview(request):
    today = date.today()
    data = {
        'slack_name': 'Amon Kibet',
        'current_day': calendar.day_name[today.weekday()],
        'utc_time': datetime.now(timezone.utc),
        'track': 'backend',
        'github_file_url': 'https://github.com/kibetAmon/HNGxEndpoint/blob/master/endpoint/myendpoint/views.py',
        'github_file_repo': 'https://github.com/kibetAmon/HNGxEndpoint',
        'status_code': 200
    }
    response = JsonResponse(data, status=200)
    return response
