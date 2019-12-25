datasets = read.csv('Salary_Data.csv')
set.seed(222)
split= sample.split(datasets$Salary, SplitRatio = 2/3)
training_set = subset(datasets, split== TRUE)
test_set = subset(datasets, split== FALSE)

#SLR
regressor = lm(formula = Salary ~ YearsExperience, 
               data = training_set) 
y_pred = predict(regressor, newdata =  test_set)
yin= predict(regressor, newdata = training_set)

# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x= training_set$YearsExperience, y=training_set$Salary),
             colour ='red') +
  geom_line(aes(x=training_set$YearsExperience, y= yin,
            colour='blue') +
    ggtitle('Salary VS Yrs ')+ xlab('Yrs')+ ylab('salary')
ggplot() +
  geom_point(aes(x= test_set$YearsExperience, y=test_set$Salary),
             colour ='red') +
  geom_line(aes(x=test_set$YearsExperience, y= predict(regressor,newdata = test_set)),
            colour='blue') +
  ggtitle('Salary VS Yrs ')+ xlab('Yrs')+ ylab('salary')
  