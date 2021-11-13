public class Solution {
    public int RepeatedNTimes(int[] A) {
           var len = A.Length;
            var sortedArr = new int[len];
            for (int i = 0; i < len; i++)
            {
                sortedArr[i] = i;
            }
            Array.Sort(A, sortedArr);

            var mid = len / 2;

            var center = A[mid];
            var centerB = A[mid - 1];
            var centerB2 = A[mid - 2];

            if (center.Equals(centerB)) return centerB;

            return centerB.Equals(centerB2) ? centerB2 : center;
    }
}