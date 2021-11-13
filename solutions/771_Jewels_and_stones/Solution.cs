  public class Solution
  {
     
        public int NumJewelsInStones(string J, string S)
        {
            var count = 0;

            var set = new HashSet<char>();
            //Stopwatch sw = new Stopwatch();

            var jwls = J.ToCharArray();
            var refStrArr = S.ToCharArray();


            //  count = refStrArr.Count(r => jwls.Any(x => x.Equals(r)));

            for (int i = 0; i < jwls.Length; i++)
            {
                set.Add(jwls[i]);
            }

            //sw.Start();
            for (int i = 0; i < refStrArr.Length; i++)
            {
                if (set.Contains(refStrArr[i])) count++;
            }
            //sw.Stop();
            //Console.WriteLine(sw.ElapsedMilliseconds);
            return count;
        }
    }