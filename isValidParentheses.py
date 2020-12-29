class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for word in s:
            if word == '(' or word == '{' or word == '[':
                stack.append(word)
            else:
                if not len(stack):
                    return False
                leftPart = stack.pop()
                if leftPart == '(' and word != ')':
                    return False
                if leftPart == '{' and word != '}':
                    return False
                if leftPart == '[' and word != ']':
                    return False

        if len(stack):
            return False
        return True


print(Solution.isValid(Solution, "){"))