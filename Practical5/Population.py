uk_countries = [57.11, 3.13, 1.91, 5.45]
zhejiang_neighbours = [65.77, 41.88 ,45.28, 61.27, 85.15]
#print the sorted lists
print ("英国各组成国家人口排序：",sorted(uk_countries))
print ("中国浙江省周边省份人口排序：", sorted(zhejiang_neighbours))

#print pie charts for the two lists
#define labels
uk_labels = ['England',  'Wales', 'Northern Ireland', ' Scotland']
zhejiang_labels = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
#define the factors of pie charts
#1.England
import matplotlib.pyplot as plt
plt.figure (figsize=(8,4))
plt.subplot(1,2,1)
plt.pie(uk_countries, labels=uk_labels, autopct='%1.1f%%', startangle=130)
plt.title('UK Countries')
#2.Zhejiang
plt.subplot(1,2,2)
plt.pie(zhejiang_neighbours, labels=zhejiang_labels, autopct='%1.1f%%', startangle=130)
plt.title('Zhejiang Neighbours')

plt.tight_layout()
plt.show()