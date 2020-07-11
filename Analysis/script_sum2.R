#' post_opening_ols.R
#'
#' contributors: @lachlandeer
#'
#' - Combines the necessary data
#' - Run an OLS regression on a (subset of) data
#'

library(dplyr)
library(tidyr)
library(readr)
library(rjson)
library(rlist)
library(tibble)


in_data1     <- "./Results/result_terms_regLogistic_top500_scaled.csv"
# in_data2     <- args[2]
in_data3     <- "./Results/result_terms_regLogistic_cap20_scaled.csv"
in_data4     <- "./Results/result_terms_regLogistic_cap100_scaled.csv"
in_data5     <- "./Results/result_terms_regLogistic_top500_scaled2.csv"
# in_data6     <- args[6]
in_data7     <- "./Results/result_terms_regLogistic_cap20_scaled2.csv"
in_data8     <- "./Results/result_terms_regLogistic_cap100_scaled2.csv"

out_data  <- "./Results/summary_regLogistic.csv"

# Load Model and Data #
print('Loading Objects in to R Session')
df1         <- read_csv(in_data1)%>%select(5)%>%as_tibble()%>%add_column(file="top500",.before=T)
# df2         <- read_csv(in_data2)%>%add_column(file="top1000",.before=T)
df3         <- t(read_csv(in_data3)%>%select(5))%>%add_column(file="cap20",.before=T)
df4         <- read_csv(in_data4)%>%select(5)%>%add_column(file="cap100",.before=T)
df5         <- read_csv(in_data5)%>%select(5)%>%add_column(file="top500_no_regularization",.before=T)
# df6         <- read_csv(in_data6)%>%add_column(file="top1000_no_regularization",.before=T)
df7         <- read_csv(in_data7)%>%select(5)%>%add_column(file="cap20_no_regularization",.before=T)
df8         <- read_csv(in_data8)%>%select(5)%>%add_column(file="cap100_no_regularization",.before=T)

print(df1)

summed <- rbind(df1,df3,df4,df5,df7,df8)

# Save Output #

write_csv(data.frame(summed), out_data)
