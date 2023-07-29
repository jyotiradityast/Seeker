import sqlite3

def search_news(keywords_list):

    conn=sqlite3.connect("huffpost_news_database.db")
    cur=conn.cursor()



    keywords_string = ' '.join(keywords_list)
    fts_keywords_string = '* OR '.join(keywords_list)
    fts_keywords_string = fts_keywords_string + '*'
        
    print('\nkeywords string: ')
    print(keywords_string)

    print('\nfts_keywords_string: ')
    print(fts_keywords_string)




    search_query_arguments = (fts_keywords_string, )
    print("\nsearch query arguments: ")
    print(search_query_arguments)
    search_query = "select * from news_fts where news_fts MATCH (?) order by rank limit 10;"

    cur.execute(search_query, search_query_arguments)
    
    search_query_result = cur.fetchall()


    top_result = list(search_query_result[0])

    print("\ntop_result: ")
    print(top_result)

    top_result_short_description = top_result[4]
    
    print("\ntop_result_short_description: ")
    print(top_result_short_description)

    if(top_result[4] == None):
        top_result[4] = ''


    news_b = top_result[2] + "." + str(top_result[4])

    cur.close()

    result_dictionary = {
        'empty' : 'no' ,
        'news_id' : top_result[0] ,
        'link' : top_result[1] ,
        'headline' : top_result[2] ,
        'category' : top_result[3] ,
        'short_description' : top_result[4] ,
        'authors' : top_result[5] ,
        'date_published' : top_result[6] ,
        'news_b' : news_b ,
        'keywords_string' : keywords_string
    }


    return result_dictionary