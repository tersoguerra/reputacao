from leia import SentimentIntensityAnalyzer
import re


class AcessoPLN(object):

    def __init__(self):
        self.leia = SentimentIntensityAnalyzer()

    def sentiment_analysis(self, text):
        leia_score = self.leia.polarity_scores(text)
        if leia_score['compound'] >= 0.05:
            result = True
        elif leia_score['compound'] > -0.05:
            result = None
        else:
            result = False
        sentiment_score = {
            'positive_percent': leia_score['pos'],
            'negative_percent': leia_score['neg'],
            'neutral_percent': leia_score['neu'],
            'sentiment_coeficient': leia_score['compound'],
            'sentiment_result': result
        }
        print('A classificação de sentimento do texto "%s" resultou nos coeficientes %s' % (text, sentiment_score))
        return sentiment_score

    def treat_stopwords(self, text):
        stopword_list = self.read_txt_list('./lexicons/stopwords.txt')
        word_list = re.sub("[^\w]", " ",  text).split()
        treated_word_list = list()
        for word in word_list:
            if word.lower() not in stopword_list:
                treated_word_list.append(word)
        teated_text = ' '.join(treated_word_list)
        return teated_text

    @staticmethod
    def read_txt_list(file_name, keep_void=False):
        final_list = []
        with open(file_name, 'r') as file:
            txt_list = file.readlines()
        for line in txt_list:
            line = line.strip().replace('\n', '').replace('\ufeff', '')
            if line != '' or keep_void:
                final_list.append(line)
        return final_list
