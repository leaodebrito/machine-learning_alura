import seaborn as sns
import pandas as pd
import numpy as np
#from sklearn.model_selection import train_test_split
#from sklearn.svm import LinearSVC
#from sklearn.metrics import accuracy_score


uri = 'https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv'

dados = pd.read_csv(uri)
