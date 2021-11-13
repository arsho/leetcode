/*
Title     : 2011. Final Value of Variable After Performing Operations
Category  : String
URL       : https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
Author    : arsho
Created   : 24 September 2021
*/

class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int value = 0;
        for(String operation: operations) {
            if(operation.indexOf("+") != -1) {
                value++;
            }
            else {
                value--;
            }
        }
        return value;
    }
}