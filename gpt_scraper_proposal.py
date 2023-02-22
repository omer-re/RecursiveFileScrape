"""
prompt: python code for website scraper that takes a url and a cookie, then goes over all items on the page recursively and if links are files from a list of types of files by extensions, if the file matches a type from the list-downloads it, keeping the hierarchy of the website as folders. the script should have a time interrupt so if a specific link or file stuck-it skips it and move on.


This code defines two functions: download_file to download a file from a URL and save it to a file path, and scrape_url to recursively scrape a URL and download files with the specified extensions. The script uses the requests library to make HTTP requests and the os library to create directories and write files. The BeautifulSoup library is used to parse the HTML content of the responses.

"""

import os
import time
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# URL and cookie for the website to scrape
url = 'https://example.com'
cookie = {'name': 'value'}

# List of file extensions to download
file_extensions = ['.pdf', '.jpg', '.png']

# Maximum time to wait for a request in seconds
timeout = 10

# Function to download a file from a URL and save it to a file path
def download_file(url, file_path):
    print('Downloading:', url)
    response = requests.get(url, cookies=cookie, timeout=timeout)
    with open(file_path, 'wb') as f:
        f.write(response.content)

# Function to recursively scrape a URL and download files with the specified extensions
def scrape_url(url, base_url, file_extensions, timeout, visited=set()):
    # Check if the URL has already been visited to avoid infinite loops
    if url in visited:
        return
    visited.add(url)
    # Parse the URL to get the hostname and path
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    path = parsed_url.path
    # Check if the URL is absolute or relative to the base URL
    if parsed_url.scheme and parsed_url.netloc:
        full_url = url
    else:
        full_url = urljoin(base_url, url)
    try:
        # Send a GET request to the URL with the cookie
        response = requests.get(full_url, cookies=cookie, timeout=timeout)
        # Check if the response is successful
        if response.status_code == 200:
            # Parse the HTML content of the response with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract all links from the HTML content
            for link in soup.find_all('a'):
                href = link.get('href')
                # Check if the link is a file with a matching extension
                for ext in file_extensions:
                    if href.endswith(ext):
                        # Create the directory hierarchy for the file
                        file_path = os.path.join(hostname, path, href)
                        os.makedirs(os.path.dirname(file_path), exist_ok=True)
                        # Download the file
                        try:
                            download_file(urljoin(full_url, href), file_path)
                        except Exception as e:
                            print('Error:', e)
            # Recursively scrape all links on the page
            for sub_link in soup.find_all('a'):
                sub_href = sub_link.get('href')
                # Check if the sub-link is a file or a directory
                if not any(sub_href.endswith(ext) for ext in file_extensions):
                    sub_url = urljoin(full_url, sub_href)
                    scrape_url(sub_url, base_url, file_extensions, timeout, visited)
    except Exception as e:
        print('Error:', e)

# Scrape the initial URL
scrape_url(url, url, file_extensions, timeout)
