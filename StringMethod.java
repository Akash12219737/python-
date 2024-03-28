public class StringMethod {
    public static void main(String[] args) {
        String name = "Akash";
        int value = name.length();
        System.out.println(value);

        String lstring = name.toLowerCase();
        System.out.println(lstring);

        String ustring = name.toUpperCase();
        System.out.println(ustring);

        String s = "          k  Akash Maurya              jbhb";
        // String trstring = s.trim();
        System.out.println(s.trim());
        System.out.println(s);

        System.out.println(name.substring(2));
        System.out.println(name.substring(1,4));

        System.out.println(name.replace("k", "s"));
    }
}
