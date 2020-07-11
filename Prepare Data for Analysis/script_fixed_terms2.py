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
#%%
# dfbypartyspeaker = pd.read_pickle(sys.argv[3])

#%%
term1_tf, term1topN_tf = m.compute_tf_idf(dfoverall,dfbyparty,500)

# %% save interim results
term1_tf.to_pickle(sys.argv[3])
term1topN_tf.to_csv(sys.argv[4])
