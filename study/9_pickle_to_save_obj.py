import pickle

#serialize object
exampleObj = {'python':3, 'kde':5, '10':5}
fileObj = open('data.obj', 'wb')
pickle.dump(exampleObj, fileObj)
fileObj.close()

#deserilaze object
fileObj = open('data.obj', 'rb')
exampleObj = pickle.load(fileObj)
fileObj.close()
print(exampleObj)




#cvičení
import pickle
fileObj = open('file_for_fun', 'wb')
file_for_fun = 'eskymáci snáší práci'
pickle.dump(file_for_fun,fileObj)

fileObj = open('file_for_fun', 'wb')
deserialized = pickle.load(file_for_fun)
file_for_fun.close()
print(deserialized)

