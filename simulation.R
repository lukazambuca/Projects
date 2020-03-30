install.packages("EpiModel")
install.packages("tidyverse")
install.packages("plotly")
install.packages("ggplot2")
install.packages("IRdisplay")
intsall.packages("leaflet")
install.packages("leafpop")
install.packages("dplyr")
install.packages("purrr")

library(tidyverse)
library(dplyr)
library(plotly)
library(ggplot2)
library(IRdisplay)
library(leaflet)
library(leafpop)
library(dplyr)
library(purrr) 
library(EpiModel)

#Sources
#1)https://timchurches.github.io/blog/posts/2020-03-10-modelling-the-effects-of-public-health-interventions-on-covid-19-transmission-part-1/
#2) https://cran.r-project.org/web/packages/EpiModel/EpiModel.pdf

#---------Simulation----------

#set controls. nsteps is number of days and we simulate 10 times

control <- control.icm(type = "SIR", nsteps = 100, nsims = 10)

#set initial conditions. s.num is the population total and i.num is number of infected
#at time zero , set r.num  = 0 for reproducibility of code

init <- init.icm(s.num = 10000, i.num = 2, r.num = 0)

#PARAMETERS 

#inf.prob is infection probability
#act.rate is exposure-to-infection rate
#rec.rate is recovery rate
#a.rate is arrival rate into our system
#ds.rate is departure rate of susecptible people from our system. SA has a crude death 
#rate of 9.5 in 1000 per annum.
#di.rate is departure rate from infected department, depends on mortality rate of virus
#but we just double ds.rate
#dr.rate is departure from recovered compartment, similar to ds.rate

#all the parameters could be estimated

param <- param.icm(inf.prob = 0.08, act.rate = 5, rec.rate = 1/20, 
                   a.rate = (10.5/365)/1000, ds.rate = (9.5/365)/1000, di.rate = (18/365)/1000, 
                   dr.rate = (7/365)/1000)

#call the icm function

sim <- icm(param, init, control)
sim

#simple plot 
plot(sim)

#if you want to see stochastic compartment model remove comment, you can choose at which day

#comp_plot(sim, at = 25, digits = 1)

#------------------Plotting our simulation-------------------

#get the mean, remember we simulate 10 times and want the mean values of the simulations

df.mean <- as.data.frame(sim, out = "mean")
df<- subset(df.mean, select=c("time", "s.num", "i.num","r.num"))


#set colours for plot

active_color <- "#1f77b4"
recovered_color <- "forestgreen"
death_color <- "red"


p2<-plot_ly(data = df)%>%
  add_trace(x = ~ time,
            y = ~ s.num,
            type = "scatter",
            mode = "lines+markers",
            name = "Susceptible",
            line = list(color = active_color),
            marker = list(color = active_color)) %>%
  add_trace(x = ~ time,
            y = ~ i.num,
            type = "scatter",
            mode = "lines+markers",
            name = "Infected",
            line = list(color = recovered_color),
            marker = list(color = recovered_color)) %>%
  add_trace(x = ~ time,
            y = ~ r.num,
            type = "scatter",
            mode = 'lines+markers',
            name = "Recovered/Dead",
            line = list(color = death_color),
            marker = list(color = death_color)) %>%
  layout(title = "",
         yaxis = list(title = "Cumulative Number of Cases"),
         xaxis = list(title = "Date"),
         legend = list(x = 0.1, y = 0.9),
         hovermode = "compare")
ggplotly(p2)

#ggplotly makes an interactive plot, useful for dashboard