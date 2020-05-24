#%%
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import GermanStemmer,SnowballStemmer
import pandas as pd
import numpy as np
from collections import Counter
import re
import spacy
from os import listdir
from os.path import isfile, join
import string

#%% set path to speech files, read look-up file for elelction dates
path = '../SwissParliament/'
elections = pd.read_csv('./lookup_files/federal_election_dates.csv')

#%% read in all session files, keep session name
def read_data(path):

    allfiles = [f for f in listdir(path) if (isfile(join(path, f)) and f.endswith(".csv"))]
    # allfiles

    alldata = pd.read_csv(join(path,allfiles[0]))
    alldata['Session'] = str.split(allfiles[0],'.')[0]

    for file in allfiles[1:]:
        # print(file)
        d = pd.read_csv(join(path,file))
        d['Session'] = str.split(file,'.')[0]
        alldata = alldata.append(d, ignore_index = True)

    return alldata


# lookup term from dates
def compute_term(df,dates_lookup):

    df['Term'] = 0
    i = 1
    for n in range(len(dates_lookup)-1):
        df.Term[df.Date.between(dates_lookup.Dates[n],dates_lookup.Dates[n+1])] =  i
        i += 1
    return df


alldata = read_data(path)
alldata = compute_term(alldata, elections)


#%%
alldata.Date.min()
alldata.Date.max()

# load stemmer for German
stemmer = GermanStemmer()

#%% compute bi-grams from speech
def preprocess_speech(speech):

    # remove non-spoken part of speeches
    speech = re.sub('((\[VS\]|\[GZ\])(.|\n)*)', '', speech)
    # remove words in brackets and parentheses
    speech = re.sub('\[.*\]', '', speech)
    speech = re.sub('\(.*\)', '', speech)

    # lemma
    # doc = nlp(speech)
    # word_list = [token.lemma_ for token in doc]

    # stanfordnlp
    # doc = nlpstdf(speech)
    # word_list = [word.lemma for sent in doc.sentences for word in sent.words]

    # split string into words
    word_list = nltk.tokenize.word_tokenize(speech)

    # remove punctuations
    table = str.maketrans('', '', string.punctuation)
    word_list = [w.translate(table) for w in word_list]

    # remove remaining non-alphabetic tokens and make lowercase
    words = [word for word in word_list if word.isalpha()]

    # remove stopwords
    stop_words = set(stopwords.words('german'))
    clean_words = [w for w in words if not w.lower() in stop_words]

    # # reduce words to stem
    # porter = PorterStemmer()
    # stemmer = SnowballStemmer("german")
    # stemmer = GermanStemmer()
    # stemmer = Cistem()
    stmd_words = [stemmer.stem(word) for word in clean_words]

    # bigrams
    bigrams = nltk.bigrams(stmd_words)

    # count and sort most common words
    countdict = dict(Counter(bigrams).most_common())

    return countdict


#%% collect dict-counts
def collect_counts(series):

    counter = Counter()
    for d in series:
        counter.update(d)

    result = dict(counter.most_common())

    return result


#%% filter data
def preprocess_data(alldata, filtervar, criterion, lang='DE'):

    data = alldata[(alldata.Language == lang) & (alldata[filtervar] == criterion)]
    data['Speech'] = data['Speech'].map(preprocess_speech)

    return data


#%% collect bi-gram counts overall
def collect_all(data):

    overall = collect_counts(data.Speech)
    dfoverall = pd.DataFrame.from_dict(overall, orient = 'index')

    dfoverall = dfoverall.reset_index()
    dfoverall.columns = ['Phrase','Counts']

    return dfoverall


#%% collect bi-gram counts by columns
def collect_by(data, columns):

    print('collecting by ', columns)
    byc = data.groupby(columns).Speech.apply(collect_counts)
    dfbyc = pd.DataFrame(byc)
    dfbyc.index.rename([*columns,'Phrase'],inplace=True)
    dfbyc.columns = ['Counts']
    dfbyclong = dfbyc.reset_index()
    dfbyclong_nona = dfbyclong.dropna()

    return dfbyclong_nona


#%%
data5 = preprocess_data(alldata, 'Term', 5)
#%%
dfoverall5 = collect_all(data5)
#%%
dfbyparty5 = collect_by(data5,['Speaker Party'])
#%%
dfbypartyspeaker5 = collect_by(data5,['Speaker Party','Speaker'])
#%%
dfbypartyspeaker5.to_csv('./term5/dfbypartyspeaker5.csv')
#%%
partyfreq = data5.groupby('Speaker Party').size()
partyfreq.to_csv('./term5/partyfreq.csv')


#%% term frequency - inverse document frequency (tf-idf)
def compute_tf_idf(dfoverall,dfbyparty,topn):

    # how many parties have used a particular phrase
    byparty_counts = dfbyparty.groupby('Phrase').size()
    dfbyparty_counts = byparty_counts.to_frame()
    dfbyparty_counts = dfbyparty_counts.reset_index()
    dfbyparty_counts.columns = ['Phrase','Freq']

    # merge with overall counts to compute tf-idf
    new = pd.merge(dfoverall,dfbyparty_counts,'left','Phrase')
    N = dfbyparty['Speaker Party'].nunique()
    new['N'] = N
    new['tf_idf'] = new.Counts*np.log(new.N/new.Freq)

    # select phrases with n-largest tf-idf metric
    newtop500 = new.nlargest(topn,'tf_idf')

    return new, newtop500


#%% filter the top phrase counts for each speaker
def select_phrases_from_df(df,newtop500,by_index,dropna=True):

    name0 = '_'.join(by_index)
    name1 = 'Counts' + name0
    top500 = pd.merge(df,newtop500,'inner', 'Phrase',suffixes=(name0,''))

    # restructure table with phrase counts as columns and index set by 'by_index'
    term5_top500_byindex = pd.pivot_table(top500, values = name1, index=by_index, columns = 'Phrase',fill_value = 0, dropna=dropna).reset_index()

    return term5_top500_byindex


#%%
term5_tf, term5top500_tf = compute_tf_idf(dfoverall5,dfbyparty,500)

# %%
term5_top500_bySpeakerParty = select_phrases_from_df(dfbypartyspeaker5,term5top500_tf,['Speaker Party','Speaker'])
term5_top500_bySpeakerParty.shape



# %% save results
term5_top500_bySpeakerParty.to_csv('./term5/term5_top500_bySpeakerParty.csv')
