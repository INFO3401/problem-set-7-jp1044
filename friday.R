#Problem 6
data <- read.csv(file="titanic.csv", head=TRUE, sep=",")
print(data)
summary(data)
#Problem 7
names(data)
print(data$PassengerId)
print(data$Survived)
table(data$Sex)
#Problem 8
prop.table(table(data$Sex, data$Survived))
prop.table(table(data$Sex, data$Survived),1)
#Problem 9
data$isChild[data$Age < 18] <- 1
data$isChild[data$Age > 18] <- 0
aggregate(Survived ~ Sex + isChild, data = data, FUN=length)
