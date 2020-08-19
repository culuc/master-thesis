#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd

#%% snakemake.input[0]
dfoverall = pd.read_pickle(sys.argv[1])
#%%
dfbyparty = pd.read_pickle(sys.argv[2])
#%%
# dfbypartyspeaker = pd.read_pickle(sys.argv[3])
pp1 = pd.read_pickle('../Data/lookup_files/procedural_phrases.pkl')
# pp2 = pd.read_pickle('procedural_phrases_SpSvpDistinct.pkl')
dfbyparty_filt = dfbyparty[dfbyparty.Phrase.isin(pp1).apply(lambda x: not x)]
#%%
term1_tf, term1topN_tf = m.compute_tf_idf2(dfoverall,dfbyparty_filt,100)

# %% save interim results
term1_tf.to_pickle(sys.argv[3])
term1topN_tf.to_csv(sys.argv[4])
