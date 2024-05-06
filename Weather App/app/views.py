from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(f"http://api.weatherapi.com/v1/current.json?key=6392993c2540458793b162924230707&q={city}&aqi=no").read()
        json_data = json.loads(res)
        print(json_data)
        data = {
            'country_code': str(json_data['location']['country']),
            'coordinate': str(json_data['location']['lon']) +' '+ str(json_data['location']['lat']),
            'temp': json_data['current']['temp_c'],
            'pressure': str(json_data['current']['pressure_mb']),
            'wind_kph': str(json_data['current']['wind_kph']),
            'humidity': str(json_data['current']['humidity'],)
        }

    else:
        city = ''
        data = {}

    return render(request,'index.html',{'city':city,'data':data})
