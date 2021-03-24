ex_1 <- function() {
  name = readline(prompt = "Your name here")
  age = readline(prompt = "Your age here")
  
  print (paste("My name is", name, " I'm ", age, " years old"))
  print(R.version.string)
}

ex_1()


ex_2 <- function () {
  name = "Python"; 
  n1 =  10; 
  n2 =  0.5
  nums = c(10, 20, 30, 40, 50, 60)
  print(ls())
  print("Details of the objects in memory:")
  print(ls.str())
  
}

ex_2()


ex_3 <- function(numbers1, numbers2, numbers3){
  print ("Sequence of numbers")
  print (seq(20,50))
  print('Mean of numbers')
  print(mean(20:60))
  print ('Sum of numbers')
  print (sum(51:9))
  
}

ex_3()


ex_4 <- function() {
  v = sample(-50:50, 10, replace = TRUE)
  
  print('Random integrer vector', v)
}

ex_4()


ex_5 <- function(){
  fibonacci <- numeric(10)
  fibonacci [1] <- fibonacci [2] <- 1
  for (i in 3:10) fibonacci[i] <- fibonacci[i-2] + fibonacci[i - 1]
  
  print('Fibonacci series, first 10 numbers')
  print(fibonacci)
  
}

ex_5()


ex_6 <- function (n){
  if (n >= 2) {
    x = seq(2, n)
    prime_nums = c()
    for (i in seq(2, n))
      if (any(x==i)) {
        prime_nums = c(prime_nums, i)
      }
  return(prime_nums)
    }
  else {
    stop('Input number should at least be *2*')
  }
}

ex_6(n = 12)


ex_7 <- function (){
  for (n in 1:100){
    if (n %% 3 == 0 & n%% 5 == 0){
      print('Duck and cover')
  }
    else if (n %% 3 == 0){
      print ('Duck')
  }
    else if (n %% 5 == 0) {
      print ('cover')}
  }
  }

ex_7 ()