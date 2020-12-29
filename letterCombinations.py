class Solution:
    def recursion(self, index, answer, word, mapping, digits) -> [str]:
        if index + 1 == len(digits):
            for i in mapping[int(digits[index])]:
                answer.append(word + i)
            return answer
        else:
            for i in mapping[int(digits[index])]:
                self.recursion(self, index+1, answer, word + i, mapping, digits)
            return answer

    def letterCombinations(self, digits: str) -> [str]:
        mapping = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        answer = self.recursion(self, index=0, answer=[], word="", mapping=mapping, digits=digits)

        return answer

