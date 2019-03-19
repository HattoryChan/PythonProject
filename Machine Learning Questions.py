import timeit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn


from sklearn.datasets import load_iris

from sklearn.model_selection import  train_test_split

from sklearn.neighbors import KNeighborsClassifier

    
    
def SpeedyNumPyCheck():
    normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))',
                                  number = 10000)

    naive_np_sec = timeit.timeit('sum(na*na)',
                                 setup="import numpy as np; na=np.arange(1000)",
                                 number=10000)

    good_np_sec = timeit.timeit('na.dot(na)',
                                setup='import numpy as np; na=np.arange(1000)',
                                number= 10000)

    print("Normal Python: %f sec" % normal_py_sec)
    print("Naive Numpy: %f sec" % naive_np_sec)
    print("Good NumPy: %f sec" % good_np_sec)


def IrisClassification():
    iris_dataset = load_iris()
    
    #familiarity with the data set
    #print("{}".format(iris_dataset.keys()))
    #print(iris_dataset['DESCR'][:193]+ '\n...')
    #print("{}".format(iris_dataset['target_names']))
    #print("{}".format(iris_dataset['feature_names']))
    #print("{}".format(type(iris_dataset['data'])))
    #print("{}".format(iris_dataset['data'].shape))
    #print("{}".format(iris_dataset['data'][:5]))
    #print("{}".format(iris_dataset['target'])) # 0 -setosa, 1 -versicolor, 2-virginica
    
    #Separate test and Cheak data
    X_train, X_test, y_train, y_test = train_test_split(
            iris_dataset['data'], iris_dataset['target'], random_state = 0)
    
    #create dataframe from X_train data
    #mark the column uses iris_dataset_feature_names
    iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
    #Create scattering matrix from dataframe, set point color with y_train help
    grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15),marker='o',
                            hist_kwds={'bins':20}, s=60,alpha=.8, cmap=mglearn.cm3)
    
    print('\n\n')
    #Knn prediction
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)
    
    X_new = np.array([[5, 2.9, 1, 0.2]])    
    prediction = knn.predict(X_new)
    print("Прогноз: {}".format(prediction))
    print("Prignazing mark: {}".format(iris_dataset['target_names'][prediction]))
    
    print('\n\n')
    #Knn accuracy
    y_pred = knn.predict(X_test)
    print("Prediction for the test case:\n {}".format(y_pred))
    print("Correctness on test case: {:.2f}".format(np.mean(y_pred == y_test)))
    print("Alternative correctness calculating on test case: {:.2f}".format(
            knn.score(X_test, y_test)))
    
def main():
    #SpeedyNumPyCheck()
    IrisClassification()
    
    

if __name__ == '__main__':
    main()



 
