# Program_15d.py: Male and Female Sample Heights. 
import matplotlib.pyplot as plt
import pylab
import scipy.stats as stats
MD = [73.8, 68.8, 74.1, 71.7, 69.9, 67.3, 68.8, 68.3, \
      67.3, 68.8, 68.3, 67.0, 63.5, 71.2, 71.6, 64.8, \
    69.3, 69.2, 67.6, 72.4, 64.3, 61.5, 74.8, 67.8,\
    69.6, 60.7, 71.3, 70.4, 67.0, 71.5, 72.7, 69.1, \
        69.0, 71.6, 70.4]
FD = [58.9, 65.2, 63.4 , 64.5, 61.7, 66.0, 62.9, 65.6, \
      61.9, 63.7, 68.1, 61.8, 63.4, 58.9, 58.4, 60.8, \
    70.1, 62.3, 61.7, 63.1, 62.3, 61.8, 66.3, \
    62.0, 65.3, 61.2, 67.0, 60.2, 63.9, 63.4, \
    63.7, 60.3, 63.4, 60.6, 67.4, 66.9, 60.9, 63.6, \
        59.6, 59.7, 65.0]
data = [FD , MD]
fig , ax = plt.subplots()
ax.set_ylim([55, 80])
ax.boxplot(data)
plt.xticks([1, 2], ['Female', 'Male'])
plt.ylabel('Heights (inches)')
plt.title('Box and Whisker Plots')
plt.show()
plt.figure()
plt.hist(MD, label='Male' , alpha=0.5)
plt.hist(FD, label='Female' , alpha=0.5)
plt.legend()
plt.title('Histograms')
plt.xlabel('Heights (inches)')
plt.ylabel('Frequency')
plt.figure()
stats.probplot(MD, dist="norm", plot=pylab)
pylab.title('Probability Plot for Male Data')
pylab.show()
plt.figure()
stats.probplot(FD, dist="norm", plot=pylab)
pylab.title('Probability Plot for Female Data')
pylab.show()
# Use Levene's test to test for equality of variances.
print(stats.levene(FD,MD,center= 'mean'))
# Student t-test.
print(stats.ttest_ind(FD,MD))

