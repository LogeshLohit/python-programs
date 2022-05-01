import requests

result = requests.get('https://www.gutenberg.org/')
# whole web page html will be downloaded


result.raise_for_status();

file = open('D:\\Logesh\\PythonPrograms\\SavedFileTxt_GutenBergPage.txt', 'wb')

for chunk in result.iter_content(100000):
	file.write(chunk)

file.close()

print("file created!")