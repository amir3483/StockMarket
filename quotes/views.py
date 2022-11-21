from django.shortcuts import render

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

def base(request):
    return render(request , 'base.html' , {})
