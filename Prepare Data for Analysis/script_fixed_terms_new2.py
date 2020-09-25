#%%
import sys
import ast
sys.path.append('../Modules')
#%%
import modules as m
import pandas as pd

p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties2 = [p1,p2]
parties4 = [p1,p2,p3,p4]

#%% snakemake.input[0]
N = ast.literal_eval(sys.argv[1])
n = ast.literal_eval(sys.argv[2])
# allphr = pd.DataFrame()
# allphr = set()
for i in range(3,8):
    df = pd.read_pickle(sys.argv[i])
    if N is not None:
        df = df.groupby('Speaker Party')['tf_idf'].nlargest(N).reset_index(level=0,drop=True).reset_index()
    if n is not None:
        df = df[df['Speaker Party'].isin(parties4[:n])]
    if i == 3:
        allphr = set(df.Phrase)
    allphr.intersection_update(set(df.Phrase))

print(len(allphr))
allphr = pd.Series(list(allphr))
allphr = pd.DataFrame(allphr, columns = ['Phrase'])
allphr['Speaker Party'] = 0
allphr.to_csv(sys.argv[8])
