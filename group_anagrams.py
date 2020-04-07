# Group Anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        hashTable = {}
        result = []
        
        for word in strs:
            ana = "".join(sorted(word))
            if ana not in hashTable:
                hashTable[ana] = [word]
            else:
                hashTable[ana].append(word)
        for value in hashTable.values():
            result.append(value)
            
        return result