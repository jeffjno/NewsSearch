import json

class QualitativeAnalysis:
    
    def __init__(self, arquivo_json):
        with open(arquivo_json, 'r', encoding='utf-8') as file:
            self.noticias = json.load(file)    

    def contar_noticias(self, palavras, logica):
        contador = 0

        if logica == 'OR':
            for noticia in self.noticias:
                if any(palavra.lower() in noticia['content'].lower() for palavra in palavras):
                    contador += 1
        elif logica == 'AND':
            for noticia in self.noticias:
                if all(palavra.lower() in noticia['content'].lower() for palavra in palavras):
                    contador += 1
        else:
            print("Logica desconhecida. Use 'OR' ou 'AND'.")
            return None

        return contador

    def contar_noticias_por_palavra(self, palavras):
        contadores = [0] * len(palavras)

        for noticia in self.noticias:
            for i, palavra in enumerate(palavras):
                if palavra.lower() in noticia['content'].lower():
                    contadores[i] += 1

        return contadores
     

