# Python program to find the k most frequent words 
# from data set 
from collections import Counter 
import matplotlib.pyplot as plt
import string

def mostFreq(data_set,n):
    """Parses the data_set to find the top n most frequent words

    Args:
        data_set (string): the string to be parsed
        n (int): the top number of words to counted for frequency

    Returns:
        list: list of tuples of the from (word,frequency) ordered in descending frequency
    """
    # remove punctuation
    if data_set is None:
        return None
    data_set = data_set.translate(str.maketrans('', '', string.punctuation))
    
    split_it = data_set.split() 
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
    fig = plt.bar(x_pos, freqs, color='#3b5998')
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(f"Top {len(words)} words that you have used on Facebook")
    
    plt.xticks(x_pos, words)
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

    n = 10 # the top most frequent words to be displayed on barchart
    mostFreqBarchart(mostFreq(data_set,n),chart_fname)

def main():
    data_set = "Welcome to the world of Geeks This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks. "
    freqWords2Barchart(data_set,'test')

if __name__=='__main__':
    main()