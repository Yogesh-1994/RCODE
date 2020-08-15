installed.packages("tree")
library(tree)
data()
data("iris")
View(iris)
library(tree)
iris_tree<-tree(Species~.,data = iris)
plot(iris_tree)
text(iris_tree)
pred_tree <- as.data.frame(predict(iris_tree,iris))
View(pred_tree)                        
pred_tree["Final"]<- NULL
for (i in 1:nrow(pred_tree)) {
  pred_tree[i,"Final"]<-ifelse(pred_tree[i,"setosa"]>0.5,"setosa",ifelse(pred_tree[i,"versicolor"]>0.5,"versicolor","verginica"))
}
library(gmodels)
CrossTable(iris$Species,pred_tree$Final)
mean(pred_tree$Final==iris$Species)
