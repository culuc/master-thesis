#%%
import sys
sys.path.append('../../Modules')
#%%
import modules as m
import pandas as pd

#%%
# dfoverall = pd.read_pickle(sys.argv[1])
#%%
dfbyparty = pd.read_pickle(sys.argv[1])
#%%
pp1 = pd.read_pickle('../../Data/lookup_files/procedural_phrases.pkl')
# pp2 = pd.read_pickle('../procedural_phrases_SpSvpDistinct.pkl')
dfbyparty_filt = dfbyparty[dfbyparty.Phrase.isin(pp1).apply(lambda x: not x)]
#%%
dfbypartyspeaker = pd.read_pickle(sys.argv[2])

#%%
#%%
# parties = sys.argv[3]
p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties2 = [p1,p2]
parties4 = [p1,p2,p3,p4]

#%%
# dfbyparty=dfbyparty[dfbyparty['Speaker Party'].isin(parties4)]
#%%
dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties4)]

#%%
dfoverall = dfbyparty.groupby('Phrase').sum()
dfoverall.reset_index(inplace=True)
#%%
term1_tf, term1topN_tf = m.compute_tf_idf_old(dfoverall,dfbyparty_filt,500)
#%%
term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties4)]
# %%
term1_topN_bySpeakerParty, topN = m.select_phrases_from_df2(dfbypartyspeaker,term1topN_tf,['Speaker Party','Speaker'])


# %% tfidf top 500
term1_topN_bySpeakerParty_scaled = m.make_share(term1_topN_bySpeakerParty)
term1_topN_bySpeakerParty_share = m.make_share(term1_topN_bySpeakerParty, scale=False)

# %% save results
term1_topN_bySpeakerParty.to_csv(sys.argv[3])
term1_topN_bySpeakerParty_scaled.to_csv(sys.argv[4])
term1_topN_bySpeakerParty_share.to_csv(sys.argv[5])

# %% save interim results
term1_tf.to_pickle(sys.argv[6])
term1topN_tf.to_csv(sys.argv[7])
