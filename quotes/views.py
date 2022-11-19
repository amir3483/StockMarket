from django.shortcuts import render

def home(request): 
    import requests
    import json
    # pk_5962d03a35b9408cb94adba159d26f73
    
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_5962d03a35b9408cb94adba159d26f73")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error...."
            
    
    return render(request , 'home.html' , {'api': api})

def about(request): 
    return render(request , 'about.html' , {})

def base(request):
    return render(request , 'base.html' , {})
