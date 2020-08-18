normalize<-function(x){
  return((x-min(x))/(max(x)-min(x)))
}
concrete_norm<-as.data.frame(lapply(concrete, normalize))
View(concrete_norm)
concrete_train<-concrete_norm[1:773,]
concrete_test<-concrete_norm[774:1030,]
View(concrete_test)
library(neuralnet)
concrete_model<-neuralnet(formula = strength~cement+slag+ash+water+superplastic+coarseagg+fineagg+age, data = concrete_train)
plot(concrete_model)
results_model<-compute(concrete_model, concrete_test[1:8])
predict_strength<-results_model$net.result
cor(predict_strength, concrete_test$strength)
concrete_model2<-neuralnet(formula = strength~cement+slag+ash+water+superplastic+coarseagg+fineagg+age, data = concrete_train, hidden = 5)
plot(concrete_model2)
model_results2<-compute(concrete_model2, concrete_test[1:8])
predict_strength2<-model_results2$net.result
cor(predict_strength2, concrete_test$strength)
concrete_model3<-neuralnet(formula = strength~cement+slag+ash+water+superplastic+coarseagg+fineagg+age, data = concrete_train, hidden = 15)
plot(concrete_model3)
model_results3<-compute(concrete_model3, concrete_test[1:8])
predict_strength3<-model_results3$net.result
cor(predict_strength3, concrete_test$strength)
