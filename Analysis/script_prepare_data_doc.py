#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
import ast
#%%
l_in = int((len(sys.argv)-2)/5)-1
print(len(sys.argv))
print(l_in)
# dfoverall = pd.read_pickle(sys.argv[1])
level = sys.argv[1]
print(level)
#%%
pp1 = pd.read_pickle('../Data/lookup_files/procedural_phrases.pkl')
p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties2 = [p1,p2]
parties4 = [p1,p2,p3,p4]
#%%

for i in range(1,l_in):
    print(sys.argv[i*2])
    print(sys.argv[i*2+1])
    dftfidf = pd.read_pickle(sys.argv[i])
    dfbypartyspeaker = pd.read_pickle(sys.argv[i+1])

    # dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties4)]
    dftfidf_filt = dftfidf[dftfidf.Phrase.isin(pp1).apply(lambda x: not x)]
    #%%
    term1_tf, term1topN_tf = m.compute_tf_idf_new(dftfidf_filt,level,250)
    #%%
    term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties4)]
    dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties4)]
    # %%
    term1_topN_bySpeakerParty, topN = m.select_phrases_from_df2(dfbypartyspeaker,term1topN_tf,['Speaker Party','Speaker'])

    # %% tfidf top 500
    term1_topN_bySpeakerParty_scaled = m.make_share(term1_topN_bySpeakerParty)
    term1_topN_bySpeakerParty_share = m.make_share(term1_topN_bySpeakerParty, scale=False)

    # %% save result
    print(sys.argv[l_in*2+1+(i-1)*5])
    # print(sys.argv)
    term1_topN_bySpeakerParty.to_csv(sys.argv[l_in*2+2+(i-1)*5])
    term1_topN_bySpeakerParty_scaled.to_csv(sys.argv[l_in*2+3+(i-1)*5])
    term1_topN_bySpeakerParty_share.to_csv(sys.argv[l_in*2+4+(i-1)*5])

    # %% save interim results
    term1_tf.to_pickle(sys.argv[l_in*2+5+(i-1)*5])
    term1topN_tf.to_csv(sys.argv[l_in*2+6+(i-1)*5])
