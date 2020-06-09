library(dplyr)
library(magrittr)
library(nnet)
library(caret)

data1 = read.csv('../Data/term1/cap/term1_cap100_scaled.csv')%>%select(-c('Speaker','X'))
data2 = read.csv('../Data/term2/cap/term2_cap100_scaled.csv')%>%select(-c('Speaker','X'))
data3 = read.csv('../Data/term3/cap/term3_cap100_scaled.csv')%>%select(-c('Speaker','X'))
data4 = read.csv('../Data/term4/cap/term4_cap100_scaled.csv')%>%select(-c('Speaker','X'))
data5 = read.csv('../Data/term5/cap/term5_cap100_scaled.csv')%>%select(-c('Speaker','X'))

model.multi1 <- train(
  Speaker.Party ~ .,
  data1,
  method = "multinom",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
  )
)
model.multi2 <- train(
  Speaker.Party ~ .,
  data2,
  method = "multinom",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
  )
)
model.multi3 <- train(
  Speaker.Party ~ .,
  data3,
  method = "multinom",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

model.multi4 <- train(
  Speaker.Party ~ .,
  data4,
  method = "multinom",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

model.multi5 <- train(
  Speaker.Party ~ .,
  data5,
  method = "multinom",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 10,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

decay <-model.multi1$results$decay
term1.multinom<-model.multi1$results$Accuracy
term2.multinom<-model.multi2$results$Accuracy
term3.multinom<-model.multi3$results$Accuracy
term4.multinom<-model.multi4$results$Accuracy
term5.multinom<-model.multi5$results$Accuracy

res.multinom.top500.scaled <- tibble(decay,term1.multinom,term2.multinom,term3.multinom,term4.multinom,term5.multinom)
readr::write_csv(res.multinom.top500.scaled,'../Results/result_terms_multinom_cap100_scaled.csv')


# saveRDS(model.multi1, "model_multi1_cap100.rds")
# saveRDS(model.multi2, "model_multi2_cap100.rds")
# saveRDS(model.multi3, "model_multi3_cap100.rds")
# saveRDS(model.multi4, "model_multi4_cap100.rds")
# saveRDS(model.multi5, "model_multi5_cap100.rds")
