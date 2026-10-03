class MinStack {

    public int[] arr;
    public int length;

    public MinStack() {
        arr = new int[1];
        length = 0;
    }
    
    public void push(int val) {
        if (length == arr.length) {
            int[] newArr = new int[length * 2];
            for (int i = 0; i < length; i++) {
                newArr[i] = arr[i];
            }
            newArr[length] = val;
            arr = newArr;
        } else {
            arr[length] = val;
        }
        length++;
    }
    
    public void pop() {
        arr[length-1] = 0;
        length--;
    }
    
    public int top() {
        return arr[length-1];
    }
    
    public int getMin() {
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
}
