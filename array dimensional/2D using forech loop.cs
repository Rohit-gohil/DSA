using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{
			int [,]a={{1,2,3,4}
				,{1,2,2,3}};
            
             foreach(int i in a)
             {
             Console.WriteLine(i);
             }
		}
	}
}