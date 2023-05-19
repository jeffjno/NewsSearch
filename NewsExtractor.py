import json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class NewsExtractor:
    def __init__(self):
        pass

    def extract_text_from_url(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extrai todo o texto visível no corpo da página
            texts = soup.stripped_strings
            extracted_text = " ".join(texts)
            return extracted_text
        except Exception as e:
            print(f"Erro ao extrair texto da URL {url}: {e}")
            return ""

    def process_news_item(self, item):
        link = item["link"]
        print(f"Extraindo notícia: {link}")
        news_text = self.extract_text_from_url(link)
        return {"link": link, "content": news_text}

    def extract_and_save_news_content(self, input_file, output_file, max_workers=10):
        # Carrega os dados do arquivo JSON de entrada
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        extracted_news = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            extracted_news = list(executor.map(self.process_news_item, data))

        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(extracted_news, file, ensure_ascii=False, indent=4)