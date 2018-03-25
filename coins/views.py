from django.shortcuts import render,redirect
from django.contrib import messages
from airtable import Airtable
import os
from coinmarketcap import Market

APIKEY='yNXRCoWSRdUIShMInMmWUVn4foIUx3'

def index(request):
    coinmarketcap = Market()
    coins=coinmarketcap.ticker(start=0, limit=3, convert='USD')
    summery=coinmarketcap.stats(convert='USD')
    coins_list={'coins':coins}
    coin_summery={'summery':summery}
    return render(request,'index.html',coin_summery)
    
    
