
#!pip install lime
#!pip install nltk

import pandas as pd
import numpy as np
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib.pyplot as plt
import lime
from lime import lime_text
import sklearn
import sklearn.ensemble
import sklearn.metrics
from sklearn import feature_extraction
from __future__ import print_function
import nltk  
from sklearn.datasets import load_files  
nltk.download('stopwords')  
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split  
from sklearn.metrics import roc_curve, auc, f1_score, recall_score, precision_score
from sklearn.pipeline import make_pipeline
from lime.lime_text import LimeTextExplainer
import re

%matplotlib inline
%config InlineBackend.figure_format='retina'

# import csv data # this only has description, claims, and codes
df = pd.read_csv('small_descr_clm_code.csv')

# vectorized method is faster than apply and map
descr_series = df['descr']
descr_series = descr_series.str.replace('^\s +Description\s*|\s\sdetailed\sdescription.*','', case=None, flags=re.IGNORECASE|re.DOTALL, regex=True)
#### OR when used on Amazon SageMaker #####
#descr_series = descr_series.str.replace('^\s +Description\s*|\s\sdetailed\sdescription.*','', flags=re.IGNORECASE|re.DOTALL)
df['descr'] = descr_series

# Merge shortened description and claims
df['descr_clm'] = df.descr + df.clm

# Drop unwanted columns
df.drop(['Unnamed: 0','descr','clm'],axis=1, inplace=True)

# remove commas while it is in pandas dataframe so you can move it to pyspark dataframe
def remove_string(dataframe,column_list,string_in_quotes):
    '''
    Input:
            dataframe: name of pandas dataframe
            column_list: list of column name strings (ex. ['col_1','col_2'])
            string_in_quotes: string to remove in quotes (ex. ',')
    
    Output:
            none
            modifies pandas dataframe to remove string.
                
    Example:
            remove_string(df, ['col_1','col_2'], ',')
    
    Warning:
            If memory issues occur, limit to one column at a time.
        
    '''
    for i in column_list:
        dataframe[i] = dataframe[i].str.replace(string_in_quotes,"").astype(str)

# [ ] clean and automate this
remove_string(df, ['descr'],',')
remove_string(df, ['clm'],',')
remove_string(df, ['descr'],'\n')
remove_string(df, ['clm'],'\n')

# change label column to category to optimize data
df['code'] = df['code'].astype('category')
df.info() #show regular info
df.info(memory_usage='deep') #show scary info

#lime visualization data prep
#split data
X = df['descr']
y = df['code']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)

#stopword removal and ngram creation
vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(lowercase=False, ngram_range=(1, 2), max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)

#Random forest
rf = sklearn.ensemble.RandomForestClassifier(n_estimators=500)
rf.fit(train_vectors, y_train)

#f1_score tuple of probability specify what it shows
pred = rf.predict(test_vectors)
sklearn.metrics.f1_score(y_test, pred, average=None)

#Lime prediction
c = make_pipeline(vectorizer, rf)
class_names = ['705','706']
explainer = LimeTextExplainer(class_names=class_names)

idx = 83
exp = explainer.explain_instance(X_test.iloc[idx], c.predict_proba, num_features=6)
print('Document id: %d' % idx)
print('Probability(706) =', c.predict_proba([X_test.iloc[idx]])[0,1])
print('True class: %s' % y_test.iloc[idx])
print(X_test.iloc[idx]) #prints the text

#top features used for classification
exp.as_list() 

#modify the prediction to see results of removing features
print('Original prediction:', rf.predict_proba(test_vectors[idx])[0,1])
tmp = test_vectors[idx].copy()
tmp[0,vectorizer.vocabulary_['transactions']] = 0
tmp[0,vectorizer.vocabulary_['state']] = 0
print('Prediction removing some features:', rf.predict_proba(tmp)[0,1])
print('Difference:', rf.predict_proba(tmp)[0,1] - rf.predict_proba(test_vectors[idx])[0,1])

#vizualize
#local explanation for class 706
fig = exp.as_pyplot_figure()

#show prediction probability for classes and show highlighted text
exp.show_in_notebook(text=True)

#confusion matrix
y_pred = c.predict(X_test)
confusion_matrix(y_test, y_pred)

unique, counts = np.unique(y_pred, return_counts=True)
print(np.asarray((unique, counts)).T)

df_cm = pd.DataFrame(confusion_matrix(y_test, y_pred), index = ['True (705)', 'True (706)'])
df_cm.columns = ['Predicted (705)', 'Predicted (706)']

heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
heatmap.set_yticklabels(labels=['True (705)', 'True (706)'],rotation=0);