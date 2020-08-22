#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
import numpy as np
import ast

#%% snakemake.input[0]
print(len(sys.argv))
print(sys.argv)

l = len(sys.argv)

in_len = int((l-3)/4)
print(in_len)
in_data = {}
N = ast.literal_eval(sys.argv[1+in_len])
n = ast.literal_eval(sys.argv[2+in_len])

p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties = [p1,p2,p3,p4]

pp1 = pd.read_pickle('../Data/lookup_files/procedural_phrases.pkl')



for i in range(in_len):
    dfbypartyspeaker = pd.read_pickle(sys.argv[1+i])

    if not n is None:
        parties = parties[:n]
        dfbypartyspeaker = dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties)]

    dfbypartyspeaker_filt = dfbypartyspeaker[dfbypartyspeaker.Phrase.isin(pp1).apply(lambda x: not x)]
    #%%
    dfbypartyspeaker_filt=dfbypartyspeaker_filt[dfbypartyspeaker_filt.Counts > N]
    # %%

    dftable = dfbypartyspeaker_filt.pivot_table(index=['Speaker Party','Speaker'],columns='Phrase',values='Counts')


    dftable=dftable.fillna(0)
    dftable.reset_index(inplace=True)

    dftable_scaled = m.make_share(dftable)
    dftable_share = m.make_share(dftable, scale=False)

    dftable.to_csv(sys.argv[in_len+3+i*3])
    dftable_scaled.to_csv(sys.argv[in_len+4+i*3])
    dftable_share.to_csv(sys.argv[in_len+5+i*3])

# dfbypartyspeaker = pd.read_pickle('../../interim/t5_byPartySpeaker.pkl')
#%%


#%%

# pp2 = pd.read_pickle('procedural_phrases_SpSvpDistinct.pkl')


# %% tfidf top 500
