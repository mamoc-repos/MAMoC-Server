package uk.ac.standrews.cs.mamoc_test.Mandelbrot;
final class Mandelbrot$1 extends java.lang.Thread {

    Mandelbrot$1()
    {
        return;
    }

    public void run()
    {
        while(true) {
            byte[] v0_3 = uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.access$000().getAndIncrement();
            int v1 = v0_3;
            if (v0_3 >= uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.access$100().length) {
                break;
            }
            uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.access$200(v1, uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.access$100()[v1]);
        }
        return;
    }
}
