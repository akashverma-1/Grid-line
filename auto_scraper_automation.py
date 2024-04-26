import requests
from bs4 import BeautifulSoup

def single_page_scraper(website_list):
    # return a list of dictionaries all the text in page
    results = []
    for idx,website in enumerate(website_list):
        try:
            response = requests.get(website)
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.text
            # clean the content
            result = {
                'idx': idx,
                'url': website,
                'content': content,
            }
            # if not already in the list
            if result not in results:
                if website:
                    results.append(result)
        except Exception as e:
            print(e)
            results.append({
                'idx': idx,
                'url': website,
                'content': None,
            })
    return results

def link_extractor(website_list):
    # extract all the links from the website
    # return a list of links
    results = []
    for website in website_list:
        try:
            response = requests.get(website)
            base_url = website.split('/')[2]
            if website.startswith('https://'):
                base_url = f'https://{base_url}'
            elif website.startswith('http://'):
                base_url = f'http://{base_url}'
            print(f'Base URL: {base_url}')
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href') or ''
                if base_url not in href:
                    if href.startswith('/'):
                        href = f'{base_url}{href}'
                    elif href.startswith('http'):
                        href = href
                    elif href.startswith('www'):
                        href = f'http://{href}'
                    elif not href.startswith(base_url):
                        href = f'{base_url}/{href}'
                else:
                    href = href
                text = link.text or ''
                website = website
                if href and not href.startswith('#') and not href.startswith('javascript'):
                    result = {
                        'website': website,
                        'text': text.strip(),
                        'href': href
                    }
                    results.append(result)
        except Exception as e:
            results.append({
                'website': website,
                'text': 'Error',
                'href': f'Error: {e}'
            })
    return results


if __name__ == '__main__':
    from pprint import pp
    websites = ['https://www.python.org/', 'https://www.bbc.com/']
    results = single_page_scraper(websites)
    pp(results)
    print('-' * 50)
    results = link_extractor(websites)
    pp(results)

