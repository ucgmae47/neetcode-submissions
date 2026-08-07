class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # separate into positives and negatives
        # create set of negatives
        # iterate over positive set and find targets
        # create set of positives
        # iterate over negative list and find targets
        # merge the two results, ignoring duplicates

        output = []
        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        set_pos = set(positives)
        set_neg = set(negatives)

        if nums.count(0) >= 3:
            output.append([0,0,0])

        found = set()
        if 0 in nums:
            for num in nums:
                if num != 0 and num not in found:
                    comp = -1 * num
                    if comp in nums:
                        output.append([0, num, comp])
                        found.add(num)
                        found.add(comp)

        for neg in set_neg:
            found = set()
            target = abs(neg)
            for pos in positives:
                if pos not in found and target - pos not in found:
                    if target - pos in set_pos:
                        if target - pos == pos and positives.count(pos) < 2:
                            continue
                        output.append([neg, pos, target - pos])
                        found.add(pos)
                        found.add(target - pos)

        for pos in set_pos:
            found = set()
            target = -1 * pos
            for neg in negatives:
                if neg not in found and target - neg not in found:
                    if target - neg in set_neg:
                        if target - neg == neg and negatives.count(neg) < 2:
                            continue
                        output.append([pos, neg, target - neg])
                        found.add(neg)
                        found.add(target - neg)
        
        return output