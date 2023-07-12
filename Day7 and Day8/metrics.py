from sklearn.metrics import classification_report,confusion_matrix
from sklearn import metrics
from nltk.translate.bleu_score import sentence_bleu
from nltk.metrics import edit_distance

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
#Precision Score
print(f'precision : {metrics.precision_score(test,pred)}')
#Recall
print(f'Recall : {metrics.recall_score(test,pred)}')
#F1 Score
print(f'F1 Score : {metrics.f1_score(test,pred)}')
#Roc Auc
print(f'ROC_Auc : {metrics.roc_auc_score(test,prop)}')

#Bleu score 

reference = [
    'this is a dog'.split(),
    'it is a dog'.split(),
    'dog it is'.split(),
    'a dog , it is'.split()
]
candidate = 'it is a dog'.split()
print(f'Bleu score : {sentence_bleu(reference,candidate)}')

#Character and Word error

getval = 'it is a dog'
predval = 'it is a cat'
print(f'Character error : {edit_distance(getval,predval)/len(getval)}')
print(f'Word error : {edit_distance(getval.split(),predval.split())/len(getval)}')


