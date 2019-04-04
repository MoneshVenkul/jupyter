import numpy as np
import pandas as pd
_mat=pd.read_csv("train.csv")
_mat=_mat[_mat.columns[0:3]].values
_t_mat=np.transpose(_mat)
print(_t_mat)
