import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
# 4(?!\d)
#%%
%mkdir ../Data/term4
%mkdir ../Data/term4/tfidf
%mkdir ../Data/term4/cap
#%%
dfoverall4 = pd.read_pickle('../../interim/t4_overall.pkl')
#%%
dfbyparty4 = pd.read_pickle('../../interim/t4_byParty.pkl')

#%%
dfbypartyspeaker4 = pd.read_pickle('../../interim/t4_byPartySpeaker.pkl')
#%%
term4_tf, term4top500_tf = m.compute_tf_idf(dfoverall4,dfbyparty4,500)

#%%
# term4_tf, term4top1000_tf = compute_tf_idf(dfoverall4,dfbyparty4,1000)
term4top1000_tf = term4_tf.nlargest(1000,'tf_idf')

# %%
term4_top500_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker4,term4top500_tf,['Speaker Party','Speaker'])
term4_top500_bySpeakerParty.shape
# %%
term4_top1000_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker4,term4top1000_tf,['Speaker Party','Speaker'])
term4_top1000_bySpeakerParty.shape


# %% include phrases mentioned at least 20 times -> 12'433 w
dfoverall4cap20 = dfoverall4[dfoverall4.Counts >= 20]

# %% include phrases mentioned at least 50 times -> 3'044 w
dfoverall4cap50 = dfoverall4[dfoverall4.Counts >= 50]

# %% include phrases mentioned at least 100 times -> 991 w
dfoverall4cap100 = dfoverall4[dfoverall4.Counts >= 100]

#%%
term4_cap20_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker4,dfoverall4cap20,['Speaker Party','Speaker'])
term4_cap20_bySpeakerParty.shape
#%%
term4_cap50_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker4,dfoverall4cap50,['Speaker Party','Speaker'])
term4_cap50_bySpeakerParty.shape
#%%
term4_cap100_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker4,dfoverall4cap100,['Speaker Party','Speaker'])
term4_cap100_bySpeakerParty.shape


# %% tfidf top 500
term4_top500_bySpeakerParty_scaled = m.make_share(term4_top500_bySpeakerParty)
term4_top500_bySpeakerParty_share = m.make_share(term4_top500_bySpeakerParty, scale=False)
# %% tfidf top 1000
term4_top1000_bySpeakerParty_scaled = m.make_share(term4_top1000_bySpeakerParty)
term4_top1000_bySpeakerParty_share = m.make_share(term4_top1000_bySpeakerParty, scale=False)
#%% cap20
term4_cap20_scaled = m.make_share(term4_cap20_bySpeakerParty)
term4_cap20_share = m.make_share(term4_cap20_bySpeakerParty, scale=False)

#%% cap50
term4_cap50_scaled = m.make_share(term4_cap50_bySpeakerParty)
term4_cap50_share = m.make_share(term4_cap50_bySpeakerParty, scale=False)

#%% cap 100
term4_cap100_scaled = m.make_share(term4_cap100_bySpeakerParty)
term4_cap100_share = m.make_share(term4_cap100_bySpeakerParty, scale=False)

# %% save results
term4_top500_bySpeakerParty.to_csv('../Data/term4/tfidf/term4_top500_bySpeakerParty.csv')
term4_top500_bySpeakerParty_scaled.to_csv('./Data./term4/tfidf/term4_top500_scaled.csv')
term4_top500_bySpeakerParty_share.to_csv('../Data/term4/tfidf/term4_top500_share.csv')
# %%
term4_top1000_bySpeakerParty.to_csv('../Data/term4/tfidf/term4_top1000_bySpeakerParty.csv')
term4_top1000_bySpeakerParty_scaled.to_csv('../Data/term4/tfidf/term4_top1000_scaled.csv')
term4_top1000_bySpeakerParty_share.to_csv('../Data/term4/tfidf/term4_top1000_share.csv')
# %%
term4_cap20_bySpeakerParty.to_csv('../Data/term4/cap/term4_cap20_bySpeakerParty.csv')
term4_cap20_scaled.to_csv('../Data/term4/cap/term4_cap20_scaled.csv')
term4_cap20_share.to_csv('../Data/term4/cap/term4_cap20_share.csv')
# %%
term4_cap50_bySpeakerParty.to_csv('../Data/term4/cap/term4_cap50_bySpeakerParty.csv')
term4_cap50_scaled.to_csv('../Data/term4/cap/term4_cap50_scaled.csv')
term4_cap50_share.to_csv('../Data/term4/cap/term4_cap50_share.csv')
# %%
term4_cap100_bySpeakerParty.to_csv('../Data/term4/cap/term4_cap100_bySpeakerParty.csv')
term4_cap100_scaled.to_csv('../Data/term4/cap/term4_cap100_scaled.csv')
term4_cap100_share.to_csv('../Data/term4/cap/term4_cap100_share.csv')


# %%
