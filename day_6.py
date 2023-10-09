import math

def minimax (cdepth, n_index,
             maxTurn, scores, 
             targetDepth):
 
    # base case : targetDepth reached
    if (cdepth == targetDepth): 
        return scores[n_index]
     
    if (maxTurn):
        return max(minimax(cdepth + 1, n_index * 2, 
                    False, scores, targetDepth), 
                   minimax(cdepth + 1, n_index * 2 + 1, 
                    False, scores, targetDepth))
     
    else:
        return min(minimax(cdepth + 1, n_index * 2, 
                     True, scores, targetDepth), 
                   minimax(cdepth + 1, n_index * 2 + 1, 
                     True, scores, targetDepth))
    
scores = list(map(int,input().split()))
 
treeDepth = math.log(len(scores), 2)
print(minimax(0, 0, True, scores, treeDepth))