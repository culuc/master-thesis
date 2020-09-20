library(magrittr)
library(dplyr)
library(tidyr)
library(caret)
library(GGally)
library(ggthemes)
library(tidyverse)
library(ranger)
library(LiblineaR)
args        <- commandArgs(trailingOnly = TRUE)
# m <- readRDS('models/all_speakers/models/multinom/individual_top100each.Rds')
# in_data     <- args[1]
# out_plot    <- args[2]
# out_data    <- args[3]
l           <- length(args)
l2          <- l-2
# 6,8

print(l)
print(l2)
in_data <- rep(NaN,l2)
out_data <- rep(NaN,2)

model <- args[1]
dfacc <- args[2]
print(dfacc)
for (i in 3:l2){
    in_data[i] <- args[i]
 }
for (i in l2+1:l){
    out_data[i] <- args[i]
}
print(in_data)
print(out_data)


calc_sd_df <- function(df,data,dfacc){
    m <- readRDS(df)
    m.acc <- readRDS(dfacc)
    print(m.acc)
    # print(dim(m$model5$trainingData))

    b <- matrix(NaN,5,100)
    b2 <- matrix(NaN,5,100)
    n <- rep(NaN,5)
    accnull <- rep(NaN,5)

    for (i in 1:5){
        d <- readr::read_csv(data[i])%>%select(-c('X1','Speaker'))
        colnames(d) <- make.names(colnames(d))
        n[i]<-dim(d)[1]
        pc <- d %>% group_by(Speaker.Party) %>% summarise(count=n())
        accnull[i] <- max(pc$count)/sum(pc$count)
        prePr = preProcess(d, c("center","scale"))
        for (j in 1:100){
            s<-d%>%
                sample_n(50,replace=T)

            s<-predict(prePr,s)

            pr<- predict(m[[i]],s%>%select(-c(Speaker.Party)))
            test <- s$Speaker.Party

            table.res <- table(factor(pr$predictions),factor(test))
            #
            b[i,j] <- sum(diag(table.res))/sum(table.res)
            b2[i,j] <- confusionMatrix(factor(pr$predictions),factor(test))$Overall[['Accuracy']]
            # test2 <- factor(test)
            # pr2 <- factor(pr$predictions)
            #
            # levs <- union(levels(test2),levels(pr2))
            # levels(pr2) <- levs
            # levels(test2) <- levs
            # cm <- confusionMatrix(pr2,test2)$overall
            # if (i==1){
            #     cms <- t(data.frame(cm))
            # } else {
            #     cms <- rbind(cms,t(data.frame(cm)))
            # }
        }
    }
    b_mean <-rowMeans(b)
    print(b)
    print(b2)
    b_de.mean <- b - b_mean
    b_de.mean.sorted <- b_de.mean
    for (i in 1:5){
        b_de.mean.sorted[i,] <- sort(b_de.mean[i,])
        }

    q2<- b_de.mean.sorted[,c(5,95)]



    q2<-q2*sqrt(50)/sqrt(n)

    qt2<-tibble('lb'=q2[,1],'ub'=q2[,2],'AccuracyNull'=accnull)

    acc<- tibble('Term'=c('Term1','Term2','Term3','Term4','Term5'),'Accuracy'=rep(NaN,5))

    for (i in 1:5){
        acc[i,2] <- m.acc[[i]]
        }

    acc2 <- cbind(acc,qt2)

 return(acc2)
}


labels     <- c('46th \n 1999\u20132003','47th \n 2003\u20132007','48th \n 2007\u20132011','49th \n 2011\u20132015','50th \n 2015\u20132019')
x = c("1","2","3","4","5")


plot_res <- function(df,out_plot,out_data){

    ggplot(df, aes(x=Term, y=Accuracy,group=1)) +
        geom_line(alpha=0.5) +
        # geom_point()+
        geom_errorbar(aes(ymin=Accuracy-ub, ymax=Accuracy-lb), width=.1,position=position_dodge(0.05),alpha=0.25)+
        # geom_line(aes(y=AccuracyNull),linetype='dotted',alpha=0.5) +
        theme_tufte(base_family='ArialMT')+
        # scale_color_few()+
        labs(x="Terms", y="Prediction Accuracy", col="Feature Selection")+
        scale_x_discrete(labels=labels)+
        theme(axis.title=element_text(size=12),
                 axis.text = element_text(size=12))

    ggsave(out_plot,height=5, width=10, units="in",dpi=400)
    readr::write_csv(df,out_data)

 return()
}


# for (i in 1:l2){
#     df_new <- calc_sd_df(in_data[i])
#     print(in_data[i])
#     print(out_data[i+l2])
#     print(out_data[i+l2+2])
#     plot_res(df_new,out_data[i+l2],out_data[i+l2+2])
#  }
# 3,5
# 4,6

df_new <- calc_sd_df(model, in_data[3:7], dfacc)
print(in_data)
# print(out_data[i+l2])
# print(out_data[i+l2+2])
plot_res(df_new,out_data[l2+1],out_data[l2+2])
