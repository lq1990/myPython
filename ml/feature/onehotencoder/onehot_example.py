from sklearn.preprocessing import OneHotEncoder
import numpy as np

enc = OneHotEncoder()

X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]

enc.fit(X)

print(enc.transform([['female', 'from US', 'uses Safari'],
               ['male', 'from Europe', 'uses Safari']]).toarray())

print(enc.categories_)

print("===")
genders = [' ', 'male']
locations = ['from Africa', 'from Asia', 'from Europe', 'from US']
browsers = ['uses Chrome', 'uses Firefox', 'uses IE', 'uses Safari']

enc = OneHotEncoder(categories=[genders, locations, browsers], handle_unknown='ignore')
enc.fit([['female', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']])
print("cate: ",enc.categories_)
print(enc.transform([['', 'from Asia', 'uses Chrome']]).toarray())
print(enc.transform([[' ', 'from Asia', 'uses Chrome']]).toarray())

exit(0)
print("=== drop first")
X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
enc = OneHotEncoder()
drop_enc = OneHotEncoder(drop='first')
enc.fit(X)
drop_enc.fit(X)
print(drop_enc.categories_)
print("no drop: \n", enc.transform(X).toarray())
print("drop first: \n",drop_enc.transform(X).toarray())
