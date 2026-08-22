class Solution:

  def addSpaces(self, s: str, spaces: list[int]) -> str:
    res = []
    prev = 0

    for idx in spaces:
      res.append(s[prev:idx])
      prev = idx

    res.append(s[prev:])

    return " ".join(res)
        
