groceries <- read.transactions(file.choose(),sep = ",")
View(groceries)
itemFrequencyPlot(groceries, topN=10)
inspect(groceries[1:10])
class(groceries)
summary(groceries)
install.packages("arules")
library(arules)
install.packages("arulesViz")
library(arulesViz)
data <- as.matrix(groceries)
data2 <- as(gro, "transactions")
arules <- apriori(gro, parameter = list(support=0.002, confidence=0.5, minlen= 2))
arules
inspect(arules[1:20,])
rules <- sort(arules, by="lift")
inspect(arules[1:20,])
inspect <- head(sort(arules, by="lift"))
head(quality(arules))
plot(arules)
plot(arules, method="grouped")
plot(arules, method = "graph")


#iteration 1 


arules <- apriori(gro, parameter = list(support=0.0021, confidence=0.6, minlen= 3))
arules
inspect(arules[1:20,])
arules <- sort(arules, by="lift")
inspect(arules[1:20,])
inspect <- head(sort(arules, by="lift"))
head(quality(arules))
plot(arules)
plot(arules, method="grouped")
plot(arules, method = "graph")

#iteration 2

arules <- apriori(gro, parameter = list(support=0.0022, confidence=0.4, minlen= 4))
arules
inspect(arules[1:20,])
rules <- sort(arules, by="lift")
inspect(arules[1:20,])
inspect <- head(sort(arules, by="lift"))
head(quality(arules))
plot(arules)
plot(arules, method="grouped")
plot(arules, method = "graph")




