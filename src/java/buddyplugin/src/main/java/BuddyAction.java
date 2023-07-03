
import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.ui.Messages;

public class BuddyAction extends AnAction {
    @Override
    public void actionPerformed(AnActionEvent event) {
        Messages.showMessageDialog("Test Action", "BuddyAction", Messages.getInformationIcon());
    }

    @Override
    public boolean isDumbAware() {
        return false;
    }
}
