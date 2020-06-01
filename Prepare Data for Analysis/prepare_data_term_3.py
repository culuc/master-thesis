import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
#%%
%mkdir ../Data/term3
%mkdir ../Data/term3/tfidf
%mkdir ../Data/term3/cap
#%%
dfoverall3 = pd.read_pickle('../../interim/t3_overall.pkl')
#%%
dfbyparty3 = pd.read_pickle('../../interim/t3_byParty.pkl')

#%%
dfbypartyspeaker3 = pd.read_pickle('../../interim/t3_byPartySpeaker.pkl')
#%%
term3_tf, term3top500_tf = m.compute_tf_idf(dfoverall3,dfbyparty3,500)

#%%
# term3_tf, term3top1000_tf = compute_tf_idf(dfoverall3,dfbyparty3,1000)
term3top1000_tf = term3_tf.nlargest(1000,'tf_idf')

# %%
term3_top500_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker3,term3top500_tf,['Speaker Party','Speaker'])
term3_top500_bySpeakerParty.shape
# %%
term3_top1000_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker3,term3top1000_tf,['Speaker Party','Speaker'])
term3_top1000_bySpeakerParty.shape


# %% include phrases mentioned at least 20 times -> 12'433 w
dfoverall3cap20 = dfoverall3[dfoverall3.Counts >= 20]

# %% include phrases mentioned at least 50 times -> 3'043 w
dfoverall3cap50 = dfoverall3[dfoverall3.Counts >= 50]

# %% include phrases mentioned at least 100 times -> 991 w
dfoverall3cap100 = dfoverall3[dfoverall3.Counts >= 100]

#%%
term3_cap20_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker3,dfoverall3cap20,['Speaker Party','Speaker'])
term3_cap20_bySpeakerParty.shape
#%%
term3_cap50_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker3,dfoverall3cap50,['Speaker Party','Speaker'])
term3_cap50_bySpeakerParty.shape
#%%
term3_cap100_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker3,dfoverall3cap100,['Speaker Party','Speaker'])
term3_cap100_bySpeakerParty.shape


# %% tfidf top 500
term3_top500_bySpeakerParty_scaled = m.make_share(term3_top500_bySpeakerParty)
term3_top500_bySpeakerParty_share = m.make_share(term3_top500_bySpeakerParty, scale=False)
# %% tfidf top 1000
term3_top1000_bySpeakerParty_scaled = m.make_share(term3_top1000_bySpeakerParty)
term3_top1000_bySpeakerParty_share = m.make_share(term3_top1000_bySpeakerParty, scale=False)
#%% cap20
term3_cap20_scaled = m.make_share(term3_cap20_bySpeakerParty)
term3_cap20_share = m.make_share(term3_cap20_bySpeakerParty, scale=False)

#%% cap50
term3_cap50_scaled = m.make_share(term3_cap50_bySpeakerParty)
term3_cap50_share = m.make_share(term3_cap50_bySpeakerParty, scale=False)

#%% cap 100
term3_cap100_scaled = m.make_share(term3_cap100_bySpeakerParty)
term3_cap100_share = m.make_share(term3_cap100_bySpeakerParty, scale=False)

# %% save results
term3_top500_bySpeakerParty.to_csv('../Data/term3/tfidf/term3_top500_bySpeakerParty.csv')
term3_top500_bySpeakerParty_scaled.to_csv('../Data/term3/tfidf/term3_top500_scaled.csv')
term3_top500_bySpeakerParty_share.to_csv('../Data/term3/tfidf/term3_top500_share.csv')
# %%
term3_top1000_bySpeakerParty.to_csv('../Data/term3/tfidf/term3_top1000_bySpeakerParty.csv')
term3_top1000_bySpeakerParty_scaled.to_csv('../Data/term3/tfidf/term3_top1000_scaled.csv')
term3_top1000_bySpeakerParty_share.to_csv('../Data/term3/tfidf/term3_top1000_share.csv')
# %%
term3_cap20_bySpeakerParty.to_csv('../Data/term3/cap/term3_cap20_bySpeakerParty.csv')
term3_cap20_scaled.to_csv('../Data/term3/cap/term3_cap20_scaled.csv')
term3_cap20_share.to_csv('../Data/term3/cap/term3_cap20_share.csv')
# %%
term3_cap50_bySpeakerParty.to_csv('../Data/term3/cap/term3_cap50_bySpeakerParty.csv')
term3_cap50_scaled.to_csv('../Data/term3/cap/term3_cap50_scaled.csv')
term3_cap50_share.to_csv('../Data/term3/cap/term3_cap50_share.csv')
# %%
term3_cap100_bySpeakerParty.to_csv('../Data/term3/cap/term3_cap100_bySpeakerParty.csv')
term3_cap100_scaled.to_csv('../Data/term3/cap/term3_cap100_scaled.csv')
term3_cap100_share.to_csv('../Data/term3/cap/term3_cap100_share.csv')


# %%
