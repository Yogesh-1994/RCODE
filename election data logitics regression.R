election_data <- read.csv("C:/Users/Yogesh/Downloads/election_data.csv")
View(election_data)
summary(election_data)
str(election_data)
attach(election_data)
logit=glm(Result ~ Election.id + Year + Amount.Spent + Popularity.Rank, family = "binomial", data = election_data)
summary(logit)
prob=predict(logit,type = c("response"),election_data)
prob
confusion<-table(prob>0.5,election_data$Result)
confusion
Accuracy<-sum(diag(confusion))/sum(confusion)
Accuracy
