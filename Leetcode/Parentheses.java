class Solution {
    public boolean isValid(String s) {
        if (s.length() == 1){
            return false;
        }

        else if (s.length() % 2 != 0){return false;}

        String Over = s;
        while (Over.contains("()") || Over.contains("{}") || Over.contains("[]")){
            Over = Over.replace("()","");
            Over = Over.replace("[]","");
            Over = Over.replace("{}","");
        }

        if (Over.equals("")){
            return true;
        }
        else {
            return false;
        }
        
    }
}