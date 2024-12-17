import requests
import re

url = "https://www.nowtv.com.tr"

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the website content.")
        return None

def extract_live_url(content):
    match = re.search(r'daionUrl\s*:\s*"(https[^"]+)"', content)
    if match:
        return match.group(1)
    else:
        print("Live URL not found in the content.")
        return None

def fetch_stream_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch content.")
        return None

def main():
    site_content = fetch_website_content(url)
    if site_content:
        live_url = extract_live_url(site_content)
        if live_url:
            stream_content = fetch_stream_content(live_url)
            if stream_content:
                print(stream_content)

if __name__ == "__main__":
    main()
