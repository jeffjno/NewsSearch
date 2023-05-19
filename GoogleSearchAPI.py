from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import json

class GoogleSearchAPI:
    def __init__(self, api_key, cx):
        self.api_key = api_key
        self.cx = cx

    def search(self, query, region, time_period, max_results):
        service = build("customsearch", "v1", developerKey=self.api_key)

        start_index = 1
        results = []
        
        # Adicione um contador de consultas
        num_queries = 0

        while start_index <= max_results:
            try:
                response = service.cse().list(
                    q=query,
                    cx=self.cx,
                    cr=region,
                    start=start_index,
                    dateRestrict=f"{time_period[0].strftime('%Y-%m-%d')}_{time_period[1].strftime('%Y-%m-%d')}",
                    num=min(10, max_results - start_index + 1)
                ).execute()
            except HttpError as error:
                print(f"An error occurred: {error}")
                break
            
            results.extend(response.get("items", []))
            start_index += 10
            
            # Atualize o contador de consultas e verifique se atingiu o limite de 1000 resultados
            num_queries += 1
            if num_queries * 10 >= 1000:
                break

        return results
