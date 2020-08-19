install.packages("plyr")
library(plyr)
X<-runif(50)
X
Y<-runif(50)
Y
data<-cbind(X,Y)
data
plot(data)
plot(data,type = "n")
text(data,rownames(data))
km<-kmeans(data,4)
str(km)
install.packages("animation")
library(animation)
km1<-kmeans.ani(data,4)
str(km1)
km$cluster
km$centers
normalized_data<-scale(mydata[,2:7])
fit<-kmeans(normalized_data,4)
str(fit)
final2<-data.frame(mydata,fit$cluster)
final2
final3<-final2[,c(ncol(final2),1:(ncol(final2)-1))]
aggregate(mydata[,2:7],by=list(fit$cluster), FUN = mean)              
wss =(nrow(normalized_data)-1)*sum(apply(normalized_data,2,var))
for (i in 2:8) wss[i]=sum(kmeans(normalized_data,centers = i)$withinss)
  
plot(1:8,wss,type = "b",xlab = "Number of clusters",ylab = "Within group sum of squares")
title(sub = "k-means clustering scree-plot")
install.packages("kselection")
library(kselection)
data()
?iris
View(iris)
k<-kselection(iris[-5],parallel = TRUE,k_threshold = 0.9,max_centers = 12)
k
install.packages("doparallel")
library(doParallel)
registerDoParallel(cores = 4)
k<-kselection(iris[-5],parallel = TRUE,k_threshold = 0.9,max_centers = 12)
k
install.packages("cluster")
library(cluster)
xds<-rbind(cbind(rnorm(5000,0,8),rnorm(5000,50,8)))
xcl<-clara(xds,2,sample =100)
clusplot(xcl)
xpm<-pam(xds,2)
clusplot(xpm)
