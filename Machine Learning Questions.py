import timeit



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



def main():
    SpeedyNumPyCheck()


if __name__ == '__main__':
    main()


 
