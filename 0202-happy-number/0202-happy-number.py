class Solution:
    def isHappy(self, n: int) -> bool:
        # store = {}
        # first = True
        # num = 0
        # while n > 0:
        #     if first:
        #         stringify = str(n)
        #         first = False
        #     else:
        #         stringify = str(num)
        #         num = 0

        #     for i in range(len(stringify)):
        #         num += int(stringify[i]) ** 2  

        #     if str(num) == "1":
        #         return True

        #     if num in store:
        #         break
        #     store[num] = num

        # return False
        used = []

        while(n>0):
            tmp = 0
            while(n>0):
                i = n%10

                tmp += i*i
                n = n//10

            if(tmp in used):
                return False
            else:
                used.append(tmp)

            if(tmp==1):
                return True
            
            n = tmp

        return False