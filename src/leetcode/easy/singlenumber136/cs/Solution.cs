using System.Collections;

public class Solution {
    public int SingleNumber(int[] nums) {
        Hashtable ht = new Hashtable();

        foreach (int i in nums) {
            if (ht.ContainsKey(i))
                ht.Remove(i);
            else
                ht.Add(i, 1);
        }
        foreach(DictionaryEntry e in ht)
            return (int)e.Key;
        return -99;
    }
}