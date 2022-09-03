import nltk
import websearch
from difflib import SequenceMatcher

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(nltk.corpus.stopwords.words('english')) 

def purify_text(string):
    words = nltk.word_tokenize(string)
    return (" ".join([word for word in words if word not in stop_words]))

def web_verify(string, results_per_sentence):
    sentences = nltk.sent_tokenize(string)
    matching_sites = []
    n = 0
    for url in websearch.bing_search(query=string, num=results_per_sentence):
        matching_sites.append(url)
        n+=1
        if(n==10):
            break
    for sentence in sentences:
        for url in websearch.bing_search(query = sentence, num = results_per_sentence):
            matching_sites.append(url)
            break
    return (list(set(matching_sites)))

def similarity(str1, str2):
    return (SequenceMatcher(None, str1, str2).ratio())*(100)

def report(text):
    matching_sites = web_verify(purify_text(text), 2)
    matches = {}
    for i in range(len(matching_sites)):
        matches[matching_sites[i]] = similarity(text, websearch.extract_text(matching_sites[i]))
    matches = {k: v for k, v in sorted(matches.items(), key=lambda item: item[1], reverse=True)}
    matches_json = []
    for k in matches.keys():
        matches_json.append({'url':k, 'score':matches[k]})
    return matches_json