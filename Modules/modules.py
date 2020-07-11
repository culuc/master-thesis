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
from sklearn.preprocessing import StandardScaler

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
    countdict = Counter(dict(Counter(bigrams).most_common()))

    return countdict



#%% collect dict-counts
def collect_counts(series):

    counter = Counter()
    for d in series:
        counter.update(d)

    result = dict(counter.most_common())

    return result


#%% collect dict-counts
def collect_counts2(series):

    result = series.apply(np.sum)

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
    dfbyc = data.groupby(columns).Speech.apply(collect_counts).dropna().to_frame()
    dfbyc.index.rename([*columns,'Phrase'],inplace=True)
    dfbyc.columns = ['Counts']
    dfbyclong = dfbyc.reset_index()

    return dfbyclong


#%% collect bi-gram counts by columns
def collect_by1(data, columns):

    print('collecting by ', columns)
    byc = data.groupby(columns).Speech.apply(collect_counts2)
    dfbyc = pd.DataFrame(byc)
    dfbyc.index.rename([*columns,'Phrase'],inplace=True)
    dfbyc.columns = ['Counts']
    dfbyclong = dfbyc.reset_index()
    dfbyclong_nona = dfbyclong.dropna()

    return dfbyclong_nona

#%% collect bi-gram counts by columns
def collect_by2(data, columns):

    print('collecting by ', columns)
    dfbyc = data.groupby(columns).Speech.apply(np.sum).sort_values(ascending=False).to_frame()
    # dfbyc = pd.DataFrame(byc)
    dfbyc.index.rename([*columns,'Phrase'],inplace=True)
    dfbyc.columns = ['Counts']
    dfbyclong = dfbyc.reset_index()
    dfbyclong_nona = dfbyclong.dropna()

    return dfbyclong_nona


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

#%% term frequency - inverse document frequency (tf-idf)
def compute_tf_idf2(dfoverall,dfbyparty,topn):

    # how many parties have used a particular phrase
    byparty_freq = dfbyparty.groupby('Phrase').size()
    dfbyparty_freq = byparty_freq.to_frame()
    dfbyparty_freq = dfbyparty_freq.reset_index()
    dfbyparty_freq.columns = ['Phrase','Freq']

    # merge with byparty counts to compute tf-idf
    new = pd.merge(dfbyparty,dfbyparty_freq,'left','Phrase')
    N = dfbyparty['Speaker Party'].nunique()
    new['N'] = N
    new['tf_idf'] = new.Counts*np.log(new.N/new.Freq)
    new.set_index(['Speaker Party','Phrase'],inplace=True)

    # select phrases with n-largest tf-idf metric
    newtop500 = new.groupby('Speaker Party')['tf_idf'].nlargest(topn).to_frame()
    # somehow speaker party is contained twice in index, drop one and reset index
    newtop500 = newtop500.reset_index(level=0,drop=True).reset_index() #level=1

    return new, newtop500


#%% term frequency - inverse document frequency (tf-idf)
def compute_tf_idf_old(dfoverall,dfbyparty,topn):

    # how many parties have used a particular phrase
    byparty_freq = dfbyparty.groupby('Phrase').size()
    dfbyparty_freq = byparty_freq.to_frame()
    dfbyparty_freq = dfbyparty_freq.reset_index()
    dfbyparty_freq.columns = ['Phrase','Freq']

    # merge with byparty counts to compute tf-idf
    new = pd.merge(dfbyparty,dfbyparty_freq,'left','Phrase')
    N = dfbyparty['Speaker Party'].nunique()
    new['N'] = N
    new['tf_idf'] = new.Counts*np.log(new.N/new.Freq)
    new.set_index(['Speaker Party','Phrase'],inplace=True)

    # select phrases with n-largest tf-idf metric
    newtop500 = new.nlargest(topn,'tf_idf')
    # somehow speaker party is contained twice in index, drop one and reset index
    newtop500 = newtop500.reset_index()


    return new, newtop500


#%% filter the top overall phrase counts for each speaker
def select_phrases_from_df(df,newtop500,by_index,dropna=True):

    name0 = '_'.join(by_index)
    name1 = 'Counts' + name0
    top500 = pd.merge(df,newtop500,'inner', 'Phrase',suffixes=(name0,''))

    # restructure table with phrase counts as columns and index set by 'by_index'
    term5_top500_byindex = pd.pivot_table(top500, values = name1, index=by_index, columns = 'Phrase',fill_value = 0, dropna=dropna).reset_index()

    return term5_top500_byindex, top500 

#%% filter the top byparty phrase counts for each speaker, such that intersection between parties' phrases are allowed and counted
def select_phrases_from_df2(df,newtop500,by_index,dropna=True):

    top500 = pd.merge(df,newtop500.drop('Speaker Party',axis=1),'inner','Phrase',suffixes=('','_2'))

    # restructure table with phrase counts as columns and index set by 'by_index'
    term5_top500_byindex = pd.pivot_table(top500, values = 'Counts', index=by_index, columns = 'Phrase',dropna=dropna,fill_value = 0).reset_index()

    return term5_top500_byindex, top500

#%% filter the top byparty phrase counts for each speaker with only the own party phrases (each party has excactly e.g. 500 phrase counts)
# makes no sense, can just map positve phrase count to party an perfectly predict party affiliation
def select_phrases_from_df3(df,newtop500,by_index,dropna=True):

    # name0 = '_'.join(by_index)
    # name1 = 'Counts' + name0
    top500 = pd.merge(df,newtop500,'inner', ['Speaker Party','Phrase'],suffixes=('','_2'))

    # restructure table with phrase counts as columns and index set by 'by_index'
    term5_top500_byindex = pd.pivot_table(top500, values = 'Counts', index=by_index, columns = 'Phrase',dropna=dropna,fill_value = 0).reset_index()

    return term5_top500_byindex

# %%
def share(series):
    integer_part = series.drop(['Speaker','Speaker Party'])
    m = integer_part.sum()
    if m > 0:
        integer_part = integer_part /m
    return series[['Speaker','Speaker Party']].append(integer_part)

# %%
def make_share(df,scale=True):
    df2 = df.drop(['Speaker','Speaker Party'],axis=1)
    df2 = df2.div(df2.sum(axis=1), axis=0).fillna(0)

    if scale:
        scaler = StandardScaler()
        df2[df2.columns] = scaler.fit_transform(df2)

    df_final = pd.concat([df[['Speaker','Speaker Party']],df2],axis=1)

    return df_final



# %% MAYBE filter bi-gram dicts before summing w.r.t speaker/party tp reduce memory space needed


# phrases = set(overall.Phrase.head(100))

def filter_dict(d,keys):
    filtered_dict = {k:v for (k,v) in d.items() if k in keys}
        
    return Counter(filtered_dict)

# filt_speech = test.apply(lambda x: filter_dict(x['Speech'], phrases), axis=1)
# filt_speech.to_csv('./test_filt.csv')