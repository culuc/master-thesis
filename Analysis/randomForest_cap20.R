library(dplyr)
library(magrittr)
library(nnet)
library(caret)

data1 = read.csv('../Data/term1/cap/term1_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data2 = read.csv('../Data/term2/cap/term2_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data3 = read.csv('../Data/term3/cap/term3_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data4 = read.csv('../Data/term4/cap/term4_cap20_scaled.csv')%>%select(-c('Speaker','X'))
data5 = read.csv('../Data/term5/cap/term5_cap20_scaled.csv')%>%select(-c('Speaker','X'))


model.rf1 <- train(
  Speaker.Party ~ .,
  data1,
  # preProcess = "range",
  method = "ranger",
  # MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verboseIter = TRUE
  )
)
model.rf2 <- train(
  Speaker.Party ~ .,
  data2,
  method = "ranger",
  # MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
  )
)
model.rf3 <- train(
  Speaker.Party ~ .,
  data3,
  method = "ranger",
  # MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

model.rf4 <- train(
  Speaker.Party ~ .,
  data4,
  method = "ranger",
  # MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

model.rf5 <- train(
  Speaker.Party ~ .,
  data5,
  method = "ranger",
  # MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

mtry <- model.rf1$results$mtry
splitrule <- model.rf1$results$splitrule
term1.rf<-model.rf1$results$Accuracy
term2.rf<-model.rf2$results$Accuracy
term3.rf<-model.rf3$results$Accuracy
term4.rf<-model.rf4$results$Accuracy
term5.rf<-model.rf5$results$Accuracy

res.rf.cap20.scaled <- tibble(mtry,splitrule,term1.rf,term2.rf,term3.rf,term4.rf,term5.rf)
readr::write_csv(res.rf.cap20.scaled,'../Results/result_terms_rf_cap20_scaled.csv')


# saveRDS(model.rf1, "model_rf1_cap20.rds")
# saveRDS(model.rf2, "model_rf2_cap20.rds")
# saveRDS(model.rf3, "model_rf3_cap20.rds")
# saveRDS(model.rf4, "model_rf4_cap20.rds")
# saveRDS(model.rf5, "model_rf5_cap20.rds")
