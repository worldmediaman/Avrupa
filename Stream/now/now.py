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

def extract_live_urls(content):
    match_mobile = re.search(r'daionUrl\s*:\s*"(https[^"]*mobile_web[^"]*)"', content)
    match_desktop = re.search(r'daionUrl\s*:\s*"(https[^"]*desktop_web[^"]*)"', content)
    if match_mobile and match_desktop:
        return match_mobile.group(1), match_desktop.group(1)
    else:
        print("Live URLs not found in the content.")
        return None, None

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
        mobile_url, desktop_url = extract_live_urls(site_content)
        if mobile_url and desktop_url:
            mobile_content = fetch_stream_content(mobile_url)
            desktop_content = fetch_stream_content(desktop_url)
            if mobile_content:
                print("Mobile URL content:\n", mobile_content)
            if desktop_content:
                print("Desktop URL content:\n", desktop_content)

if __name__ == "__main__":
    main()
