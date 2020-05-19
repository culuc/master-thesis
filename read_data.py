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
#%%
path = 'SwissParliament/'
elections = pd.read_csv('federal_election_dates.csv')

#%%
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

#%%
# file1 = pd.read_csv(join(path,allfiles[0]))
# fileger = file1[file1.Language == "DE"]
# fileger

# fileg5 = alldata[(alldata.Language == 'DE') & (alldata.Term == 5)]
stemmer = GermanStemmer()

#%%
def preprocess_speech(speech):
    # remove words in brackets and parentheses
    speech = re.sub('((\[VS\]|\[GZ\])(.|\n)*)', '', speech)
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
#%%

def collect_counts(series):
    counter = Counter()
    for d in series:
        counter.update(d)

    result = dict(counter.most_common())

    return result

#%%
def run(alldata, filtervar, criterion, topn):
    # filter data
    print('preprocessing data')
    data = alldata[(alldata.Language == 'DE') & (alldata[filtervar] == criterion)]
    data['Speech'] = data['Speech'].map(preprocess_speech)

    # overall
    print('collecting overall counts')
    overall = collect_counts(data.Speech)
    dfoverall = pd.DataFrame.from_dict(overall, orient = 'index')

    dfoverall = dfoverall.reset_index()
    dfoverall.columns = ['Phrase','Counts']

    # by party
    print('collecting by party counts')
    byparty = data.groupby('Speaker Party').Speech.apply(collect_counts)
    dfbyparty = pd.DataFrame(byparty)
    dfbyparty.index.rename(['Speaker Party','Phrase'],inplace=True)
    dfbyparty.columns = ['Counts']
    dfbypartylong = dfbyparty.reset_index()
    dfbypartylong_nona = dfbypartylong.dropna()
    
    print('Compute Frequency')
    byparty_counts = dfbypartylong_nona.groupby('Phrase').size()
    dfbyparty_counts = byparty_counts.to_frame()
    dfbyparty_counts = dfbyparty_counts.reset_index()
    dfbyparty_counts.columns = ['Phrase','Freq']

    new = pd.merge(dfoverall,dfbyparty_counts,'left','Phrase')
    N = dfbypartylong_nona['Speaker Party'].nunique()
    new['N'] = N
    new['tf_idf'] = new.Counts*np.log(new.N/new.Freq)
    
    newtop500 = new.nlargest(topn,'tf_idf')
    top500 = pd.merge(dfbypartylong_nona,newtop500,'inner','Phrase',suffixes=('_byparty',''))
    top500_2 = top500.pivot(index='Speaker Party', columns='Phrase',values='Counts_byparty').fillna(0)

    return data,dfoverall,dfbypartylong_nona,new,newtop500,top500_2

#%%
# filter data
def preproc(alldata, filtervar, criterion):
    print('preprocessing data')
    data = alldata[(alldata.Language == 'DE') & (alldata[filtervar] == criterion)]
    data['Speech'] = data['Speech'].map(preprocess_speech)

    return data

data5 = preproc(alldata, 'Term', 5)

#%%
# overall
def collect_all(data):
    print('collecting overall counts')
    overall = collect_counts(data.Speech)
    dfoverall = pd.DataFrame.from_dict(overall, orient = 'index')

    dfoverall = dfoverall.reset_index()
    dfoverall.columns = ['Phrase','Counts']

    return dfoverall

dfoverall5 = collect_all(data5)
#%%
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
dfbyparty = collect_by(data5,'Speaker Party')

#%%
dfbypartyspeaker = collect_by(data5,['Speaker Party','Speaker'])
#%%
dfbypartyspeaker.to_csv('./term5/dfbypartyspeaker5.csv')
#%%
def compute_tf_idf(dfoverall, dfbypartylong_nona,topn):
    print('Compute Frequency')
    byparty_counts = dfbypartylong_nona.groupby('Phrase').size()
    dfbyparty_counts = byparty_counts.to_frame()
    dfbyparty_counts = dfbyparty_counts.reset_index()
    dfbyparty_counts.columns = ['Phrase','Freq']

    new = pd.merge(dfoverall,dfbyparty_counts,'left','Phrase')
    N = dfbypartylong_nona['Speaker Party'].nunique()
    new['N'] = N
    new['tf_idf'] = new.Counts*np.log(new.N/new.Freq)
    newtop500 = new.nlargest(topn,'tf_idf')

    return new, newtop500


#%%
def select_phrases_from_df(df,newtop500,by_index,dropna=True):
    name0 = '_'.join(by_index)
    name1 = 'Counts' + name0 
    top500 = pd.merge(df,newtop500,'inner', 'Phrase',suffixes=(name0,''))
    term5_top500_byindex = pd.pivot_table(top500, values = name1, index=by_index, columns = 'Phrase',fill_value = 0, dropna=dropna).reset_index()

    return term5_top500_byindex


#%%
new5, new5top500 = compute_tf_idf(dfoverall5,dfbyparty,500)

# %%
dfbypartyspeaker_top500 = select_phrases_from_df(dfbypartyspeaker,new5top500)

# %%
term5_top500_byspeakerparty = pd.pivot_table(top500, values = 'Counts_byparty', index=['Speaker Party','Speaker'], columns = 'Phrase',fill_value = 0 ).reset_index()

# %%
term5_top500_byspeakerparty.to_csv('./term5/term5_top500_bySpeakerParty.csv')


#%%
new5top10 = new5top500.head(10)

# %%
dfbypartyspeaker_top10 = select_phrases_from_df(dfbypartyspeaker,new5top10,['Speaker Party','Speaker'])


# %%
dfbypartyspeaker_top10.to_csv('./term5/term5_top10_bySpeakerParty.csv')



#%%
new5top100 = new5top500.head(100)

# %%
dfbypartyspeaker_top100 = select_phrases_from_df(dfbypartyspeaker,new5top100,['Speaker Party','Speaker'])


# %%
dfbypartyspeaker_top100.to_csv('./term5/term5_top100_bySpeakerParty.csv')



#%%
new5top15 = new5top500.head(15)

# %%
dfbypartyspeaker_top15 = select_phrases_from_df(dfbypartyspeaker,new5top15,['Speaker Party','Speaker'])


# %%
dfbypartyspeaker_top15.to_csv('./term5/term5_top15_bySpeakerParty.csv')




# %%
dfbypartyspeaker_top500 = select_phrases_from_df(dfbypartyspeaker,new5top500,['Speaker Party','Speaker'],dropna=False)


# %%
dfbypartyspeaker_top500.to_csv('./term5/term5_top500_bySpeakerParty_long.csv')

# %%
dfbypartyspeaker = pd.read_csv('./term5/dfbypartyspeaker5.csv')

# %%
dfbypartyspeaker = pd.read_csv('./term5/dfbypartyspeaker5.csv')


# %%
term5_all = pd.pivot_table(dfbypartyspeaker, values = 'Counts', index=['Speaker Party','Speaker'], columns = 'Phrase',fill_value = 0, dropna=False).reset_index()

# %%
term5_all

# %%
