import csv


def performance_rate_knn():
    matrix = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
    neg = [" <=50K", " <=50K ", "<=50K ", "<=50K"]
    pos = [">50K", ">50K ", " >50K", " >50K "]
    with open("output/knn_result_income.csv") as table:
        #positive is over 50k, negative is under 50k
        read=csv.reader(table)
        next(read)
        for row in read:
            if row[1] in neg:
                if row[2] in neg:
                    matrix["True Negative"]=matrix["True Negative"]+1
                if row[2] in pos:
                    matrix["False Positive"]=matrix["False Positive"]+1
            if row[1] in pos:
                if row[2] in pos:
                    matrix["True Positive"]=matrix["True Positive"]+1
                if row[2] in neg:
                    matrix["False Negative"]=matrix["False Negative"]+1
    table.close()
    return matrix
def performance_rate_posterior(threshold):
    matrix = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
    neg = [" <=50K", " <=50K ", "<=50K ", "<=50K"]
    pos = [">50K", ">50K ", " >50K", " >50K "]
    with open("output/knn_result_income.csv") as table:
        read=csv.reader(table)
        next(read)
        for row in read:
            if float(row[-1]) <threshold:
                if row[2] in neg:
                    matrix["True Negative"]=matrix["True Negative"]+1
                if row[2] in pos:
                    matrix["False Negative"]=matrix["False Positive"]+1
            if float(row[-1]) >=threshold:
                if row[2] in pos:
                    matrix["True Positive"] = matrix["True Positive"] + 1
                if row[2] in neg:
                    matrix["False Positive"] = matrix["False Negative"] + 1
    table.close()
    return matrix

def roc():
    thresholds=[.97,.95,.93,.81,.55,.28,.17,.15,.10,.03]
    table=[]
    for i in thresholds:
        matrix=performance_rate_posterior(i)
        table.append([i,matrix["True Positive"],matrix["False Positive"]])
    return table

def precision(matrix):
    return matrix["True Positive"]/(matrix["True Positive"]+matrix["False Positive"])

def recall(matrix):
    return matrix["True Positive"]/(matrix["True Positive"]+matrix["False Negative"])

def f_measure(matrix):
    num=precision(matrix)*recall(matrix)
    denom=precision(matrix)+recall(matrix)
    return 2*num/denom

def main():
    matrix=performance_rate_knn()
    print("matrix")
    print(matrix)
    print("roc")
    print(roc())
    print("f measure")
    print(f_measure(matrix))

main()