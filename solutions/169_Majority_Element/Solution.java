/*
Title     : 169. Majority Element
Category  : Hash Table
URL       : https://leetcode.com/problems/majority-element/
Author    : arsho
Created   : 25 August 2021
*/
class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        int major = nums[0];
        HashMap<Integer, Integer> occurrences = new HashMap<Integer, Integer>();
        for(int i=0; i<n; i++) {
            int numberOfOccurrences;
            if(occurrences.get(nums[i]) != null) {
                numberOfOccurrences = occurrences.get(nums[i]) + 1;
            }
            else {
                numberOfOccurrences = 1;
            }
            occurrences.put(nums[i], numberOfOccurrences);
            if(numberOfOccurrences > n/2) {
                major = nums[i];
                break;
            }
        }
        return major;
    }
}