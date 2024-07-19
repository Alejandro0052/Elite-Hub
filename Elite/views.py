from django.http import HttpResponse, JsonResponse
from .models import  Usuario, Deportista
from django.shortcuts import  render, redirect, get_list_or_404
