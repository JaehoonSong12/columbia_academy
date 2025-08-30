public class StringOperations {
    public static void main(String[] args) {
        String myName = "Tai";
        System.out.println(myName);

        String modifiedName = "A" 
            + myName.substring(1, myName.length() - 1) 
            + "Z";
        System.out.println(modifiedName);

        String website = "www.gatech.edu";
        System.out.println(website);

        int startIndex = 4;
        int endIndex = website.length() - 4;
        String siteName = website.substring(startIndex, endIndex);
        String siteNameWithNumber = siteName + "1331";
        System.out.println(siteNameWithNumber);
    }
}
