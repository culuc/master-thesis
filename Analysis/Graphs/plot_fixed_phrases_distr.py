import pandas as pd
import sys
sys.path.append('../../Modules')
import modules as m

d=pd.DataFrame({'Speaker':[1,2],'Speaker Party':[2,2],'a':[1,2],'b':[2,2]})
d
m.make_share(d,scale=False)
dfbypartyspeaker = pd.read_pickle('../../../interim/all_byPartySpeakerTerm.pkl')

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
