url = 'https://math-ege.sdamgia.ru'
page = requests.get(url)

#print(page.status_code)


filteredExercises = []
allExercises = []

soup = BeautifulSoup(page.text, "html.parser")
#print(soup)
