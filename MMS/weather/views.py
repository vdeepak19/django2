from django.shortcuts import render

# Create your views here.
# weather/views.py

from django.shortcuts import render
from .models import WeatherReport
import requests

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '98c9fe0696484df631f05ef073b66aa4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            report = WeatherReport(city=city, temperature=temperature, weather_description=description)
            report.save()
        else:
            temperature = None
            description = 'Weather data not available for this city.'
    else:
        temperature = None
        description = ''

    reports = WeatherReport.objects.all()

    return render(request, 'weather.html', {'reports': reports, 'temperature': temperature, 'description': description})
