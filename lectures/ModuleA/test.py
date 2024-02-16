def test():
    stringlist = {1:"old str"}
    
    def nested():
        stringlist[1] = "it's changed!"
        stringlist[2] = maxnum+1
    maxnum = 1
    nested()
    return stringlist
    
print(test())

def depthSum(nestedList) -> int:
    ans = 0
    
    def setdict(depth, entry):
        nonlocal ans
        ans += depth * entry
        return ans+1

    #parse list into dict with corresponding depth     
    for entry in nestedList:
        ans += setdict(1, entry)
    return ans

print(depthSum([1,2,3]))