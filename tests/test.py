import requests

def fetch_meal():
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata'
    response = requests.get(url)
    data = response.json()
    
    # Print or process the data as needed
    print(response.status_code)

if __name__ == "__main__":
    fetch_meal()
