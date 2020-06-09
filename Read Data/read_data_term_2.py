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
data2 = m.preprocess_data(alldata, 'Term', 2)
# del alldata
# %%
data2.drop(columns=['Date','Session','Term','Topic','Language'],inplace=True)

# %%
overall = m.collect_all(data2)
#%%
by_party = m.collect_by(data2, ['Speaker Party'])
#%%
by_party_speaker = m.collect_by(data2, ['Speaker Party','Speaker'])


#%% save to overal
overall.to_csv('../../interim/t2_overall.csv')
overall.to_pickle('../../interim/t2_overall.pkl')
overall.to_json('../../interim/t2_overall.json')
#%% save to byparty
by_party.to_csv('../../interim/t2_byParty.csv')
by_party.to_pickle('../../interim/t2_byParty.pkl')
by_party.to_json('../../interim/t2_byParty.json')
#%% save to by party speaker
by_party_speaker.to_csv('../../interim/t2_byPartySpeaker.csv')
by_party_speaker.to_pickle('../../interim/t2_byPartySpeaker.pkl')
by_party_speaker.to_json('../../interim/t2_byPartySpeaker.json')