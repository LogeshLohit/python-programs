import requests, sys, webbrowser, bs4

result = requests.get('https://www.gutenberg.org/')

# whole web page is loaded in to text file

result.raise_for_status();

print('Gng to start!')

soup = bs4.BeautifulSoup(result.text)


linkElements = soup.select('div div div a')
# the links to the books are there inside that a

numOfTabsToOpen = min(5, len(linkElements))

for linkCount in range(numOfTabsToOpen):
	webbrowser.open('https://www.gutenberg.org/' + linkElements[linkCount].get('href'))
	print('All href elements : ' + linkElements[linkCount].get('href'))


print("Opened all tabs!")