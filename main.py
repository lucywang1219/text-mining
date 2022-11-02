from nltk.stem import PorterStemmer
import pickle
import string
from mediawiki import MediaWiki
import nltk
import collections
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from thefuzz import fuzz
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt


wikipedia = MediaWiki()
china_plan = wikipedia.page("Five-year plans of China")
china_plan_text = str(china_plan.content)

with open('china_plan.pickle', 'wb') as f:  # store data
    pickle.dump(china_plan_text, f)

stop_words = set(stopwords.words('english'))
strippables = string.punctuation + string.whitespace


def process_file(fp):
    """to divide the wikipedia page by sections and store into a dictionary and nested dictionaries. Specifically, there are sub-sections in the 13th and the 14th plans, which are stored in nested dictionaries. Get rid of unrelated sections: 'See also' and 'References'. """
    f = fp.split("\n\n\n==")
    d = {}
    d1 = {}
    for i in f:
        d["Introduction"] = f[0] # name the section before the numbered plan section "Introduction"
        if "==\n" in i:
            a = i.split("==\n")
            d[a[0]] = a[1]
    d = {k.strip(): v.strip() for (k, v) in d.items()}

    dict = d.copy()  # {plan: content}
    dict["Thirteenth Plan (2016–2020)"] = {} # nested dictionary packed with subsections
    dict["Fourteenth Plan (2021–2025)"] = {}
    for k in d:
        if "=" in k:
            k1 = k.replace('=', '')
            k1 = k1.strip()
            d1[k1] = d[k]
            dict.pop(k)
    dt = list(d1.items()) # put sections in nested dictionaries into a list 
    for t in dt[:2]:
        dict["Thirteenth Plan (2016–2020)"][t[0]] = t[1]
    for t in dt[2:]:
        dict["Fourteenth Plan (2021–2025)"][t[0]] = t[1]
    
    dict.pop('See also')
    dict.pop('References')
    return dict


def print_china_plan_events(dict):
    """return a list of (which plan, time period) in the history """
    dict_copy = dict.copy()
    dict_copy.pop("Introduction")
    year_list = list()
    for k in dict_copy.keys():
        v = k[k.find("(")+1:k.find(")")]  
        k_list = k.split('(') # Separate the years from the key 
        k = k_list[0]
        t = (k, v) # (numbered plan, year period) 
        year_list.append(t)
    return year_list


def simplify_words(fp):
    """Simplify the words to narrow down the collection """
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(fp)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_words


def get_hist(fp):
    """to get a dictionary with different words but without stopwords or numbers and their frequency"""
    # f = fp.split()
    words = simplify_words(fp)
    hist = {}  # {word, frequency}
    for word in words:
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

    for word in list(hist.keys()):
        if word in stop_words or word == '' or word.isalpha() == False:
            del hist[word]

    return hist


""""""


def rank_most_common(hist):
    """return the top meaningful words that appear most frequently """
    reverse = {}
    for word in hist:
        val = hist[word]
        reverse[val] = word
        reverse = collections.OrderedDict(
            sorted(reverse.items(), reverse=True))
    most_common = list(reverse.items())
    return most_common


def draw_frequency_dstr(most_common):
    """draw a frequency distribution histogram that shows the freguency of top meaning words appear in the text. """
    dstr = pd.DataFrame(most_common, columns=['frequency', 'word'])
    dstr.plot(kind='bar', x='word')
    return plt.show()


""""""


def stem_words(s):
    """This function returns a list of stemmed words. This is to capture the main meaning of the what the text expresses and narrow down the word selections """
    words = list(s.keys())
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words


def compare_stemmed_words(s1, s2):
    """This function compare two texts using stemmed words to show what words that show up in both text and what words only show in one of the two. """
    overlap_words = list(set(s1) & set(s2))
    exclusive_words_late = list(set(s1).difference(s2))
    exclusive_words_early = list(set(s2).difference(s1))
    return overlap_words, exclusive_words_late, exclusive_words_early


def make_dispersion_plot(text, keywords):
    """This funciton draws a dispersion plot for selected keywords to show where they appear throughout the selected text. """
    tokens = word_tokenize(text)
    mytext = nltk.Text(tokens)
    dispersion_plot = mytext.dispersion_plot(keywords)
    return dispersion_plot


""""""


def sentiment_analysis(text):
    """This function conducts sentiment analysis """
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score


def compare_similiarity(s1, s2):
    """This function returns similiarity ratio between two texts, using TheFuzz library. """
    return fuzz.ratio(s1, s2)


def get_similiarity_list(all_plans):
    """This function returns progressive similiarity ratios between two consecutive plans in a list. """
    similiarity_list = []
    for i in range(len(all_plans)-1):
        s1 = all_plans[i]
        s2 = all_plans[i + 1]
        similiarity = compare_similiarity(s1, s2)
        similiarity_list.append(similiarity)
    return similiarity_list


""""""


def get_key(p, dict):
    """This is a function that use value to find key in the dictionary. Used for printing results in testing."""
    v = {i for i in dict if dict[i] == p}
    return v


def main():
    with open('china_plan.pickle', 'rb') as input_file:
        fp = pickle.load(input_file)
    # plan_dict = process_file(fp)
    # plan_list = list(plan_dict.items())
    # print(plan_list)

    dict = process_file(fp)
    hist = get_hist(fp)

    # define plans 1 to 14
    p1 = dict['First Plan (1953–1957)']
    p2 = dict['Second Plan (1958–1962)']
    p3 = dict['Third Plan (1966–1970)']
    p5 = dict['Fifth Plan (1976–1980)']
    p6 = dict["Sixth Plan (1981–1985)"]
    p7 = dict['Seventh Plan (1986–1990)']
    p8 = dict['Eighth Plan (1991–1995)']
    p9 = dict['Ninth Plan (1996–2000)']
    p10 = dict['Tenth Plan (2001–2005)']
    p11 = dict["Eleventh Plan (2006–2010)"]
    p12 = dict['Twelfth Plan (2011–2015)']
    v13 = list(dict['Thirteenth Plan (2016–2020)'].values())
    p13 = ' '.join(v13)
    v14 = list(dict['Fourteenth Plan (2021–2025)'].values())
    p14 = ' '.join(v14)
    all_plans = [p1, p2, p3, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]

    # The first to the sixth are early plans. The seventh to the tenth are mid plans. The eleventh to the fourteenth are later plans. This function divides plans due to different eras and return the combined string for each era.
    early_plans_text = p1 + p2 + p3 + p5 + p6
    mid_plans_text = p7 + p8 + p9 + p10
    later_plans_text = p11 + p12 + p13 + p14

    # conduct sentiment analysis for each period
    print(f'The sentiment score for early plans is {sentiment_analysis(early_plans_text)}') # highest positive and negative
    print(f'The sentiment score for mid plans is {sentiment_analysis(mid_plans_text)}. ')
    print(f'The sentiment score for later plans is {sentiment_analysis(later_plans_text)}.') # highest neutral

    # print by sections
    for k, v in dict.items():
        print(k, '\n', v)
        print("\n")

    # print a China Plan calendar side by side
    year_list = (print_china_plan_events(dict))
    print('\t\t', 'China Plan', '\n')
    for t in year_list:
        print('{:<30}{}'.format(t[0], t[1]))

    # print the most common words in the later plans and draw a frequency histogram
    t3 = rank_most_common(get_hist(later_plans_text))
    print('10 most common words in later plans are: ')
    for freq, word in t3[:10]:
        print('{:<15}{}'.format(word, freq))
    print(draw_frequency_dstr(t3))
    # print the most common words in the early plans and draw a frequency histogram
    t1 = rank_most_common(get_hist(early_plans_text))
    print('10 most common words in early plans are: ')
    for freq, word in t1[:10]:
        print('{:<15}{}'.format(word, freq))
    print(draw_frequency_dstr(t1))

    # Draw a frequency plot that show the most common words in the whole text
    most_common = rank_most_common(hist)
    print(draw_frequency_dstr(most_common))

    # Compare overlap words in an early plan and a later plan; words that only appear in the later plan but not the early plan. This is to observe the trend of China national strategic plans.
    stem_early = stem_words(get_hist(early_plans_text))
    stem_late = stem_words(get_hist(later_plans_text))
    overlap_words, exclusive_words_late, exclusive_words_early = compare_stemmed_words(
        stem_late, stem_early)
    print("Stemmed words that appear in both China Plans are: ")
    # market, industry, reform, economy, communist, manufacture, highway, transport
    print(overlap_words, '\n')
    print("Stemmed words that only appear in the later China Plans but not the early plans are: ")
    # environment, ecosystem, conserve, carbon, pollution, Taiwan, southwest, nuclear
    print(exclusive_words_late, '\n')
    print("Stemmed words that only appear in the early China Plans but not the later plans are: ")
    print(exclusive_words_early)

    # draw a dispersion plot to see where do the keyowrds appear in the text.
    keywords = ['infrastructure', 'industrial', 'technology', 'ecosystems',
                'environment', 'carbon', 'reform', 'energy', 'healthcare', 'agriculture']
    print(make_dispersion_plot(fp, keywords))

    # compare similiarity
    f1 = p1
    f2 = p12
    ratio = compare_similiarity(f1, f2)
    print(
        f'The similiarity ratio between {get_key(f1, dict)} and {get_key(f2, dict)} is {ratio}. \n')
    print('The similiarity ratios for all plans are as follows: ')
    ratio_list = get_similiarity_list(all_plans)
    for i in range(len(ratio_list)):
        print(f"p{i+1} & p{i+2}:\t{ratio_list[i]}")


if __name__ == '__main__':
    main()
