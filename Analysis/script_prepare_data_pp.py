#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd
import ast
#%%
l_in = int((len(sys.argv)-6)/5)-1
print(len(sys.argv))
print(l_in)
# dfoverall = pd.read_pickle(sys.argv[1])
pp = sys.argv[1]
indiv=sys.argv[2]
n = sys.argv[3]
N = sys.argv[4]
fixed_phrases = sys.argv[5]
print(pp)
#%%
pp1 = pd.read_pickle(pp)
p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties2 = [p1,p2]
parties4 = [p1,p2,p3,p4]
#%%

for i in range(1,l_in):
    print(sys.argv[i*2+4])
    print(sys.argv[i*2+4+1])
    dftfidf = pd.read_pickle(sys.argv[i*2+4])
    dfbypartyspeaker = pd.read_pickle(sys.argv[i*2+4+1])

    # dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties4)]
    dftfidf_filt = dftfidf[dftfidf.Phrase.isin(pp1).apply(lambda x: not x)]
    #%%
    if indiv==1 and len(fixed_phrases) > 8:
        term1_tf, term1topN_tf = m.compute_tf_idf_new(dftfidf_filt,'Speaker Party',n)
    elif len(fixed_phrases) >8:
        dfoverall = dftfidf_filt.groupby('Phrase').sum()
        term1_tf, term1topN_tf = m.compute_tf_idf(dfoverall,dftfidf_filt,n)
    else:
        term1topN_tf = pd.read_csv(fixed_phrases)
    #%%
    if N==4:
        term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties4)]
        dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties4)]
    elif N==2:
        term1topN_tf=term1topN_tf[term1topN_tf['Speaker Party'].isin(parties2)]
        dfbypartyspeaker=dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties2)]
    # %%
    if indiv==1:
        term1_topN_bySpeakerParty, topN = m.select_phrases_from_df2(dfbypartyspeaker,term1topN_tf,['Speaker Party','Speaker'])
    else:
        term1_topN_bySpeakerParty, topN = m.select_phrases_from_df(dfbypartyspeaker,term1topN_tf,['Speaker Party','Speaker'])
    # %% tfidf top 500
    term1_topN_bySpeakerParty_scaled = m.make_share(term1_topN_bySpeakerParty)
    term1_topN_bySpeakerParty_share = m.make_share(term1_topN_bySpeakerParty, scale=False)

    # %% save result
    print(sys.argv[l_in*2+4+(i-1)*5])
    # print(sys.argv)
    term1_topN_bySpeakerParty.to_csv(sys.argv[l_in*2+4+(i-1)*5])
    term1_topN_bySpeakerParty_scaled.to_csv(sys.argv[l_in*2+4+1+(i-1)*5])
    term1_topN_bySpeakerParty_share.to_csv(sys.argv[l_in*2+4+2+(i-1)*5])

    # %% save interim results
    term1_tf.to_pickle(sys.argv[l_in*2+4+3+(i-1)*5])
    term1topN_tf.to_csv(sys.argv[l_in*2+4+4+(i-1)*5])
