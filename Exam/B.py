def get_area(n, measures):
    stack = []
    result = 0
    i = 0

    while i < n:
        if (not stack
                or measures[i] >= measures[stack[-1]]):
            stack.append(i)
            i += 1

        else:
            top_index = stack.pop()
            h = measures[top_index]
            w = i if not stack else i - stack[-1] - 1
            result = max(result, h * w)

    while stack:
        top_index = stack.pop()
        h = measures[top_index]
        w = n if not stack else n - stack[-1] - 1
        result = max(result, h * w)

    return result


n = int(input())
measures = list(map(int, input().split()))
print(get_area(n, measures))
