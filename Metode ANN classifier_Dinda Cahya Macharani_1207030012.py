from sklearn.neural_network import MLPClassifier
import pandas as pd

# Database: Gerbang logika AND
# Membaca data dari file
FileDB = 'logikaand.csv'
# file dapat berbentuk text, misal: logikaand.txt
Database = pd.read_csv(FileDB, sep=",", header=0)
print(Database)

# x = Data, y = target
x = Database[[u'Feature1', u'Feature2', u'Target' ]] #ciri1
# ciri2, dst
y = Database.Target

# Training and Classify
clf = MLPClassifier(solver='lbfgs', alpha=1e-2,hidden_layer_sizes=(10, 5),random_state=1,max_iter=1000, warm_start=True)
clf.fit(x, y)

# Prediksi
print ("Logika AND Metode Artificial Neural Network (ANN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))

