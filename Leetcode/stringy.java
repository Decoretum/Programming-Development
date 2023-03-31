class Solution {
    public int strStr(String haystack, String needle) {
        int found = -1;
        int index = 0;
        int len = needle.length();
        int len2 = haystack.length();
        for (; index + len <= len2; index++){
            String word = "";
            for (int i = index, j = 0; j < len; i++, j++){
                word += haystack.charAt(i);
            }
    
            if (word.equals(needle)){
                return index;
            }
        }
        return found;
    }
}