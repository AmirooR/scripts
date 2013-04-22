from sklearn.utils import shuffle
from sklearn import datasets
from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.metrics import mean_squared_error
import numpy as np
import pickle
#from sklearn.grid_search import G
from sklearn.grid_search import IterGrid

def mean_abs_err( y_test, y_pred ):
	gg = abs(np.exp(y_test) - np.exp(y_pred))/np.exp(y_test)
	return gg.mean()

def mean_log_err( y_test, y_pred):
	gg = abs(y_test - y_pred)
	return gg.mean()

(X,y) = datasets.load_svmlight_file('/Users/amirrahimi/Desktop/doc/visionTools/lasik-2.4/amir/Features/bld_new/all/below_79.selected.building.log.txt')

#(X,y) = datasets.load_svmlight_file('/Users/amirrahimi/Desktop/doc/visionTools/lasik-2.4/amir/Features/gnd/below_79.ground.selected.log.txt')
X_train, y_train = shuffle(X,y,random_state=13)
#(X_test,y_test) = datasets.load_svmlight_file('/Users/amirrahimi/Desktop/doc/visionTools/lasik-2.4/amir/Features/gnd/below_79.ground.rest.log.txt')
(X_test,y_test) = datasets.load_svmlight_file('/Users/amirrahimi/Desktop/doc/visionTools/lasik-2.4/amir/Features/bld_new/all/below_79.rest.building.log.txt')

X_train = X_train.todense()
clf = GBR(n_estimators=200, loss='ls',max_depth=4, min_samples_split = 1, learn_rate = 0.1) # FIXME maxdepth = 8
X_test = X_test.todense()
#clf.fit(X_train, y_train)
#clf = GBR(max_depth=8, min_samples_split = 1)
#tuned_parameters = [{'n_estimators': [100,200,300,400,500], 'loss' : ['ls','lad'], 'learn_rate':[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1]}]
tuned_parameters = [{'n_estimators': [500,600,700], 'loss' : ['ls'], 'learn_rate':[0.075,0.1,0.25]}]
#tuned_parameters = [{'n_estimators':[100], 'loss' : ['ls','lad'], 'learn_rate':[1]}]
scores = [('mse', mean_squared_error),
       ('abs_err', mean_abs_err),
       ('log_err', mean_log_err)
       ]

grid_list = list(IterGrid(tuned_parameters))
for i in range(len(grid_list)):
	clf.set_params(**grid_list[i])
	print 'training '+ str(grid_list[i])
	clf.fit( X_train, y_train)
	y_pred = clf.predict( X_test)
	for score_name, score_func in scores:
		print score_name + ': ' + str( score_func( y_pred, y_test ) )

