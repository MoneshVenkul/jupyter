from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score
y_actu = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
y_pred = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
cm1 = confusion_matrix(y_actu, y_pred)
print(confusion_matrix(y_actu, y_pred))
print("Accuracy : ",accuracy_score(y_actu, y_pred))
print("Precision : ",precision_score(y_actu,y_pred))
print("Recall : ",recall_score(y_actu,y_pred))
sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1 )
specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1)
