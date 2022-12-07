def fixer(data):
    cid = {}
    j = 0
    for i, row in data.iterrows():
        if (row['CustomerDOB'], row['CustLocation'], row['CustAccountBalance']) not in cid:
            cid[row['CustomerDOB'], row['CustLocation'], row['CustAccountBalance']] = j
            j += 1

    data['cid'] = data.apply(lambda x: cid[x['CustomerDOB'], x['CustLocation'], x['CustAccountBalance']], axis=1)
    data['cid'] = data['cid'].astype(int)

    # To check the validity of the new cid, count the number of genders per cid
    sum(data.groupby('cid')['CustGender'].nunique() == 2)
    data = data.drop(columns=['CustomerID'])
    return data
