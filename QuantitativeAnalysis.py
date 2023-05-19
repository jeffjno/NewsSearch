import json
import matplotlib.pyplot as plt

class QuantitativeAnalysis:
    def __init__(self, news_data_file):
        with open(news_data_file) as f:
            self.news_data = json.load(f)

    def analyze_news(self):
        # Conta o número de notícias para cada site
        site_counts = {}
        for news_item in self.news_data:
            site = news_item["displayLink"]
            if site in site_counts:
                site_counts[site] += 1
            else:
                site_counts[site] = 1

        # Seleciona os top 10 sites com mais notícias e agrupa os demais em uma única categoria "Outros"
        top_sites = sorted(site_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        other_count = sum([count for site, count in site_counts.items() if site not in dict(top_sites)])
        top_sites.append(("Outros", other_count))

        # Prepara os dados para o gráfico de barras
        labels = [site for site, count in top_sites]
        counts = [count for site, count in top_sites]

        # Prepara os dados para o gráfico de pizza
        sizes = counts
        labels_pie = labels

        # Prepara o resultado
        total_news = sum(counts)
        analysis_result = {
            "total_news": total_news,
            "top_sites": top_sites
        }
        return analysis_result
    
    def save_to_file(self, output_file):
        result = self.analyze_news()
        with open(output_file, "w") as f:
            json.dump(result, f)

    def plot_graph(self, output_file):
        result = self.analyze_news()
        top_sites = result["top_sites"]

        # Prepara o gráfico de barras
        labels = [site for site, count in top_sites]
        counts = [count for site, count in top_sites]
        fig, ax = plt.subplots()
        ax.bar(labels, counts)
        ax.set_xticklabels(labels, rotation=45, ha="right")
        ax.set_title("Top 10 sites com mais notícias")
        ax.set_xlabel("Site")
        ax.set_ylabel("Quantidade de notícias")

        # Adiciona a contagem na legenda
        for i, v in enumerate(counts):
            ax.text(i, v + 1, str(v), color='blue', ha='center')

        plt.tight_layout()

        # Salva o gráfico de barras
        plt.savefig(output_file + "_bar.png")

        # Prepara o gráfico de pizza
        top_labels = labels[:-1]
        top_sizes = counts[:-1]
        other_label = labels[-1]
        other_size = counts[-1]
        sizes = top_sizes + [other_size]
        labels_pie = top_labels + [other_label]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels_pie, autopct="%1.1f%%")
        ax.set_title("Distribuição das notícias por site")
        plt.tight_layout()

        # Salva o gráfico de pizza
        plt.savefig(output_file + "_pie.png")

        
    def contar_total_noticias(self):
        return len(self.news_data)

    def contar_sites_unicos(self):
        site_counts = {}
        for news_item in self.news_data:
            site = news_item["displayLink"]
            if site in site_counts:
                site_counts[site] += 1
            else:
                site_counts[site] = 1
        return len(site_counts)
   