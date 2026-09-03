class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        smallest_even = float('inf')
        smallest_odd = float('inf')

        for n in nums1:

            if n % 2 == 0:

                smallest_even = min(smallest_even , n)

            else:

                smallest_odd = min(smallest_odd , n)

        if smallest_odd == float('inf') or smallest_even == float('inf'):
            return True

        return smallest_odd < smallest_even 