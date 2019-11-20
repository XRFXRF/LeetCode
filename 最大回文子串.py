#先找收尾相同，再中间比较
class Solution:
    def pp(self,h:str):
            left=0
            right=len(h)-1
            while(left<right):
                if h[left]!=h[right]:
                    return False
                left+=1
                right-=1
            return h
    def longestPalindrome(self, s: str) -> str:
        if s=='':
            return ''
        results=[]
        for i in range(len(s)):
            for k in range(len(s)-1,i,-1):
                if s[k]==s[i]:
                    h=self.pp(s[i:k+1])
                    if h:
                        results+=[h]
                        break
        if not results:
            return s[0]
        else:
            length=[len(i) for i in results]
            return results[length.index(max(length))]

#中心扩散法，便利每个间隔和元素，从中间向两侧比较，不同的时候则结束
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
