import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
# 2(?!\d)
#%% works only for jupyter noteoooks
%mkdir ../Data/term2
%mkdir ../Data/term2/tfidf
%mkdir ../Data/term2/cap
#%%
dfoverall2 = pd.read_pickle('../../interim/t2_overall.pkl')
#%%
dfbyparty2 = pd.read_pickle('../../interim/t2_byParty.pkl')

#%%
dfbypartyspeaker2 = pd.read_pickle('../../interim/t2_byPartySpeaker.pkl')
#%%
term2_tf, term2top500_tf = m.compute_tf_idf(dfoverall2,dfbyparty2,500)

#%%
# term2_tf, term2top1000_tf = compute_tf_idf(dfoverall2,dfbyparty2,1000)
term2top1000_tf = term2_tf.nlargest(1000,'tf_idf')

# %%
term2_top500_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker2,term2top500_tf,['Speaker Party','Speaker'])
term2_top500_bySpeakerParty.shape
# %%
term2_top1000_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker2,term2top1000_tf,['Speaker Party','Speaker'])
term2_top1000_bySpeakerParty.shape


# %% include phrases mentioned at least 20 times -> 12'433 w
dfoverall2cap20 = dfoverall2[dfoverall2.Counts >= 20]

# %% include phrases mentioned at least 50 times -> 3'042 w
dfoverall2cap50 = dfoverall2[dfoverall2.Counts >= 50]

# %% include phrases mentioned at least 100 times -> 991 w
dfoverall2cap100 = dfoverall2[dfoverall2.Counts >= 100]

#%%
term2_cap20_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker2,dfoverall2cap20,['Speaker Party','Speaker'])
term2_cap20_bySpeakerParty.shape
#%%
term2_cap50_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker2,dfoverall2cap50,['Speaker Party','Speaker'])
term2_cap50_bySpeakerParty.shape
#%%
term2_cap100_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker2,dfoverall2cap100,['Speaker Party','Speaker'])
term2_cap100_bySpeakerParty.shape


# %% tfidf top 500
term2_top500_bySpeakerParty_scaled = m.make_share(term2_top500_bySpeakerParty)
term2_top500_bySpeakerParty_share = m.make_share(term2_top500_bySpeakerParty, scale=False)
# %% tfidf top 1000
term2_top1000_bySpeakerParty_scaled = m.make_share(term2_top1000_bySpeakerParty)
term2_top1000_bySpeakerParty_share = m.make_share(term2_top1000_bySpeakerParty, scale=False)
#%% cap20
term2_cap20_scaled = m.make_share(term2_cap20_bySpeakerParty)
term2_cap20_share = m.make_share(term2_cap20_bySpeakerParty, scale=False)

#%% cap50
term2_cap50_scaled = m.make_share(term2_cap50_bySpeakerParty)
term2_cap50_share = m.make_share(term2_cap50_bySpeakerParty, scale=False)

#%% cap 100
term2_cap100_scaled = m.make_share(term2_cap100_bySpeakerParty)
term2_cap100_share = m.make_share(term2_cap100_bySpeakerParty, scale=False)

# %% save results
term2_top500_bySpeakerParty.to_csv('../Data/term2/tfidf/term2_top500_bySpeakerParty.csv')
term2_top500_bySpeakerParty_scaled.to_csv('../Data/term2/tfidf/term2_top500_scaled.csv')
term2_top500_bySpeakerParty_share.to_csv('../Data/term2/tfidf/term2_top500_share.csv')
# %%
term2_top1000_bySpeakerParty.to_csv('../Data/term2/tfidf/term2_top1000_bySpeakerParty.csv')
term2_top1000_bySpeakerParty_scaled.to_csv('../Data/term2/tfidf/term2_top1000_scaled.csv')
term2_top1000_bySpeakerParty_share.to_csv('../Data/term2/tfidf/term2_top1000_share.csv')
# %%
term2_cap20_bySpeakerParty.to_csv('../Data/term2/cap/term2_cap20_bySpeakerParty.csv')
term2_cap20_scaled.to_csv('../Data/term2/cap/term2_cap20_scaled.csv')
term2_cap20_share.to_csv('../Data/term2/cap/term2_cap20_share.csv')
# %%
term2_cap50_bySpeakerParty.to_csv('../Data/term2/cap/term2_cap50_bySpeakerParty.csv')
term2_cap50_scaled.to_csv('../Data/term2/cap/term2_cap50_scaled.csv')
term2_cap50_share.to_csv('../Data/term2/cap/term2_cap50_share.csv')
# %%
term2_cap100_bySpeakerParty.to_csv('../Data/term2/cap/term2_cap100_bySpeakerParty.csv')
term2_cap100_scaled.to_csv('../Data/term2/cap/term2_cap100_scaled.csv')
term2_cap100_share.to_csv('../Data/term2/cap/term2_cap100_share.csv')
