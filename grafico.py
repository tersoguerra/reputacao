import matplotlib.pyplot as plt     # add python3-tk
from wordcloud import WordCloud


class Grafico(object):

    def wordcloud(self, text, start_name):
        # https://python-graph-gallery.com/260-basic-wordcloud/
        wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.savefig(start_name + '.png')
        plt.close()

    def sentiment_pizza(self, positive_count, neutral_count, negative_count, query):
        label_list = ['Positivo', 'Neutro', 'Negativo']
        size_list = [positive_count, neutral_count, negative_count]
        color_list = ['blue', 'grey', 'red']
        self.pizza(label_list, size_list, color_list, 'pizza_graphic_' + query)
        print('Gráfico Pizza de sentimento gerado para análise %s' % query)

    def pizza(self, label_list, size_list, color_list, start_name):
        # https://pythonspot.com/matplotlib-pie-chart/
        plt.pie(size_list, labels=label_list, colors=color_list, autopct='%1.1f%%')
        plt.axis('equal')
        plt.savefig(start_name + '.png')
        plt.close()
