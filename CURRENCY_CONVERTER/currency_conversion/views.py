from django.shortcuts import render

# Create your views here.
# currency_conversion/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests

API_KEY = 'fca_live_02FuP1qob2it7MjdudUvrwzmz2PuJRe6UBVHSHel'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["INR", "USD", "CAD", "EUR", "AUD", "CNY"]

@require_GET
def convert_currency(request):
    base = request.GET.get('base', '').upper()
    target = request.GET.get('target', '').upper()
    den = float(request.GET.get('denomination', 0))

    if not base or not target or den <= 0:
        return JsonResponse({'error': 'Invalid input parameters'})

    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()['data']
        if target not in data:
            return JsonResponse({'error': 'Invalid currency'})
        
        tgt = float(data[target])
        del data[base]

        result = {'result': tgt * den, 'currency': target}
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'})

