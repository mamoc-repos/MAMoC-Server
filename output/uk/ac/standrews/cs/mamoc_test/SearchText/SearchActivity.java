package uk.ac.standrews.cs.mamoc_test.SearchText;
public class SearchActivity extends uk.ac.standrews.cs.mamoc_test.DemoBaseActivity {
    private android.widget.Button cloudButton;
    private android.widget.Button edgeButton;
    private String fileSize;
    private String keyword;
    private android.widget.TextView keywordTextView;
    private android.widget.Button localButton;
    private android.widget.Button mamocButton;
    android.widget.RadioGroup radioGroup;
    private android.widget.TextView searchOutput;

    public SearchActivity()
    {
        return;
    }

    private void addLog(int p4, double p5)
    {
        if (p4 != 0) {
            android.widget.TextView v0_0 = this.searchOutput;
            String v1_6 = new StringBuilder();
            v1_6.append("Number of occurences: ");
            v1_6.append(p4);
            v1_6.append("\n");
            v0_0.append(v1_6.toString());
            android.widget.TextView v0_1 = this.searchOutput;
            String v1_2 = new StringBuilder();
            v1_2.append("Execution took: ");
            v1_2.append(p5);
            v1_2.append(" seconds.\n");
            v0_1.append(v1_2.toString());
        } else {
            this.searchOutput.append("no occurences found!\n");
        }
        return;
    }

    private String getContentFromTextFile(String p3)
    {
        try {
            String v0 = this.readFromAssets(this, p3);
        } catch (java.io.IOException v1_1) {
            v1_1.printStackTrace();
        }
        return v0;
    }

    public static synthetic void lambda$onCreate$0(uk.ac.standrews.cs.mamoc_test.SearchText.SearchActivity p1, android.widget.RadioGroup p2, int p3)
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

    private String readFromAssets(android.content.Context p5, String p6)
    {
        java.io.BufferedReader v0_1 = new java.io.BufferedReader(new java.io.InputStreamReader(p5.getAssets().open(p6)));
        StringBuilder v1_3 = new StringBuilder();
        String v2_0 = v0_1.readLine();
        while (v2_0 != null) {
            v1_3.append(v2_0);
            v2_0 = v0_1.readLine();
        }
        v0_1.close();
        return v1_3.toString();
    }

    protected int getContentView()
    {
        return 2131296287;
    }

    protected void onCreate(android.os.Bundle p3)
    {
        super.onCreate(p3);
        this.localButton = ((android.widget.Button) this.findViewById(2131165222));
        this.edgeButton = ((android.widget.Button) this.findViewById(2131165221));
        this.cloudButton = ((android.widget.Button) this.findViewById(2131165219));
        this.mamocButton = ((android.widget.Button) this.findViewById(2131165223));
        this.keywordTextView = ((android.widget.TextView) this.findViewById(2131165301));
        this.searchOutput = ((android.widget.TextView) this.findViewById(2131165318));
        this.radioGroup = ((android.widget.RadioGroup) this.findViewById(2131165248));
        this.radioGroup.setOnCheckedChangeListener(new uk.ac.standrews.cs.mamoc_test.SearchText.-$$Lambda$SearchActivity$xlnLtK9f7azTZr3kJJMnxVA7Hfs(this));
        this.showBackArrow("Searching Demo");
        return;
    }
}
