class Solution {
    public int lengthOfLastWord(String s) {
        if (s.length() == 1){
            return 1;
        }
        String new1 = s.trim();
        int pointer = new1.length()-1;
        int len = 0;
        if (new1.length() == 1){
            return 1;
        }

        for (; String.valueOf(new1.charAt(pointer)).isBlank() != true && pointer >= 0; pointer--){
            len++;
            if (pointer == 0){
                return len;
            }
        } 
        return len;
    }
}