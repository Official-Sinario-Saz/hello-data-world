import pandas as pd

print("Hello, Data World!")

data = {
	'Name' : ['ali', 'sara', 'reza'],
	'Age': [25, 30, 28],
	'City' : ['tehran', 'shiraz', 'mashhad']

}

df = pd.DataFrame(data)
print("\nHere is a simple DateFrame : ")
print(df)
print("\nAverage Age : ", df['Age'].mean())
