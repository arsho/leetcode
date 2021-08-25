/*
Title     : 169. Majority Element
Category  : Hash Table
URL       : https://leetcode.com/problems/majority-element/
Author    : arsho
Created   : 25 August 2021
*/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return nums[0];
        int major;
        map<int, int> occurrences;
        for(auto i: nums) {
            if(occurrences.find(i) == occurrences.end()) {
                occurrences[i] = 1;
            }
            else {
                occurrences[i]++;
                if(occurrences[i] > n/2) {
                    major = i;
                    break;
                }
            }
        }
        return major;
    }
};