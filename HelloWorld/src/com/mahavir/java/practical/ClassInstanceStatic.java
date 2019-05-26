package com.mahavir.java.practical;

public class ClassInstanceStatic {

    int x;
    static int y;
    private static int z;

    public void fun1() {
    }

    public static void fun2() {
        y = 4;
    }

    static class Test {

        public static String country = "India";
    }
}
    class CallInstanceStaticMember
    {
        public static void main(String args[])
        {
            //Creating Object for 1st Instance
            ClassInstanceStatic ex1 = new ClassInstanceStatic();
            //Creating object for 2nd instance
            ClassInstanceStatic ex2 = new ClassInstanceStatic();

            System.out.println(ClassInstanceStatic.y);

            ClassInstanceStatic.fun2();

            System.out.println(ClassInstanceStatic.Test.country);


        }
    }

