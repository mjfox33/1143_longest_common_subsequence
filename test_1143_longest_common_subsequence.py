from code_1143_longest_common_subsequence import Solution

def test_example_1():
    s = Solution()
    t1 = "abcde"
    t2 = "ace"
    output = 3
    assert s.longestCommonSubsequence(t1,t2) == output