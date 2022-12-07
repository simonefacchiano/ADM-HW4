def ele(bucket_ele,data):
    return data.index.get_loc(bucket_ele)
def Jsim(bucket,data):
    from sklearn.metrics import jaccard_score
    from sklearn.metrics.pairwise import pairwise_distances
    jac_sim = 1 - pairwise_distances(data.T, metric = "hamming")
    # optionally convert it to a dataFrame
    jac_sim = pd.DataFrame(jac_sim, index=data.columns, columns=data.columns)
    result=[]
    for i in range(len(bucket)-1):
        for j in range(i+1,len(bucket)):
            #print(f'Sim({bucket[i]},{bucket[j]}): ',jaccard_score(data.iloc[ele(bucket[i],data),:], data.iloc[ele(bucket[j],data),:]))
            similarity = jaccard_score(data.iloc[ele(bucket[i],data),:], data.iloc[ele(bucket[j],data),:])
            x = {"cust1": bucket[i], "cust2": bucket[j], "similarity": similarity}
            result.append(x)
    
    df1 = pd.DataFrame(result)
    print(df1)
