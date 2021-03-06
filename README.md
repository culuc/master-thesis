# master-thesis

## Summary Stats of the Dataset
|    |Speaker Party|Speaker Party                                        |Speaker Party|Speaker|Speaker                |Speaker|Phrase |Phrase |Phrase               |Phrase|Counts   |Counts            |Counts            |Counts|Counts|Counts|Counts|Counts|
|----|-------------|-----------------------------------------------------|-------------|-------|-----------------------|-------|-------|-------|---------------------|------|---------|------------------|------------------|------|------|------|------|------|
|    |unique       |top                                                  |freq         |unique |top                    |freq   |count  |unique |top                  |freq  |count    |mean              |std               |min   |25%   |50%   |75%   |max   |
|Term|             |                                                     |             |       |                       |       |       |       |                     |      |         |                  |                  |      |      |      |      |      |
|1   |13           |FDP.Die Liberalen (FDP-Liberale)                     |933620       |218    |Kaspar Villiger        |192278 |2985289|1894845|('million', 'frank') |198   |2985289.0|1.1386991343216686|1.2071007127226212|1.0   |1.0   |1.0   |1.0   |877.0 |
|2   |13           |FDP.Die Liberalen (FDP-Liberale)                     |801180       |227    |Hans-Rudolf Merz       |142279 |3202591|1993820|('million', 'frank') |202   |3202591.0|1.142585175565659 |1.154597995549102 |1.0   |1.0   |1.0   |1.0   |593.0 |
|3   |15           |Christlichdemokratische Volkspartei der Schweiz (CVP)|741225       |232    |Eveline Widmer-Schlumpf|128645 |3314197|2033677|('million', 'frank') |195   |3314197.0|1.147402523145124 |1.1349287025228894|1.0   |1.0   |1.0   |1.0   |322.0 |
|4   |12           |Sozialdemokratische Partei der Schweiz (SP)          |733029       |236    |Simonetta Sommaruga    |151986 |3427431|2096203|('artikel', 'absatz')|204   |3427431.0|1.160670192922921 |1.3422703360246826|1.0   |1.0   |1.0   |1.0   |568.0 |
|5   |15           |Sozialdemokratische Partei der Schweiz (SP)          |735257       |237    |Simonetta Sommaruga    |169380 |3149257|1941602|('million', 'frank') |204   |3149257.0|1.156980837067283 |1.244432181289119 |1.0   |1.0   |1.0   |1.0   |567.0 |


<!-- Previous Results: Prediction accuracy determined with 10-fold cross-validation:

[Results for Multinomial Logistic](Results/old/summary_result_terms_multinom_scaled.csv)

[Results for Regularized Logistic](Results/old/summary_result_terms_regLogistic_scaled.csv)

[Results for Random Forest](Results/old/summary_result_terms_randomForest_scaled_best.csv) -->
# Confidence Intervals
## All Parties

<!-- Model | Feature Selection --- Individual Top 100 each |Feature Selection --- Individual Fixed Top 20 Each Party and Term
:--|:--:|:---:
Multinom |  ![](Results/plots_sd/multinom/all_speakers_multinom_individual_top100each.png) |  ![](Results/plots_sd/multinom/all_speakers_multinom_individual_fixed_top100each.png)
RegLogistic |  ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_individual_top100each.png) | ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_individual_fixed_top100each.png)
RandomForest |  ![](Results/plots_sd/randomForest/all_speakers_randomForest_individual_top100each.png) |  ![](Results/plots_sd/randomForest/all_speakers_randomForest_individual_fixed_top100each.png) -->


Feature Selection | Multinom |RegLogistic | RandomForest
:--|:--:|:---:|:---:
Individual |  ![](Results/plots_sd/multinom/all_speakers_multinom_individual_top100each.png) |  ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_individual_top100each.png) | ![](Results/plots_sd/randomForest/all_speakers_randomForest_individual_top100each.png)
Individual Fixed |  ![](Results/plots_sd/multinom/all_speakers_multinom_individual_fixed_top100each.png) | ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_individual_fixed_top100each.png) |  ![](Results/plots_sd/randomForest/all_speakers_randomForest_individual_fixed_top100each.png)
Individual No-ref & Ext. Stopwords |  ![](Results/plots_sd/multinom/noref_ext_multinom_individual_top100each.png) |  ![](Results/plots_sd/regLogistic/noref_ext_regLogistic_individual_top100each.png) | ![](Results/plots_sd/randomForest/noref_ext_randomForest_individual_top100each.png)
Individual Fixed No-ref & Ext. Stopwords |  ![](Results/plots_sd/multinom/noref_ext_multinom_individual_fixed_top100each.png) |  ![](Results/plots_sd/regLogistic/noref_ext_regLogistic_individual_fixed_top100each.png) | ![](Results/plots_sd/randomForest/noref_ext_randomForest_individual_fixed_top100each.png)



## SP, CVP, FDP & SVP

Feature Selection | Multinom |RegLogistic | RandomForest
:--|:--:|:---:|:---:
Individual |  ![](Results/plots_sd/multinom/all_speakers_multinom_P4_individual_top250each_P4.png) |  ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_P4_individual_top250each_P4.png) | ![](Results/plots_sd/randomForest/all_speakers_randomForest_P4_individual_top250each_P4.png)
Individual Fixed |  ![](Results/plots_sd/multinom/all_speakers_multinom_P4_individual_fixed_top250each_P4.png) | ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_P4_individual_fixed_top250each_P4.png) |  ![](Results/plots_sd/randomForest/all_speakers_randomForest_P4_individual_fixed_top250each_P4.png)
Individual No-ref & Ext. Stopwords |  ![](Results/plots_sd/multinom/noref_ext_multinom_P4_individual_top250each_P4.png) |  ![](Results/plots_sd/regLogistic/noref_ext_regLogistic_P4_individual_top250each_P4.png) | ![](Results/plots_sd/randomForest/noref_ext_randomForest_P4_individual_top250each_P4.png)
Individual Fixed No-ref & Ext. Stopwords |  ![](Results/plots_sd/multinom/noref_ext_multinom_P4_individual_fixed_top250each_P4.png) |  ![](Results/plots_sd/regLogistic/noref_ext_regLogistic_P4_individual_fixed_top250each_P4.png) | ![](Results/plots_sd/randomForest/noref_ext_randomForest_P4_individual_fixed_top250each_P4.png)

# SP & SVP
Feature Selection | Multinom |RegLogistic | RandomForest
:--|:--:|:---:|:---:
Individual |  ![](Results/plots_sd/multinom/all_speakers_multinom_P2_individual_top500each_P2.png) |  ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_P2_individual_top500each_P2.png) | ![](Results/plots_sd/randomForest/all_speakers_randomForest_P2_individual_top500each_P2.png)
Individual Fixed |  ![](Results/plots_sd/multinom/all_speakers_multinom_P2_individual_fixed_top500each_P2.png) | ![](Results/plots_sd/regLogistic/all_speakers_regLogistic_P2_individual_fixed_top500each_P2.png) |  ![](Results/plots_sd/randomForest/all_speakers_randomForest_P2_individual_fixed_top500each_P2.png)
Individual No-ref & Ext. Stopwords |  ![](Results/plots_sd/multinom/noref_ext_multinom_P2_individual_top500each_P2.png) |  ![](Results/plots_sd/regLogistic/noref_ext_regLogistic_P2_individual_top500each_P2.png) | ![](Results/plots_sd/randomForest/noref_ext_randomForest_P2_individual_top500each_P2.png)
Individual Fixed No-ref & Ext. Stopwords |  ![](Results/plots_sd/multinom/noref_ext_multinom_P2_individual_fixed_top500each_P2.png) |  ![](Results/plots_sd/regLogistic/noref_ext_regLogistic_P2_individual_fixed_top500each_P2.png) | ![](Results/plots_sd/randomForest/noref_ext_randomForest_P2_individual_fixed_top500each_P2.png)


## Cutoff > 10
### Regularized Logisitc

For SP & SVP, the results are more mixed, with some indicating an increase --- and not a clear trough as with most of tf-idf --- at the 48th term.

For SP, CVP, FDP & SVP, the results are very similar, apart from the fact that the peak at the 49th term is less pronounced.

Overall, the cutoff analysis seems to reveal similar trends as the tf-idf analysis.

Excluding Phrases | SP & SVP | SP, CVP, FDP & SVP
:--|:--:|:--:
Normal |![](Results/plots/cutoff_elasticnet_P2_summary.png) | ![](Results/plots/cutoff_elasticnet_P4_summary.png)
NoRef & Ext. Stopwords  | ![](Results/plots/noref_ext_cutoff_elasticnet_P2_summary.png) | ![](Results/plots/noref_ext_cutoff_elasticnet_P4_summary.png)


*Update: I made a mistake. Now the results between glmnet and regLogistic are comparable.*

*glmnet_a001....* fixes alpha to fit an elasticnet with 0.99*L2 + 0.01 *L1

The other models fit for each term the specification between L1 and L2 that fits best.

### Random Forest
However, with randomForest the results are gain comparable to tfidf, although the peak is more pronounced at the 47th term.
Normal | NoRef & Ext. Stopwords
:--:|:--:
![](Results/plots/cutoff_rf_cutoff_summary.png) | ![](Results/plots/noref_ext_cutoff_rf_noref_ext_summary.png)


## Tf-Idf (& a bit of Qui-Squared)

Feature selection based on tf-idf score is done at the following two levels:

- Parties: _Overall_ vs. _Individual Party-wise_
- Time: _Individual Term-wise_ vs. _Fixed_

### All vs. Broader Definition of Stopwords and No Party References
Remove all bigrams that include the word 'fraktion' (parliamentary group in engl.) and any party references. Also any bigrams where the first word is either 'herr' or 'frau' to exclude references to members. Along the same lines, any bigrams including ['kolleg', 'kollegin', 'standerat', 'standeratin', 'nationalrat', 'nationalratin', 'bundesrat', 'bundesratin', 'conseil', 'koleginn'].
Furthermore bigrams including 'artikel', 'absatz' or 'ziffer' are removed to exclude common occurring references to part of a law under discussion.

#### Results for Restricted Analysis: SP & SVP
<!-- Multinom | regLogistic | randomForest
:--:|:--:|:--:
![](Analysis/Graphs/summary_plot_P2.png)|![](Analysis/Graphs/summary_plot_P2_rl.png)|![](Analysis/Graphs/summary_plot_P2_rf.png) -->
Model | All Speakers | NoRef & Ext. Stopwords
:--:|:--:|:--:
|Multinom   | ![](Results/plots/all_speakers_multinom_P2_summary.png) |![](Results/plots/noref_ext_multinom_P2_summary.png) |
|regLogistic   |![](Results/plots/all_speakers_regLogistic_P2_summary.png)|![](Results/plots/noref_ext_regLogistic_P2_summary.png)
|randomForest|![](Results/plots/all_speakers_randomForest_P2_summary.png)|![](Results/plots/noref_ext_randomForest_P2_summary.png)


<!-- |glmnet| ![](Results/plots/cutoff_elasticnet_P2_summary.png)|  |   | -->
<!--
#### Some Summary Stats About the _individual_fixed_ Analysis
For each party, the 500 most significant phrases are selected from the entire speech catalog and kept fixed for the analysis over each term.
These stats examine the resulting distribution over the five terms from this method.

Distribution of Phrases  | Distribution of Speakers
:--:|:--:
 ![](Analysis/Graphs/summary_fixed_indiv_phrase_plot_P2.png) | ![results P2](Analysis/Graphs/summary_fixed_indiv_speaker_plot_P2.png)
 -->

#### Results for Restricted Analysis: SP, CVP, FDP & SVP
<!-- Multinom | regLogistic | randomForest
:--:|:--:|:--:
![](Analysis/Graphs/summary_plot_P4.png)|![](Analysis/Graphs/summary_plot_P4_rl.png)|![](Analysis/Graphs/summary_plot_P4_rf.png) -->

Model | All Speakers | NoRef & Ext. Stopwords
:--:|:--:|:--:
|Multinom   | ![](Results/plots/all_speakers_multinom_P4_summary.png)| ![](Results/plots/noref_ext_multinom_P4_summary.png)
|regLogistic   | ![](Results/plots/all_speakers_regLogistic_P4_summary.png) | ![](Results/plots/noref_ext_regLogistic_P4_summary.png)
|randomForest| ![](Results/plots/all_speakers_randomForest_P4_summary.png)| ![](Results/plots/noref_ext_randomForest_P4_summary.png)
<!-- |glmnet| ![](Results/plots/cutoff_elasticnet_P4_summary.png)|  |   | -->
<!--
#### Some Summary Stats About the _individual_fixed_ Analysis
For each party, the 250 most significant phrases are selected from the entire speech catalog and kept fixed for the analysis over each term.

Distribution of Phrases  | Distribution of Speakers
:--:|:--:
![](Analysis/Graphs/summary_fixed_indiv_phrase_plot_P4.png) | ![](Analysis/Graphs/summary_fixed_indiv_speaker_plot_P4.png)
 -->

#### Results for Analysis With All Parties
<!-- Multinom | regLogistic | randomForest
:--:|:--:|:--:
![](Analysis/Graphs/summary_plot_ALL.png)|![](Analysis/Graphs/summary_plot_ALL_rl.png)|![](Analysis/Graphs/summary_plot_ALL_rf.png) -->
Model | All Speakers | NoRef & Ext. Stopwords
:--:|:--:|:--:
|Multinom   | ![](Results/plots/all_speakers_multinom_summary.png) |![](Results/plots/noref_ext_multinom_summary.png)
|regLogistic| ![](Results/plots/all_speakers_regLogistic_summary.png) | ![](Results/plots/noref_ext_regLogistic_summary.png)
|randomForest| ![](Results/plots/all_speakers_randomForest_summary.png) |![](Results/plots/noref_ext_randomForest_summary.png)

### All vs. Consecutive
#### Results for Restricted Analysis: SP & SVP
<!-- Multinom | regLogistic | randomForest
:--:|:--:|:--:
![](Analysis/Graphs/summary_plot_P2.png)|![](Analysis/Graphs/summary_plot_P2_rl.png)|![](Analysis/Graphs/summary_plot_P2_rf.png) -->
Model | All Speakers | Consecutive Speakers
:--:|:--:|:--:
|Multinom   | ![](Results/plots/all_speakers_multinom_P2_summary.png) |![](Results/plots/consecutive_speakers_multinom_P2_summary.png) |
|regLogistic   |![](Results/plots/all_speakers_regLogistic_P2_summary.png)|![](Results/plots/consecutive_speakers_regLogistic_P2_summary.png)
|randomForest|![](Results/plots/all_speakers_randomForest_P2_summary.png)|![](Results/plots/consecutive_speakers_randomForest_P2_summary.png)


<!-- |glmnet| ![](Results/plots/cutoff_elasticnet_P2_summary.png)|  |   | -->
<!--
#### Some Summary Stats About the _individual_fixed_ Analysis
For each party, the 500 most significant phrases are selected from the entire speech catalog and kept fixed for the analysis over each term.
These stats examine the resulting distribution over the five terms from this method.

Distribution of Phrases  | Distribution of Speakers
:--:|:--:
 ![](Analysis/Graphs/summary_fixed_indiv_phrase_plot_P2.png) | ![results P2](Analysis/Graphs/summary_fixed_indiv_speaker_plot_P2.png)
 -->

#### Results for Restricted Analysis: SP, CVP, FDP & SVP
<!-- Multinom | regLogistic | randomForest
:--:|:--:|:--:
![](Analysis/Graphs/summary_plot_P4.png)|![](Analysis/Graphs/summary_plot_P4_rl.png)|![](Analysis/Graphs/summary_plot_P4_rf.png) -->

Model | All Speakers | Consecutive Speakers
:--:|:--:|:--:
|Multinom   | ![](Results/plots/all_speakers_multinom_P4_summary.png)| ![](Results/plots/consecutive_speakers_multinom_P4_summary.png)
|regLogistic   | ![](Results/plots/all_speakers_regLogistic_P4_summary.png) | ![](Results/plots/consecutive_speakers_regLogistic_P4_summary.png)
|randomForest| ![](Results/plots/all_speakers_randomForest_P4_summary.png)| ![](Results/plots/consecutive_speakers_randomForest_P4_summary.png)
<!-- |glmnet| ![](Results/plots/cutoff_elasticnet_P4_summary.png)|  |   | -->
<!--
#### Some Summary Stats About the _individual_fixed_ Analysis
For each party, the 250 most significant phrases are selected from the entire speech catalog and kept fixed for the analysis over each term.

Distribution of Phrases  | Distribution of Speakers
:--:|:--:
![](Analysis/Graphs/summary_fixed_indiv_phrase_plot_P4.png) | ![](Analysis/Graphs/summary_fixed_indiv_speaker_plot_P4.png)
 -->

#### Results for Analysis With All Parties
<!-- Multinom | regLogistic | randomForest
:--:|:--:|:--:
![](Analysis/Graphs/summary_plot_ALL.png)|![](Analysis/Graphs/summary_plot_ALL_rl.png)|![](Analysis/Graphs/summary_plot_ALL_rf.png) -->
Model | All Speakers | Consecutive Speakers
:--:|:--:|:--:
|Multinom   | ![](Results/plots/all_speakers_multinom_summary.png) |![](Results/plots/consecutive_speakers_multinom_summary.png)
|regLogistic| ![](Results/plots/all_speakers_regLogistic_summary.png) | ![](Results/plots/consecutive_speakers_regLogistic_summary.png)
|randomForest| ![](Results/plots/all_speakers_randomForest_summary.png) |![](Results/plots/consecutive_speakers_randomForest_summary.png)
<!--
#### Some Summary Stats About the _individual_fixed_ Analysis
For each party, the 100 most significant phrases are selected from the entire speech catalog and kept fixed for the analysis over each term.

Distribution of Phrases  | Distribution of Speakers
:--:|:--:
![](Analysis/Graphs/summary_fixed_indiv_phrase_plot_ALL.png) | ![](Analysis/Graphs/summary_fixed_indiv_speaker_plot_ALL.png)
 -->

## Overview of (non-)consecutive speakers

![](Data/lookup_files/speaker_servetime_all_color.png)


<!-- | data         | term1.rf.best      | term2.rf.best      | term3.rf.best      | term4.rf.best      | term5.rf.best      |
|--------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| tfidf top500 | 0.7060330371383003 | 0.7024822134387352 | 0.6639619800489366 | 0.7229813664596273 | 0.6859479578392622 |
| tfidf top100 | 0.7154159608507434 | 0.662403538490495  | 0.6657872200263505 | 0.7280683229813665 | 0.7029644268774704 |
| cap 100      | 0.7071229457041814 | 0.6554663090532655 | 0.6446982872200263 | 0.6828379446640316 | 0.618729907773386  |
| cap 20       | 0.697914747342665  | 0.6758493318275927 | 0.6525179023874677 | 0.699111424807077  | 0.6835641025641026 | -->

## Compare definitions of *documents* (four main parties)

Define *documents* by the level of _party_ (the specification of the previous analysis), _speaker_ and _speech_. Then, aggregate the phrases' tf-idf scores to party-level and select for each of the four main parties the 250 phrases with highest tf-idf score.

Normal | Ext. Stopwords & No Party Ref
:-----:|:-------:
![](Results/plots/def_doc_doc_regLogistic_P4_pp_base_summary.png)|![](Results/plots/def_doc_doc_regLogistic_P4_summary.png)
