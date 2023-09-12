class Solution:
    def isHappy(self, n: int) -> bool:
        store = {}
        first = True
        num = 0
        while n > 0:
            if first:
                stringify = str(n)
                first = False
            else:
                stringify = str(num)
                num = 0

            for i in range(len(stringify)):
                num += int(stringify[i]) ** 2  

            if str(num) == "1":
                return True

            if num in store:
                break
            store[num] = num

        return False