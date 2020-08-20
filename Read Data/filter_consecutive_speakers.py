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

cons_speakers = pd.read_csv('../Data/lookup_files/speaker_terms_servetime_consecutive_years.csv')
cons_speakers = set(cons_speakers.Speaker)
# %mkdir '../../interim/consecutive_speakers'
for i in range(1,2):
    byPartySpeaker = pd.read_pickle('../../interim/t'+str(i)+'_byPartySpeaker.pkl')
    byPartySpeaker = byPartySpeaker[byPartySpeaker.Speaker.isin(cons_speakers)]

    byParty = byPartySpeaker.groupby(['Speaker Party','Phrase']).sum().sort_values(['Speaker Party','Counts'],ascending=False).reset_index()
    overall = byParty.groupby('Phrase').sum().sort_values(['Counts'],ascending=False).reset_index()

    byPartySpeaker.to_pickle('../../interim/consecutive_speakers/t'+str(i)+'_byPartySpeaker.pkl')
    byParty.to_pickle('../../interim/consecutive_speakers/t'+str(i)+'_byParty.pkl')
    overall.to_pickle('../../interim/consecutive_speakers/t'+str(i)+'_overall.pkl')


#new[new.Speaker.isin(cons_speakers)]

# old = pd.read_pickle('../../interim/t1_overall.pkl')
#new = pd.read_pickle('../../interim/consecutive_speakers/t1_byPartySpeaker.pkl')

#new
#set(old.Speaker)- cons_speakers
#set(new.Speaker)-cons_speakers
