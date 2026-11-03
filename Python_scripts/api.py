import requests

# --- EXAMPLE 1: Status 200 (OK) ---
# This is a real URL for a real to-do item that exists on the server.
url_success = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url_success)

print("--- 1. Successful Request ---")
print(f"Target URL: {url_success}")
print(f"HTTP Status Code: {response.status_code}")  # Will print 200
print(f"Response Data: {response.json()}\n")


# --- EXAMPLE 2: Status 404 (Not Found) ---
# This URL tries to fetch item #99999, which does not exist.
url_not_found = "https://jsonplaceholder.typicode.com/todos/99999"

response_404 = requests.get(url_not_found)

print("--- 2. Resource Not Found Request ---")
print(f"Target URL: {url_not_found}")
print(f"HTTP Status Code: {response_404.status_code}")  # Will print 404
print(f"Response Data: {response_404.text}")