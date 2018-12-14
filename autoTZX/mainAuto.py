from autoTZX import utils



class autoProcess(object):

    def __init__(self, estimatorType, dataDescriptions, multiDefaultModel=False, verbose=True):
        if estimatorType == 'classifier' or estimatorType == 'regressor':
            self.estimatorType = estimatorType
        else:
            raise ValueError('Invalid value for estimator, please choose regressor or classifier instead')
        self.dataDescriptions = dataDescriptions
        self.verbose = verbose
        self.multiDefaultModel = multiDefaultModel


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


    def defaultEstimator(self):
        if self.estimatorType == 'regressor':
            baseEstimator = ['GradientBoostingRegressor']

            if self.multiDefaultModel == True:
                baseEstimator.append('RANSACRegressor')
                baseEstimator.append('RandomForestRegressor')
                baseEstimator.append('LinearRegression')
                baseEstimator.append('AdaBoostRegressor')
                baseEstimator.append('ExtraTreesRegressor')
                return baseEstimator
            else:
                return baseEstimator

        elif self.estimatorType == 'classifier':
            baseEstimator = ['GradientBoostingClassifier']
            if self.multiDefaultModel == True:
                baseEstimator.append('LogisticRegression')
                baseEstimator.append('RandomForestClassifier')
                return baseEstimator
            else:
                return baseEstimator

        else:
            raise ('TypeError: type of estimator must be either classifier or regressor')




    def prepareData(self, data):
        self.valideDataDescriptions()
        if len(self.ignoreColumns)>0:
            X_train = utils.dropIgnoreColumns(data, self.ignoreColumns)

        X_train = utils.dropNaNTarget(X_train, self.outColumn)
        X_train = utils.dropDuplicateColumns(X_train)
        y_train = X_train[self.outColumn]
        X_train.drop(self.outColumn, axis=1, inplace=True)
        y_train = utils.transformY(self.estimatorType, y_train)

        return X_train, y_train



    def constructPipline(self, Model='LogisticRegression', featureLearning=False, HPSearch=False):
        pipLine = []
        pipLine.append(('basicDataTransform',utils.BasicDatacleaning()))


    def fitSinglePipline(self,X, y):
        # placeholder for fucntion

    def fitModelSearch(self,X, y, searchModel):




    def trainEstimator(self, modelNames, X, y):
        if len(modelNames) == 1:
            trainFinalModel = self.fitSinglePipline(X, y)

        elif len(modelNames)>1 and self.optimizeModel == False:
            searchModel = {}
            ModelWithParams = map(utils.mapModels, modelNames)
            searchModel['model'] = list(ModelWithParams)
            self.searchModel = searchModel
            searchResult = self.fitModelSearch(X, y, searchModel)
            trainFinalModel = searchResult.best_estimator_



    def train(self, data, model=None, score=False, optimizeModel=False):
        X_train, y_train = self.prepareData(data)
        self.model = model
        if self.model == None:
            self.model = self.defaultEstimator()

        #main logic

        self.finalModel = self.trainEstimator(self.model, X_train, y_train)






