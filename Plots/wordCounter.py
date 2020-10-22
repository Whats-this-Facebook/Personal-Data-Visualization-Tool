# Python program to find the k most frequent words 
# from data set 
from collections import Counter 
import matplotlib.pyplot as plt
import string
import matplotlib.style as style


def mostFreq(data_set,n):
    """Parses the data_set to find the top n most frequent words

    Args:
        data_set (string): the string to be parsed
        n (int): the top number of words to counted for frequency

    Returns:
        list: list of tuples of the from (word,frequency) ordered in descending frequency
    """
    # List of stop words for preprocessing natural language https://gist.github.com/sebleier/554280
    stopWords = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
     "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she",
      "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
       "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am",
        "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
         "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or",
          "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
           "against", "between", "into", "through", "during", "before", "after", "above",
            "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
             "again", "further", "then", "once", "here", "there", "when", "where", "why",
              "how", "all", "any", "both", "each", "few", "more", "most", "other", "some",
               "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
                "very", "s", "t", "can", "will", "just", "don", "should", "now"}

    if data_set is None:
        return None
    
    # Preprocess data: lowercase, remove punctuation and stop words
    data_set = data_set.translate(str.maketrans('', '', string.punctuation)).lower()
    split_it = [w for w in data_set.split() if not w in stopWords]

    if not split_it:
        return None
    
    # Pass the split_it list to instance of Counter class. 
    cntr = Counter(split_it) 
  
    # most_common() produces k frequently encountered 
    # input values and their respective counts. 
    return cntr.most_common(n) 

def mostFreqBarchart(freq_words,bar_chart_name):
    """plots a list of tuples (word, freq) on a barchart (.png) where the x-axis is
    the most frequent words and the y-axis is their frequencies.

    Args:
        freq_words (list): list of tuples (word, freq) of the most frequent words
        bar_chart_name (string): the name of the barchart file to be saved (can include filepath)
    """
    if freq_words is None:
        return 0

    words = [i[0] for i in freq_words]
    freqs = [i[1] for i in freq_words]
    
    x_pos = [i for i, _ in enumerate(words)]

    # 3b5998 is the official color of facebook blue
    # color='#3b5998'
    c_map = ['#3B5998','#3460A3','#2E67AF','#276EBA','#2175C6','#1A7DD1',
        '#1484DD','#0D8BE8','#0792F4','#0099FF']
    style.use('seaborn-poster')

    fig, ax = plt.subplots()
    barplot = plt.bar(x_pos, freqs)
    for i,c in enumerate(c_map):
        barplot[i].set_color(c)

    plt.ylabel("Frequency")
    plt.title(f"Top {len(words)} words that you have used on Facebook")
    
    plt.xticks(x_pos, words,rotation=45, horizontalalignment='right', fontweight='light')
    plt.tight_layout()


    if bar_chart_name == '':
        return fig
    else:
        plt.savefig(bar_chart_name + '.png')

def freqWords2Barchart(data_set,chart_fname=''):
    """Finds the top 10 most frequent words in data_set and generates a barchart at 
    <chart_fname>.png 

    Args:
        data_set (string): the string to be parsed
        char_fname (string): the name of the barchart file to be saved (can include filepath)
    """

    n = 10 # the top n most frequent words to be displayed on barchart
    return mostFreqBarchart(mostFreq(data_set,n),chart_fname)

def main():
    print(style.available)
    data_set = "Welcome to the world of Geeks This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks. "
    print(mostFreq(data_set,10))
    freqWords2Barchart(data_set,'test')

if __name__=='__main__':
    main()