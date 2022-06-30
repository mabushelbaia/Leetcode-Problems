class Solution {
    public int reverse(int x) {
        boolean isNegative = false;
        if(x<0) {
            isNegative = true;
            x = - x;
        }
        long result = 0;
        while(x>0){
            int digit = x%10;
            result = result * 10 + digit;
            x /= 10;
        }
        if (result > Integer.MAX_VALUE){ return 0;}
        return (int) (isNegative? -result: result);
    }
}
