class Solution {
    public String addBinary(String a, String b) {
        String who = "";
        int sum = 0;
        if (a.length() != b.length()){
            if (a.length() > b.length()){
                who = b;
                sum = a.length() - b.length();
                for (int i = 0; i < sum; i++){
                    b = "0" + b;
                }
            } else {
                who = a;
                sum = b.length() - a.length();
                for (int i = 0; i < sum; i++){
                    a = "0" + a;
                }
            }
        } 

        int carry = 0;
        String answer = "";
        for (int i = a.length()-1; i>=0; i--){
            int first = Integer.parseInt(String.valueOf(a.charAt(i)));
            int second = Integer.parseInt(String.valueOf(b.charAt(i)));
            int result = first + second + carry;
            if (result > 1){
                if (result == 2){
                    answer = "0" + answer;
                    carry = 1;
                } else if (result == 3){
                    answer = "1" + answer;
                    carry = 1;
                }
            } else {
                carry = 0;
                answer = String.valueOf(result) + answer;
            }
        }
        
        if (carry == 1){
            answer = "1" + answer;
        }
        return answer;
        

    }
}