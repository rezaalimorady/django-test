from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


# Create your views here.
@login_required(login_url='/login')
def ApiView(request):
    response_Crocodile = requests.get(
        'https://tiyam.filmgardi.com/_api/_v1/votes?n=21901&u=MTY0TVEza0h5bGhlb3krL3Z5cXBrQjNYMXRpdVA3RllHUXZoRlBtRFRFRlpSbmUy')
    data_Crocodile = response_Crocodile.json()
    response_johnwick= requests.get('https://tiyam.filmgardi.com/_api/_v1/votes?n=17824&u=MTY0TVEza0h5bGhlb3krL3Z5cXBrQjNYMXRpdVA3RllHUXZoRlBtRFRFRlpSbmUy')
    data_johnwick = response_johnwick.json()
    return render(request, 'api/api.html', {
        'like': data_johnwick['body'],
        'like1': data_Crocodile['body']['like'],
        'dislike1': data_Crocodile['body']['dislike'],
        'total1': data_Crocodile['body']['total'],
        'like2': data_johnwick['body']['like'],
        'dislike2': data_johnwick['body']['dislike'],
        'total2': data_johnwick['body']['total'],
    })
