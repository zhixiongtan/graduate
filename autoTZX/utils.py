from sklearn.base import BaseEstimator, TransformerMixin

#
# class BasicDataCleaning(object):
#
#     def __init__(self, dataDescriptions=None):
#         self.dataDescription = dataDescriptions
#         self.TransformedDataDescription = dataDescriptions.copy()
#         self.numericType = ['int8','int16','int32','int64','float16','float32','float64']
#
#     def get(self, propName, default=None):
#         try:
#             return getattr(self, propName)
#         except:
#             return default
#
#     # def fit(self, X, y=None):


def dropIgnoreColumns(X, ignoreColumns):
    dropcolumns = []
    for col in ignoreColumns:
        if col in X.columns:
            dropcolumns.append(col)
    X.drop(dropcolumns, axis=1, inplace=True)
    return X

def dropDuplicateColumns(X):
    dropCounts = 0
    cols = list(X.columns)
    for idx, item in enumerate(X.columns):
        if item in X.columns[:idx]:
            dropCounts += 1
            cols[idx] = 'drop'
            print('drop duplication column {}'.join(item))

    if dropCounts >0 :
        X.columns = cols
        X.drop('drop', axis=1, inplace=True)
    return X

def transformY(estimator, y):
    if estimator == 'classifier':
        try:
            y_ = []
            for val in y:
                y_.append(int(val))
            y = y_
        except:
            pass

    else:
        try:
            y_ = []
            for val in y:
                y_.append(float(val))
            y = y_
        except:
            raise ValueError('There is a invalid type for regressor mission, please check it')
    return y


def dropNaNTarget(X, target):
    X = X.loc[X[target].notnull()]
    return X