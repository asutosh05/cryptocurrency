from django.shortcuts import render,redirect
from django.contrib import messages
from airtable import Airtable
import os

def index(request):
    return render(request,'index.html',{})