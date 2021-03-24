tirada <- function(size = 3 ){

    dado <- 1:20
    roll <- sample(x = dado, size = size)
    return (roll)
}

tirada()


vector_tiradas <- c()

vector_tiradas <- c(vector_tiradas, tirada())



