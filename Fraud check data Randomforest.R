install.packages("randomForest")
library(randomForest)
Fraud_check <- read.csv("C:/Users/Yogesh/Downloads/Fraud_check.csv")
View(Fraud_check)
summary(Fraud_check)
Fraud_check_Single<-Fraud_check[Fraud_check$Marital.Status=="Single",] # 50
Fraud_check_Divorced <- Fraud_check[Fraud_check$Marital.Status=="Divorced",]
Fraud_check_Married<-Fraud_check[Fraud_check$Marital.Status=="Married",]
Fraud_check_train <- rbind(Fraud_check_Single[1:25,],Fraud_check_Divorced[1:25,],Fraud_check_Married[1:25,])
Fraud_check_test <- rbind(Fraud_check_Single[26:50,],Fraud_check_Divorced[26:50,],Fraud_check_Married[26:50,])
fit.forest <- randomForest(Marital.Status~.,data=Fraud_check_train, na.action=na.roughfix,importance=TRUE)
mean(Fraud_check_train$Marital.Status==predict(fit.forest,Fraud_check_train))  
pred_train <- predict(fit.forest,Fraud_check_train)
library(caret)
confusionMatrix(Fraud_check_train$Marital.Status, pred_train)
pred_test <- predict(fit.forest,newdata=Fraud_check_test)
mean(pred_test==Fraud_check_test$Marital.Status)
confusionMatrix(Fraud_check_test$Marital.Status, pred_test)
plot(fit.forest,lwd=2)
legend("topright", colnames(fit.forest$err.rate),col=1:4,cex=0.8,fill=1:4)
Fraud_check_forest <- randomForest(Marital.Status~.,data=Fraud_check,importance=TRUE)
plot(Fraud_check)
legend("topright",colnames(Fraud_check_forest$err.rate),col=1:3,cex=0.8,fill=1:3)
acc_Fraud_check <- mean(Fraud_check$Marital.Status==predict(Fraud_check_forest))
acc_Fraud_check
varImpPlot(Fraud_check_forest)

