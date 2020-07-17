#' - Run caret models for all 5 terms using 10-fold CV and the mutinom model
#'

library(dplyr)
library(tidyr)
library(readr)
library(rjson)
library(rlist)
library(caret)


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

# source(in_lib)

# Load Model and Data #
print('Loading Objects in to R Session')
print(in_data1)
print(in_data2)
print(in_data5)
print(out_models)
df1         <- read_csv(in_data1)%>%select(-c('X1'))
df2         <- read_csv(in_data2)%>%select(-c('X1'))
df3         <- read_csv(in_data3)%>%select(-c('X1'))
df4         <- read_csv(in_data4)%>%select(-c('X1'))
df5         <- read_csv(in_data5)%>%select(-c('X1'))
# df1         <- read_csv(in_data[2])%>%select(-c('X1'))
model_info <- fromJSON(file = in_model)

colnames(df1) <- make.names(colnames(df1), unique=TRUE)
colnames(df2) <- make.names(colnames(df2), unique=TRUE)
colnames(df3) <- make.names(colnames(df3), unique=TRUE)
colnames(df4) <- make.names(colnames(df4), unique=TRUE)
colnames(df5) <- make.names(colnames(df5), unique=TRUE)

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

print(paste('Working with', nrow(df), 'rows of data', sep = " "))

# Estimate Models #
print('Estimating Models')
print('Model 1...')

caret_1 <- train(
  Speaker.Party ~ .,
  df1,
  method = method,
  tuneGrid = tuneGrid,
  MaxNWts = 10000000,
  trControl = trainControl(
      method = "cv",
      number = 10,
      verboseIter = TRUE
    )
)
caret_2 <- train(
  Speaker.Party ~ .,
  df2,
  method = method,
  tuneGrid = tuneGrid,
  MaxNWts = 10000000,
  trControl = trainControl(
    method = "cv",
    number = 10,
    verboseIter = TRUE
  )
)
caret_3 <- train(
  Speaker.Party ~ .,
  df3,
  method = method,
  tuneGrid = tuneGrid,
  MaxNWts = 10000000,
  trControl = trainControl(
    method = "cv",
    number = 10,
    verboseIter = TRUE
  )
)
caret_4 <- train(
  Speaker.Party ~ .,
  df4,
  method = method,
  tuneGrid = tuneGrid,
  MaxNWts = 10000000,
  trControl = trainControl(
    method = "cv",
    number = 10,
    verboseIter = TRUE
  )
)
caret_5 <- train(
  Speaker.Party ~ .,
  df5,
  method = method,
  tuneGrid = tuneGrid,
  MaxNWts = 10000000,
  trControl = trainControl(
    method = "cv",
    number = 10,
    verboseIter = TRUE
  )
)
# summary(caret_1)
# summary(caret_2)
print("saving results ...")

# pack it into a list #
model_list <- list(
                   model1    = caret_1,
                   model2    = caret_2,
                   model3    = caret_3,
                   model4    = caret_4,
                   model5    = caret_5
                   )

acc_list <- list(
                  model1    = mean(caret_1$resample$Accuracy),
                  model2    = mean(caret_2$resample$Accuracy),
                  model3    = mean(caret_3$resample$Accuracy),
                  model4    = mean(caret_4$resample$Accuracy),
                  model5    = mean(caret_5$resample$Accuracy)
                  )

# Save Output #
list.save(model_list, out_models)
list.save(acc_list, out_acc)
write_csv(data.frame(acc_list), out_acc2)
