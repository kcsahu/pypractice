from collections import deque

def removeInvalidParentheses( s: str) -> list[str]:
        if not s:
            return []

        def is_valid(node):
            count = 0
            for c in node:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        result = []
        visited = {s}
        found = False
        while queue:
            node = queue.pop()
            if is_valid(node):
                result.append(node)
                found = True
            if found:
                continue
            for i in range(len(node)):
                if node[i] not in '()':
                    continue
                next = node[:i] + node[i + 1 :]
                if next not in visited:
                    queue.appendleft(next)
                    visited.add(next)
        return result

if __name__ == "__main__":
    s = "()())()"
    res = removeInvalidParentheses(s)
    print(res)
    assert res == ["(())()","()()()"]

    s = '(a)())()'
    res = removeInvalidParentheses(s)
    print(res)
    assert res == ["(a())()","(a)()()"]

    s = ')('
    res = removeInvalidParentheses(s)
    print(res)
    assert res == ['']