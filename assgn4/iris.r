data <- read.csv("/home/pranav/Downloads/iris-species/Iris.csv")
View(data)
colnames(data) <- c("id", "sepal_length", "sepal_width", "petal_length", "petal_width", "species")
summary(data)
plot(data)
cor(data$petal_length,data$petal_width)
fit <- lm(data$petal_length ~ data$petal_width)
par(mfrow=c(2,2))
plot(fit)
residuals(fit)
summary(fit)
