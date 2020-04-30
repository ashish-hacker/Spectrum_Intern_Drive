#To plot inline
%matplotlib inline

#import essential modules
import numpy as np
import matplotlib.pyplot as plt

#Scores Dictionary that Billy provided for 30 days
scores = {"Day 1": 100, "Day 2": 108, "Day 3":112, "Day 4":115, "Day 5":150,
          "Day 6":178, "Day 7": 143, "Day 8": 132, "Day 9":190, "Day 10": 235,
          "Day 11":253, "Day 12": 298, "Day 13": 328, "Day 14":390, "Day 15": 257,
          "Day 16":288, "Day 17": 393, "Day 18": 425, "Day 19":458, "Day 20": 450,
          "Day 21":473, "Day 22": 333, "Day 23": 452, "Day 24":490, "Day 25": 495,
          "Day 26":488, "Day 27": 543, "Day 28": 532, "Day 29":590, "Day 30": 605}
#Scores array from the 'Scores' Dictionary which contains the scores 
score_array = [scores[i] for i in scores]
Scores = np.array(score_array)

#Days array containing days from 1 to 30
Days = np.array(np.arange(1,31))

#Plot of Scores vs Days 
plt.plot(Scores,Days,color = 'g')

#Defining the x-label
plt.xlabel('Days')

#Defining the y-label
plt.ylabel('Scores')

plt.show()

#Calculating Mean ,Median ,Maximum and Minimum of the Array 'Scores'
Mean = np.mean(Scores)
Median = np.median(Scores)
Max = np.max(Scores)
Min = np.min(Scores)

print("Mean is {}".format(Mean))
print("Median is {}".format(Median))
print("Maximum is {}".format(Max))
print("Minimum is {}".format(Min))


