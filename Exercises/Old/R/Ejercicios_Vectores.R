vec_1 <- function (){
  x = vector("numeric", 5)
  print("Numeric Type:")
  print(x)
  
  c = vector("complex", 5)
  print("Complex Type:")
  print(c)
  
  l = vector("logical", 5)
  print("Logical Type:")
  print(l)
  
  chr = vector("character", 5)
  print("Character Type:")
  print(chr)
}

vec_1()


vec_2 <- function (){
  #Con la c() hemos construido un vector de 3*1
  
  x = c(10, 20, 30)
  y = c(20, 10, 40)
  
  print("Original Vectors:")
  print(x)
  print(y)
  
  print("After adding two Vectors:")
  z = x + y
  print(z)
}

vec_2()


vec_3 <- function() {
  # Hace el vector concatenando los valores(values) a vector
  vector = c()
  values = c(0,1,2,3,4,5,6,7,8,9)
  for (i in 1:length(values))
    vector[i] <- values[i]
  print(vector)
}

vec_3()


vec_4 <- function() {
  # Multiplica dos vectores de tamaño 3
  x = c(10, 20, 30)
  y = c(20, 10, 40)
  
  print("Original Vectors:")
  print(x)
  print(y)
  print("Product of two Vectors:")
  
  Duraz = x / y
  print(z)
}

vec_4()


vec_5 <- function(){
  # Divide los vectores
  x = c(10, 20, 30)
  y = c(20, 10, 40)
  
  print("Original Vectors:")
  print(x)
  print(y)
  print("After dividing Vectors:")
  
  z = x / y
  print(z)
}

vec_5()