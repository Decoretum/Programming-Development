class Solution {
    public int[] plusOne(int[] digits) {
        if (digits.length == 1){
            if (digits[0] < 9){
                digits[0] = digits[0] + 1;
                return digits;
            }
            else{
                int [] ten = new int[2];
                ten[0] = 1;
                ten[1] = 0; 
                return ten;
            }
        }

        else{
            if (digits[digits.length-1] != 9){
                digits[digits.length-1] = digits[digits.length-1] + 1;
            }
            else{
                String building = "";

                for (int i : digits){
                    building += String.valueOf(i);
                }
                
                
                int pointer = building.length()-1;
                int carry = 0;
                String finalvalue = "";
    
                while (pointer >= 0){

                    int value = 0;
                    int current = 0;
                    int wordvalue = Integer.parseInt(String.valueOf(building.charAt(pointer)));
                    if (pointer == building.length()-1){
                        value = carry + 1 + wordvalue;
                    }
                    else{
                        value = carry + wordvalue;
                    }

                    if (value >= 10){
                        current = Integer.parseInt(String.valueOf(String.valueOf(value).charAt(1)));
                        int carried = Integer.parseInt(String.valueOf(String.valueOf(value).charAt(0)));
                        carry = carried;
                    }
                    
                    else{
                        current = Integer.parseInt(String.valueOf(String.valueOf(value).charAt(0)));
                        carry = 0;
                    } 

                    finalvalue += String.valueOf(current);

                    if (pointer == 0 && carry != 0){
                        finalvalue += String.valueOf(carry);
                    }
                    
                    pointer--;

                }


                int result[] = new int [finalvalue.length()];
                for (int i=finalvalue.length()-1, j=0; i>=0; i--,j++){
                    result[j] = Integer.parseInt(String.valueOf(finalvalue.charAt(i)));
                }

                return result;
            }
        }
        return digits;


    }
}