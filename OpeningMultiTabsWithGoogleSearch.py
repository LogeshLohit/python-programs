import requests, sys, webbrowser, bs4


print('Value got in args : ' + ' '.join(sys.argv[1:]))

result = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))

# whole web page html will be downloaded

result.raise_for_status();

print('Result:' + result.text)

soup = bs4.BeautifulSoup(result.text)


linkElements = soup.select('a')

numOfTabsToOpen = min(5, len(linkElements))

for linkCount in range(numOfTabsToOpen):
	webbrowser.open('http://google.com' + linkElements[linkCount].get('href'))

print("Opened all tabs!")