import json
import requests


def fetch_and_print_articles(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        # The API returns a list of post objects directly
        articles = response.json()

        # Iterate over the first article and pretty-print it using jprint
        for index, article in enumerate(articles[:1], start=1):
            print(f"Article {index}:")
            jprint(article)
    else:
        print(f"Error: {response.status_code}")


def jprint(obj):
    # Formats and prints any Python dictionary/list as clean JSON
    print(json.dumps(obj, sort_keys=True, indent=4))


# Free public API endpoint (No API key needed)
api_endpoint = "https://jsonplaceholder.typicode.com/posts"

fetch_and_print_articles(api_endpoint)