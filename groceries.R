install.packages("readr")
library(readr)

install.packages("arules")
library("arules") 

groceries <- read.csv(file.choose())

View(groceries)
class(groceries)
summary(groceries)

arules_groceries <- apriori(groceries, parameter = list(support = 0.002, confidence = 0.75, minlen =2))
arules_groceries

inspect(head(sort(arules_groceries, by = "lift")))

head(quality(arules_groceries))

install.packages("arulesViz")
library("arulesViz")

plot(arules_groceries)

plot(arules_groceries, method = "grouped")
plot(arules_groceries[1:10], method = "graph")

write(arules_groceries, file = "groceries.csv", sep = ",")
getwd()
