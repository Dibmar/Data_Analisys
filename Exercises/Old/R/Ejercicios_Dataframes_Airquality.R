df_1 <- airquality
library(caret)
library(logging)

df_1 <- df_1[!is.na(df_1)]

# 1a columna seleccionada como target
validation_index <- createDataPartition(df_1$Ozone, p=0.80, list=FALSE)
validation <- df_1[-validation_index,]

dataset <- dataset[validation_index,]

loginfo("Resumen estadístico", logger = 'log')
dataset_summary <- summary(dataset)
loginfo(dataset_summary, logger = 'log')
loginfo("Resumen terminado", logger = 'log')

x <- dataset[,-1]
y <- dataset$Ozone

# Linear Regression
set.seed(7)
fit.lda <- train(y, data=dataset, method="lda", metric=metric, trControl=control)

# CART
set.seed(7)
fit.cart <- train(y, data=dataset, method="rpart", metric=metric, trControl=control)
# KNN
set.seed(7)
fit.knn <- train(y, data=dataset, method="knn", metric=metric, trControl=control)

# SVM
set.seed(7)
fit.svm <- train(y, data=dataset, method="svmRadial", metric=metric, trControl=control)
# Random Forest
set.seed(7)
fit.rf <- train(y, data=dataset, method="rf", metric=metric, trControl=control)

models <- c(fit.lda, fit.cart, fit.knn, fit.svm, fit.rf)