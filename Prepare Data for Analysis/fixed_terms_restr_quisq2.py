#%%
import sys
import ast
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd

#%% snakemake.input[0]
N = 200
allphr = pd.DataFrame()

for i in range(1,6):
    phr = pd.read_csv('../Data/term'+str(i)+'/noref/qui_sqrd/term'+str(i)+'_quisq_top1000_topN_P2.csv',index_col=0)
    phr.Phrase = phr.Phrase.apply(ast.literal_eval)
    if N is not None:
        phr=phr.nlargest(N,'qui')
    allphr = allphr.append(phr,ignore_index=True)

allphr
pnr=set(allphr.Phrase)
# allphr
len(pnr)
pnr

allphr.to_csv('../Data/lookup_files/phrases_quisq_top1k_noref_ext.csv')
