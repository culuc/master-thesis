#' - Run caret models for all 5 terms using 10-fold CV and the specified statistical model
#'

library(dplyr)
library(tidyr)
library(readr)
# library(rjson)
# library(rlist)
# library(caret)
library(ggplot2)
library(GGally)
library(ggthemes)
# library(extrafont)

# font_import()
# extrafont::font_import(paths = NULL, recursive = TRUE, prompt = TRUE,pattern = "Arial")
# extrafont::fonttable()

# version

# --- Unpack CLI --- #
args        <- commandArgs(trailingOnly = TRUE)
l           <- length(args)
l2          <- l/2
print(l)
print(l2)
in_data <- rep(NaN,l2)
out_data <- rep(NaN,l2)

for (i in 1:l2){
    in_data[i] <- args[i]
 }
for (i in l2+1:l){
    out_data[i] <- args[i]
}
print(in_data)
print(out_data)
# Load Model and Data #


# source(in_lib)

# Load Model and Data #
print('Loading Objects in to R Session')
print(in_data)
print(out_data)


labels     <- c('46th \n 1999\u20132003','47th \n 2003\u20132007','48th \n 2007\u20132011','49th \n 2011\u20132015','50th \n 2015\u20132019')
x = c("1","2","3","4","5")


print_res <- function(in_data,out_data){
    df         <- read_csv(in_data)

    res.plot <- ggparcoord(df,
        groupColumn='file',
        columns = 2:ncol(df),
        scale='globalminmax'
        )+
        theme_tufte(base_family='ArialMT')+
        scale_color_few()+
        labs(x="Terms", y="Prediction Accuracy", col="Feature Selection")+
        scale_x_discrete(labels=labels)


    re.plot.formated <- res.plot +
      theme(axis.title=element_text(size=12),
            axis.text = element_text(size=12))

    ggsave(out_data,height=5, width=10, units="in",dpi=400)

    return()
}


for (i in 1:l2){
    print_res(in_data[i],out_data[i+l2])
 }
