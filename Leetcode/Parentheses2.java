class Solution {
    public boolean isValid(String s) {
        if (s.length() == 1){
            return false;
        }

        else if (s.length() % 2 != 0){return false;}

        Stack<String>Mystack = new Stack<>();
        HashMap<String,String> hashy = new HashMap<>();
        hashy.put("(",")");
        hashy.put("{","}");
        hashy.put("[","]");
        int i = 0;
        int left = 0;
        while (i < s.length()){
            String dig = String.valueOf(s.charAt(i));
            String peek = "";
            if (dig.equals("(") || dig.equals("{") || dig.equals("[")){Mystack.push(dig);}
            
            if (Mystack.empty()){
                peek = "";
            }
            else{
                peek = Mystack.peek();
            }
            if (dig.equals(hashy.get(peek))){
                String popped = Mystack.pop();
                left--;
                if (left <= 0){
                    left = 0;
                }
                }
            else{left += 1;}
            
            i++;
        }
        if (Mystack.empty() && left == 0){
            return true;
        }
        else{
            return false;
        }
        
        
    }
}