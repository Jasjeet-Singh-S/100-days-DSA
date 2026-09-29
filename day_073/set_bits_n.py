# https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1

# class Solution:
#     def countSetBits(self,n):
#         count = 0
#         for i in range(1,n+1):
#             count += self.setBits(i)
#         return count
        
#     def setBits(self, n):
#         count = 0
#         while(n):
#             n = n & n-1
#             count += 1
#         return count

# this gives a TLE 

# https://youtu.be/g6OxU-hRGtY?si=VBV6jpVTNIR1MoXR

class Solution:
    def countSetBits(self,n):
        count = 0
        bit_length = n.bit_length()
        # largest power of two smaller than n
        power_of_two = 1<<(bit_length-1)
        # number of set bits upto this power of two will be ((power of two)/2)*(bit length of power of two - 1)
        count += (power_of_two/2)*(power_of_two.bit_length() - 1)

        # now we just have to count from power of two + 1 to n
        
        for i in range(power_of_two+1,n+1):
            count += self.setBits(i)
        return count
        
    def setBits(self, n):
        count = 0
        while(n):
            n = n & n-1
            count += 1
        return count