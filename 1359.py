"""
---> Count All Valid Pickup and Delivery Options
---> Hard

"""

def countOrders(n: int) -> int:
    ans = 1
    for i in range(1, 2*n + 1):
        a = i
        if i % 2 == 0:
            a = i//2
        # print(a)
        ans *= a
    return ans % 1000000007


print(countOrders(2))

"""

---> Logic: 

countOrders(n + 1)
    = countOrders(n) * sum(valid P(n+1),D(n+1)) positions
    = countOrders(n) * ((2n+1) + (2n) + ... + 1)
    = countOrders(n) * (2n+1) * (2n+2) / 2
    
countOrders(n) = (2n)! / 2^n

countOrders(n + 1) = ((2n)! / 2^n) * ((2n+1 * 2n+2) / 2)
                   = (2n! * (2n+1) * (2n+2)) / (2^n * 2)
                   = (2n + 2)! / 2^(n+1)
                   = (2 * (n+1))! / 2^(n+1)

Complexities:
Time ->  O(N)
Space -> O(1)

"""
