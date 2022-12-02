# Discover which ELve is carrying the most calories
# Read a webpage with numbers
# The Elves calories are seperated by a blank space
# Find the Elf carrying the most calories
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://adventofcode.com/2022/day/1/input"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# Extract all scripts and styles
for script in soup(["script", "style"]):
    script.extract()

# get text
text = soup.get_text()

print(text)

