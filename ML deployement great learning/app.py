import flask
import pickle
pickle_out = open("adult.pkl","wb")
pickle.dump(model,pickle_out)
loaded_model=pickle.load(open("adult.pkl","rb"))
result=loaded_model.score(X_test,Y_test)
print(result)
