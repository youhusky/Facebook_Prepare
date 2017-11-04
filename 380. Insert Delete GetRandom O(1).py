# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
# Example:

# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

# use array to save index
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

        self.array = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val in self.dic:
            return False
        # use array.length as the value!
        self.dic[val] = len(self.array)
        self.array.append(val)
        #print 'insert', self.array
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        
        index = self.dic[val]

        if index < len(self.array)-1:

            last_item = self.array[-1]
            
            self.array[index] = last_item
            self.dic[last_item] = index
          
            
            
        #print 'remove',self.array
        self.array.pop()
        #print 'removed',self.array
        del(self.dic[val])
        return True
        
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.array[random.randint(0,len(self.array)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

 
# Add to List
# 381. Insert Delete GetRandom O(1) - Duplicates allowed

# Note: Duplicate elements are allowed.

# 146
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic ={}
        self.array = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val not in self.dic:
            self.dic[val] = set()
            self.dic[val].add(len(self.array))
            self.array.append(val)
            return True
        else:
            self.dic[val].add(len(self.array))
            self.array.append(val)
            
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        
        index = self.dic[val].pop() # remove first item with index
        
        # compare the dic[val] -- max value whether equals to the last index of the self.array
        if index < len(self.array)-1:
           
            last_item = self.array[-1]
            self.array[index] = last_item
            
            # last item - index delete
            self.dic[last_item].remove(len(self.array)-1)

            # add new index which belonged to pop()
            self.dic[last_item].add(index)
            
            
        self.array.pop()
        if not self.dic[val]:
            del(self.dic[val])
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.array[random.randint(0,len(self.array)-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()