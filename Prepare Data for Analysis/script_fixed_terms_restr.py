#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
import ast
#%% snakemake.input[0]
dfoverall = pd.read_pickle(sys.argv[1])
#%%
dfbyparty = pd.read_pickle(sys.argv[2])
#&&
pp1 = pd.read_pickle('../Data/lookup_files/procedural_phrases.pkl')
# pp2 = pd.read_pickle('procedural_phrases_SpSvpDistinct.pkl')
dfbyparty_filt = dfbyparty[dfbyparty.Phrase.isin(pp1).apply(lambda x: not x)]
#%%
n = ast.literal_eval(sys.argv[3])
topN = ast.literal_eval(sys.argv[4])
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
term1_tf, term1topN_tf = m.compute_tf_idf2(dfoverall,dfbyparty_filt,topN)

#%%
term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties)]


# %% save interim results
term1_tf.to_pickle(sys.argv[5])
term1topN_tf.to_csv(sys.argv[6])
