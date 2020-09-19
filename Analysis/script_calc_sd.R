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
    n <- rep(NaN,5)


    for (i in 1:5){
        d <- readr::read_csv(data[i])%>%select(-c('X1','Speaker'))
        colnames(d) <- make.names(colnames(d))
        n[i]<-dim(d)[1]
        prePr = preProcess(d, c("center","scale"))
        for (j in 1:100){
            s<-d%>%
                sample_n(50,replace=T)

            s<-predict(prePr,s)

            pr<- predict(m[[i]],s%>%select(-c(Speaker.Party)))
            test <- s$Speaker.Party

            table.res <- table(factor(pr$prediction),factor(test))
            #
            b[i,j] <- sum(diag(table.res))/sum(table.res)

            test2 <- factor(test)
            pr2 <- factor(pr)

            levs <- union(levels(test2),levels(pr2))
            levels(pr2) <- levs
            levels(test2) <- levs
            cm <- confusionMatrix(pr2,test2)$overall
            if (i==1){
                cms <- t(data.frame(cm))
            } else {
                cms <- rbind(cms,t(data.frame(cm)))
            }
        }
    }
    b_mean <-rowMeans(b)
    print(b)
    b_de.mean <- b - b_mean
    b_de.mean.sorted <- b_de.mean
    for (i in 1:5){
        b_de.mean.sorted[i,] <- sort(b_de.mean[i,])
        }

    q2<- b_de.mean.sorted[,c(5,95)]



    q2<-q2*sqrt(50)/sqrt(n)

    qt2<-tibble('lb'=q2[,1],'ub'=q2[,2])

    acc<- tibble('Term'=c('Term1','Term2','Term3','Term4','Term5'),'Accuracy1'=rep(NaN,5))

    for (i in 1:5){
        acc[i,2] <- m.acc[[i]]
        }

    acc2 <- cbind(acc,qt2,cms)

 return(acc2)
}

# m <- readRDS(in_data)
#
# print(dim(m$model5$trainingData))
#
# b <- matrix(NaN,5,100)
#
# for (i in 1:5){
#     for (j in 1:100){
#         s<-m[[i]]$trainingData%>%
#             sample_n(50,replace=T)
#
#         s<-predict(m[[i]]$preProcess,s)
#
#         pr<- predict(m[[i]],s%>%select(-c(.outcome)))
#         test <- s$.outcome
#         # pr<-droplevels(pr)
#         # levels(test)<-levels(pr)
#         # pr
#         table.res <- table(factor(pr),factor(test))
#         #
#         b[i,j] <- sum(diag(table.res))/sum(table.res)
#         # b[i]<-confusionMatrix(factor(pr),factor(test))[[3]][[1]]
#         }
#     }
#
#
# b_mean <-rowMeans(b)
#
# b_de.mean <- b - b_mean
# b_de.mean.sorted <- b_de.mean
# for (i in 1:5){
#     b_de.mean.sorted[i,] <- sort(b_de.mean[i,])
# }
#
#
#
# # q <- matrix(NaN,5,2)
# # print(q[1,])
# # for (i in 1:5){
# #     q[i,]<-quantile(b_de.mean.sorted[i,], c(0.05,0.95))
# # }
# #
# # print(q)
# #
#
# q2<- b_de.mean.sorted[,c(5,95)]
#
#
# n <- rep(NaN,5)
# for (i in 1:5){
#     n[i]<-dim(m[[i]]$trainingData)[1]
#     }
#
# q2<-q2*sqrt(50)/sqrt(n)
#
# qt2<-tibble('lb'=q2[,1],'ub'=q2[,2])
#
# # qt<-tibble('q05'=q[,1],'q95'=q[,2])
# # q<-quantile(b_de.mean.sorted, c(0.05,0.95))
# # q[[1]]
# # q[[2]]
# # q
#
# #
# #
# # ggparcoord(acc,
# #     groupColumn='file',
# #     columns = 2:ncol(acc),
# #     scale='globalminmax'
# #     )+
# #     # theme_tufte(base_family='ArialMT')+
# #     # scale_color_few()+
# #     labs(x="Terms", y="Prediction Accuracy", col="Feature Selection")+
# #     geom_errorbar(aes(ymin=len-sd, ymax=len+sd), width=.2,
# #                    position=position_dodge(0.05))
#
# acc<- tibble('Term'=c('Term1','Term2','Term3','Term4','Term5'),'Prediction Accuracy'=rep(NaN,5))
#
# for (i in 1:5){
#     acc[i,2] <- m[[i]]$result$Accuracy
# }
#
#
#

# acc3 <- cbind(acc2,tibble('q95'=q[[2]]))
# acc3 <- cbind(acc3,tibble('q05'=q[[1]]))
# acc3 <- cbind(acc3,tibble('b_mean'=b_mean))
# acc2 <- cbind(acc,qt2)
# acc3<-acc3%>%add_column('terms'=rownames(acc3))



labels     <- c('46th \n 1999\u20132003','47th \n 2003\u20132007','48th \n 2007\u20132011','49th \n 2011\u20132015','50th \n 2015\u20132019')
x = c("1","2","3","4","5")


plot_res <- function(df,out_plot,out_data){

    ggplot(df, aes(x=Term, y=Accuracy1,group=1)) +
        geom_line(alpha=0.5) +
        # geom_point()+
        geom_errorbar(aes(ymin=Accuracy1-ub, ymax=Accuracy1-lb), width=.1,position=position_dodge(0.05),alpha=0.25)+
        geom_line(aes(y=AccuracyNull),linetype='dotted',alpha=0.5) +
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
