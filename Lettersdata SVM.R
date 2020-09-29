letters <- read.csv("C:/Users/Yogesh/Downloads/letterdata.csv")
View(letters)
letters_train<-letters[1:16000,]
letters_test<-letters[16001:20000,]
View(letters)
install.packages("kernlab")
library(kernlab)
install.packages()
library(caret)
model1<-ksvm(letter ~.,data = letters_train,kernel = "vanilladot")
model1
model_rfdot<-ksvm(letter ~.,data = letters_train,kernel = "rbfdot")
pred_rfdot<-predict(model_rfdot,newdata=letters_test)
mean(pred_rfdot==letters_test$letter) 
model_vanilla<-ksvm(letter ~.,data = letters_train,kernel = "vanilladot")
pred_vanilla<-predict(model_vanilla,newdata=letters_test)
mean(pred_vanilla==letters_test$letter) 
model_besseldot<-ksvm(letter ~.,data = letters_train,kernel = "besseldot")
pred_bessel<-predict(model_besseldot,newdata=letters_test)
mean(pred_bessel==letters_test$letter)
model_poly<-ksvm(letter ~.,data = letters_train,kernel = "polydot")
pred_poly<-predict(model_poly,newdata = letters_test)
mean(pred_poly==letters_test$letter) 




