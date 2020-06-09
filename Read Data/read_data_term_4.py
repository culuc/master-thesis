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
data4 = m.preprocess_data(alldata, 'Term', 4)
# del alldata
# %%
data4.drop(columns=['Date','Session','Term','Topic','Language'],inplace=True)

# %%
overall = m.collect_all(data4)
#%%
by_party = m.collect_by(data4, ['Speaker Party'])
#%%
by_party_speaker = m.collect_by(data4, ['Speaker Party','Speaker'])


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
