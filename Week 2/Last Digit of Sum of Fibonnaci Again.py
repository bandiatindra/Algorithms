def last_digit_fibonnaci (n):

    if n==0:
        return 0

    if n==1:
        return 1
    
    else:

        arr = [0 for i in range(n+1)] 
        arr[0] = 0
        arr[1] = 1

        for i in range(2,n+1):
            arr[i] = (arr[i-1]%10 + arr[i-2]%10)%10 #Storing only the last digit. 

        return (sum(arr)%10)

if __name__ == '__main__':
    a, b = map(int, input().split())
    a_sum = last_digit_fibonnaci((a-1) %60)
    b_sum = last_digit_fibonnaci(b%60) 
    diff = b_sum - a_sum

    if diff >=0:
        print (diff)
    else: 
        print ((10-abs(diff)))

   