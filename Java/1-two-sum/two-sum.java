class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sol = new int[2];
        for (int i = 0; i < nums.length; i++)
         for (int n = i + 1; n < nums.length; n++){
            if (nums[n] + nums[i] == target){
                sol[0] = n;
                sol[1] = i;
                return sol;
            }
         }
         return sol;
    }
}