class MinStack {

    public int[] arr;
    public int[] mins;
    public int length;

    public MinStack() {
        arr = new int[1];
        mins = new int[1];
        length = 0;
    }
    
    public void push(int val) {
        if (length == arr.length) {
            int[] newArr = new int[length * 2];
            int[] newMins = new int[length * 2];
            for (int i = 0; i < length; i++) {
                newArr[i] = arr[i];
                newMins[i] = mins[i];
            }
            newArr[length] = val;
            newMins[length] = Math.min(mins[length-1], val);
            arr = newArr;
            mins = newMins;
        } else {
            arr[length] = val;
            if (length >= 1) {
                mins[length] = Math.min(mins[length-1], val);
            } else {
                mins[0] = val;
            }
        }
        length++;
    }
    
    public void pop() {
        arr[length-1] = 0;
        mins[length-1] = 0;
        length--;
    }
    
    public int top() {
        return arr[length-1];
    }
    
    public int getMin() {
        return mins[length-1];
    }
}
