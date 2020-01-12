'''
7. 整数反转
123	-> 321
-123 -> -321
2147483647 -> 0
2147483646 -> 0
120 -> 21
-2147483648 -> 0
-2147483647 -> 0
'''
class Solution7:
    def reverse(self, x: int) -> int:
        #最大的值与最小的值为：[−2^31, 2^31 − 1]， 即：[-2147483648, 2147483647]
        y = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        while x:
            if sign == 1:
                if y > 2147483647:
                    return 0
            else:
                if y > 2147483648:
                    return 0

            last = x % 10
            y = y * 10 + last
            x = x // 10

        if sign == 1:
            if y > 2147483647:
                return 0
        else:
            if y > 2147483648:
                return 0
        return sign * y