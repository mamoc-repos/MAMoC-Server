package uk.ac.standrews.cs.mamoc_test.NQueens;
public class NQueensActivity extends uk.ac.standrews.cs.mamoc_test.DemoBaseActivity {
    private int N;
    private final String RPC_NAME;
    private android.widget.Button cloudButton;
    private android.widget.Button edgeButton;
    private android.widget.Button localButton;
    private android.widget.Button mamocButton;
    private android.widget.TextView nOutput;
    private android.widget.TextView nqueensOutput;

    public NQueensActivity()
    {
        this.RPC_NAME = "uk.ac.standrews.cs.mamoc_test.nqueens";
        return;
    }

    protected int getContentView()
    {
        return 2131296286;
    }

    protected void onViewReady(android.os.Bundle p2, android.content.Intent p3)
    {
        super.onViewReady(p2, p3);
        this.localButton = ((android.widget.Button) this.findViewById(2131165222));
        this.edgeButton = ((android.widget.Button) this.findViewById(2131165221));
        this.cloudButton = ((android.widget.Button) this.findViewById(2131165219));
        this.mamocButton = ((android.widget.Button) this.findViewById(2131165223));
        this.nqueensOutput = ((android.widget.TextView) this.findViewById(2131165318));
        this.nOutput = ((android.widget.TextView) this.findViewById(2131165274));
        this.showBackArrow("NQueens Demo");
        return;
    }
}
