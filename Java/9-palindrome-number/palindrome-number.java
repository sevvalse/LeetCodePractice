class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
            }

        String test_var = "";
        String st_x = String.valueOf(x);           //String.valueOf(x);

        for(int i=st_x.length() - 1; i>-1; i--){
            test_var += st_x.charAt(i);            //st_x.charAt(i)
            }

        return st_x.equals(test_var);
        }
    }