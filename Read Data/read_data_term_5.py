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
data5 = m.preprocess_data(alldata, 'Term', 5)
# del alldata
# %%
data5.drop(columns=['Date','Session','Term','Topic','Language'],inplace=True)

# %%
overall = m.collect_all(data5)
#%%
by_party = m.collect_by(data5, ['Speaker Party'])
#%%
by_party_speaker = m.collect_by(data5, ['Speaker Party','Speaker'])


#%% save to overall
overall.to_csv('../../interim/t5_overall.csv')
overall.to_pickle('../../interim/t5_overall.pkl')
overall.to_json('../../interim/t5_overall.json')
#%% save to byparty
by_party.to_csv('../../interim/t5_byParty.csv')
by_party.to_pickle('../../interim/t5_byParty.pkl')
by_party.to_json('../../interim/t5_byParty.json')
#%% save to by party speaker
by_party_speaker.to_csv('../../interim/t5_byPartySpeaker.csv')
by_party_speaker.to_pickle('../../interim/t5_byPartySpeaker.pkl')
by_party_speaker.to_json('../../interim/t5_byPartySpeaker.json')
