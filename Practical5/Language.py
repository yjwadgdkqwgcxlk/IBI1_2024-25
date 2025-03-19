# tell the information of language data using a list
language_data = {
    "JavaScript" : 62.3,
    "HTML" : 52.9,
    "Python" : 51,
    "SQL" : 51,
    "TypeScript" : 38.5
}
# draw a bar picture using matplotlib
import matplotlib.pyplot as plt
 
languages = list(language_data.keys())
percentages = list(language_data.values())

plt.bar(languages,percentages)
plt.xlabel("Programming Languages")
plt.ylabel("Percentage of Developers")
plt.title("Global Developer Language Popularity")
plt.show()
# to get the percentage of different types of languages' users
# for key,value in language_data.items():
#     print (f"The percent of people using {key}is{value}%")
# method 2
#e.g.
target_language = "Python"
print (f"The percentage of {target_language} users is {language_data[target_language]}%")