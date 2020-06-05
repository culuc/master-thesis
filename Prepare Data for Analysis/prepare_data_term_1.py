import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
# 1(?!\d)
#%% works only for jupyter noteoooks
%mkdir ../Data/term1
%mkdir ../Data/term1/tfidf
%mkdir ../Data/term1/cap
#%%
dfoverall1 = pd.read_pickle('../../interim/t1_overall.pkl')
#%%
dfbyparty1 = pd.read_pickle('../../interim/t1_byParty.pkl')

#%%
dfbypartyspeaker1 = pd.read_pickle('../../interim/t1_byPartySpeaker.pkl')
#%%
term1_tf, term1top500_tf = m.compute_tf_idf(dfoverall1,dfbyparty1,500)

#%%
# term1_tf, term1top1000_tf = compute_tf_idf(dfoverall1,dfbyparty1,1000)
term1top1000_tf = term1_tf.nlargest(1000,'tf_idf')

# %%
term1_top500_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker1,term1top500_tf,['Speaker Party','Speaker'])
term1_top500_bySpeakerParty.shape
# %%
term1_top1000_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker1,term1top1000_tf,['Speaker Party','Speaker'])
term1_top1000_bySpeakerParty.shape


# %% include phrases mentioned at least 20 times -> 11'433 w
dfoverall1cap20 = dfoverall1[dfoverall1.Counts >= 20]

# %% include phrases mentioned at least 50 times -> 3'041 w
dfoverall1cap50 = dfoverall1[dfoverall1.Counts >= 50]

# %% include phrases mentioned at least 100 times -> 991 w
dfoverall1cap100 = dfoverall1[dfoverall1.Counts >= 100]

#%%
term1_cap20_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker1,dfoverall1cap20,['Speaker Party','Speaker'])
term1_cap20_bySpeakerParty.shape
#%%
term1_cap50_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker1,dfoverall1cap50,['Speaker Party','Speaker'])
term1_cap50_bySpeakerParty.shape
#%%
term1_cap100_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker1,dfoverall1cap100,['Speaker Party','Speaker'])
term1_cap100_bySpeakerParty.shape


# %% tfidf top 500
term1_top500_bySpeakerParty_scaled = m.make_share(term1_top500_bySpeakerParty)
term1_top500_bySpeakerParty_share = m.make_share(term1_top500_bySpeakerParty, scale=False)
# %% tfidf top 1000
term1_top1000_bySpeakerParty_scaled = m.make_share(term1_top1000_bySpeakerParty)
term1_top1000_bySpeakerParty_share = m.make_share(term1_top1000_bySpeakerParty, scale=False)
#%% cap20
term1_cap20_scaled = m.make_share(term1_cap20_bySpeakerParty)
term1_cap20_share = m.make_share(term1_cap20_bySpeakerParty, scale=False)

#%% cap50
term1_cap50_scaled = m.make_share(term1_cap50_bySpeakerParty)
term1_cap50_share = m.make_share(term1_cap50_bySpeakerParty, scale=False)

#%% cap 100
term1_cap100_scaled = m.make_share(term1_cap100_bySpeakerParty)
term1_cap100_share = m.make_share(term1_cap100_bySpeakerParty, scale=False)

# %% save results
term1_top500_bySpeakerParty.to_csv('../Data/term1/tfidf/term1_top500_bySpeakerParty.csv')
term1_top500_bySpeakerParty_scaled.to_csv('../Data/term1/tfidf/term1_top500_scaled.csv')
term1_top500_bySpeakerParty_share.to_csv('../Data/term1/tfidf/term1_top500_share.csv')
# %%
term1_top1000_bySpeakerParty.to_csv('../Data/term1/tfidf/term1_top1000_bySpeakerParty.csv')
term1_top1000_bySpeakerParty_scaled.to_csv('../Data/term1/tfidf/term1_top1000_scaled.csv')
term1_top1000_bySpeakerParty_share.to_csv('../Data/term1/tfidf/term1_top1000_share.csv')
# %%
term1_cap20_bySpeakerParty.to_csv('../Data/term1/cap/term1_cap20_bySpeakerParty.csv')
term1_cap20_scaled.to_csv('../Data/term1/cap/term1_cap20_scaled.csv')
term1_cap20_share.to_csv('../Data/term1/cap/term1_cap20_share.csv')
# %%
term1_cap50_bySpeakerParty.to_csv('../Data/term1/cap/term1_cap50_bySpeakerParty.csv')
term1_cap50_scaled.to_csv('../Data/term1/cap/term1_cap50_scaled.csv')
term1_cap50_share.to_csv('../Data/term1/cap/term1_cap50_share.csv')
# %%
term1_cap100_bySpeakerParty.to_csv('../Data/term1/cap/term1_cap100_bySpeakerParty.csv')
term1_cap100_scaled.to_csv('../Data/term1/cap/term1_cap100_scaled.csv')
term1_cap100_share.to_csv('../Data/term1/cap/term1_cap100_share.csv')
