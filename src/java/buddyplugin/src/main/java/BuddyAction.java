import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.actionSystem.CommonDataKeys;
import com.intellij.openapi.actionSystem.PlatformDataKeys;
import com.intellij.openapi.command.WriteCommandAction;
import com.intellij.openapi.editor.Caret;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.Editor;
import com.intellij.openapi.project.Project;
import java.io.IOException;

public class BuddyAction extends AnAction {
    @Override
    public void actionPerformed(AnActionEvent event) {
        Editor editor = event.getData(PlatformDataKeys.EDITOR);
        String selectedCode = editor.getSelectionModel().getSelectedText();
        HttpResponse<String> result = null;
        try {
            result = sendPostWithJsonBody("http://127.0.0.1:8000/predictor/predict", selectedCode);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Project project = event.getRequiredData(CommonDataKeys.PROJECT);
        Document document = editor.getDocument();
        Caret primaryCaret = editor.getCaretModel().getPrimaryCaret();
        int start = primaryCaret.getSelectionStart();
        int end = primaryCaret.getSelectionEnd();

        ObjectMapper mapper = new ObjectMapper();
        JsonNode nameNode = null;
        try {
            nameNode = mapper.readTree(result.body());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        JsonNode finalNameNode = nameNode;
        WriteCommandAction.runWriteCommandAction(project, () ->
                document.replaceString(start, end, finalNameNode.get("result").asText())
        );
        primaryCaret.removeSelection();
    }

    @Override
    public boolean isDumbAware() {
        return false;
    }


    public static HttpResponse<String> sendPostWithJsonBody(String serviceUrl, String selectedCode) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(serviceUrl))
                .POST(HttpRequest.BodyPublishers.ofString(String.format("{\"code\":\"%s\"}", selectedCode)))
                .build();
        return client.send(request, HttpResponse.BodyHandlers.ofString());
    }
}
