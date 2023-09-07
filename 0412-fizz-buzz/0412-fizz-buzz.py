class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        response = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                response.append("FizzBuzz")
            elif i % 3 == 0:
                response.append("Fizz")
            elif i % 5 == 0:
                response.append("Buzz")
            else:
                response.append(f"{i}")
                
        return response
        