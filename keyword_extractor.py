import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



def extract_keywords(sentence):

    # Tokenize the sentence
    tokens = word_tokenize(sentence)


    # Remove the stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]


    # Extract the keywords
    initial_keywords_list = [token for token in filtered_tokens if token.isalpha()]

    # using list comprehension to remove duplicates from [initial_keywords_list]
    keywords = []
    [keywords.append(x) for x in initial_keywords_list if x not in keywords]
  

    print('\nkeywords list: ')
    print(keywords)

    return keywords

    # We will have to think about synonyms and paraphrases even when lookin up for the keywords in our feeds.