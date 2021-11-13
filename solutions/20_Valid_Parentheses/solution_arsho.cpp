/*
Title     : 20. Valid Parentheses
Category  : Stack
URL       : https://leetcode.com/problems/valid-parentheses/
Author    : arsho
Created   : 30 March 2021
*/
#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> parentheses;
        for(char c: s){
            if((c=='(')||(c=='{')||(c=='[')){
                parentheses.push(c);
            }
            else if((c==')' && !parentheses.empty() && parentheses.top()=='(') ||
                    (c=='}' && !parentheses.empty() && parentheses.top()=='{') ||
                    (c==']' && !parentheses.empty() && parentheses.top()=='[')){
                parentheses.pop();
            }
            else{
                return false;
            }
        }
        return parentheses.empty();
    }
};