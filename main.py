import tkinter
import customtkinter
from tkinter import *
import keyword_extractor
import header_texts
import database_operations
import comparator
import generate_response_text
import webbrowser



source_url = ''
google_search_url_b = ''
google_keywords_url= ''


# i really should have used classes. i'm really sorry for this.

def fill_header():
   
    instruction_textbox.insert(0.0, header_texts.instruction_text, tags = None)
    information_textbox.insert(0.0, header_texts.information_text, tags = None)
   
    instruction_textbox.configure(state = 'disabled')
    information_textbox.configure(state = 'disabled')



def visit_source():

    webbrowser.open_new(source_url)

    return

def google_search():

    webbrowser.open_new('https://www.google.com/search?q=' + google_search_url_b)

    return

def google_keywords():

    webbrowser.open_new('https://www.google.com/search?q=' + google_keywords_url)

def button_function_paste():
    prompt_textbox.delete(0.0, END)
    cliptext=app.clipboard_get()
    prompt_textbox.insert(0.0, cliptext)


def check_prompt():

    global google_keywords_url
    global google_search_url_b
    global source_url

    prompt = prompt_textbox.get(0.0, END)
    print("\nprompt: " + prompt)

    if(len(prompt)>=0 and len(prompt)<8):

        prompt_textbox.delete(0.0, END)
        prompt_textbox.insert(0.0, 'prompt not entered or too short. please reset and try again.', tags=None)
        prompt_textbox.configure(text_color = '#ffb347', border_color = '#ffb347', state = 'disabled')
        check_button.configure(state = 'disabled')

        
    else:
        
        keywords_list = keyword_extractor.extract_keywords(prompt)
        
        search_result_dictionary = database_operations.search_news(keywords_list)
        news_b = search_result_dictionary['news_b']
        

        comparison_verdict = comparator.compare_texts(prompt, news_b)
        print("\ncomparison final verdict: ")
        print(comparison_verdict)
        print(type(comparison_verdict))


        if('same' in comparison_verdict):

            response_textbox.configure(state = 'normal')

            response_text = generate_response_text.response_text_same(search_result_dictionary)

            response_textbox.insert(0.0, response_text, tags = None)

            check_button.configure(state = 'disabled')

            response_textbox.configure(border_color = 'light green')

            prompt_textbox.configure(border_color = 'light green')

            source_url = str(search_result_dictionary['link'])
            google_search_url_b = prompt
            google_keywords_url = str(search_result_dictionary['keywords_string'])

            visit_source_button.configure(state = 'normal')
            search_google_button.configure(state = 'normal')
            google_keywords_button.configure(state = 'normal')

            return



        elif('opposite' in comparison_verdict):

            response_textbox.configure(state = 'normal')

            response_text = generate_response_text.response_text_opposite(search_result_dictionary)

            response_textbox.insert(0.0, response_text, tags = None)

            check_button.configure(state = 'disabled')

            response_textbox.configure(border_color = '#ff6961')

            prompt_textbox.configure(border_color = '#ff6961')

            source_url = str(search_result_dictionary['link'])
            google_search_url_b = prompt
            google_keywords_url = str(search_result_dictionary['keywords_string'])

            visit_source_button.configure(state = 'normal')
            search_google_button.configure(state = 'normal')
            google_keywords_button.configure(state = 'normal')


            return



        elif('different' in comparison_verdict):

            response_textbox.configure(state = 'normal')

            response_text = generate_response_text.response_text_different(search_result_dictionary)

            response_textbox.insert(0.0, response_text, tags = None)

            check_button.configure(state = 'disabled')

            response_textbox.configure(border_color = '#ffb347')

            prompt_textbox.configure(border_color = '#ffb347')

            source_url = str(search_result_dictionary['link'])
            google_search_url_b = prompt
            google_keywords_url = str(search_result_dictionary['keywords_string'])

            visit_source_button.configure(state = 'normal')
            search_google_button.configure(state = 'normal')
            google_keywords_button.configure(state = 'normal')

            return





    return






def reset_all():

    prompt_textbox.configure(state = 'normal', text_color = 'white', border_color = '#585d60')
    prompt_textbox.delete(0.0, END)
    check_button.configure(state = 'normal')

    response_textbox.delete(0.0, END)
    response_textbox.configure(border_color = '#585d60')
    response_textbox.configure(state = 'disabled')

    visit_source_button.configure(state = 'disabled')
    search_google_button.configure(state = 'disabled')
    google_keywords_button.configure(state = 'disabled')




    return








#-----GUI-----

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

custom_font=("default", 16)



app = customtkinter.CTk()  # create CTk window
app.title("[PROTOTYPE] final application. [SEEKER]")
app.geometry("1000x700")
app.grid_columnconfigure((0,1,2), weight=1)
app.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)



prompt_frame = customtkinter.CTkFrame(master = app, border_width=2, border_color = "#1f6aa5")
prompt_frame.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew", rowspan = 2, columnspan = 3)
prompt_frame.grid_columnconfigure((0), weight=1)
prompt_frame.grid_rowconfigure((0,1), weight=1)

prompt_label = customtkinter.CTkLabel(master = prompt_frame, text = "enter prompt below.", font = custom_font)
prompt_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew", rowspan = 1, columnspan = 1)



prompt_textbox = customtkinter.CTkTextbox(     master = prompt_frame,  state =   "normal", border_width=2 , border_color = "#585d60", font = custom_font, wrap = "word", text_color = '#add8e6')
response_textbox = customtkinter.CTkTextbox(     master = app,           state = "disabled", border_width=2 , border_color = "#585d60", font = custom_font, wrap = "word", text_color = '#add8e6')
instruction_textbox = customtkinter.CTkTextbox(master = app,           state =   "normal", border_width=2 , border_color = "#585d60", font = custom_font, wrap = "word", text_color = '#add8e6')
information_textbox = customtkinter.CTkTextbox(master = app,           state =   "normal", border_width=2 , border_color = "#585d60", font = custom_font, wrap = "word", text_color = '#add8e6')



instruction_textbox.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew", rowspan = 2, columnspan = 2)
information_textbox.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew", rowspan = 2, columnspan = 2)
prompt_textbox.grid(     row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew", rowspan = 1, columnspan = 1)
response_textbox.grid(     row = 6, column = 0, padx = 5, pady = 5, sticky = "nsew", rowspan = 3, columnspan = 3)


check_button = customtkinter.CTkButton(master = app, text = "\n\ncheck\n\n", font = ('default', 16), fg_color="#1d1e1e", border_width=2, border_color = "#1f6aa5", command = check_prompt)
paste_button = customtkinter.CTkButton(master = app, text = "paste",         font = ('default', 16), fg_color="#1d1e1e", border_width=2, border_color = "#1f6aa5", command = button_function_paste)
feed_button  = customtkinter.CTkButton(master = app, text = "feed" ,         font = ('default', 16), fg_color="#1d1e1e", border_width=2, border_color = "#1f6aa5")
reset_button = customtkinter.CTkButton(master = app, text = "reset",         font = ('default', 16), fg_color="#1d1e1e", border_width=2, border_color = "#1f6aa5", command = reset_all)

check_button.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew", rowspan = 2, columnspan = 3)
paste_button.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew", rowspan = 1, columnspan = 1)
feed_button.grid (row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew", rowspan = 2, columnspan = 1)
reset_button.grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew", rowspan = 1, columnspan = 1)

visit_source_button    = customtkinter.CTkButton(master = app, text = "visit source" ,    font = ('default', 16), fg_color="#1d1e1e", border_width=2, border_color = "#1f6aa5", state = 'disabled', command = visit_source)
search_google_button   = customtkinter.CTkButton(master = app, text = "search on google", font = ('default', 16), fg_color="#1d1e1e", border_width=2, border_color = "#1f6aa5", state = 'disabled', command = google_search)
google_keywords_button = customtkinter.CTkButton(master = app, text = "google keywords",  font = ('default', 16), fg_color="#1d1e1e", border_width=2, border_color = "#1f6aa5", state = 'disabled', command = google_keywords)

visit_source_button.grid (  row = 6, column = 3, padx = 5, pady = 5, sticky = "nsew", rowspan = 1, columnspan = 1)
search_google_button.grid(  row = 7, column = 3, padx = 5, pady = 5, sticky = "nsew", rowspan = 1, columnspan = 1)
google_keywords_button.grid(row = 8, column = 3, padx = 5, pady = 5, sticky = "nsew", rowspan = 1, columnspan = 1)


fill_header()

app.mainloop()