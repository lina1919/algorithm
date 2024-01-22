stack = []
result = 0

# 입력 받기
len_str = int(input())
str_input = input()

for i in range(len(str_input)):
    # )( => pop
    if str_input[i] == '(' and stack and stack[-1] == ')':
        stack.pop()

    # ( => push
    elif str_input[i] == '(':
        stack.append(str_input[i])

    # () => pop
    elif str_input[i] == ')' and stack and stack[-1] == '(':
        stack.pop()

    # ) => push
    elif str_input[i] == ')':
        stack.append(str_input[i])

    #stack의 최대 크기
    result = max(len(stack), result)

# 원하는 문자열을 만들지 못했다면
if stack:
    print(-1)
else:
    print(result)
