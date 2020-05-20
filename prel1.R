library(ISLR)
library(MASS)
library(dplyr)
library(magrittr)

data = read.csv('term5/term5_top500_bySpeakerParty.csv')
data = read.csv('term5/term5_top500_bySpeakerParty_long.csv')

data2 <- data%>%select(-c('Speaker','X'))

# split data into train and test set
df.train <- data2%>%
    dplyr::sample_frac(0.8,axis=0)

df.test <- data2%>%
  dplyr::setdiff(df.train)

# single-out prediction targets
to_predict <- df.test%>%select(c('Speaker.Party'))
df.test <- df.test%>%select(-c('Speaker.Party'))


## linear discriminant analysis

lda.fit=lda(Speaker.Party~.,data=df.train)

lda.fit$prior

pr.lda <- predict(lda.fit,df.test)
pr.lda$class

ctable.lda <- table(to_predict$Speaker.Party, pr.lda$class)
ctable.lda
diag(ctable.lda)
res.lda <- round((sum(diag(ctable.lda))/sum(ctable.lda))*100,2)
res.lda


## multinomial logisitc regression

library(nnet)
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


rf2=ranger::ranger(Speaker.Party~.,data=df.train,mtry=500)

pr <- predict(rf2,data=df.test)


ctable <- table(to_predict$Speaker.Party, pr$predictions)
res.randomForest <- round((sum(diag(ctable))/sum(ctable))*100,2)


# vector support machine
library(e1071)

fit.svm = svm(Speaker.Party ~ ., data = df.train, scale = FALSE, kernel = "radial", cost = 5)

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


res <- data.frame(res.lda,res.logistic,res.lasso,res.ridge,res.lasso.cv,res.randomForest,res.svm)
res <- res/100
readr::write_csv(res,"prediction_results.csv")
