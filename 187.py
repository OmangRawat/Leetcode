"""

---> Repeated DNA Sequences
---> Medium

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        seen_seq, repeat_seq = set(), set()

        n = len(s)

        if n < 10:
            return repeat_seq

        for i in range(0, n - 9):
            seq = s[i:i + 10]
            if seq in seen_seq:
                repeat_seq.add(seq)
            else:
                seen_seq.add(seq)

        return repeat_seq
