df = data.frame(Ints = integer(), Doubles = double(), Logicals = logical(), Factors = factor(), stringsAsFactors = FALSE)

df

uno = c(1, 2, 3, NaN)
dos = c('Dave Lister', 'Arnold Rimmer', 'Cat', 'Kriten')
tres = c('Craig Charles', 'Chris Barrie', 'Danny John Jules', NaN)


df2 = data.frame(col1= uno, col2 = dos, col3 =  tres)

df2[1, 3] #equivalente a iloc. Los números van ORDINALES
df2 = na.exclude(df2, na.action = "exclude", fill = NULL)
# Dropna

dfex_1 <- function(df){
print("Structure:")
print(str(df))
}
dfex_1(df2)

dfex_2 <-function(df){
  print("Statistical summary and nature of the data of the said dataframe:")
  print(summary(df))
}
dfex_2(df2)

dfex_3 <- function(df, column){
  print("Extract Specific columns:")
  result <- data.frame(df$column,df$score)
  print(result)
}
dfex_3(df2, uno)

result =  df2[c(1,3),c(1,2)]
print(result)

