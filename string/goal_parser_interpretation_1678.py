class Solution:
    def interpret(self, command: str) -> str:
        # Solution 1- Chain the Replace method
        # return command.replace("()", "o").replace("(al)", "al")

        # Solution 2 - Parse the string and form new string
        # result = ""
        # for i in range(len(command)):
        #     if command[i] == 'G':
        #         result += 'G'
        #     elif command[i] == '(':
        #         if command[i+1] == ')':
        #             result += 'o'
        #             i += 1
        #         else:
        #             result += 'al'
        #             i+=3
        # return result

        # Solution 3 - Hashing

        string_mapping = {
            'G': 'G',
            '(al)': 'al',
            '()': 'o'
        }

        # command ="(al)(al)(al)(al)G()G(al)"
        result = ''
        temp = ''
        for character in command:
            temp += character
            if temp in string_mapping:
                result += string_mapping[temp]
                temp = ''
        return result


sol = Solution()

command = "G()(al)"
print(command, sol.interpret(command))

command = "(al)(al)(al)(al)G()G(al)"
print(command, sol.interpret(command))

command = "G()()()()(al)"
print(command, sol.interpret(command))

command = "(al)G(al)()()G"
print(command, sol.interpret(command))
