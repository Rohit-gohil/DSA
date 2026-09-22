using System;

namespace HelloWorld
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int[,,,] a = new int[3, 3, 3, 3];

            int value = 1;

            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    for (int k = 0; k < 3; k++)
                    {
                        for (int l = 0; l < 3; l++)
                        {
                            a[i, j, k, l] = value++;
                            Console.WriteLine(a[i, j, k, l]);
                        }
                    }
                }
            }
        }
    }
}
