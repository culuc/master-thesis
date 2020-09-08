#' - Run caret models for all 5 terms using 10-fold CV and the specified statistical model
#'

library(dplyr)
library(tidyr)
library(readr)
library(rjson)
library(rlist)
library(caret)
library(data.table)

# --- Unpack CLI --- #
args        <- commandArgs(trailingOnly = TRUE)
in_model    <- args[1]
# in_data     <- args[2]
in_data1     <- args[2]
in_data2     <- args[3]
in_data3     <- args[4]
in_data4     <- args[5]
in_data5     <- args[6]
# in_lib      <- args[3]
out_models  <- args[7]
out_acc <- args[8]
out_acc2 <- args[9]
# out_models2  <- args[5]
in_data <- args[2:6]
# source(in_lib)

# Load Model and Data #
print('Loading Objects in to R Session')
print(in_data1)
print(in_data2)
print(in_data5)
print(out_models)
print(Cstack_info())
# df1         <- read_csv(in_data1)%>%select(-c('X1','Speaker'))
# df2         <- read_csv(in_data2)%>%select(-c('X1','Speaker'))
# df3         <- read_csv(in_data3)%>%select(-c('X1','Speaker'))
# df4         <- read_csv(in_data4)%>%select(-c('X1','Speaker'))
# df5         <- read_csv(in_data5)%>%select(-c('X1','Speaker'))
# # df1         <- read_csv(in_data[2])%>%select(-c('X1'))
model_info <- fromJSON(file = in_model)
#
# colnames(df1) <- make.names(colnames(df1), unique=TRUE)
# colnames(df2) <- make.names(colnames(df2), unique=TRUE)
# colnames(df3) <- make.names(colnames(df3), unique=TRUE)
# colnames(df4) <- make.names(colnames(df4), unique=TRUE)
# colnames(df5) <- make.names(colnames(df5), unique=TRUE)

# Unpack Model Info #
print('Unpacking JSON data')
# tuneGrid <- expand.grid(cost=10e10, loss='L1', epsilon = 0.001)
tuneGrid <- if (!is.null(model_info$tuneGrid)) {
  expand.grid(model_info$tuneGrid)
 } else {
  NULL
 }
method <- model_info$method$name

print(method)

print(tuneGrid)

# Create Regression Models #
print('Running Caret Models')



# Estimate Models #
print('Estimating Models')

caret_model <- vector(mode="list", length=5)

for (i in 1:5){
    print(paste('Model ',i,'...'))

    df         <- read_csv(in_data[i])%>%select(-c('X1','Speaker'))
    colnames(df) <- make.names(colnames(df), unique=TRUE)

    print(paste('Working with', nrow(df), 'rows and', ncol(df), 'columns of data', sep = " "))

    caret_model[[i]] <- train(
      Speaker.Party ~ .,
      df,
      method = method,
      preProcess=c("scale", "center"),
      tuneGrid = tuneGrid,
      trControl = trainControl(
          method = "cv",
          number = 10,
          verboseIter = TRUE
        )
    )
}

#
# caret_1 <- train(
#   Speaker.Party ~ .,
#   df1,
#   method = method,
#   tuneGrid = tuneGrid,
#   trControl = trainControl(
#       method = "cv",
#       number = 10,
#       verboseIter = TRUE
#     )
# )
# caret_2 <- train(
#   Speaker.Party ~ .,
#   df2,
#   method = method,
#   tuneGrid = tuneGrid,
#   trControl = trainControl(
#     method = "cv",
#     number = 10,
#     verboseIter = TRUE
#   )
# )
# caret_3 <- train(
#   Speaker.Party ~ .,
#   df3,
#   method = method,
#   tuneGrid = tuneGrid,
#   trControl = trainControl(
#     method = "cv",
#     number = 10,
#     verboseIter = TRUE
#   )
# )
# caret_4 <- train(
#   Speaker.Party ~ .,
#   df4,
#   method = method,
#   tuneGrid = tuneGrid,
#   trControl = trainControl(
#     method = "cv",
#     number = 10,
#     verboseIter = TRUE
#   )
# )
# caret_5 <- train(
#   Speaker.Party ~ .,
#   df5,
#   method = method,
#   tuneGrid = tuneGrid,
#   trControl = trainControl(
#     method = "cv",
#     number = 10,
#     verboseIter = TRUE
#   )
# )
# summary(caret_1)
# summary(caret_2)


# pack it into a list #
model_list <- list(
                   model1    = caret_model[[1]],
                   model2    = caret_model[[2]],
                   model3    = caret_model[[3]],
                   model4    = caret_model[[4]],
                   model5    = caret_model[[5]]
                   )

acc_list <- list(
                  term1    = mean(caret_model[[1]]$resample$Accuracy),
                  term2    = mean(caret_model[[2]]$resample$Accuracy),
                  term3    = mean(caret_model[[3]]$resample$Accuracy),
                  term4    = mean(caret_model[[4]]$resample$Accuracy),
                  term5    = mean(caret_model[[5]]$resample$Accuracy)
                  )

# Save Output #
list.save(model_list, out_models)
list.save(acc_list, out_acc)
write_csv(data.frame(acc_list), out_acc2)
