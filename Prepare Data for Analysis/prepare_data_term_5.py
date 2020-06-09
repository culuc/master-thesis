import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
# 4(?!\d)
#%%
%mkdir ../Data/term5
%mkdir ../Data/term5/tfidf
%mkdir ../Data/term5/cap
#%%
dfoverall5 = pd.read_pickle('../../interim/t5_overall.pkl')
#%%
dfbyparty5 = pd.read_pickle('../../interim/t5_byParty.pkl')

#%%
dfbypartyspeaker5 = pd.read_pickle('../../interim/t5_byPartySpeaker.pkl')
#%%
term5_tf, term5top500_tf = m.compute_tf_idf(dfoverall5,dfbyparty5,500)

#%%
# term5_tf, term5top1000_tf = compute_tf_idf(dfoverall5,dfbyparty5,1000)
term5top1000_tf = term5_tf.nlargest(1000,'tf_idf')

# %%
term5_top500_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker5,term5top500_tf,['Speaker Party','Speaker'])
term5_top500_bySpeakerParty.shape
# %%
term5_top1000_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker5,term5top1000_tf,['Speaker Party','Speaker'])
term5_top1000_bySpeakerParty.shape


# %% include phrases mentioned at least 20 times -> 12'433 w
dfoverall5cap20 = dfoverall5[dfoverall5.Counts >= 20]

# %% include phrases mentioned at least 50 times -> 3'044 w
dfoverall5cap50 = dfoverall5[dfoverall5.Counts >= 50]

# %% include phrases mentioned at least 100 times -> 991 w
dfoverall5cap100 = dfoverall5[dfoverall5.Counts >= 100]

#%%
term5_cap20_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker5,dfoverall5cap20,['Speaker Party','Speaker'])
term5_cap20_bySpeakerParty.shape
#%%
term5_cap50_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker5,dfoverall5cap50,['Speaker Party','Speaker'])
term5_cap50_bySpeakerParty.shape
#%%
term5_cap100_bySpeakerParty = m.select_phrases_from_df(dfbypartyspeaker5,dfoverall5cap100,['Speaker Party','Speaker'])
term5_cap100_bySpeakerParty.shape


# %% tfidf top 500
term5_top500_bySpeakerParty_scaled = m.make_share(term5_top500_bySpeakerParty)
term5_top500_bySpeakerParty_share = m.make_share(term5_top500_bySpeakerParty, scale=False)
# %% tfidf top 1000
term5_top1000_bySpeakerParty_scaled = m.make_share(term5_top1000_bySpeakerParty)
term5_top1000_bySpeakerParty_share = m.make_share(term5_top1000_bySpeakerParty, scale=False)
#%% cap20
term5_cap20_scaled = m.make_share(term5_cap20_bySpeakerParty)
term5_cap20_share = m.make_share(term5_cap20_bySpeakerParty, scale=False)

#%% cap50
term5_cap50_scaled = m.make_share(term5_cap50_bySpeakerParty)
term5_cap50_share = m.make_share(term5_cap50_bySpeakerParty, scale=False)

#%% cap 100
term5_cap100_scaled = m.make_share(term5_cap100_bySpeakerParty)
term5_cap100_share = m.make_share(term5_cap100_bySpeakerParty, scale=False)

# %% save results
term5_top500_bySpeakerParty.to_csv('../Data/term5/tfidf/term5_top500_bySpeakerParty.csv')
term5_top500_bySpeakerParty_scaled.to_csv('./Data./term5/tfidf/term5_top500_scaled.csv')
term5_top500_bySpeakerParty_share.to_csv('../Data/term5/tfidf/term5_top500_share.csv')
# %%
term5_top1000_bySpeakerParty.to_csv('../Data/term5/tfidf/term5_top1000_bySpeakerParty.csv')
term5_top1000_bySpeakerParty_scaled.to_csv('../Data/term5/tfidf/term5_top1000_scaled.csv')
term5_top1000_bySpeakerParty_share.to_csv('../Data/term5/tfidf/term5_top1000_share.csv')
# %%
term5_cap20_bySpeakerParty.to_csv('../Data/term5/cap/term5_cap20_bySpeakerParty.csv')
term5_cap20_scaled.to_csv('../Data/term5/cap/term5_cap20_scaled.csv')
term5_cap20_share.to_csv('../Data/term5/cap/term5_cap20_share.csv')
# %%
term5_cap50_bySpeakerParty.to_csv('../Data/term5/cap/term5_cap50_bySpeakerParty.csv')
term5_cap50_scaled.to_csv('../Data/term5/cap/term5_cap50_scaled.csv')
term5_cap50_share.to_csv('../Data/term5/cap/term5_cap50_share.csv')
# %%
term5_cap100_bySpeakerParty.to_csv('../Data/term5/cap/term5_cap100_bySpeakerParty.csv')
term5_cap100_scaled.to_csv('../Data/term5/cap/term5_cap100_scaled.csv')
term5_cap100_share.to_csv('../Data/term5/cap/term5_cap100_share.csv')
