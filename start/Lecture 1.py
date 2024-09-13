import pandas as pd  
import numpy as np  

# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, None, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']} 

# df = pd.DataFrame(data) 

# print(df) 
# # filtering    

# # age_find = df[df['Age']>30] 
# # print()
# # print()
# # print()
# # print(age_find) 

# print(df.isnull()) 
# df_filled = df.fillna('unknown') 
# print(df_filled) 

# import numpy as np                     
# a=random_arr= np.random.randint(1,10 , size=[3,3]) 

# print(np.linalg.det(a))
# print(np.linalg.inv(a)) 


# df1 = pd.DataFrame({'ID': [1, 2, 3],
#                     'Name': ['Alice', 'Bob', 'Charlie']})

# df2 = pd.DataFrame({'ID': [1, 2, 3],
#                     'Score': [85, 90, 95]}) 

# df3= pd.merge(df1,df2, on='ID') 

# print(df3)

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 28],
        'Score': [90, 85, 88, 95]}

df = pd.DataFrame(data)

# Pivot table to summarize scores by 'Name'
pivot = df.pivot_table(values='Score', index='Name', aggfunc='mean')
print(pivot)