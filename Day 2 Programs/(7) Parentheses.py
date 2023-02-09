def generateParenthesis(n): 
    result = [] 
    generateParenthesisUtil(n, n, "", result) 
    return result 
def generateParenthesisUtil(left, right, string, result): 
    if left == 0 and right == 0: 
        result.append(string) 
        return
    if left > 0: 
        generateParenthesisUtil(left - 1, right, string + "(", result) 
    if right > left: 
        generateParenthesisUtil(left, right - 1, string + ")", result) 
if __name__ == "__main__": 
    n = int(input("Enter the number of pairs of parentheses: "))
    result = generateParenthesis(n) 
    print("All combinations of well-formed parentheses are: ") 
    for i in result: 
        print(i)
