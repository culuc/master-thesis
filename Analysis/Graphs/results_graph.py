import pandas as pd
import ast

df = pd.read_csv('../out/accuracy/multinom_P2/summary.csv')
df_4 = pd.read_csv('../out/accuracy/multinom_P4_old/summary.csv')
df_42 = pd.read_csv('../out/accuracy/multinom_P4/summary.csv')
df2 = pd.read_csv('../out/accuracy/regLogistic_P2/summary.csv')
df2 = pd.read_csv('../out/accuracy/glm_P2/summary.csv')
df3 = pd.read_csv('../out/accuracy/glm_P2_old/summary.csv')
#%%
df
para_plot = pd.plotting.parallel_coordinates(df,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))

para_plot42 = pd.plotting.parallel_coordinates(df_42,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))

para_plot4 = pd.plotting.parallel_coordinates(df_4,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
fig = para_plot.get_figure()
fig.savefig('./summary_plot_P2.png', dpi=600,bbox_inches='tight')
fig2 = para_plot42.get_figure()
fig2.savefig('./summary_plot_P4.png', dpi=600,bbox_inches='tight')


para_plot2 = pd.plotting.parallel_coordinates(df2,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))
para_plot3 = pd.plotting.parallel_coordinates(df3,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))


dfbypartyspeaker = pd.read_pickle('../../../interim/all_byPartySpeakerTerm.pkl')
dfbypartyspeaker.Speaker.describe()

dfbypartyspeaker.Phrase.describe()
summary_stats = dfbypartyspeaker.groupby('Term').describe(include='all')

summary_stats2 = summary_stats.dropna(axis=1)

summary_stats3 = summary_stats2.drop([('Speaker','count'),('Speaker Party','count')],axis=1)

summary_stats2.to_csv('./summary_stats.csv')
summary_stats3.to_csv('./summary_stats_new.csv')



summary_stats2.to_html('summary_stats.html')

summary_stats2.to_markdown('summary_stats.md',mode="object")

summary_stats2.to_latex('summary_stats.latex')





phrases = pd.read_csv('../../../interim/fixd_P2/phrases_all_terms_tfidf_top500each_P2.csv')
phrases = phrases.Phrase.apply(ast.literal_eval)
phrases4 = pd.read_csv('../../../interim/fixd_P4/phrases_all_terms_tfidf_top250each_P4.csv')
phrases4 = phrases4.Phrase.apply(ast.literal_eval)

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

sumry = dfbypartyspeaker2filt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)

sumry4 = dfbypartyspeaker4filt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)

sumry2 = dfbypartyspeaker2filt.groupby(['Term']).describe(include='all').dropna(axis=1)

sumry2.to_csv('summary_stats_P2.csv')
sumry.to_csv('summary_stats_P2_byParty.csv')


sumry3 = sumry2.drop([('Speaker','count'),('Speaker Party','count')],axis=1)

sumry3.to_csv('summary_stats_P2_new.csv')



sumry.columns
sumry_phrase2 = sumry[('Phrase','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Phrase', 'unique')).plot.bar(stacked=False,color = ['green','red'],rot=0)
sumry_phrase2.set_ylabel('# Unique Phrases')
sumry_phrase2.legend(bbox_to_anchor=(1,1))
sumry_phrase2.get_figure().savefig('./summary_fixed_indiv_phrase_plot_P2.png', dpi=600,bbox_inches='tight')

sumry_speaker2 = sumry[('Speaker','unique')].reset_index().pivot(index='Term',columns = 'Speaker Party', values=('Speaker', 'unique')).plot.bar(stacked=True,color = ['orange','blue','green','red'],rot=0)
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
