class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def check(test, target):
            if len(test) == 1:
                if target == int(test):
                    return True
                return False
            val = ""
            checker = False
            for i in range(len(test)-1):
                val += test[i]
                if (int(val) + int(test[i+1:])==target):
                    return True
                else:
                    if check(test[i+1:],target-int(val)):
                        checker = True
            return checker

        final = 0
        for i in range(1, n+1):
            test = str(i*i)
            if check(test, i):
                final += int(test)

        return final
