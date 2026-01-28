class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String a="";
        int b;
         if (strs[0].length()>strs[strs.length-1].length()){
            b=strs[strs.length-1].length();
         }
         else{
            b=strs[0].length();
         }
         for (int i=0;i<b;i++){
            if (strs[0].charAt(i)==strs[strs.length-1].charAt(i)){
                a+=strs[0].charAt(i);
            }
            else{
                break;
            }
         } 
         return a;
        }
    }