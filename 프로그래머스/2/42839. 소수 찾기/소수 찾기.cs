using System;
using System.Collections.Generic;

public class Solution {
    static HashSet<int> answer = new HashSet<int>();

    // 중복 제거와 자리 수 조절을 위한 메서드
    static void GetPermutations(char[] arr, int depth, int length)
    {
        if (depth == length)
        {
            string numStr = new string(arr, 0, length);
            int num = int.Parse(numStr);
            CheckPrime(num);
            return;
        }

        for (int i = depth; i < arr.Length; i++)
        {
            Swap(ref arr[depth], ref arr[i]);
            GetPermutations(arr, depth + 1, length);
            Swap(ref arr[depth], ref arr[i]); // backtrack
        }
    }

    static void Swap(ref char a, ref char b)
    {
        char temp = a;
        a = b;
        b = temp;
    }

    static void CheckPrime(int number)
    {
        if (number < 2 || answer.Contains(number)) return;

        for (int i = 2; i * i <= number; i++)
        {
            if (number % i == 0)
                return;
        }

        answer.Add(number);
    }
    
    public int solution(string numbers) {
        answer.Clear();
        char[] digits = numbers.ToCharArray();
        int n = digits.Length;

        for (int i = 1; i <= n; i++)
        {
            GetPermutations(digits, 0, i);
        }

        return answer.Count;
    }
}