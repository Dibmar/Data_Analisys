list_1 <- function() {
  # Una lista que contiene diferentes tipos de elementos
  list_data = list("R", "PHP", c(5, 7, 9, 11), TRUE, 125.17, 75.83)
  print("Data of the list:")
  print(list_data)
}
list_1()

list_2 <- function() {
  # Una lista de listas, vectores y matrices
  list_data <- list(c("Red","Green","Black"), matrix(c(1,3,5,7,9,11), nrow = 2),list("Python", "PHP", "Java"))
  
  print("List:")
  print(list_data)
  names(list_data) = c("Color", "Odd numbers", "Language(s)")
  
  print("List with column names:")
  print(list_data)
}
list_2()

# Nótese cómo funciona R. Dentro de las listas estas se diferencian c() para vectores, matrix() para matrices
# Se accede a las listas igual que Python

list_3 <- function() {
  # Una lista con un vector, matriz. Los elementos de la lista tienen nombre
  list_data <- list(c("Red","Green","Black"), matrix(c(1,3,5,7,9,11), nrow = 2), list("Python", "PHP", "Java"))
  
  print("List:")
  print(list_data)
  names(list_data) = c("Color", "Odd numbers", "Language(s)")
  
  print("List with column names:")
  print(list_data)
  print('1st element:')
  print(list_data[1])
  print('2nd element:')
  print(list_data[2])
}
list_3()

list_4 <- function() {
  # Concatena un nuevo elemento a la lista
  list_data <- list(c("Red","Green","Black"), matrix(c(1,3,5,7,9,11), nrow = 2), list("Python", "PHP", "Java"))
  
  print("List:")
  print(list_data)
  print("Add a new element at the end of the list:")
  list_data[4] = "New element"
  print("New list:")
  print(list_data)
}
list_4()

list_4b <- function() {
  lister <- list(c('Red_Dwarf', 'Holly'), matrix(c(1,3,5,7,9,11), nrow = 2), list('Doug_Naylor', 'Rob_Grant'))
  print (lister)
  
  print ('Adding a smeghead')
  lister[4] = 'Rimmer'
  
  print (lister)
  }
list_4b()

list_5 <- function() {
  # Crea una lista y anida un elemento en la 2ª lista
  x = list(list(0,2), list(3,4), list(5,6))
  
  print("Original nested list:")
  print(x)
  
  e = lapply(x, '[[', 2)
  print("Second element of the nested list:")
  print(e)
}
list_5()

list_6 <- function() {
  # Removes an element from the list by making it NULL
  list_data <- list(c("Red","Green","Black"), matrix(c(1,3,5,7,9,11), nrow = 2), list("Python", "PHP", "Java"))
  
  print("List:")
  print(list_data)
  
  print("Remove the second element of the list:")
  list_data[2] = NULL
  print("New list:")
  print(list_data)
}
list_6()

list_7 <- function() {
  # Actualiza un elemento de la lista
  list_data <- list(c("Red","Green","Black"), matrix(c(1,3,5,7,9,11), nrow = 2), list("Python"))
  
  print("List:")
  print(list_data)
  
  print("Update the second element of the list:")
  list_data[3] =  "R programming is fun"
  
  print("New list:")
  print(list_data)
}
list_7()

