#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
import ast
#%% snakemake.input[0]
#%%
dfbyparty = pd.read_pickle('../../interim/all_byParty.pkl')
#&&
pp1 = pd.read_pickle('procedural_phrases.pkl')
# pp2 = pd.read_pickle('procedural_phrases_SpSvpDistinct.pkl')
dfbyparty_filt = dfbyparty[dfbyparty.Phrase.isin(pp1).apply(lambda x: not x)]
#%%
# n = ast.literal_eval(sys.argv[3])
n=2
# topN = ast.literal_eval(sys.argv[4])
topN = 1000
#%%
p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties = [p1,p2,p3,p4]
parties = parties[:n]
print(parties)
#%%
# dfbypartyspeaker = pd.read_pickle(sys.argv[3])
# dfbyparty_filtered=dfbyparty[dfbyparty['Speaker Party'].isin(parties)]
#%%
# term1_tf, term1topN_tf = m.compute_tf_idf2(dfoverall,dfbyparty_filt,topN)
dfnew,quisq_topN = m.compute_qui_sqrd(dfbyparty_filt,1000)
#%%
# term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties2)]
# %%

#%%
# term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties)]


# %% save interim results
dfnew.to_pickle('./P2/allterms_quisq.pkl')
quisq_topN.to_csv('./P2/phrases_quisq_top1k.csv')
