class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer,Integer> nums1=new HashMap<>();
        int diff;
        for(int i=0;i<nums.length;i++){
            diff=target-nums[i];
            if (nums1.containsKey(diff)){
                return new int[]{i,nums1.get(diff)};
            }
            nums1.put(nums[i],i);
        }
        return new int[]{};
    }
}