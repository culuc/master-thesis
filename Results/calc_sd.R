library(magrittr)
library(dplyr)
library(tidyr)
library(caret)
library(GGally)
library(ggthemes)
library(tidyverse)

data5n = readr::read_csv('term5_top100each_share.csv')%>%select(-c('X1','Speaker'))
colnames(data5n) <- make.names(colnames(data5n),unique=T)


data5n2 = readr::read_csv('term5_top250each_share_P4.csv')%>%select(-c('X1','Speaker'))
colnames(data5n2) <- make.names(colnames(data5n2),unique=T)


data5 = readr::read_csv('../Data/term5/tfidf_indiv/term5_top100each_scaled.csv')%>%select(-c('X1','Speaker'))
colnames(data5) <- make.names(colnames(data5),unique=T)


preProcValues <- preProcess(data5n, method = c("center", "scale"))

predict(preProcValues,data5n)


m3<- train(
  Speaker.Party ~ .,
  data5n2,
  method = "regLogistic",
  preProcess=c("scale", "center"),
  # num.trees = 1500,
  # importance = 'permutation',
  # MaxNWts = 10000000,
  # tuneGrid = expand.grid(decay = 1e-04),
  trControl = trainControl(
    method = "cv",
    number = 5,
    allowParallel = TRUE,
    verbose = TRUE
    # verboseIter = TRUE
  )
)
colnames(data5n2)
m2<- train(
  Speaker.Party ~ .,
  data5n,
  method = "regLogistic",
  preProcess=c("scale", "center"),
  # MaxNWts = 10000000,
  # num.trees = 1500,
  # importance = 'permutation',
  # tuneGrid = expand.grid(decay = 0),
  trControl = trainControl(
    method = "cv",
    number = 5,
    allowParallel = TRUE,
    verbose = TRUE
    # verboseIter = TRUE
  )
)
data5n2<-data5n[,-nearZeroVar(data5n)]
dim(data5n)
dim(data5n[,-nearZeroVar(data5n)])
m3$resample$Accuracy
m2$resample$Accuracy
s2 <- m2$trainingData%>%
    sample_n(50,replac=T)

s2
p<-predict(m2$finalModel,s2%>%select(-.outcome))
p
s2%>%select(.outcome)


s3<-predict(m2$preProcess,s2)
p3<-predict(m2$finalModel,s3%>%select(-.outcome))
# p$predictions
t <- table(s3$`.outcome`,p3)
sum(diag(t))/sum(t)

m2$preProcess
predict(m3$preProcess,m3$trainingData)
pr<- predict(m2$finalModel,predict(m2$preProcess,m2$trainingData)%>%select(-c(.outcome)))
pr
table.res <- table(m2$trainingData$`.outcome`,pr$predictions)
sum(diag(table.res))/sum(table.res)

b[i] <- sum(diag(table.res))/sum(table.res)
p<-predict(m2$finalModel,s2%>%select(-.outcome),type='se',probability=TRUE)


m <- readRDS("models/no_ref_ext/multinom/individual_top100each.Rds")
m <- readRDS("models/no_ref_ext/multinom_P4/individual_top250each_P4.Rds")

m <- readRDS("multinom_P4/individual_top250each_P4.Rds")
m <- readRDS("models/regLogistic_P4/individual_top250each_P4.Rds")
m <- readRDS("models/noref_ext/models/regLogistic/individual_top100each.Rds")



m$model5$results
m <- readRDS("models/all_speakers/models/multinom_P2/individual_top500each_P2.Rds")



m1 <- readRDS("models/all_speakers/models/randomForest/individual_top100each.Rds")
m1 <- readRDS("models/noref_ext/models/randomForest/individual_top100each.Rds")

varImp(m1$model5)

max(m$model1$results$Accuracy)

max(mean(m$model1$resample$Accuracy))
coef(m$model5$finalModel)
predict(m$model5$preProcess,m$model5$trainingData)
m$model1$preProcess
m2$preProcess



dim(m$model5$trainingData)[1]
231/10
m$model1$finalModel

b <- rep(NaN,100)
b <- matrix(NaN,5,100)
b[1,]
m
m3$trainingData
m2$trainingData
m$model5$resample$Accuracy
m[[1]]$preProcess

for (i in 1:5){
    for (j in 1:100){
        s<-m[[i]]$trainingData%>%
            sample_n(50,replace=T)

        s<-predict(m[[i]]$preProcess,s)

        pr<- predict(m[[i]],s%>%select(-c(.outcome)))
        test <- s$.outcome
        # pr<-droplevels(pr)
        # levels(test)<-levels(pr)
        # pr
        table.res <- table(factor(pr),factor(test))
        #
        b[i,j] <- sum(diag(table.res))/sum(table.res)
        # b[i]<-confusionMatrix(factor(pr),factor(test))[[3]][[1]]
        }
    }



b
rowMeans(b)
mean(m$model5$resample$Accuracy)
m$model5$results$Accuracy


b_mean <-rowMeans(b)

b_de.mean <- b - b_mean
b_de.mean
b_de.mean.sorted <- b_de.mean
for (i in 1:5){
    b_de.mean.sorted[i,] <- sort(b_de.mean[i,])

}



b_de.mean.sorted
q <- matrix(NaN,5,2)
q[1,]
for (i in 1:5){
    q[i,]<-quantile(b_de.mean.sorted[i,], c(0.05,0.95))
}

q


q2<- b_de.mean.sorted[,c(5,95)]

q2
q2

n <- rep(NaN,5)
for (i in 1:5){
    n[i]<-dim(m[[i]]$trainingData)[1]
    }
q2
q2<-q2*sqrt(50)/sqrt(n)

qt2<-tibble('lb'=q2[,1],'ub'=q2[,2])

qt2
qt<-tibble('q05'=q[,1],'q95'=q[,2])
q<-quantile(b_de.mean.sorted, c(0.05,0.95))
q[[1]]
q[[2]]
q
q2[[5,1]]*sqrt(50)/sqrt(dim(m$model5$trainingDat)[1])
q2[[1]]*sqrt(50)/sqrt(dim(m$model5$trainingDat)[1])


#
#
# ggparcoord(acc,
#     groupColumn='file',
#     columns = 2:ncol(acc),
#     scale='globalminmax'
#     )+
#     # theme_tufte(base_family='ArialMT')+
#     # scale_color_few()+
#     labs(x="Terms", y="Prediction Accuracy", col="Feature Selection")+
#     geom_errorbar(aes(ymin=len-sd, ymax=len+sd), width=.2,
#                    position=position_dodge(0.05))

acc <- readr::read_csv('all_speakers/multinom_P4/individual_top250each_P4.csv')
acc2 <- t(acc)
colnames(acc2) <- 'res'
m$model5$results$AccuracySD
acc2
# acc3 <- cbind(acc2,tibble('q95'=q[[2]]))
# acc3 <- cbind(acc3,tibble('q05'=q[[1]]))
# acc3 <- cbind(acc3,tibble('b_mean'=b_mean))
acc3 <- cbind(acc2,qt2)
acc3<-acc3%>%add_column('terms'=rownames(acc3))
acc3


ggplot(acc3, aes(x=terms, y=res,group=1)) +
      geom_line(alpha=0.5) +
      # geom_point()+
      geom_errorbar(aes(ymin=res-ub, ymax=res-lb), width=.1,
                     position=position_dodge(0.05),alpha=0.25)+
     theme_tufte(base_family='ArialMT')+
     # scale_color_few()+
     labs(x="Terms", y="Prediction Accuracy", col="Feature Selection")+
       theme(axis.title=element_text(size=12),
             axis.text = element_text(size=12))
