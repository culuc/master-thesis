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
# dfbyparty=dfbyparty[dfbyparty['Speaker Party'].isin(parties2)]
#%%
dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties2)]

#%%
dfoverall = dfbyparty.groupby('Phrase').sum()
dfoverall.reset_index(inplace=True)
#%%
term1_tf, term1topN_tf = m.compute_tf_idf_old(dfoverall,dfbyparty,500)
#%%
term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties2)]

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
