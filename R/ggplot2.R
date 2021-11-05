install.packages("tidyverse")
library(tidyverse)
ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy))

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy,color=class))

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy,shape=class))

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy,size=class))

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy,alpha=class))

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy,alpha=class),color="red")

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy,color=class),shape=5)

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy))+
  facet_wrap(~class,nrow=2)

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy))+
  facet_grid(drv~cyl)#Let grids be by cylinder and gear number

ggplot(data=mpg)+
  geom_smooth(mapping=aes(x=displ,y=hwy))

ggplot(data=mpg)+
  geom_smooth(mapping=aes(x=displ,y=hwy,linetype=drv))

ggplot(data=mpg)+
  geom_smooth(mapping=aes(x=displ,y=hwy,color=drv))

ggplot(data=mpg)+
  geom_point(mapping=aes(x=displ,y=hwy))+
geom_smooth(mapping=aes(x=displ,y=hwy))

ggplot(data=mpg,mapping=aes(x=displ,y=hwy))+
  geom_point(mapping=aes(color=class))+
  geom_smooth()

ggplot(data=mpg,mapping=aes(x=displ,y=hwy))+
  geom_point(mapping=aes(color=class))+
  geom_smooth(
    data=filter(mpg,class=="subcompact"),
    se=FALSE,color="magenta")

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut))

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut,fill=clarity))

ggplot(data=diamonds,mapping=aes(x=cut,fill=clarity))+
  geom_bar(alpha=1/5,position="identity")

ggplot(data=diamonds,mapping=aes(x=cut,color=clarity))+
  geom_bar(fill=NA,position="identity")

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut,fill=clarity),position="fill")

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut,fill=clarity),position="dodge")

ggplot(data=mpg,mapping=aes(x=class,y=hwy))+
  geom_boxplot()

