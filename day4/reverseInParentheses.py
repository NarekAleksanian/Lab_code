def solution(inputString):
    end = inputString.find(")")
    start = inputString.rfind("(", 0, end)
    if end == -1:
        return inputString
    return solution(inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:])
