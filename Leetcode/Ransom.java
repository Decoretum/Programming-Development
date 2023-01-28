package Leetcode;
import java.util.*;

public class Ransom {

    static boolean canConstruct(String ransomNote, String magazine) {
        HashMap <String,Integer> letters = new HashMap<>();
        HashMap <String,Integer> magaletters = new HashMap<>();
        boolean condition = true;
        if (ransomNote.length() > magazine.length()){
            condition = false;
            return condition;
        }

        for (int i = 0; i < ransomNote.length(); i++){
            letters.put(String.valueOf(ransomNote.charAt(i)),0);
        }

        for (int i = 0; i < magazine.length(); i++){
            magaletters.put(String.valueOf(magazine.charAt(i)),0);
        }

        for (int i = 0; i < ransomNote.length(); i++){    
            String letter = String.valueOf(ransomNote.charAt(i));
            if (letters.containsKey(letter)){
                letters.put(letter, letters.get(letter) + 1);
            } 
        }


        for (int j = 0; j < magazine.length(); j++){
            String letter = String.valueOf(magazine.charAt(j));
            if (magaletters.containsKey(letter)){
                magaletters.put(letter, magaletters.get(letter) + 1);
            } 
        }

        for (String i : letters.keySet()){
            System.out.println(i + " " + letters.get(i));
            System.out.println(i + " " + magaletters.get(i));

            if (letters.get(i) == null || magaletters.get(i) == null){
                if (letters.get(i) != magaletters.get(i)){
                condition = false;
            }
            }

            else{
                if (letters.get(i) > magaletters.get(i)){
                condition = false;
                }
            }

        }

        return condition;
}
    public static void main (String args[]){
        System.out.println(canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"));
    }

}