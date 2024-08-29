x <- c(500,500,495,490,473,441,429,419,405,400,390,390,390,376,353,350,300,258,240,220,210,200,192,190,150,130,125,110,100,100)
########################################
#     Medidas de tendencia central     #
########################################
# Tamaño de Muestra
n = length(x)
n
[1] 30
# Mínimo
 min(x)
[1] 100
# Máximo
max(x)
[1] 500
# Media
me <- mean(x)
me
[1] 310.8667
# Mediana
median(x)
[1] 351.5
# Moda
library(modeest)
mfv(x)
[1] 390
#Percentil 0.16
quantile(x, 0.16)
  16% 
142.8 
# Percentil 0.84
quantile(x, 0.84)
   84% 
452.52 
# Primer decil
quantile(x, 0.1)
  10% 
123.5 
# Quinto decil
quantile(x, 0.5)
  50% 
351.5 
# Noveno Decil
quantile(x, 0.9)
  90% 
490.5 
#################################
#     Medidas de dispersion     #
#################################
# Varianza
var(x)
[1] 18598.53
# Desviacion estandar
s = sd(x)
s
[1] 136.3764
# Rango
range(x)
[1] 100 500
R = max(x) - min(x)
R
[1] 400
# Rango Intercuartilico
RIC <- quantile(x, 0.75) - quantile(x, 0.25)
RIC
  75% 
221.5 
ran_inter=mdn[4]-mdn[2]
Error: object 'mdn' not found
mdn = median(x)
ran_inter=mdn[4]-mdn[2]
ran_inter
[1] NA
# Coeficiente de Variación
cv <- s / me*100
cv
[1] 43.86975
hist(indemnizaciones, main = "Histograma de Indemnizaciones", xlab = "Monto (miles de pesos)")
Error: object 'indemnizaciones' not found
hist(x, main = "Histograma de Indemnizaciones", xlab = "Monto (miles de pesos)")