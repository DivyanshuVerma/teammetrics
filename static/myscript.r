
data <- read.table(file='/home/divyanshu/Projects/v2/teammetrics/static/demo.data', sep = '	', fill=TRUE, header=TRUE )

mycolors=c('red', 'blue', 'darkorange', 'darkgreen', 'darkorchid', 
           'brown', 'cornflowerblue', 'brown2', 'chartreuse3', 'aquamarine4')

plotcolors <- mycolors[1:6]

png('/home/divyanshu/Projects/v2/teammetrics/static/res.png', width = 1366, height = 768)

barplot(t(data),
    beside=TRUE,col=plotcolors,main='Graph for Accessibility', 
    legend.text=c("Samuel_T","Mario_L","Jason_W","Kenny_H","Jean_Philippe_M","mattias","Halim_S","Cyril_B","Veli_Pekka_T","Sebastian_D","Frans_P","Andor_D","Sebastian_H","Jan_and_Bertil_Smark_N","Odd_Martin_B","Simon_B","Milan_Z","Nath","Daniel_D","Paul_G","Jude_D","Petra_R","Denis_B","Gaijin","Luke_Y","Boris_D","mike_cutie_and_m","Bill_C","Anthony_S","Christian_P"), 
    ylab='Statistics', 
    xlab='Year',names.arg=c("2003","2004","2005","2006","2007","2008","2009","2010","2011","2012"))

dev.off()