
data <- read.table(file='/home/divyanshu/Projects/v2/teammetrics/static/demo.data', sep = '	', fill=TRUE, header=TRUE )

mycolors=c('red', 'blue', 'darkorange', 'darkgreen', 'darkorchid', 
           'brown', 'cornflowerblue', 'brown2', 'chartreuse3', 'aquamarine4')

plotcolors <- mycolors[1:6]

png('/home/divyanshu/Projects/v2/teammetrics/static/res.png', width = 1366, height = 768)

barplot(t(data),
    beside=TRUE,col=plotcolors,main='Graph for Teammetrics_discuss', 
    legend.text=c("Sukhbir_S","Andreas_T","Alexander_W","Scott_H","Christian_P","Tollef_Fog_H","Cord_B","Martin_Z","Stephen_G","David_B","Ana_G","Charles_P"), 
    ylab='Statistics', 
    xlab='Year',names.arg=c("2011","2012"))

dev.off()