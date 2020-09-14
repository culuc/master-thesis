#%%
import sys
import ast
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd

#%% snakemake.input[0]
N = ast.literal_eval(sys.argv[1])
allphr = pd.DataFrame()

for i in range(2,7):
    phr = pd.read_csv(sys.argv[i],index_col=0)
    phr.Phrase = phr.Phrase.apply(ast.literal_eval)
    if N is not None:
        phr=phr.groupby('Speaker Party').head(N)
    allphr = allphr.append(phr,ignore_index=True)

pnr=set(allphr.Phrase)
# allphr
len(pnr)


allphr.to_csv(sys.argv[7])
