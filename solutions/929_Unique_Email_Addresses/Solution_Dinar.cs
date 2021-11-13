public class Solution
{

  public int NumUniqueEmails(string[] emails)
        {
            var set = new HashSet<string>();
            var emailsLen = emails.Length;

            for (int i = 0; i < emailsLen; i++)
            {
                var item = emails[i];
                var sp = item.Split("@");
                var fp = sp[0].Replace(".", "");
                var lp = sp[1];

                set.Add(fp.Split("+")[0] + lp);
            }

            return set.Count;

        }

}