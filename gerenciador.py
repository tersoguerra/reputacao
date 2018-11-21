from twitter import AcessoTwitter
from pln import AcessoPLN
from grafico import Grafico
import json


class Gerenciador(object):

    def __init__(self):
        self.twitter = AcessoTwitter()
        self.pln = AcessoPLN()
        self.grafico = Grafico()

    def quick_execution(self, query):
        tweet_list = self.twitter.quick_start(query)
        self.process_data(query, tweet_list)

    def import_json(self, json_file):
        query = 'imported_json'
        tweet_list = self.read_json_file(json_file)['tweet_list']
        self.process_data(query, tweet_list)

    def process_data(self, query, tweet_list):
        positive_count, neutral_count, negative_count, repercussion_count = self.count_sentiment(tweet_list)
        self.twitter.save_tweets(tweet_list, query)
        self.grafico.sentiment_pizza(positive_count, neutral_count, negative_count, query)
        self.tweet_to_wordcloud(tweet_list, query)
        self.print_metrics(query, tweet_list, positive_count, negative_count, neutral_count, repercussion_count)

    def count_sentiment(self, tweet_list):
        positive_count = neutral_count = negative_count = repercussion_count = 0
        for tweet_idx, tweet_dict in enumerate(tweet_list):
            tweet_dict['sentiment'] = self.pln.sentiment_analysis(tweet_dict['text'])['sentiment_result']
            tweet_list[tweet_idx] = tweet_dict
            repercussion_count += tweet_dict['repercussion_count']
            if tweet_dict['sentiment'] is True:
                positive_count += 1
            elif tweet_dict['sentiment'] is False:
                negative_count += 1
            else:
                neutral_count += 1
        return positive_count, neutral_count, negative_count, repercussion_count

    def tweet_to_wordcloud(self, tweet_list, query):
        wordcloud_text = str()
        for tweet_dict in tweet_list:
            treated_text = self.pln.treat_stopwords(tweet_dict['text'])
            wordcloud_text = wordcloud_text + treated_text + ' '
        self.grafico.wordcloud(wordcloud_text, 'wordcloud_graphic_' + query)
        print('Gráfico Wordcloud gerado para análise %s' % query)

    @staticmethod
    def print_metrics(query, tweet_list, positive_count, negative_count, neutral_count, repercussion_count):
        print('A soma dos coeficiente de repercussão é: %d' % repercussion_count)
        print('A soma das métricas de sentimento para os %d comentários é:' % len(tweet_list))
        print('Total de comentários positivos: %d' % positive_count)
        print('Total de comentários negativos: %d' % negative_count)
        print('Total de comentários neutros: %d' % neutral_count)
        print('Fim da coleta da análise %s' % query)

    @staticmethod
    def read_json_file(file_name):
        """
        Read JSON file and return dictionary
        :param file_name: JSON file name
        :return: dictionary from JSON file
        """
        with open(file_name, "r") as file:
            dictionary = json.load(file)
        return dictionary
