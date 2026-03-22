import requests
import urllib

SUBTITLES_ENDPOINT = "https://api.opensubtitles.com/api/v1/subtitles"
DOWNLOAD_ENDPOINT = "https://api.opensubtitles.com/api/v1/download"

HEADERS = {
    "Api-Key": "QeHbhOpCiKTbiQaKZifFUvkzi5xWWgVP",
    "User-Agent": "Learn with movies v1"
}

def get_subtitles(movie_id):
    try:
        params = {
            "imdb_id": movie_id,
            "languages": "en",
            "order_by": "ratings,download_count",
            "order_direction": "desc"
        }

        response = requests.get(SUBTITLES_ENDPOINT, headers=HEADERS, params=params)
        print(response)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e


def get_subtitle_file(file_id):
    try:
        data = {
            "file_id": file_id
        }
        response = requests.post(DOWNLOAD_ENDPOINT, headers=HEADERS, data=data)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

def get_subtitle_file_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

