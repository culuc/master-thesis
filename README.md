# master-thesis

## Summary Stats of the Dataset

|    |Speaker Party|Speaker Party|Speaker Party                                        |Speaker Party|Speaker|Speaker|Speaker                |Speaker|Phrase |Phrase |Phrase               |Phrase|Counts   |Counts            |Counts            |Counts|Counts|Counts|Counts|Counts|
|----|-------------|-------------|-----------------------------------------------------|-------------|-------|-------|-----------------------|-------|-------|-------|---------------------|------|---------|------------------|------------------|------|------|------|------|------|
|    |count        |unique       |top                                                  |freq         |count  |unique |top                    |freq   |count  |unique |top                  |freq  |count    |mean              |std               |min   |25%   |50%   |75%   |max   |
|Term|             |             |                                                     |             |       |       |                       |       |       |       |                     |      |         |                  |                  |      |      |      |      |      |
|1   |2985289      |13           |FDP.Die Liberalen (FDP-Liberale)                     |933620       |2985289|218    |Kaspar Villiger        |192278 |2985289|1894845|('million', 'frank') |198   |2985289.0|1.1386991343216686|1.2071007127226212|1.0   |1.0   |1.0   |1.0   |877.0 |
|2   |3202591      |13           |FDP.Die Liberalen (FDP-Liberale)                     |801180       |3202591|227    |Hans-Rudolf Merz       |142279 |3202591|1993820|('million', 'frank') |202   |3202591.0|1.142585175565659 |1.154597995549102 |1.0   |1.0   |1.0   |1.0   |593.0 |
|3   |3314197      |15           |Christlichdemokratische Volkspartei der Schweiz (CVP)|741225       |3314197|232    |Eveline Widmer-Schlumpf|128645 |3314197|2033677|('million', 'frank') |195   |3314197.0|1.147402523145124 |1.1349287025228894|1.0   |1.0   |1.0   |1.0   |322.0 |
|4   |3427431      |12           |Sozialdemokratische Partei der Schweiz (SP)          |733029       |3427431|236    |Simonetta Sommaruga    |151986 |3427431|2096203|('artikel', 'absatz')|204   |3427431.0|1.160670192922921 |1.3422703360246826|1.0   |1.0   |1.0   |1.0   |568.0 |
|5   |3149257      |15           |Sozialdemokratische Partei der Schweiz (SP)          |735257       |3149257|237    |Simonetta Sommaruga    |169380 |3149257|1941602|('million', 'frank') |204   |3149257.0|1.156980837067283 |1.244432181289119 |1.0   |1.0   |1.0   |1.0   |567.0 |


Prediction accuracy determined with 10-fold cross-validation:

[Results for Multinomial Logistic](Results/summary_result_terms_multinom_scaled.csv)

[Results for Regularized Logistic](Results/summary_result_terms_regLogistic_scaled.csv)

[Results for Random Forest](Results/summary_result_terms_randomForest_scaled_best.csv)


## Results for Restricted Analysis: SP & SVP
![results P2](Analysis/Graphs/summary_plot_P2.png)


### Some summary stats

Distribution of Phrases  | Distribution of Speakers
:--:|:--:
 ![results P2](Analysis/Graphs/summary_phrase_plot_P2.png) | ![results P2](Analysis/Graphs/summary_speaker_plot_P2.png)

<!-- | data         | term1.rf.best      | term2.rf.best      | term3.rf.best      | term4.rf.best      | term5.rf.best      |
|--------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| tfidf top500 | 0.7060330371383003 | 0.7024822134387352 | 0.6639619800489366 | 0.7229813664596273 | 0.6859479578392622 |
| tfidf top100 | 0.7154159608507434 | 0.662403538490495  | 0.6657872200263505 | 0.7280683229813665 | 0.7029644268774704 |
| cap 100      | 0.7071229457041814 | 0.6554663090532655 | 0.6446982872200263 | 0.6828379446640316 | 0.618729907773386  |
| cap 20       | 0.697914747342665  | 0.6758493318275927 | 0.6525179023874677 | 0.699111424807077  | 0.6835641025641026 | -->
