class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            if (Character.isLetter(s.charAt(i)))
                sb.append(Character.toLowerCase(s.charAt(i)));
            if (Character.isDigit(s.charAt(i)))
                sb.append(s.charAt(i));
        }
        // goated
        return sb.toString().equals(sb.reverse().toString());
    }
}
