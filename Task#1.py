import requests

def search_gifs(query):
    url = f"https://api.giphy.com/v1/gifs/search?api_key=rntXRSrqvzEs4Kmo7ti4BcfXJgcoKLE8&q={query}&limit=5"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        gif_urls = [gif["images"]["original"]["url"] for gif in data["data"]]
        return gif_urls
    else:
        print("Error:", response.status_code)
        return []

def main():
    query = input("Please enter the key words: ")
    gifs = search_gifs(query)

    if gifs:
        for gif_url in gifs:
            print(gif_url)
    

if __name__ == "__main__":
    main()