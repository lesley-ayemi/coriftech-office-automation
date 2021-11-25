from django.http.response import HttpResponse
from django.urls import path
from django.http import HttpResponse
def test(request):
    return HttpResponse('heyebhwe')
urlpatterns = [
    path('', test)
]
