package uk.ac.standrews.cs.mamoc_test;
public abstract class DemoBaseActivity extends android.support.v7.app.AppCompatActivity {
    private android.app.ProgressDialog mProgressDialog;

    public DemoBaseActivity()
    {
        return;
    }

    protected abstract int getContentView();

    public void hideDialog()
    {
        if ((this.mProgressDialog != null) && (this.mProgressDialog.isShowing())) {
            this.mProgressDialog.dismiss();
        }
        return;
    }

    public void noInternetConnectionAvailable()
    {
        this.showToast("No Internet");
        return;
    }

    protected void onCreate(android.os.Bundle p2)
    {
        super.onCreate(p2);
        this.setContentView(this.getContentView());
        this.onViewReady(p2, this.getIntent());
        return;
    }

    protected void onDestroy()
    {
        super.onDestroy();
        return;
    }

    public boolean onSupportNavigateUp()
    {
        this.onBackPressed();
        return 1;
    }

    protected void onViewReady(android.os.Bundle p1, android.content.Intent p2)
    {
        return;
    }

    protected void showAlertDialog(String p4)
    {
        android.support.v7.app.AlertDialog$Builder v0_1 = new android.support.v7.app.AlertDialog$Builder(this);
        v0_1.setTitle(0);
        v0_1.setIcon(2131361792);
        v0_1.setMessage(p4);
        v0_1.setPositiveButton("OK", new uk.ac.standrews.cs.mamoc_test.DemoBaseActivity$1(this));
        v0_1.setCancelable(0);
        v0_1.show();
        return;
    }

    protected void showBackArrow(String p3)
    {
        android.support.v7.app.ActionBar v0 = this.getSupportActionBar();
        if (v0 != null) {
            v0.setDisplayHomeAsUpEnabled(1);
            v0.setDisplayShowHomeEnabled(1);
            v0.setTitle(p3);
        }
        return;
    }

    public void showProgressDialog()
    {
        if (this.mProgressDialog == null) {
            this.mProgressDialog = new android.app.ProgressDialog(this);
            this.mProgressDialog.setMessage("Loading");
            this.mProgressDialog.setCancelable(0);
        }
        if (!this.mProgressDialog.isShowing()) {
            this.mProgressDialog.show();
        }
        return;
    }

    protected void showToast(String p2)
    {
        android.widget.Toast.makeText(this, p2, 1).show();
        return;
    }
}
