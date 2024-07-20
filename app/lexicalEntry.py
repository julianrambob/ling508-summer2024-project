import requests

def fetch_wiktionary_data(word):
    """
    Args:
        word (str): The word to look up.
        lang (str): The language of the word.
    Returns:
        dict: A dictionary containing word data.
    """
    url = f"https://ru.wiktionary.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'revisions',
        'titles': word,
        'rvprop': 'content',
        'rvslots': '*',
        'redirects': 1
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for word '{word}': {response.status_code}")
        return {}

def parse_wiktionary_data(data):
    """
    Args:
        data (dict): The raw data fetched from Wiktionary.
    Returns:
        dict: A dictionary with nouns and verbs.
    """
    pages = data.get('query', {}).get('pages', {})
    pos_data = {'nouns': [], 'verbs': []}
    
    for page_id, page in pages.items():
        revisions = page.get('revisions', [])
        for revision in revisions:
            content = revision.get('slots', {}).get('main', {}).get('*', '')
            if '{{сущ ru' in content:
                pos_data['nouns'].append(content)
            if '{{гл ru' in content:
                pos_data['verbs'].append(content)
    
    return pos_data

def create_russian_dictionary(words):
    """
    Args:
        words (list): List of words to fetch.
    Returns:
        dict: A dictionary with nouns and verbs.
    """
    dictionary = {'nouns': [], 'verbs': []}
    
    for word in words:
        data = fetch_wiktionary_data(word)
        parsed_data = parse_wiktionary_data(data)
        dictionary['nouns'].extend(parsed_data['nouns'])
        dictionary['verbs'].extend(parsed_data['verbs'])

    return dictionary

if __name__ == "__main__":
    words = ['дом', 'бегать', 'книга', 'писать']  # Example words

    russian_dictionary = create_russian_dictionary(words)
    print("Nouns:")
    for noun in russian_dictionary['nouns']:
        print(noun)
    print("\nVerbs:")
    for verb in russian_dictionary['verbs']:
        print(verb)
