library(magrittr)
library(dplyr)
library(tidyr)
library(caret)
library(GGally)
library(ggthemes)
library(tidyverse)



df1 <- readr::read_csv('../Data/term1/tfidf_indiv/P4/term1_top250each_share_P4.csv')%>%select(-'X1')%>%add_column('Term'=1)
df2 <- readr::read_csv('../Data/term2/tfidf_indiv/P4/term2_top250each_share_P4.csv')%>%select(-'X1')%>%add_column('Term'=2)
df3 <- readr::read_csv('../Data/term3/tfidf_indiv/P4/term3_top250each_share_P4.csv')%>%select(-'X1')%>%add_column('Term'=3)
df4 <- readr::read_csv('../Data/term4/tfidf_indiv/P4/term4_top250each_share_P4.csv')%>%select(-'X1')%>%add_column('Term'=4)
df5 <- readr::read_csv('../Data/term5/tfidf_indiv/P4/term5_top250each_share_P4.csv')%>%select(-'X1')%>%add_column('Term'=5)


colnames(df1)<-make.names(colnames(df1),unique=T)
colnames(df2)<-make.names(colnames(df2),unique=T)
colnames(df3)<-make.names(colnames(df3),unique=T)
colnames(df4)<-make.names(colnames(df4),unique=T)
colnames(df5)<-make.names(colnames(df5),unique=T)



sum(dim(df1)[2],dim(df2)[2],dim(df3)[2],dim(df4)[2],dim(df5)[2])
dim(df5)
dflong <- dplyr::bind_rows(df1,df2,df3,df4,df5)%>%replace(is.na(.),0)

dflong <- dflong%>%
    mutate(Term = factor(Term))%>%
    mutate(Speaker = factor(Speaker))%>%
    select(Speaker.Party, Term, Speaker, everything())

dflong

dim(dflong)
preP<-preProcess(dflong,c('center','scale'))
data_scaled <- predict(preP,dflong)
data_scaled


m<- train(
  Speaker.Party ~ . -1,
  data_scaled,
  method = 'multinom',
  MaxNWts = 10000000,
  # preProcess = c('scale', 'center'),
  tuneGrid = expand.grid(decay=0),
  trControl = trainControl(
      method ="none"
    )
    )
colnames(coef(m$finalModel))[['Term2']]
coef(m$finalModel)[,c('Term2','Term3','Term4','Term5')]
summary(m$finalModel)$coefficients[1,4]

pVal <- anova(m)$'Pr(>F)'[1][1]
summary(m$finalModel)$coefficients[4,4]
