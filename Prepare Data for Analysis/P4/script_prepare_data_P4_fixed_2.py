#%%
import sys
sys.path.append('../../Modules')
#%%
import modules as m
import pandas as pd
import ast
#%%
dfbypartyspeaker = pd.read_pickle(sys.argv[1])

termtopN_tf = pd.read_csv(sys.argv[2],index_col=0)

#%%
termtopN_tf.Phrase = termtopN_tf.Phrase.map(ast.literal_eval)

#%%
# parties = sys.argv[3]
p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties2 = [p1,p2]
parties4 = [p1,p2,p3,p4]

#%%
dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties4)]
# %%
term_topN_bySpeakerParty, topN = m.select_phrases_from_df2(dfbypartyspeaker,termtopN_tf,['Speaker Party','Speaker'])


# %% tfidf top 500
term_topN_bySpeakerParty_scaled = m.make_share(term_topN_bySpeakerParty)
term_topN_bySpeakerParty_share = m.make_share(term_topN_bySpeakerParty, scale=False)

# %% save results
term_topN_bySpeakerParty.to_csv(sys.argv[3])
term_topN_bySpeakerParty_scaled.to_csv(sys.argv[4])
term_topN_bySpeakerParty_share.to_csv(sys.argv[5])

# %% save interim results
# term_tf.to_pickle(sys.argv[7])
# termtopN_tf.to_csv(sys.argv[8])
