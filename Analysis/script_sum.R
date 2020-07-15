#' - Collect results for a particular statistical model / folder


library(dplyr)
library(tidyr)
library(readr)
library(rjson)
library(rlist)
library(tibble)



# --- Unpack CLI --- #
args        <- commandArgs(trailingOnly = TRUE)
l           <- length(args)
print(l)
in_data <- rep(NaN,l-1)

for (i in 1:l-1){
    in_data[i] <- args[i]
 }
out_data  <- args[l]
print(in_data)
# out_models2  <- args[5]

# source(in_lib)
print(in_data[1])
print(tail(strsplit(in_data[1],"/")[[1]],n=1))
# Load Model and Data #
print('Loading Objects in to R Session')
name1 <- tail(strsplit(in_data[1],"/")[[1]],n=1)
print(name1)
df <- read_csv(in_data[1])%>%add_column(file=name1,.before=T)
for (i in 2:(l-1)){
    print(i)
    print(in_data[i])
    name <- tail(strsplit(in_data[i],"/")[[1]],n=1)
    print(name)
    df2 <- read_csv(in_data[i])
    print(df2)
    df2 <- df2%>%add_column(file=name,.before=T)
    df <- rbind(df,df2)
 }

# df1         <- read_csv(in_data[1,1])%>%add_column(file="top500",.before=T)
# df2         <- read_csv(in_data[2,1])%>%add_column(file="top1000",.before=T)
# df3         <- read_csv(in_data[3,1])%>%add_column(file="cap20",.before=T)
# df4         <- read_csv(in_data[4,1])%>%add_column(file="cap100",.before=T)
# df5         <- read_csv(in_data[5,1])%>%add_column(file="top500_no_regularization",.before=T)
# df6         <- read_csv(in_data[6,1])%>%add_column(file="top1000_no_regularization",.before=T)
# df7         <- read_csv(in_data[7,1])%>%add_column(file="cap20_no_regularization",.before=T)
# df8         <- read_csv(in_data[8,1])%>%add_column(file="cap100_no_regularization",.before=T)


# summed <- rbind(df[1],df[2],df[3],df[4],df[5],df[6],df[7],df[8])
summed <- df

# Save Output #

write_csv(data.frame(summed), out_data)
