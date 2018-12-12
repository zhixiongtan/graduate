from autoTZX import utils




class mainAuto(object):

    def __init__(self, estimatorType, dataDescriptions, verbose=True):
        if estimatorType.lower in ['regressor', 'regression']:
            self.estimatorType = 'regressor'
        elif estimatorType.lower in ['classifier','classification']:
            self.estimatorType = 'classifier'
        else:
            raise ValueError('Invalid value for estimator, please choose regressor or classifier instead')
        self.dataDescriptions = dataDescriptions
        self.verbose = verbose


    def valideDataDescriptions(self):
        outputColumn = False
        self.ignoreColumns = []
        for key, value in self.dataDescriptions.items():
            value = value.lower()
            self.dataDescriptions[key] = value
            if value == 'output':
                self.outColumn = key
                outputColumn = True
            if value == 'ignore':
                self.ignoreColumns.append(key)
        if outputColumn is False:
            raise ValueError('make sure excatly one column has the value OUTPUT for model training')


    def constructPipline(self, Model='LogisticRegression', featureLearning=False, HPSearch=False):
        pipLine = []
        pipLine.append(('basicDataTransform',utils.BasicDatacleaning()))





