#%%
import sys
import ast
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd

#%% snakemake.input[0]
pp = pd.read_pickle(sys.argv[1])
indiv=sys.argv[2]
n=ast.literal_eval(sys.argv[3])
N = ast.literal_eval(sys.argv[4])

#%%
p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties2 = [p1,p2]
parties4 = [p1,p2,p3,p4]
# # dfbypartyspeaker = pd.read_pickle(sys.argv[3])
# pp1 = pd.read_pickle('../Data/lookup_files/procedural_phrases.pkl')
# pp2 = pd.read_pickle('procedural_phrases_SpSvpDistinct.pkl')



dfoverall = pd.read_pickle(sys.argv[5])
#%%
dfbyparty = pd.read_pickle(sys.argv[6])

dfbyparty_filt = dfbyparty[dfbyparty.Phrase.isin(pp).apply(lambda x: not x)]

if N is not None:
    dfbyparty_filt = dfbyparty_filt[dfbyparty_filt.Phrase.isin(parties4[0:N])]
#%%
if indiv ==1:
    term1_tf, term1topN_tf = m.compute_tf_idf_new(dfbyparty_filt,'Speaker Party',n)
else:
    dfoverall = dfbyparty_filt.groupby('Phrase').sum()
    term1_tf, term1topN_tf = m.compute_tf_idf_old(dfoverall,dfbyparty_filt,500)
# %% save interim results
term1_tf.to_pickle(sys.argv[7])
term1topN_tf.to_csv(sys.argv[8])
