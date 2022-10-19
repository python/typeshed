from typing import overload

from cv2 import Mat, _MatF
from cv2.cv2 import (
    _NumericScalar,
    _UMat,
    ml_ANN_MLP,
    ml_Boost,
    ml_DTrees,
    ml_EM,
    ml_KNearest,
    ml_LogisticRegression,
    ml_ParamGrid,
    ml_RTrees,
    ml_SVM,
    ml_SVMSGD,
    ml_TrainData,
)

ANN_MLP_ANNEAL: int
ANN_MLP_BACKPROP: int
ANN_MLP_GAUSSIAN: int
ANN_MLP_IDENTITY: int
ANN_MLP_LEAKYRELU: int
ANN_MLP_NO_INPUT_SCALE: int
ANN_MLP_NO_OUTPUT_SCALE: int
ANN_MLP_RELU: int
ANN_MLP_RPROP: int
ANN_MLP_SIGMOID_SYM: int
ANN_MLP_UPDATE_WEIGHTS: int
BOOST_DISCRETE: int
BOOST_GENTLE: int
BOOST_LOGIT: int
BOOST_REAL: int
Boost_DISCRETE: int
Boost_GENTLE: int
Boost_LOGIT: int
Boost_REAL: int
COL_SAMPLE: int
DTREES_PREDICT_AUTO: int
DTREES_PREDICT_MASK: int
DTREES_PREDICT_MAX_VOTE: int
DTREES_PREDICT_SUM: int
DTrees_PREDICT_AUTO: int
DTrees_PREDICT_MASK: int
DTrees_PREDICT_MAX_VOTE: int
DTrees_PREDICT_SUM: int
EM_COV_MAT_DEFAULT: int
EM_COV_MAT_DIAGONAL: int
EM_COV_MAT_GENERIC: int
EM_COV_MAT_SPHERICAL: int
EM_DEFAULT_MAX_ITERS: int
EM_DEFAULT_NCLUSTERS: int
EM_START_AUTO_STEP: int
EM_START_E_STEP: int
EM_START_M_STEP: int
KNEAREST_BRUTE_FORCE: int
KNEAREST_KDTREE: int
KNearest_BRUTE_FORCE: int
KNearest_KDTREE: int
LOGISTIC_REGRESSION_BATCH: int
LOGISTIC_REGRESSION_MINI_BATCH: int
LOGISTIC_REGRESSION_REG_DISABLE: int
LOGISTIC_REGRESSION_REG_L1: int
LOGISTIC_REGRESSION_REG_L2: int
LogisticRegression_BATCH: int
LogisticRegression_MINI_BATCH: int
LogisticRegression_REG_DISABLE: int
LogisticRegression_REG_L1: int
LogisticRegression_REG_L2: int
ROW_SAMPLE: int
STAT_MODEL_COMPRESSED_INPUT: int
STAT_MODEL_PREPROCESSED_INPUT: int
STAT_MODEL_RAW_OUTPUT: int
STAT_MODEL_UPDATE_MODEL: int
SVMSGD_ASGD: int
SVMSGD_HARD_MARGIN: int
SVMSGD_SGD: int
SVMSGD_SOFT_MARGIN: int
SVM_C: int
SVM_CHI2: int
SVM_COEF: int
SVM_CUSTOM: int
SVM_C_SVC: int
SVM_DEGREE: int
SVM_EPS_SVR: int
SVM_GAMMA: int
SVM_INTER: int
SVM_LINEAR: int
SVM_NU: int
SVM_NU_SVC: int
SVM_NU_SVR: int
SVM_ONE_CLASS: int
SVM_P: int
SVM_POLY: int
SVM_RBF: int
SVM_SIGMOID: int
StatModel_COMPRESSED_INPUT: int
StatModel_PREPROCESSED_INPUT: int
StatModel_RAW_OUTPUT: int
StatModel_UPDATE_MODEL: int
TEST_ERROR: int
TRAIN_ERROR: int
VAR_CATEGORICAL: int
VAR_NUMERICAL: int
VAR_ORDERED: int

def ANN_MLP_create() -> ml_ANN_MLP: ...
def ANN_MLP_load(filepath: str) -> ml_ANN_MLP: ...
def Boost_create() -> ml_Boost: ...
def Boost_load(filepath: str, nodeName: str | None = ...) -> ml_Boost: ...
def DTrees_create() -> ml_DTrees: ...
def DTrees_load(filepath: str, nodeName: str | None = ...) -> ml_DTrees: ...
def EM_create() -> ml_EM: ...
def EM_load(filepath: str, nodeName: str | None = ...) -> ml_EM: ...
def KNearest_create() -> ml_KNearest: ...
def KNearest_load(filepath: str) -> ml_KNearest: ...
def LogisticRegression_create() -> ml_LogisticRegression: ...
def LogisticRegression_load(filepath: str, nodeName: str | None = ...) -> ml_LogisticRegression: ...
def NormalBayesClassifier_create() -> ml_LogisticRegression: ...
def NormalBayesClassifier_load(filepath: str, nodeName: str | None = ...) -> ml_LogisticRegression: ...
def ParamGrid_create(minVal: float | None = ..., maxVal: float | None = ..., logstep: float | None = ...) -> ml_ParamGrid: ...
def RTrees_create() -> ml_RTrees: ...
def RTrees_load(filepath: str, nodeName: str | None = ...) -> ml_RTrees: ...
def SVMSGD_create() -> ml_SVMSGD: ...
def SVMSGD_load(filepath: str, nodeName: str | None = ...) -> ml_SVMSGD: ...
def SVM_create() -> ml_SVM: ...
def SVM_getDefaultGridPtr(param_id: int | None) -> ml_ParamGrid: ...
def SVM_load(filepath: str) -> ml_SVM: ...
def TrainData_create(
    samples: _UMat,
    layout: int | None,
    responses: _UMat,
    varIdx: _UMat = ...,
    sampleIdx: _UMat = ...,
    sampleWeights: _UMat = ...,
    varType: _UMat = ...,
) -> ml_TrainData: ...
@overload
def TrainData_getSubMatrix(matrix: None, idx: Mat | None, layout: Mat | _NumericScalar) -> None: ...
@overload
def TrainData_getSubMatrix(matrix: Mat | float | bool, idx: Mat | None, layout: Mat | _NumericScalar) -> _MatF: ...
def TrainData_getSubVector(vec: Mat | float | bool, idx: Mat | None) -> _MatF: ...
