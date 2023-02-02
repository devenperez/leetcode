public class Solution {
    const int INT_MAX = 2147483647;
    public int ReverseHelper(int x, int reversed) {
        if (reversed > (int) (INT_MAX / 10)) {
            return 0;
        }
        
        if (x < 10) {
            return reversed * 10 + x;
        }
        
        return ReverseHelper(x / 10, reversed * 10 + x % 10);
    }
    
    public int Reverse(int x) {
        if (x == - INT_MAX - 1) {
            return 0;
        }
        else if (x < 0) {
            return -1 * ReverseHelper(Math.Abs(x), 0);
        }
        return ReverseHelper(Math.Abs(x), 0);
    }
}