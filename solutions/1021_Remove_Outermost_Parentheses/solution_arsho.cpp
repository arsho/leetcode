/*
Title     : 1021. Remove Outermost Parentheses
Category  : Stack
URL       : https://leetcode.com/problems/remove-outermost-parentheses/
Author    : arsho
Created   : 30 March 2021
*/

#include <stack>

class Solution {
public:
    string removeOuterParentheses(string S) {
        string result = "";
        stack<char> compositions;
        int composition_flag = 0;
        for(int i=0;i<S.length();i++){
            if(S[i] == '('){
                compositions.push(S[i]);
            }
            else{
                compositions.pop();
            }
            if(compositions.empty()){
                result += S.substr(composition_flag+1, i-composition_flag-1);
                composition_flag = i+1;
            }
        }
        return result;
    }
};
