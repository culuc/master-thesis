library(ISLR)
library(MASS)
library(dplyr)
library(magrittr)
library(caret)
library(stepPlr)
library(LiblineaR)

data = read.csv('term5/term5_top500_bySpeakerParty.csv')
data = read.csv('term5/tfidf/term5_top500_scaled.csv')
data = read.csv('term1/tfidf/term1_top500_scaled.csv')
data1 = read.csv('Data/term1/tfidf/term1_top500_scaled.csv')%>%select(-c('Speaker','X'))
data2 = read.csv('Data/term2/tfidf/term2_top500_scaled.csv')%>%select(-c('Speaker','X'))
data3 = read.csv('Data/term3/tfidf/term3_top500_scaled.csv')%>%select(-c('Speaker','X'))
data4 = read.csv('Data/term4/tfidf/term4_top500_scaled.csv')%>%select(-c('Speaker','X'))
data5 = read.csv('Data/term5/tfidf/term5_top500_scaled.csv')%>%select(-c('Speaker','X'))

data5 = read.csv('term5/cap/term5_cap20_scaled.csv')%>%select(-c('Speaker','X'))

data2 <- data%>%select(-c('Speaker','X'))

# split data into train and test set
df.train <- data2%>%
    dplyr::sample_frac(0.8,axis=0)

df.test <- data2%>%
  dplyr::setdiff(df.train)

# single-out prediction targets
to_predict <- df.test%>%select(c('Speaker.Party'))
df.test <- df.test%>%select(-c('Speaker.Party'))

# single-out prediction targets for all data
to_predict_all <- data5%>%select(c('Speaker.Party'))
df.test_all <- data5%>%select(-c('Speaker.Party'))


## linear discriminant analysis


lda.fit

pr.lda <- predict(lda.fit,df.test)
pr.lda$class

ctable.lda <- table(to_predict$Speaker.Party, pr.lda$class)
ctable.lda
diag(ctable.lda)
res.lda <- round((sum(diag(ctable.lda))/sum(ctable.lda))*100,2)
res.lda


## multinomial logisitc regression

library(nnet)
multinom.fit5 <- multinom(Speaker.Party~., data = data5, MaxNWts = 10000000)

multinom.fit1 <- multinom(Speaker.Party~., data = data1, MaxNWts = 10000000)


multinom.fit <- multinom(Speaker.Party~., data = df.train, MaxNWts = 10000000)
summary(multinom.fit)
multinom.fit

pr.multinom <- predict(multinom.fit,df.test)
pr.multinom

ctable.multinom <- table(to_predict$Speaker.Party, pr.multinom)
ctable.multinom
res.logistic <- round((sum(diag(ctable.multinom))/sum(ctable.multinom))*100,2)
res.logistic


## multinomial lasso regression

library(glmnet)
x <- df.train%>%
    select(-c('Speaker.Party'))%>%
    as.matrix()
y <- df.train$Speaker.Party


df.train$Speaker.Party


lasso.fit <- glmnet(x,y,family="multinomial", alpha = 0)
coef(lasso.fit)

# ridge resgression
ridge.fit <- glmnet(x,y,family="multinomial", alpha = 1)
coef(ridge.fit)

# cross-validate optimal lambda for lasso
lasso.fit.cv = cv.glmnet(x, y, family = "multinomial", type.measure="class", keep=TRUE,nfolds=10,alpha=0)

lam.min <- lasso.fit.cv$lambda.min

plot(lasso.fit.cv)


lasso.pred <- predict(lasso.fit, newx = as.matrix(df.test), type = "class",s=0.001)
ridge.pred <- predict(ridge.fit, newx = as.matrix(df.test), type = "class",s=0.001)
lasso.pred2 <- predict(lasso.fit.cv$glmnet.fit, newx = as.matrix(df.test), type = "class",s=0.001,lambda=lam.min)

lasso.pred2
lasso.pred

ctable.lasso <- table(to_predict$Speaker.Party, lasso.pred)
res.lasso <- round((sum(diag(ctable.lasso))/sum(ctable.lasso))*100,2)
ctable.ridge <- table(to_predict$Speaker.Party, ridge.pred)
res.ridge <- round((sum(diag(ctable.ridge))/sum(ctable.ridge))*100,2)
ctable.lasso.cv <- table(to_predict$Speaker.Party, lasso.pred2)
res.lasso.cv <- round((sum(diag(ctable.lasso.cv))/sum(ctable.lasso.cv))*100,2)
res.lasso
res.lasso.cv
res.ridge


## random forest

library(randomForest)
set.seed (1)
sample
rf1=randomForest(Speaker.Party~.,data=data2,mtry=500,importance =TRUE)
getTree(rf1)



yhat.bag = predict(rf1 ,newdata=data2)
yhat.bag


df.test%>%dplyr::select(-c('Speaker.Party'))
df.train

rf=ranger::ranger(Speaker.Party~.,data=data2,mtry=500)
rf$predictions
ctable <- table(data2$Speaker.Party, rf$predictions)
ctable
round((sum(diag(ctable))/sum(ctable))*100,2)
sum(diag(ctable))
sum(ctable)
rf1=ranger::ranger(Speaker.Party~.,data=data1,mtry=500)
rf4=ranger::ranger(Speaker.Party~.,data=df.train,mtry=500)
rf5=ranger::ranger(Speaker.Party~.,data=data5,mtry=500)


rf2=ranger::ranger(Speaker.Party~.,data=df.train,mtry=500)
rf1$prediction.error
rf5$prediction.error
rf4$prediction.error

rf2$prediction.error
pr <- predict(rf5,data=df.test)

ctable <- table(to_predict$Speaker.Party, pr$predictions)
res.randomForest <- round((sum(diag(ctable))/sum(ctable))*100,2)
res.randomForest

# vector support machine
library(e1071)

fit.svm = svm(Speaker.Party ~ ., data = df.train, scale = FALSE, kernel = "linear", cost = 5)

# tune model to find optimal cost, gamma values
tune.out <- tune(svm, Speaker.Party~., data = df.train, kernel = "radial",
                 ranges = list(cost = c(0.1,1,10,100,1000),
                 gamma = c(0.5,1,2,3,4)))


tune.out <- tune(svm, Speaker.Party~., data = df.train, kernel = "radial",
              ranges = list(cost = c(10),
              gamma = c(1)))
# show best model
tune.out$best.model

pr.svm <- predict(fit.svm, df.test)

ctable.svm <- table(to_predict$Speaker.Party, pr.svm)
ctable.svm

res.svm <- round((sum(diag(ctable.svm))/sum(ctable.svm))*100,2)
res.svm

res <- data.frame(res.lda,res.logistic,res.lasso,res.ridge,res.lasso.cv,res.randomForest,res.svm)
res <- res/100
readr::write_csv(res,"prediction_results.csv")


# caret CV


model <- train(
  Speaker.Party ~ .,
  data5,
  method = "multinom",
  MaxNWts = 10000000,
  trControl = trainControl(
    method = "cv",
    number = 10,
    verboseIter = TRUE
  )
)
model
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
  method = "plr",
  MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 5,
    verbose = TRUE
    # verboseIter = TRUE
  )
)

model.multi5$results

decay <- model.multi1$results$decay
term1.multinom<-model.multi1$results$Accuracy
term2.multinom<-model.multi2$results$Accuracy
term3.multinom<-model.multi3$results$Accuracy
term4.multinom<-model.multi4$results$Accuracy
term5.multinom<-model.multi5$results$Accuracy

res.multinom.top500.scaled <- tibble(decay,term1.multinom,term2.multinom,term3.multinom,term4.multinom,term5.multinom)
res.multinom.top500.scaled
readr::write_csv(res.multinom.top500.scaled,'./result_terms_multinom_top500scaled.csv')

model.rf5 <- train(
  Speaker.Party ~ .,
  data5,
  trControl = trainControl(
    method = "cv",
    summaryFunction = multiClassSummary,
    verboseIter = TRUE
  )
)
mean(model.rf5$resample$Accuracy)
model.rf5$results
