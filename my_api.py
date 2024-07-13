import requests


def sentiment(text):
    url = "https://sentiment-analyzer3.p.rapidapi.com/Sentiment"

    querystring = {"text": text}

    headers = {
        "x-rapidapi-key": "c44b39d835mshe737bccbf9f49c2p14e6b7jsn140aedcc2ff5",
        "x-rapidapi-host": "sentiment-analyzer3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


def ner(text):
    url = "https://named-entity-extraction1.p.rapidapi.com/api/lingo"

    payload = {
        "extractor": "en",
        "text": text}
    headers = {
        "x-rapidapi-key": "c44b39d835mshe737bccbf9f49c2p14e6b7jsn140aedcc2ff5",
        "x-rapidapi-host": "named-entity-extraction1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")

def emotion(text):
    url = "https://ez-sentiment.p.rapidapi.com/"

    payload = {"text": "Hello world for the worst and the best!"}
    headers = {
        "x-rapidapi-key": "c44b39d835mshe737bccbf9f49c2p14e6b7jsn140aedcc2ff5",
        "x-rapidapi-host": "ez-sentiment.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")