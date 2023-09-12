class Solution:
    def isHappy(self, n: int) -> bool:
        store = {}
        tries = 100
        stringify = str(n)
        num = 0
        while tries > 0:
            if tries != 100:
                stringify = str(num)
                num = 0
            for i in range(len(stringify)):
                if stringify[i] not in store:
                    store[stringify[i]] = int(stringify[i]) ** 2  
                num += store[stringify[i]]
            if str(num) == "1":
                return True
            tries = tries - 1

        return False