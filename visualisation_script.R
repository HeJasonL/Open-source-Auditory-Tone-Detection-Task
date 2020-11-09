rm(list = ls()) #Clear everything in environment

# Packages -------------------------------------------------------

load.packages <- function(pkg) {
  new.pkg <- pkg[!(pkg %in% installed.packages()[ , "Package"])]
  if (length(new.pkg)) {
    install.packages(new.pkg, dependencies = T)
  }
  sapply(pkg, require, character.only = T)
}

packages <- c("tidyverse", "nlme", "ggpubr", "Hmisc", "plyr", "Rmisc", "retimes", "data.table", "lme4","multcomp", 
              "pastecs", "effects", "DataCombine", "gridExtra", "leaps", "ppcor", "ggm", "readxl", "emmeans",
              "eeptools", "psych","weights", "here", "cowplot", "corrplot", "here")


# Themes ------------------------------------------------------------------
theme_JH = ggplot2::theme(
  text = ggplot2::element_text(size = 12, family = "Helvetica"),
  plot.tag = ggplot2::element_text(size = 20, face = "bold"),
  axis.title.x = ggplot2::element_text(size = 10),#, margin = unit(c(1, 0, 0, 0), "mm")),
  axis.title.y = ggplot2::element_text(size = 10, margin = ggplot2::unit(c(0, 1, 0, 0), "mm")),
  axis.text = ggplot2::element_text(size = 8),
  axis.text.x = ggplot2::element_text(angle = 0, vjust = 0, color = "black"),
  legend.title = ggplot2::element_text(size=16),
  legend.text = ggplot2::element_text(size=16),
  legend.position = "none",
  plot.title = ggplot2::element_text(lineheight=.8, face= "bold", size = 16),
  panel.border = ggplot2::element_blank(),
  panel.grid.minor = ggplot2::element_blank(),
  panel.grid.major = ggplot2::element_blank(),
  panel.background = ggplot2::element_blank(),
  axis.line = ggplot2::element_line(color = "black"),
  axis.ticks = ggplot2::element_line(colour = "black"))

cols <- c("0" = "red", "1" = "royalblue", "-" = "gray") #0's are incorrect, coded as red, and 1's are correct, coded as blue



# Analysis ----------------------------------------------------------------


load.packages(packages)
library(here)
files <- list.files(here("Auditory Tone Detection Task", "data"), pattern = c(".csv"))
pilot_files <- files[188:190]



# Quiet -------------------------------------------------------------------
data <- read_csv(here("Auditory Tone Detection Task", "data", pilot_files[1]))
data <- data[data$trialType=="Test",] #subset to trialtypes that are test ...
data <- data[!is.na(data$trialType),] # ... and remove any NAs

plot_a <- ggplot(data, aes(x=Trial, y= Desired_dB, colour = as.factor(Accuracy))) +
  geom_point(size =3) + theme_JH +
  labs(subtitle = data$Condition, tag = "a", y = "dB SPL", x = "Trial Number")  + 
  scale_colour_manual(values = cols) + ylim(30,80)


# Simultaneous ------------------------------------------------------------
data <- read_csv(here("Auditory Tone Detection Task", "data", pilot_files[2]))
data <- data[data$trialType=="Test",] #subset to trialtypes that are test ...
data <- data[!is.na(data$trialType),] # ... and remove any NAs
data$Condition

plot_b <- ggplot(data, aes(x=Trial, y= Desired_dB, colour = as.factor(Accuracy))) +
  geom_point(size = 3) + theme_JH +
  labs(subtitle = data$Condition, tag = "b", y = "dB SPL", x = "Trial Number")  + 
  scale_colour_manual(values = cols) + ylim(30,80)


# Backward ----------------------------------------------------------------
data <- read_csv(here("Auditory Tone Detection Task", "data", pilot_files[3]))
data <- data[data$trialType=="Test",] #subset to trialtypes that are test ...
data <- data[!is.na(data$trialType),] # ... and remove any NAs

plot_c <- ggplot(data, aes(x=Trial, y= Desired_dB, colour = as.factor(Accuracy))) +
  geom_point(size =3) + theme_JH +
  labs(subtitle = data$Condition, tag = "c", y = "dB SPL", x = "Trial Number")  + 
  scale_colour_manual(values = cols) + ylim(30,80)

all_plots <- ggarrange(plot_a, plot_b, plot_c, nrow = 1, ncol = 3)
