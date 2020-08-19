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
dfbypartyspeaker = pd.read_pickle(sys.argv[3])
#%%
pp1 = pd.read_pickle('../Data/lookup_files/procedural_phrases.pkl')
# pp2 = pd.read_pickle('procedural_phrases_SpSvpDistinct.pkl')
dfbyparty_filt = dfbyparty[dfbyparty.Phrase.isin(pp1).apply(lambda x: not x)]
#%%
term1_tf, term1topN_tf = m.compute_tf_idf(dfoverall,dfbyparty_filt,500)

# %%
term1_topN_bySpeakerParty, topN = m.select_phrases_from_df(dfbypartyspeaker,term1topN_tf,['Speaker Party','Speaker'])


# %% tfidf top 500
term1_topN_bySpeakerParty_scaled = m.make_share(term1_topN_bySpeakerParty)
term1_topN_bySpeakerParty_share = m.make_share(term1_topN_bySpeakerParty, scale=False)

term1_topN_bySpeakerParty.to_csv(sys.argv[4])
term1_topN_bySpeakerParty_scaled.to_csv(sys.argv[5])
term1_topN_bySpeakerParty_share.to_csv(sys.argv[6])

# %% save interim results
term1_tf.to_pickle(sys.argv[7])
term1topN_tf.to_csv(sys.argv[8])
