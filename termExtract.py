from rutermextract import TermExtractor
from typing import List
import pymorphy2
from rake_nltk import Metric, Rake
import yake
from nltk.corpus import stopwords

def rutermextract(text: str) -> List[str]:
    term_extractor = TermExtractor()
    definition_list: List[str] = list()
    for term in term_extractor.__call__(text, nested=True):
        definition_list.append(term.normalized)
        #print(str(term.normalized.split(' ')))
    str1=""
    for item in definition_list:
        if len(item)>16:
            str1 = str1 + item + "\n "
        
    return str1

def Rake_Summarizer(ttext):
    # !pip install nlp-rake
    # !pip install nltk
    from nlp_rake import Rake
    stops = list(set(stopwords.words("russian")))

    rake = Rake(stopwords=stops, max_words=3)
    return rake.apply(ttext)[:1][0][0]


def YakeSummarizer(ttext):
    # !pip install yake
    extractor = yake.KeywordExtractor(
        lan="ru",     # язык
        n=3,          # максимальное количество слов в фразе
        dedupLim=0.3,  # порог похожести слов
        top=1        # количество ключевых слов
    )
    l = list(extractor.extract_keywords(ttext))
    return l[0][0]


def get_normal_form_mas(words):
    morph = pymorphy2.MorphAnalyzer()
    result = []
    for word in words.split():
        p = morph.parse(word)[0]
        result.append(p.normal_form)
    return result


def get_normal_form(words):
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse(words)[0]
    return p.normal_form

def installStopWords():
    import nltk
    from nltk.corpus import stopwords
    nltk.download ("stopwords")

def all_sum(data):
    res=""
    res+= f"Исходный текст: {data}"
    rte = rutermextract(data)
    res+= f"\n\n rutermextract: {rte}"
    gnf = get_normal_form(data)
    res+= f"\n get_normal_form: {gnf}"
    ys = YakeSummarizer(data)
    res+= f"\n\n YakeSummarizer: {ys}"
    rs = Rake_Summarizer(data)
    res+= f"\n\n Rake_Summarizer: {rs}"    
    return res
    

if __name__ == '__main__':
    data="Системы на основе машинного обучения активно внедряются в самых разных сферах жизни. Но знаете ли вы, как часто они ошибаются и насколько легко их взломать? И можно ли вообще позволять им принимать решения без человеческого контроля?"
    # installStopWords()
    res = all_sum(data)
    print(res)
