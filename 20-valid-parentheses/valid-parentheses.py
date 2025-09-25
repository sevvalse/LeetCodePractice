class Solution:
    def isValid(self, s: str) -> bool:
        stack = []      #LIFO
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)         #if opening par, append stack. Collecting the openings in order. If closing par, pop from stack in LIFO.
                                           #find reversed par from map. look if the par are the same.
        return not stack                             #if stack is empty, then all pars are closed.
        