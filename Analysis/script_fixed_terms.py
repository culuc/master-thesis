#%%
import sys
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd

#%% snakemake.input[0]
dfoverall = pd.read_pickle(sys.argv[1])
#%%
dfbyparty = pd.read_pickle(sys.argv[2])
pp = pd.read_pickle(sys.argv[3])
indiv=sys.argv[4]
n=sys.argv[5]
N = sys.argv[6]

#%%
pp1 = pd.read_pickle(pp)
p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties2 = [p1,p2]
parties4 = [p1,p2,p3,p4]
# # dfbypartyspeaker = pd.read_pickle(sys.argv[3])
# pp1 = pd.read_pickle('../Data/lookup_files/procedural_phrases.pkl')
# pp2 = pd.read_pickle('procedural_phrases_SpSvpDistinct.pkl')
dfbyparty_filt = dfbyparty[dfbyparty.Phrase.isin(pp1).apply(lambda x: not x)]

if N is not None:
    dfbyparty_filt = dfbyparty_filt[dfbyparty_filt.Phrase.isin(parties4[0:N])]
#%%
if indiv ==1:
    term1_tf, term1topN_tf = m.compute_tf_idf_new(dfbyparty_filt,'Speaker Party',n)
else:
    dfoverall = dfbyparty_filt.groupby('Phrase').sum()
    term1_tf, term1topN_tf = m.compute_tf_idf(dfoverall,dfbyparty_filt,500)
# %% save interim results
term1_tf.to_pickle(sys.argv[7])
term1topN_tf.to_csv(sys.argv[8])
