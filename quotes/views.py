from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Stock
from .forms import StockForm

def home(request): 
    import requests
    import json
    
    if request.method == 'POST' :
       ticker = request.POST['ticker']
       api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_5962d03a35b9408cb94adba159d26f73")
    
       try:
           api = json.loads(api_request.content)
       except Exception as e:
           api = "Error...."
       return render(request , 'home.html' , {'api' : api})
   
    else:
        return render(request , 'home.html' , {'ticker': "Enter a ticker"})
 

def about(request): 
    import requests
    import json
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_5962d03a35b9408cb94adba159d26f73")
    api = json.loads(api_request.content)
    return render(request , 'about.html' , {'api' : api})

def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Add Success"))
            return redirect('add_stock')
            
    else:        
         ticker = Stock.objects.all()
         output = []
         for ticker_item in ticker:
             api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_5962d03a35b9408cb94adba159d26f73")
             try:
                api = json.loads(api_request.content)
                output.append(api)
             except Exception as e:
                api = "Error..."    
         return render(request , 'add_stock.html' , {'ticker' : ticker , 'output' : output})

def base(request):
    return render(request , 'base.html' , {})

def delete(request , stock_id):
    item = Stock.objects.get(pk = stock_id)
    item.delete()
    messages.success(request, ("Deleted"))
    return redirect('add_stock')
