import time

import requests
from bs4 import BeautifulSoup

# Send GET request with user-agent header to avoid blocking
url = "https://news.ycombinator.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all story titles (inspect HN's HTML to get selectors)
titles = soup.find_all("span", class_="titleline")

# Extract and print titles
for title in titles:
    link = title.find("a")
    if link:
        print(f"- {link.text.strip()} ({link['href']})")

print("--------------")

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.content, "html.parser")

# Find Python job titles
jobs = soup.find_all("h2", string=lambda text: text and "python" in text.lower())
for job in jobs[:5]:  # Top 5
    print(job.get_text())
    time.sleep(1)  # Be respectful
