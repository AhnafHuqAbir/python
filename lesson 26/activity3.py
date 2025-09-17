class pair_elements:

    def twosSum(self, nums, target):

        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num], i)
            lookup[num] = i

choice = int(input("Enter sum for which you want to make this search :"))
print("index1=%d, index2=%d" %
pair_elements().twosSum([10, 20, 10, 40, 50, 60, 70], choice))