import pandas as pd
import ast

df = pd.read_csv('../out/accuracy/multinom/summary.csv')

#%%
df
para_plot = pd.plotting.parallel_coordinates(df,'file',colormap = 'Accent').legend(bbox_to_anchor=(1,1))

fig = para_plot.get_figure()
fig.savefig('./summary_plot_P2.png', dpi=600,bbox_inches='tight')


dfbypartyspeaker = pd.read_pickle('../../../interim/all_byPartySpeakerTerm.pkl')
dfbypartyspeaker.Speaker.describe()

dfbypartyspeaker.Phrase.describe()
summary_stats = dfbypartyspeaker.groupby('Term').describe(include='all')

summary_stats2 = summary_stats.dropna(axis=1)

summary_stats2.to_csv('./summary_stats.csv')


summary_stats2.to_html('summary_stats.html')

summary_stats2.to_markdown('summary_stats.md',mode="object")

summary_stats2.to_latex('summary_stats.latex')





phrases = pd.read_csv('../../../interim/fixd_P2/phrases_all_terms_tfidf_top500each_P2.csv')
phrases = phrases.Phrase.apply(ast.literal_eval)

p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
p2 = 'Schweizerische Volkspartei (SVP)'
p3 = 'FDP.Die Liberalen (FDP-Liberale)'
p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
parties = [p1,p2,p3,p4]
parties2 = parties[:2]

dfbypartyspeaker2 = dfbypartyspeaker[dfbypartyspeaker['Speaker Party'].isin(parties2)]


dfbypartyspeaker2filt = dfbypartyspeaker2[dfbypartyspeaker2.Phrase.isin(phrases)]

sumry = dfbypartyspeaker2filt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)
sumry2 = dfbypartyspeaker2filt.groupby(['Term']).describe(include='all').dropna(axis=1)

sumry2.to_csv('summary_stats_P2.csv')
sumry.to_csv('summary_stats_P2_byParty.csv')


sumry3 = dfbypartyspeaker2filt.groupby(['Term','Speaker Party','Speaker']).describe(include='all').dropna(axis=1)


sumry.columns
sumry_phrase = sumry[('Phrase','unique')].plot.bar(color = ['green','red'])
sumry_phrase.set_ylabel('# Unique Phrases')
sumry_phrase.get_figure().savefig('./summary_phrase_plot_P2.png', dpi=600,bbox_inches='tight')
sumry_speaker = sumry[('Speaker','unique')].plot.bar(color = ['green','red'])
sumry_speaker.set_ylabel('# Speakers')
sumry_speaker.get_figure().savefig('./summary_speaker_plot_P2.png', dpi=600,bbox_inches='tight')
