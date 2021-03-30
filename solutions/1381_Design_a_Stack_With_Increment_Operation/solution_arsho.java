/*
Title     : 1381. Design a Stack With Increment Operation
Category  : Design
URL       : https://leetcode.com/problems/design-a-stack-with-increment-operation/
Author    : arsho
Created   : 30 March 2021
*/
class CustomStack {
    private int[] stack;
    private int totalElements;
    private int stackMaxSize;
    public CustomStack(int maxSize) {
        this.stack = new int[maxSize];
        this.totalElements = 0;
        this.stackMaxSize=maxSize;
    }

    public void push(int x) {
        if(this.totalElements<this.stackMaxSize)
            this.stack[this.totalElements++] = x;
    }

    public int pop() {
        if(this.totalElements==0){
            return -1;
        }
        else{
            this.totalElements--;
            int temp = this.stack[this.totalElements];
            this.stack[this.totalElements] = 0;
            return temp;
        }

    }

    public void increment(int k, int val) {
        for(int i=0;i<k;i++){
            if(i>=0 && i<this.stackMaxSize)
                this.stack[i]+=val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */