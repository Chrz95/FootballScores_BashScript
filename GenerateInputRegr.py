import random as rd

files = 2

for j in range(1,files+1):

    X = []
    Y = []

    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    err = 0

    filename = "input"+str(j)
    f = open(filename,"w")

    length = rd.randint(3,20)

    print(filename + ": ")

    for i in range (0,length):
        x_val = rd.uniform(-10, 10)
        X.append(x_val)
        y_val = rd.uniform(-10, 10)
        Y.append(y_val)
        f.write(str(x_val) + ":" + str(y_val) + "\n")

        sum_x = sum_x + x_val
        sum_x2 = sum_x2 + (x_val * x_val)
        sum_y = sum_y + y_val
        sum_xy = sum_xy + (x_val * y_val)

    a = ((length * sum_xy) - (sum_x*sum_y))/((length * sum_x2) - (sum_x*sum_x))
    b = (sum_y - (a*sum_x))/length
    for i in range(0,len(X)):
        err = ((Y[i] - (a*X[i] + b))*(Y[i] - (a*X[i] + b))) + err

    print("a =",str(a),"b =",str(b),"c = 1 err =",str(err))
    f.close()
