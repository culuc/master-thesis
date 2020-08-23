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
data = m.preprocess_data(alldata, 'Term', 3)
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
data_e = data.reset_index().rename({'index':'SpeechID'})
by_party_speaker_speech = m.collect_by(data_e, ['Speaker Party','Speaker','SpeechID'])

#%% save to overal
overall.to_csv('../../interim/t3_overall.csv')
overall.to_pickle('../../interim/t3_overall.pkl')
overall.to_json('../../interim/t3_overall.json')
#%% save to byparty
by_party.to_csv('../../interim/t3_byParty.csv')
by_party.to_pickle('../../interim/t3_byParty.pkl')
by_party.to_json('../../interim/t3_byParty.json')
#%% save to by party speaker
by_party_speaker.to_csv('../../interim/t3_byPartySpeaker.csv')
by_party_speaker.to_pickle('../../interim/t3_byPartySpeaker.pkl')
by_party_speaker.to_json('../../interim/t3_byPartySpeaker.json')
#%% save to by party speaker speech
by_party_speaker.to_pickle('../../interim/t3_byPartySpeakerSpeech.pkl')
