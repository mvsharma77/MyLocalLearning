package com.mahavir.java.practical;

import java.lang.reflect.Member;

public class ClassMember {

    private int l, b, h;

    public void setVariables (int L, int B, int H)
    {
        l = L;
        b  = B;
        h = H;

    }

    public void showVariables ()
    {
        System.out.println("L=" +l);
        System.out.println("B=" +b);
        System.out.println("H=" +h);


    }
}


class example
{

    public static void main(String args[])
    {

        ClassMember member = new ClassMember();
        member.setVariables(1,9,1988);
        member.showVariables();

    }
}