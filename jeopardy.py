import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
#pd.set_option('display.max_colwidth', None)
data = pd.read_csv('jeopardy.csv')
#print(data)
#print(data.columns)
#print(data.info())
data.columns = ['Show_Number', 'Air_Date', 'Round', 'Category', 'Value', 'Question', 'Answer']

#3,4 Filtering a dataset by a list of words
def count_word (world_list,data,column):
    count = lambda x : all(i.lower() in str(x).lower() for i in world_list)
    data['Counts'] = data[column].apply(count)
count_word(['King','England'],data,'Question')
#print(data.loc[data['Counts'] == True,'Question'])

#5 finding the average value of those questions
data['Value'] = data.Value.apply(lambda x : 0 if x == 'None' else float(x[1:].replace(',','')))
count_word(['King'],data,'Question')
#print(data.loc[data['Counts'] == True,'Value'].mean())

#6 find the unique answers of a set of data
count_word(['King'],data,'Question')
print(data.loc[data['Counts'] == True,'Answer'].value_counts())

