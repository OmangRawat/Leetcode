"""

---> Powerful Integers
---> Medium

"""

class Solution:
    def powerful_integers(self, x, y, bound):
        a, b, i, ans = 0, 0, 0, set()
        x_pow, y_pow = [], []
        if x == 1:
            if bound != 0:
                x_pow.append(1)
            a = 1
        if y == 1:
            if bound != 0:
                y_pow.append(1)
            b = 1
        while True:
            q = x ** i
            r = y ** i
            if a and b:
                break
            if a == 0:
                if q <= bound:
                    x_pow.append(q)
                else:
                    a = 1
            if b == 0:
                if r <= bound:
                    y_pow.append(r)
                else:
                    b = 1
            i += 1
        ans = set([x + y for x in x_pow for y in y_pow if x + y <= bound])
        return ans


xi = 3
yi = 5
bound = 15

a = Solution()
print(a.powerful_integers(xi, yi, bound))


"""

Get set of all powers of x and y smaller than bound then make set of pairs with sum smaller than the bound

Complexities:
Time ->  
Space -> 

"""
