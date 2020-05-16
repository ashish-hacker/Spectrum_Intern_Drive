#importing libraries
import pandas as pd 
import matplotlib.pyplot as plt 

#upload dataFiles
df = pd.read_csv('student-math.csv')


#Calculate final grade by adding three Grades
final_grade = df.G1 + df.G2 + df.G3

#insert it to the DataFrame
df.insert(31, "Final_Grade", final_grade)

#Delete the three different Grade columns
df.drop(['G1','G2','G3'], axis= 1, inplace=True)

#Replace all binary values with 1 and 0
df.replace(to_replace=['M','F','U','R','LE3','GT3','T','A','yes','no','GP','MS'], value=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

#plot the scatter plot using matplotlib
plt.scatter(df.studytime, df.Final_Grade, color='y')
plt.xlabel('Study Time of Students')
plt.ylabel('Final Grades')
plt.title('Scatter plot between study time and Final Grade of students')

#Now its time for boxplot
df.boxplot(column = 'Final_Grade', by = 'studytime', color='r')
plt.suptitle(' ')

