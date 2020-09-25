#%%
import sys
import ast
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd

#%% snakemake.input[0]
N = ast.literal_eval(sys.argv[1])
# allphr = pd.DataFrame()
# allphr = set()
for i in range(2,7):
    df = pd.read_pickle(sys.argv[i])
    if N is not None:
        df = df.groupby('Speaker Party')['tf_idf'].nlargest(N).reset_index(level=0,drop=True).reset_index()
    if i == 2:
        allphr = set(df.Phrase)
    allphr.intersection_update(set(df.Phrase))

print(len(allphr))
allphr = pd.Series(list(allphr))
allphr = pd.Series(allphr, columns = ['Phrase'])
allphr.to_csv(sys.argv[7])
