from django.shortcuts import render,redirect
from django.contrib import messages
from airtable import Airtable
import os

APIKEY='yNXRCoWSRdUIShMInMmWUVn4foIUx3'

def index(request):   
    return render(request,'index.html',{})
    
    
