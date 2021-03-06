my_movies <- read.csv("C:/Users/Yogesh/Downloads/my_movies.csv", header=FALSE)
View(my_movies)
summary(my_movies)
install.packages("arules")
library(arules)
install.packages("arulesViz")
library(arulesViz)
arules<-apriori(as.matrix(my_movies[,6:15]),parameter = list(support=0.2,confidence=0.7,minlen=2))
inspect(arules)
inspect(sort(arules,by="lift"))
inspect(head(sort(arules,by="lift")))
head(quality(arules))
plot(arules)
windows()
plot(arules,method = "grouped")
plot(arules[1:7],method = "graph")
write(arules,file = "a_rules.csv",sep=",")
getwd()
