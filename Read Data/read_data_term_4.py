#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
# %%
# import importlib
#%%
# importlib.reload(m)

#%% set path to speech files, read look-up file for elelction dates
path = '../../SwissParliament/'
elections = pd.read_csv('../Data/lookup_files/federal_election_dates.csv')

# %%
alldata = m.read_data(path)
# %%
alldata = m.compute_term(alldata,elections)

# %%
data = m.preprocess_data(alldata, 'Term', 4)
# del alldata
# %%
data.drop(columns=['Date','Session','Term','Topic','Language'],inplace=True)

# %%
overall = m.collect_all(data)
#%%
by_party = m.collect_by(data, ['Speaker Party'])
#%%
by_party_speaker = m.collect_by(data, ['Speaker Party','Speaker'])
#%%
data = data.reset_index().rename(columns={'index':'SpeechID'})
n = 20000  #chunk row size
list_df = [data[i:i+n] for i in range(0,data.shape[0],n)]
col = m.collect_by(list_df[0], ['Speaker Party','Speaker','SpeechID'])
for df in list_df:
    res = m.collect_by(df, ['Speaker Party','Speaker','SpeechID'])
    col = col.append(res,ignore_index=True)

by_party_speaker_speech = col.sort_values(['Speaker Party','Speaker','Counts'])

#%% save to csv
overall.to_csv('../../interim/t4_overall.csv')
by_party.to_csv('../../interim/t4_byParty.csv')
by_party_speaker.to_csv('../../interim/t4_byPartySpeaker.csv')
#%% save to pickle
overall.to_pickle('../../interim/t4_overall.pkl')
by_party.to_pickle('../../interim/t4_byParty.pkl')
by_party_speaker.to_pickle('../../interim/t4_byPartySpeaker.pkl')
#%% save to json
overall.to_json('../../interim/t4_overall.json')
by_party.to_json('../../interim/t4_byParty.json')
by_party_speaker.to_json('../../interim/t4_byPartySpeaker.json')
#%% save to by party speaker speech
by_party_speaker.to_pickle('../../interim/t4_byPartySpeakerSpeech.pkl')
