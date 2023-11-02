letter_dict = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
result = []


def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    def dfs(idx, path):
        if len(path) == len(digits):
            result.append(path)
            return
        for x in letter_dict[digits[idx]]:
            dfs(idx + 1, path + x)
    dfs(0, "")
    return result


digits = "2"
print(letterCombinations(digits))
