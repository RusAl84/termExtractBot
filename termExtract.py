from rutermextract import TermExtractor
from typing import List

def analyz(text: str) -> List[str]:
    term_extractor = TermExtractor()
    definition_list: List[str] = list()
    for term in term_extractor.__call__(text, nested=True):
        definition_list.append(term.normalized)
        #print(str(term.normalized.split(' ')))
    return definition_list

if __name__ == '__main__':
    data="Системы на основе машинного обучения активно внедряются в самых разных сферах жизни. Но знаете ли вы, как часто они ошибаются и насколько легко их взломать? И можно ли вообще позволять им принимать решения без человеческого контроля?"
    res= analyz(data)
    print(res)
