from wordcloud import WordCloud
import matplotlib.pyplot as plt
import polars as pl

def generate_wordcloud(df, textCol: str):
    """
    Takes the dataframe and the relevant column as input.
    
    Returns a wordcloud visual.
    """
    # join the words in the text column to form a single string
    text_combined = ' '.join(df[textCol])
    
    # create a WordCloud object
    wordcloud = WordCloud(width=800, height=500,
                          background_color='white',
                          colormap='plasma').generate(text_combined)

    # display the WordCloud
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, 
               interpolation='nearest')
    plt.axis('off')
    plt.show()