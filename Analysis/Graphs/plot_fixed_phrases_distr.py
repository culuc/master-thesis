import pandas as pd
import sys
sys.path.append('../../Modules')
import modules as m
import ast

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

sumry4 = dfbypartyspeaker4.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)
colors = pd.read_csv('../../Data/lookup_files/partycolors.csv',index_col=0)

colors.columns = pd.MultiIndex.from_product([[''],['Speaker Party','color']])

sumry4.columns
colors.columns
sumryc = pd.merge(sumry4.reset_index(), colors, on='Speaker Party', how='left')

sumry2 = dfbypartyspeaker2filt.groupby(['Term']).describe(include='all').dropna(axis=1)

sumry2.to_csv('summary_stats_P2.csv')
sumry.to_csv('summary_stats_P2_byParty.csv')


sumry3 = sumry2.drop([('Speaker','count'),('Speaker Party','count')],axis=1)

sumry3.to_csv('summary_stats_P2_new.csv')

sumryALL = dfbypartyspeakerALLfilt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)


def plot_fixed_distr(df, phrases, N, outpath, level='Phrase',stacked=False):

    colors = pd.read_csv('../../Data/lookup_files/partycolors.csv',index_col=0)
    p1 = 'Sozialdemokratische Partei der Schweiz (SP)'
    p2 = 'Schweizerische Volkspartei (SVP)'
    p3 = 'FDP.Die Liberalen (FDP-Liberale)'
    p4 = 'Christlichdemokratische Volkspartei der Schweiz (CVP)'
    parties = [p1,p2,p3,p4]
    parties2 = parties[:2]

    if N==2:
        df = df[df['Speaker Party'].isin(parties2)]
    if N==4:
        df = df[df['Speaker Party'].isin(parties)]

    if type(phrases)==str:
        phrases = pd.read_csv(phrases)
        phrases = phrases.Phrase.apply(ast.literal_eval)

    dffilt = df[df.Phrase.isin(phrases)]

    sumry = dffilt.groupby(['Term','Speaker Party']).describe(include='all').dropna(axis=1)
    sumry = pd.merge(sumry.reset_index(level=0), colors, on='Speaker Party', how='left')
    sumry.columns=sumry.columns.str.join('')


    # yield sumry
    # return sumry
    sumry=sumry.pivot(index='Term',columns = ['Speaker Party','color'], values=level+'unique')
    ax=sumry.plot.bar(stacked=stacked,color=sumry.columns.get_level_values(level=1),rot=0,alpha=0.8)

    ax.legend(labels=sumry.columns.get_level_values(level=0),bbox_to_anchor=(1,1),frameon=False)
    ax.set_ylabel('# Unique '+level+'s')

    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_figure().savefig(outpath, dpi=600,bbox_inches='tight')

    return sumry, ax.get_figure()

type('../../Data/fixed/nore') == str

type(allphr.Phrase) == pd.core.series.Series

a=plot_fixed_distr(dfbypartyspeaker,'../../Data/fixed/noref/P2/noref_fixed_phrases_top500each_P2.csv',2,'testpic2.png')
b=plot_fixed_distr(dfbypartyspeaker,'../../../interim/fixd_P4/phrases_all_terms_tfidf_top250each_P4.csv',4,'testpic_old.png')

s=pd.read_pickle('phrases_over_all_terms_P4.pkl')
pd.Series(list(s)).to_frame().rename(columns={0:'Phrase'}).to_csv('phrases_over_all_terms_P4.csv')
s2=pd.read_pickle('phrases_over_all_terms_P4_noref.pkl')
pd.Series(list(s2)).to_frame().rename(columns={0:'Phrase'}).to_csv('phrases_over_all_terms_P4_noref.csv')

s==s2
c=plot_fixed_distr(dfbypartyspeaker,'phrases_over_all_terms_P4_noref.csv',4,'testpic_new.png')
c=plot_fixed_distr(dfbypartyspeaker,'phrases_over_all_terms_P4.csv',4,'testpic_newold.png')

allphr = pd.DataFrame()

for i in range(1,6):
    phr = pd.read_csv('../../Data/term'+str(i)+'/tfidf_indiv/term'+str(i)+'_top100each_topN.csv',index_col=0)
    phr.Phrase = phr.Phrase.apply(ast.literal_eval)
    phr=phr.groupby('Speaker Party').head(40)
    allphr = allphr.append(phr,ignore_index=True)

pnr=set(allphr.Phrase)
# allphr
len(pnr)
allphr.to_csv('../../Data/fixed2/noref/noref_fixed_top40eacheach.csv')


d=plot_fixed_distr(dfbypartyspeaker,pnr,None,'phrase_distr_All_top40eacheach.png',stacked=True)

e=plot_fixed_distr(dfbypartyspeaker,'../../../interim/fixed_old/fixd_P2/phrases_all_terms_tfidf_top500each_P2.csv',2,'phrase_distr_P2.png')
e=plot_fixed_distr(dfbypartyspeaker,'../../../interim/fixed_old/fixed/phrases_all_terms_tfidf_top100each.csv',None,'phrase_distr_ALL.png',stacked=True)
a.columns=a.columns.str.join('')
a
b=a.pivot(index='Term',columns = ['Speaker Party','color'], values='Phraseunique')
b.columns
ax=b.plot.bar(stacked=False,color=b.columns.get_level_values(level=1),rot=0,alpha=0.8)
ax.legend(labels=b.columns.get_level_values(level=0))
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.get_figure()



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
