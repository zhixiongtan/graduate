from sklearn.base import BaseEstimator, TransformerMixin


class BasicDataCleaning(BaseEstimator, TransformerMixin):

    def __init__(self, dataDescriptions=None):
        self.dataDescription = dataDescriptions
        self.TransformedDataDescription = dataDescriptions.copy()
        self.numericType = ['int8','int16','int32','int64','float16','float32','float64']

    def get(self, propName, default=None):
        try:
            return getattr(self, propName)
        except:
            return default

    def fit(self, X, y=None):


