/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		
		Scanner read = new Scanner(System.in);
		int T = read.nextInt();
		
	 while(T-->0)
	    {
	       int W=read.nextInt();
	       int X=read.nextInt();
	       int Y=read.nextInt();
	       int Z=read.nextInt();
	       
	       int B = W+(X-Y)*Z ;
	       
	       System.out.println(B);
	     
	    }
	}
}
