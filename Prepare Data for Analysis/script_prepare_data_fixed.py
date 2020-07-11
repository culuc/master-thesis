#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
import ast
#%%
dfbypartyspeaker = pd.read_pickle(sys.argv[1])

termtopN_tf = pd.read_csv(sys.argv[2],index_col=0)

# term1topN_tf = pd.read_csv('../Data/fixed/all_terms_tfidf_top100each.csv',)
#%%
termtopN_tf.Phrase = termtopN_tf.Phrase.map(ast.literal_eval)
# %%
term_topN_bySpeakerParty, topN = m.select_phrases_from_df2(dfbypartyspeaker,termtopN_tf,['Speaker Party','Speaker'])

# %% tfidf top 500
term_topN_bySpeakerParty_scaled = m.make_share(term_topN_bySpeakerParty)
term_topN_bySpeakerParty_share = m.make_share(term_topN_bySpeakerParty, scale=False)

term_topN_bySpeakerParty.to_csv(sys.argv[3])
term_topN_bySpeakerParty_scaled.to_csv(sys.argv[4])
term_topN_bySpeakerParty_share.to_csv(sys.argv[5])

# %% save interim results
# term_tf.to_pickle(sys.argv[7])
# termtopN_tf.to_csv(sys.argv[8])
