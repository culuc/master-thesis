library(dplyr)
library(magrittr)
library(nnet)
library(caret)


data1 = read.csv('../Data/term1/cap/term1_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data2 = read.csv('../Data/term2/cap/term2_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data3 = read.csv('../Data/term3/cap/term3_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data4 = read.csv('../Data/term4/cap/term4_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data5 = read.csv('../Data/term5/cap/term5_cap20_scaled.csv')%>%select(-c('Speaker','X'))

model.p.log1 <- train(
  Speaker.Party ~ .,
  data1,
  method = "regLogistic",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verboseIter = TRUE
  )
)
model.p.log2 <- train(
  Speaker.Party ~ .,
  data2,
  method = "regLogistic",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
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
  # tuneGrid = expand.grid(decay = 1e-04),
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
  # tuneGrid = expand.grid(decay = 1e-04),
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
  # tuneGrid = expand.grid(decay = 1e-04),
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

res.p.log.cap20.scaled <- rbind(term1.p.log,term2.p.log,term3.p.log,term4.p.log,term5.p.log)
readr::write_csv(res.p.log.cap20.scaled,'../Results/result_terms_regLogistic_cap20_scaled.csv')


# saveRDS(model.p.log1, "model_p.log1_cap20.rds")
# saveRDS(model.p.log2, "model_p.log2_cap20.rds")
# saveRDS(model.p.log3, "model_p.log3_cap20.rds")
# saveRDS(model.p.log4, "model_p.log4_cap20.rds")
# saveRDS(model.p.log5, "model_p.log5_cap20.rds")
