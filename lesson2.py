import  random;
#shani!!!!!!!!!!!!!!!!!!
random.seed(34556);
import  numpy as np;
np.random.seed(778777);
a=np.array([1,2,3,4,5,6],int);
b=np.arange(0,6,1);
c=np.random.randint(5,10,6)
print(a)
print(b)
print(c)
print(b*c);
print(np.argmax(a))
a=a.reshape(2,3);
print(a.mean(axis=1))
print(np.logical_and(a>1,a<5))
print(a[np.logical_and(a>1,a<5)])
a=np.where(np.logical_and(a>1,a<5),a**a,10);
print(a)
d=np.random.randint(100,200,21).reshape(3,7);
print(d)