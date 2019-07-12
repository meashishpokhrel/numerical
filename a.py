import numpy as np
import matplotlib.pyplot as plt
x=np.arange (-5,5,1)
y1=x**2
y2=2*x+15
plt.plot(x,y1,'r')
plt.plot(x,y2,'r')


plt.plot(x,y, 'r:*')
plt.title('quadratic graph', color='red',fontsize=20, fontweight='bold')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.text(-3,15,'$y=x^2$')