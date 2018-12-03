def check(m,pos1,pos2):
    p=''
    return p==m[pos1][pos2]

def full_Matrix_check(board,n):
    for j in range(n):
        for i in range(n):
            if check(board, i,j):
                return False
    return True


def Non_repetitivee_move(m,n):
    import random
    num1=random.randint(0,n-1)
    num2=random.randint(0,n-1)
    while not check(m,num1,num2):
        
        num1=random.randint(0,n-1)
        num2=random.randint(0,n-1)
        print('Not Enter correct random number')
        if full_Matrix_check(m,n):
            print('The Matrix is full')
            break
    return num1,num2
def My_Percolation(n,p):
    import random
    kkk=[['' for i in range(n)] for i in range(n)]

    #for j in range(8):

        #for i in range(10):
            #kkk[i][j]='*'
    print(kkk)
    for i in range(n):
        for j in kkk[i]:
            print(j,end=' ')
        print()

    #print(Non_repetitivee_move(kkk))
    while True:
        if full_Matrix_check(kkk,n):
            print('The matrix is full')
            break
        else:
            pass
        nu1,nu2=Non_repetitivee_move(kkk,n)
        print(nu1,nu2)
        x=random.choices(['O','X'],cum_weights=[p,1],k=1)
        print(x)
        kkk[nu1][nu2]=x[0]
        print(kkk)
        for i in range(n):

            for j in kkk[i]:

                print(j,end=' ')
            print()
    return kkk

My_Percolation(20,0.6)
