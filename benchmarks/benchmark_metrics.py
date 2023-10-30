'''
all functions must have these three parameters:
predicts:dict, positives:dict, negatives:dict
'''
def basic_metric(predicts:dict, positives:dict, negatives:dict):
    pass

'''
MRR
Only calculate overlapped portion between prediction and ground truth
'''
def MRR(predicts:dict, positives:dict, negatives:dict):
    sm = 0
    cnt = 0
    for disease in positives:
        if disease not in predicts:
            continue
        for treatment in positives[disease]:
            try:
                rank = predicts[disease]
                sm += 1/(rank+1)
            except ValueError:
                pass
            cnt += 1
    if not cnt:
        return None
    return sm / cnt
            

'''
Hits@k
Only calculate overlapped portion between prediction and ground truth
'''
def hitsk(predicts:dict, positives:dict, negatives:dict, k=10000):
    pos = 0
    cnt = 0
    for disease in positives:
        if disease not in predicts:
            continue
        for i, treatment in enumerate(predicts[disease]):
            if i >= k:
                break
            cnt += 1
            if treatment in positive[disease]:
                pos += 1
    if not cnt:
        return None
    return pos/cnt 

