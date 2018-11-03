package uk.ac.standrews.cs.mamoc_test;
public class MainActivity extends android.support.v7.app.AppCompatActivity {
    private android.widget.Button discoveryBtn;
    private android.widget.Button mandelbrotDemo;
    private android.widget.Button nqueensDemo;
    private android.widget.Button searchTextDemo;
    private android.widget.Button sortingDemo;

    public MainActivity()
    {
        return;
    }

    public static synthetic void lambda$onCreate$0(uk.ac.standrews.cs.mamoc_test.MainActivity p0, android.view.View p1)
    {
        p0.openSearchTextDemo();
        return;
    }

    public static synthetic void lambda$onCreate$1(uk.ac.standrews.cs.mamoc_test.MainActivity p0, android.view.View p1)
    {
        p0.openSortingDemo();
        return;
    }

    public static synthetic void lambda$onCreate$2(uk.ac.standrews.cs.mamoc_test.MainActivity p0, android.view.View p1)
    {
        p0.openNQueensDemo();
        return;
    }

    public static synthetic void lambda$onCreate$3(uk.ac.standrews.cs.mamoc_test.MainActivity p0, android.view.View p1)
    {
        p0.openMandelbrotDemo();
        return;
    }

    private void openMandelbrotDemo()
    {
        this.startActivity(new android.content.Intent(this, uk.ac.standrews.cs.mamoc_test.Mandelbrot.MandelbrotActivity));
        return;
    }

    private void openNQueensDemo()
    {
        this.startActivity(new android.content.Intent(this, uk.ac.standrews.cs.mamoc_test.NQueens.NQueensActivity));
        return;
    }

    private void openSearchTextDemo()
    {
        this.startActivity(new android.content.Intent(this, uk.ac.standrews.cs.mamoc_test.SearchText.SearchActivity));
        return;
    }

    private void openSortingDemo()
    {
        this.startActivity(new android.content.Intent(this, uk.ac.standrews.cs.mamoc_test.Sorting.SortingActivity));
        return;
    }

    protected void onCreate(android.os.Bundle p3)
    {
        super.onCreate(p3);
        this.setContentView(2131296284);
        this.discoveryBtn = ((android.widget.Button) this.findViewById(2131165220));
        this.searchTextDemo = ((android.widget.Button) this.findViewById(2131165225));
        this.searchTextDemo.setOnClickListener(new uk.ac.standrews.cs.mamoc_test.-$$Lambda$MainActivity$njkoMAzVNXScLefBbXt-QzQybKA(this));
        this.sortingDemo = ((android.widget.Button) this.findViewById(2131165319));
        this.sortingDemo.setOnClickListener(new uk.ac.standrews.cs.mamoc_test.-$$Lambda$MainActivity$zE7t7PJJxjxLHiIMpKJmDS5SXog(this));
        this.nqueensDemo = ((android.widget.Button) this.findViewById(2131165280));
        this.nqueensDemo.setOnClickListener(new uk.ac.standrews.cs.mamoc_test.-$$Lambda$MainActivity$71MGRJ_Rgtx19oT3maOlnp-XTqM(this));
        this.mandelbrotDemo = ((android.widget.Button) this.findViewById(2131165275));
        this.mandelbrotDemo.setOnClickListener(new uk.ac.standrews.cs.mamoc_test.-$$Lambda$MainActivity$lOAzxPu2FrGozfugiCnH8x2tWWo(this));
        return;
    }
}
