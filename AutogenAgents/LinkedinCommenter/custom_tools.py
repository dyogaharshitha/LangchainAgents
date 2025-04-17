import requests
from bs4 import BeautifulSoup

def get_url_content(site_url : str) -> str:
    try:
        response = requests.get(site_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx/5xx)

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract visible text (basic approach)
        text = soup.get_text(separator='\n', strip=True)
        return text

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL content: {e}"
