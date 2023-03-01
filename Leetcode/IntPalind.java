class Solution {
    public boolean isPalindrome(int x) {
        Integer a = x;
        String temp = "";
        for (int i = a.toString().length()-1; i >= 0; i--){
            temp += String.valueOf(a.toString().charAt(i));
        }
        return (temp.equals(String.valueOf(a)));
    }
}