import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from autoTZX import utils
from autoTZX import mainAuto




boston = load_boston()
data = pd.DataFrame(boston.data, columns=boston.feature_names)
data['MEDV'] = boston['target']

dataDescription = {
    'MEDV':'output',
    'CHAS':'ignore'
}

process = mainAuto.autoProcess('regressor',dataDescriptions=dataDescription)
x, y = process.train(data)

