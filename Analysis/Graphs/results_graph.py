import pandas as pd
import ast

df_P2 = pd.read_csv('../out/accuracy/multinom_P2/summary.csv')
df_P2rf = pd.read_csv('../out/accuracy/randomForest_P2/summary.csv')
df_P2rl = pd.read_csv('../out/accuracy/regLogistic_P2/summary.csv')
df_quisq_P2 = pd.read_csv('../out/accuracy/multinom_quisq/summary.csv')

df_P4 = pd.read_csv('../out/accuracy/multinom_P4_old/summary.csv')
df_P42 = pd.read_csv('../out/accuracy/multinom_P4/summary.csv')
df_P4rf = pd.read_csv('../out/accuracy/randomForest_P4/summary.csv')
df_P4rl = pd.read_csv('../out/accuracy/regLogistic_P4/summary.csv')


df2 = pd.read_csv('../out/accuracy/regLogistic_P2/summary.csv')
df2 = pd.read_csv('../out/accuracy/glm_P2/summary.csv')
df3 = pd.read_csv('../out/accuracy/glm_P2_old/summary.csv')

df_all = pd.read_csv('../out/accuracy/multinom/summary.csv')
df_all2 = pd.read_csv('../out/accuracy/regLogistic/summary.csv')
df_all3 = pd.read_csv('../out/accuracy/randomForest/summary.csv')


#%%
df
para_plot2 = pd.plotting.parallel_coordinates(df,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plot2rf = pd.plotting.parallel_coordinates(df_P2rf,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plot2rl = pd.plotting.parallel_coordinates(df_P2rl,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plot4 = pd.plotting.parallel_coordinates(df_42,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plot4rf = pd.plotting.parallel_coordinates(df_P4rf,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plot4rl = pd.plotting.parallel_coordinates(df_P4rl,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))

para_plotALL = pd.plotting.parallel_coordinates(df_all,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plotALLrl = pd.plotting.parallel_coordinates(df_all2,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plotALLrf = pd.plotting.parallel_coordinates(df_all3,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))

fig2 = para_plot2.get_figure()
fig2.savefig('./summary_plot_P2.png', dpi=400,bbox_inches='tight')
fig2rf = para_plot2rf.get_figure()
fig2rf.savefig('./summary_plot_P2_rf.png', dpi=400,bbox_inches='tight')
fig2rl = para_plot2rl.get_figure()
fig2rl.savefig('./summary_plot_P2_rl.png', dpi=400,bbox_inches='tight')

fig4 = para_plot4.get_figure()
fig4.savefig('./summary_plot_P4.png', dpi=400,bbox_inches='tight')
fig4rf = para_plot4rf.get_figure()
fig4rf.savefig('./summary_plot_P4_rf.png', dpi=400,bbox_inches='tight')
fig4rl = para_plot4rl.get_figure()
fig4rl.savefig('./summary_plot_P4_rl.png', dpi=400,bbox_inches='tight')

fig = para_plotALL.get_figure()
fig.savefig('./summary_plot_ALL.png', dpi=400,bbox_inches='tight')
figrf = para_plotALLrf.get_figure()
figrf.savefig('./summary_plot_ALL_rf.png', dpi=400,bbox_inches='tight')
figrl = para_plotALLrl.get_figure()
figrl.savefig('./summary_plot_ALL_rl.png', dpi=400,bbox_inches='tight')



para_plot2 = pd.plotting.parallel_coordinates(df2,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plot3 = pd.plotting.parallel_coordinates(df3,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))


dfbypartyspeaker = pd.read_pickle('../../../interim/all_byPartySpeakerTerm.pkl')
dfbypartyspeaker.Speaker.describe()

dfbypartyspeaker.Phrase.describe()

dfbypartyspeaker['TotalCounts'] = dfbypartyspeaker.groupby(['Term','Phrase']).Counts.transform('sum')

all = dfbypartyspeaker[['Term','Phrase','TotalCounts']]
uniq = dfbypartyspeaker[['Term','Phrase','TotalCounts']].drop_duplicates()
all.groupby('Term').describe(include='all').dropna(axis=1)

uniqq = uniq.groupby('Term').describe()
uniqq.T
uniqqq = uniqq.T.apply(lambda x: round(x,1))

summary_stats = dfbypartyspeaker.groupby('Term').describe(include='all')

summary_stats2 = summary_stats.dropna(axis=1)

summary_stats3 = summary_stats2.drop([('Speaker','count'),('Speaker Party','count')],axis=1)

import numpy as np
tmp = summary_stats3.select_dtypes(include=[np.number])
summary_stats3.loc[:, tmp.columns] = np.round(tmp,1)

summary_stats4 = summary_stats3.T.drop('TotalCounts')
summary_stats4=summary_stats4.append(uniqqq)




summary_stats2.to_csv('./summary_stats.csv')
summary_stats3.to_csv('./summary_stats_new.csv')

summary_stats4.to_csv('./summary_stats2.csv')


summary_stats2.to_html('summary_stats.html')

summary_stats2.to_markdown('summary_stats.md',mode="object")

summary_stats2.to_latex('summary_stats.latex')





phrases = pd.read_csv('../../../interim/fixd_P2/phrases_all_terms_tfidf_top500each_P2.csv')
phrases = phrases.Phrase.apply(ast.literal_eval)
phrases4 = pd.read_csv('../../../interim/fixd_P4/phrases_all_terms_tfidf_top250each_P4.csv')
phrases4 = phrases4.Phrase.apply(ast.literal_eval)

phrasesALL = pd.read_csv('../../../interim/fixed/phrases_all_terms_tfidf_top100each.csv')
phrasesALL = phrasesALL.Phrase.apply(ast.literal_eval)


p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties = [p1,p2,p3,p4]
parties2 = parties[:2]

dfbypartyspeaker2 = dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties2)]
dfbypartyspeaker4 = dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties)]


dfbypartyspeaker2filt = dfbypartyspeaker2[dfbypartyspeaker2.Phrase.isin(phrases)]
dfbypartyspeaker4filt = dfbypartyspeaker4[dfbypartyspeaker4.Phrase.isin(phrases4)]
dfbypartyspeakerALLfilt = dfbypartyspeaker[dfbypartyspeaker.Phrase.isin(phrasesALL)]

sumry = dfbypartyspeaker2filt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)

sumry4 = dfbypartyspeaker4filt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)

sumry2 = dfbypartyspeaker2filt.groupby(['Term']).describe(include='all').dropna(axis=1)

sumry2.to_csv('summary_stats_P2.csv')
sumry.to_csv('summary_stats_P2_byParty.csv')


sumry3 = sumry2.drop([('Speaker','count'),('Speaker Party','count')],axis=1)

sumry3.to_csv('summary_stats_P2_new.csv')

sumryALL = dfbypartyspeakerALLfilt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)


sumry.columns
sumry_phrase2 = sumry[('Phrase','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Phrase', 'unique')).plot.bar(stacked=False,color = ['green','red'],rot=0)
sumry_phrase2.set_ylabel('# Unique Phrases')
sumry_phrase2.legend(bbox_to_anchor=(1,1))
sumry_phrase2.get_figure().savefig('./summary_fixed_indiv_phrase_plot_P2.png', dpi=600,bbox_inches='tight')

sumry_speaker2 = sumry[('Speaker','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Speaker', 'unique')).plot.bar(stacked=True,color = ['green','red'],rot=0)
sumry_speaker2.set_ylabel('# Speakers')
sumry_speaker2.legend(bbox_to_anchor=(1,1))
sumry_speaker2.get_figure().savefig('./summary_fixed_indiv_speaker_plot_P2.png', dpi=600,bbox_inches='tight')


sumry4_2 = sumry4[('Phrase','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Phrase', 'unique'))

sumry4_2.plot.bar(stacked=False,color = ['orange','blue','green','red'],rot=0).legend(bbox_to_anchor=(1,1))

sumry_phrase4 = sumry4[('Phrase','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Phrase', 'unique')).plot.bar(stacked=False,color = ['orange','blue','green','red'],rot=0)
sumry_phrase4.set_ylabel('# Unique Phrases')
sumry_phrase4.legend(bbox_to_anchor=(1,1))
sumry_phrase4.get_figure().savefig('./summary_fixed_indiv_phrase_plot_P4.png', dpi=600,bbox_inches='tight')

sumry4[('Speaker','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Speaker', 'unique')).plot.bar(stacked=True,color = ['orange','blue','green','red'],rot=0).legend(bbox_to_anchor=(1,1))

sumry_speaker4 = sumry4[('Speaker','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Speaker', 'unique')).plot.bar(stacked=True,color = ['orange','blue','green','red'],rot=0)
sumry_speaker4.set_ylabel('# Speakers')
sumry_speaker4.legend(bbox_to_anchor=(1,1))
sumry_speaker4.get_figure().savefig('./summary_fixed_indiv_speaker_plot_P4.png', dpi=600,bbox_inches='tight')

sumry_phraseALL = sumryALL[('Phrase','unique')].reset_index().pivot(columns='Term',index = 'Speaker Party', values=('Phrase', 'unique')).plot.bar(stacked=False)
sumry_phraseALL.set_ylabel('# Unique Phrases')
sumry_phraseALL.legend(bbox_to_anchor=(1,1))
sumry_phraseALL.get_figure().savefig('./summary_fixed_indiv_phrase_plot_ALL.png', dpi=600,bbox_inches='tight')

sumry_speakerALL = sumryALL[('Speaker','unique')].reset_index().pivot(columns='Term',index = 'Speaker Party', values=('Speaker', 'unique')).plot.bar(stacked=True)
sumry_speakerALL.set_ylabel('# Speakers')
sumry_speakerALL.get_figure().savefig('./summary_fixed_indiv_speaker_plot_ALL.png', dpi=600,bbox_inches='tight')






proc_phr = pd.read_csv('../../Data/lookup_files/procedural_phrases.csv',index_col=0)

ppdf = pd.DataFrame.from_dict(set(proc_phr.index))


dfs = []
for i in range(6):
    pp = ppdf.iloc[61*i:61*(i+1)].reset_index(drop=True)
    pp.columns = ['row' + str(i+1)]
    dfs.append(pp)

pp_table = pd.concat(dfs,ignore_index=False,axis=1)


pp_table.to_csv('proceduarl_phrases_table.csv',index=False)
