import requests
from bs4 import BeautifulSoup

def fetch_noun_links(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all links from the list
    noun_links = []
    list_items = soup.select('ul li a')

    for item in list_items:
        href = item.get('href')
        if href and href.startswith('/wiki/'):
            full_url = f"https://en.wiktionary.org{href}"
            noun_links.append(full_url)

    return noun_links

def fetch_noun_data(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    form = pos = definition = None
    noun_case = gender = number = declension = None
    pos_element = soup.select_one('.mw-parser-output .pos')
    definition_element = soup.select_one('.mw-parser-output .definition')
    form_element = soup.select_one('.mw-parser-output h1')

    if form_element:
        form = form_element.get_text(strip=True)
    if pos_element:
        pos = pos_element.get_text(strip=True)
    if definition_element:
        definition = definition_element.get_text(strip=True)

    noun_case = 'nominative'
    gender = 'masculine'
    number = 'singular'
    declension = 'first'

    return (form, pos, definition, noun_case, gender, number, declension)

def write_to_file(entries, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in entries:
            file.write(f"('{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}', '{entry[4]}', '{entry[5]}', '{entry[6]}')\n")


list_url = 'https://en.wiktionary.org/wiki/Category:Russian_nouns'
noun_links = fetch_noun_links(list_url)

all_entries = []
for link in noun_links:
    print(f"Fetching data from: {link}")
    noun_data = fetch_noun_data(link)
    if noun_data[0]:
        all_entries.append(noun_data)

write_to_file(all_entries, 'russian_nouns.txt')
print(f"Scraped {len(all_entries)} entries and saved to 'russian_nouns.txt'")


