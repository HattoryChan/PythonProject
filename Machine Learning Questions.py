import timeit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn


from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
#add words frequency(CountVectorizer) and weighted word frequencies(TfidfVectorizer)
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn.cluster.hierarchical import AgglomerativeClustering                        
from sklearn.cluster import KMeans

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
    
    
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

def CancerClassification():
    cancer = load_breast_cancer()
    print(f"Key Cancer(): \n {cancer.keys()}")
    print(f"Data array form for Cancer case: {cancer.data.shape}")
    print("Number of examples for each classes: {}".format({ n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))
    print(f"Signs name: \n {cancer.feature_names}")
    mglearn.plots.plot_knn_classification(n_neighbors=3)
  
def TrainTestSplit():
    X, y = mglearn.datasets.make_forge()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)
    
    print(f"Forecasts on the test case: {clf.predict(X_test)}")
    print("Correctness on the test case: {:.2f}".format(clf.score(X_test, y_test)))
    
    fig, axes = plt.subplot(1,3,figsize=(10, 3))
    
    for n_neighbors, ax in zip([1, 3, 9], axes):
        #creating classified object 
        clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
        mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title(f"Neighbors count: {n_neighbors}")
        ax.set_xlabel("Zero Sign")
        ax.set_ylabel("First Sign")
    axes[0].legend(loc=3)

def GenerateDataCase():
    #generate data case
    X,y = mglearn.datasets.make_forge()
    mglearn.discrete_scatter(X[:,0], X[:,1], y)
    plt.legend(["Class 0", "Class 1"], loc=4)
    plt.xlabel("First mark")
    plt.ylabel("Second mark")
    print(f"Array form X: {X.shape}")
    
    X,y = mglearn.datasets.make_wave(n_samples=40)
    plt.plot(X, y, 'o')
    plt.ylim(-3, 3)
    plt.xlabel("Mark")
    plt.ylabel("Target Variable")
 
class NapoleonIT:
    
    def TextClasterization(self):
        #train_all = fetch_20newsgroups(subset='train')
        #print (train_all.target_names)
        
        #simple_dataset = fetch_20newsgroups(subset = 'train',
         #   categories = ['comp.sys.mac.hardware', 'soc.religion.christian',
          #                'rec.sport.hockey'])
        #print(simple_dataset.data[0]) #Show first letter
        #print(simple_dataset.data[-1]) #Show last letter
        #print(simple_dataset.data[-2]) #Show penultimate letter
        
        #simple_dataset.target # letter subject
        
        #print( len(simple_dataset.data)) #all object in sample
        
        #Set min/max border
        vectorizer = CountVectorizer(max_df=500, min_df=10)
        
        #Discard unnecessary word(cheate object-sign matrix)
        
        #matrix = vectorizer.fit_transform(simple_dataset.data)
        #print(matrix.shape)
        
        #list of sign
        #print(vectorizer.get_feature_names())
        
        #Use NeighbourJoining:        
        #Create cosine measure
        #model = AgglomerativeClustering(n_clusters=3, affinity='cosine',
         #                              linkage = 'complete')
        #preds = model.fit_predict(matrix.toarray())
        
        #print( list(preds))
        
        #Use KMeans method
        #use random state to reproducibility of results
        #model = KMeans(n_clusters=3, random_state=1)
        #preds = model.fit_predict(matrix.toarray())
        
        #clusterization results
        #print(preds)
        #True answer
        #print(simple_dataset.target)
        
        #we made a right predictions
        #if we change the numbering of the clusters
        #mapping = {2: 1, 1: 2, 0: 0}
        #mapped_preds = [mapping[pred] for pred in preds]
        #we can calculate wrong share of predictions
        #and accurance ~33%
        #print( float(sum(mapped_preds != simple_dataset.target)) / 
         #      len(simple_dataset.target))
        #for compression we can take another classifier
        #clf = LogisticRegression()
        #print( cross_val_score(clf, matrix, simple_dataset.target).mean() )
        
        #Now take 3 similar theme
        dataset = fetch_20newsgroups(
                subset='train',
                categories=['comp.sys.mac.hardware',
                            'comp.os.ms-windows.misc',
                            'comp.graphics'])
        #use K-means method
        matrix = vectorizer.fit_transform(dataset.data)
        model = KMeans(n_clusters=3, random_state=42)
        preds = model.fit_predict(matrix.toarray())
        print(preds)
        print(dataset.target)
        
        #we see how alghorithm quality was dropped
        mapping = {2: 0, 1: 1, 0: 2}
        mapped_preds = [mapping[pred] for pred in preds]
        #accurance ~33%
        print( float(sum(mapped_preds != dataset.target)) / len(dataset.target))
        
        #for compression we can take another classifier
        clf = LogisticRegression()
        print (cross_val_score(clf, matrix, dataset.target).mean() )
        
    
def main():
    #SpeedyNumPyCheck()
    #IrisClassification()
    #CancerClassification()
    #TrainTestSplit()
    lection_2 = NapoleonIT()
    lection_2.TextClasterization()
    
    
    
if __name__ == '__main__':
    main()



 
