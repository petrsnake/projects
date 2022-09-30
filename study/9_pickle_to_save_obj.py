import pickle

#serialize object
exampleObj = {'python':3, 'kde':5, '10':5}
fileObj = open('data.obj', 'wb')
pickle.dump(exampleObj, fileObj)
fileObj.close()