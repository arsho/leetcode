/*
Title     : 1441. Build an Array With Stack Operations
Category  : Stack
URL       : https://leetcode.com/problems/build-an-array-with-stack-operations/
Author    : arsho
Created   : 31 March 2021
*/
import java.util.ArrayList;

class Solution {
    public List<String> buildArray(int[] target, int n) {
        ArrayList<String> operations = new ArrayList<String>();
        int pos = 0;
        int targetLength = target.length;
        for(int i=1;i<=n;i++){
            if(i==target[pos]){
                pos++;
                operations.add("Push");
            }
            else{
                operations.add("Push");
                operations.add("Pop");
            }
            if(pos == targetLength)
                break;
        }
        return operations;
    }
}