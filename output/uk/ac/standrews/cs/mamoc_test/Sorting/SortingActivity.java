package uk.ac.standrews.cs.mamoc_test.Sorting;
public class SortingActivity extends uk.ac.standrews.cs.mamoc_test.DemoBaseActivity {
    private android.widget.Button cloudButton;
    private android.widget.Button edgeButton;
    private String fileSize;
    private String keyword;
    private android.widget.Button localButton;
    private android.widget.Button mamocButton;
    android.widget.RadioGroup radioGroup;
    private android.widget.TextView sortOutput;

    public SortingActivity()
    {
        return;
    }

    public static synthetic void lambda$onCreate$0(uk.ac.standrews.cs.mamoc_test.Sorting.SortingActivity p1, android.widget.RadioGroup p2, int p3)
    {
        if (p3 != 2131165317) {
            if (p3 != 2131165276) {
                p1.fileSize = "large";
            } else {
                p1.fileSize = "medium";
            }
        } else {
            p1.fileSize = "small";
        }
        return;
    }

    protected int getContentView()
    {
        return 2131296288;
    }

    protected void onCreate(android.os.Bundle p3)
    {
        super.onCreate(p3);
        this.localButton = ((android.widget.Button) this.findViewById(2131165222));
        this.edgeButton = ((android.widget.Button) this.findViewById(2131165221));
        this.cloudButton = ((android.widget.Button) this.findViewById(2131165219));
        this.mamocButton = ((android.widget.Button) this.findViewById(2131165223));
        this.sortOutput = ((android.widget.TextView) this.findViewById(2131165318));
        this.radioGroup = ((android.widget.RadioGroup) this.findViewById(2131165248));
        this.radioGroup.setOnCheckedChangeListener(new uk.ac.standrews.cs.mamoc_test.Sorting.-$$Lambda$SortingActivity$KepT6KTkq6xZllC-Tnq2-JKvN9U(this));
        this.showBackArrow("Sorting Demo");
        return;
    }
}
