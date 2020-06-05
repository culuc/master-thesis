library(dplyr)
library(magrittr)
library(nnet)
library(caret)

data1 = read.csv('../Data/term1/tfidf/term1_top500_scaled.csv')%>%select(-c('Speaker','X'))
data2 = read.csv('../Data/term2/tfidf/term2_top500_scaled.csv')%>%select(-c('Speaker','X'))
data3 = read.csv('../Data/term3/tfidf/term3_top500_scaled.csv')%>%select(-c('Speaker','X'))
data4 = read.csv('../Data/term4/tfidf/term4_top500_scaled.csv')%>%select(-c('Speaker','X'))
data5 = read.csv('../Data/term5/tfidf/term5_top500_scaled.csv')%>%select(-c('Speaker','X'))


model.p.log1 <- train(
  Speaker.Party ~ .,
  data1,
  method = "regLogistic",
  MaxNWts = 10000000,
  tuneGrid = expand.grid(cost=10e10, loss='L1', epsilon = 0.001),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
  )
)
model.p.log2 <- train(
  Speaker.Party ~ .,
  data2,
  method = "regLogistic",
  MaxNWts = 10000000,
  tuneGrid = expand.grid(cost=10e10, loss='L1', epsilon = 0.001),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
  )
)
model.p.log3 <- train(
  Speaker.Party ~ .,
  data3,
  method = "regLogistic",
  MaxNWts = 10000000,
  tuneGrid = expand.grid(cost=10e10, loss='L1', epsilon = 0.001),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

model.p.log4 <- train(
  Speaker.Party ~ .,
  data4,
  method = "regLogistic",
  MaxNWts = 10000000,
  tuneGrid = expand.grid(cost=10e10, loss='L1', epsilon = 0.001),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

model.p.log5 <- train(
  Speaker.Party ~ .,
  data5,
  method = "regLogistic",
  MaxNWts = 10000000,
  tuneGrid = expand.grid(cost=10e10, loss='L1', epsilon = 0.001),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)


term1.p.log<-cbind(term=1,'bestTune'=model.p.log1$bestTune,'Accuracy CV-10Fold'=mean(model.p.log1$resample$Accuracy))
term2.p.log<-cbind(term=2,'bestTune'=model.p.log2$bestTune,'Accuracy CV-10Fold'=mean(model.p.log2$resample$Accuracy))
term3.p.log<-cbind(term=3,'bestTune'=model.p.log3$bestTune,'Accuracy CV-10Fold'=mean(model.p.log3$resample$Accuracy))
term4.p.log<-cbind(term=4,'bestTune'=model.p.log4$bestTune,'Accuracy CV-10Fold'=mean(model.p.log4$resample$Accuracy))
term5.p.log<-cbind(term=5,'bestTune'=model.p.log5$bestTune,'Accuracy CV-10Fold'=mean(model.p.log5$resample$Accuracy))
# term1.p.log<-cbind(term=1,'Accuracy CV-10Fold'=mean(model.p.log1$resample$Accuracy))
# term2.p.log<-cbind(term=2,'Accuracy CV-10Fold'=mean(model.p.log2$resample$Accuracy))
# term3.p.log<-cbind(term=3,'Accuracy CV-10Fold'=mean(model.p.log3$resample$Accuracy))
# term4.p.log<-cbind(term=4,'Accuracy CV-10Fold'=mean(model.p.log4$resample$Accuracy))
# term5.p.log<-cbind(term=5,'Accuracy CV-10Fold'=mean(model.p.log5$resample$Accuracy))

res.p.log.top500.scaled <- rbind(term1.p.log,term2.p.log,term3.p.log,term4.p.log,term5.p.log)
readr::write_csv(data.frame(res.p.log.top500.scaled),'../Results/result_terms_regLogistic_top500_scaled2.csv')


# saveRDS(model.p.log1, "model_p.log1_top500.rds")
# saveRDS(model.p.log2, "model_p.log2_top500.rds")
# saveRDS(model.p.log3, "model_p.log3_top500.rds")
# saveRDS(model.p.log4, "model_p.log4_top500.rds")
# saveRDS(model.p.log5, "model_p.log5_top500.rds")
