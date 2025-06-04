# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
   
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    # Asegurémonos de que endpoint comienza con / y que no lo duplicamos
    if not endpoint.startswith('/'):
        endpoint = '/' + endpoint
        
    # Asegurémonos de que backend_url comienza con http://
    url = backend_url
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    
    request_url = url + endpoint
    if params:
        request_url += "?" + params

    print("GET from {} ".format(request_url))

    # Resto del código...
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text[:200]}")  # Imprime los primeros 200 caracteres
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")
        return []

    if params:
        request_url += "?" + params

    print("backend_url: {}".format(backend_url))
    print("GET from {} ".format(request_url))

    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)        
        print(f"Response status: {response.status_code}")
        print(f"Response content type: {response.headers.get('content-type')}")
        print(f"Response content length: {len(response.text)}")
        print(f"Response content sample: {response.text[:100]}")
        
        data = response.json()
        print(f"Parsed data type: {type(data)}")
        if isinstance(data, list):
            print(f"List length: {len(data)}")
            if len(data) > 0:
                print(f"First item: {data[0]}")
        
        return data
    except Exception as e:
        # If any error occurs
        print(f"Network exception occurred: {str(e)}")
        return []


# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments

# def post_review(data_dict):
# Add code for posting review
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")
        return {"sentiment": "neutral"}

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
        return None
