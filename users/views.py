from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse




class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


def home(request):

 
    return render(request, 'users/home.html', {})  



def all_users(request):
    users = CustomUser.objects.all().values('id', 'username', 'email')
    return JsonResponse(list(users), safe=False)