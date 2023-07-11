from sklearn.metrics import classification_report,confusion_matrix
from sklearn import metrics

c= 'cat'
d = 'donkey'
e = 'elephant'
true = [c,c,c,c,c,e,e,e,d,e,d,e,c,d,e,e,e,d,d,d]
pred = [c,c,c,c,d,d,e,d,d,d,c,c,d,d,e,e,e,d,e,e]
print("Confusion matrix")
print(confusion_matrix(true , pred))
print(classification_report(true , pred, digits=3))
test = [1,0,0,1,1,0]
pred = [1,1,0,1,1,0]
prop = [0.2,0.4,0.1,0.6,0.7,0.3]
print(f'precision : {metrics.precision_score(test,pred)}')
print(f'Recall : {metrics.recall_score(test,pred)}')
print(f'F1 Score : {metrics.f1_score(test,pred)}')
print(f'ROC_Auc : {metrics.roc_auc_score(test,prop)}')
