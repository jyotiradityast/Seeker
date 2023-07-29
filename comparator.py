import openai

# set up the OpenAI API key
openai.api_key = "[API key here]"


# define a function to compare the meanings of two sentences
def compare_texts(news_a, news_b):

    print("\ntext_a : " + news_a)
    print("\ntext_b : " + news_b)


    # set up the OpenAI request
    prompt = f"Are the following news same or different or opposite? Answer with one word.\n1. {news_a}\n2. {news_b}\nAnswer:"

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.5,
    )


    # parse the OpenAI response
    print(type(completions))
    print(completions)
    comparison_verdict = completions.choices[0].text.strip().lower()
    print("\ncomparison_verdict: ")
    print(comparison_verdict)
    print("\ncomparison_finished.")

    return comparison_verdict