class Solution {
    public String longestCommonPrefix(String[] strs) {
        int i=0;
        int counter=0;
        String pref = "";
        
        if (strs.length == 0 || strs == null){
            return "";
        }

        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length-1];
        while (i < first.length()){
            if (first.charAt(i) == last.charAt(i)){
                pref += String.valueOf(first.charAt(i));
                counter++;
                i++;
            }
            else{
                break;
            }
        }
        if (counter == 0){
            return "";
        }
        else{
            return pref;
        }
       
    }
}