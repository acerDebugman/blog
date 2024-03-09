# numpy常用

### concatenate
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
np.concatenate((a, b.T), axis=1)
array([[1, 2, 5],
       [3, 4, 6]])
       
  
### transpose 矩阵的转置
np.transpose(x) 函数


###　矩阵
矩阵是 matrix类型，通过使用matrix类型，可以进行矩阵乘法等应用
如果matrix是有进行点乘，要使用 multiple()　进行




