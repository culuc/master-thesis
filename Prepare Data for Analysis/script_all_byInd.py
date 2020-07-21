import pandas as pd
import sys
import json
import ast

ind = ['Speaker Party','Speaker','Phrase']

df1 = pd.read_pickle(sys.argv[1])
df2 = pd.read_pickle(sys.argv[2])
df3 = pd.read_pickle(sys.argv[3])
df4 = pd.read_pickle(sys.argv[4])
df5 = pd.read_pickle(sys.argv[5])
i = ast.literal_eval(sys.argv[6])



print(ind[::-i][::-1])


dfbypartyspeaker=pd.concat([df1,df2,df3,df4,df5]).groupby(ind[::-i][::-1]).sum().reset_index()

dfbypartyspeaker.to_pickle(sys.argv[7])
