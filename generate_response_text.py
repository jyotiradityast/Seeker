def response_text_base_function(result_dictionary):

    keywords_text = "keywords: " + str(result_dictionary['keywords_string'])
    headline_text = "headline: " + str(result_dictionary['headline'])
    short_description_text = "short description" + str(result_dictionary['short_description'])
    link_text = "link: " + str(result_dictionary['link'])
    authors_text = "authors: " + str(result_dictionary['authors'])
    date_text = "date published: " + str(result_dictionary['date_published'])
    category_text = "category: " + str(result_dictionary['category'])

    response_text_base = keywords_text + '\n\n' + headline_text + '\n\n' + short_description_text + '\n\n' + link_text + '\n\n' + authors_text + '\n\n' + date_text + '\n\n' + category_text

    return response_text_base


def response_text_same(result_dictionary):

    response_text_base = response_text_base_function(result_dictionary)
    response_text = 'true.\n\n' + response_text_base

    return response_text

def response_text_opposite(result_dictionary):

    response_text_base = response_text_base_function(result_dictionary)
    response_text = 'false.\n\n' + response_text_base

    return response_text

def response_text_different(result_dictionary):

    response_text_base = response_text_base_function(result_dictionary)
    response_text = "can't validate. sorry. \n\n" + response_text_base

    return response_text