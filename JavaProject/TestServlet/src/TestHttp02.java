import java.io.*;
import java.net.*;

public class TestHttp02 {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(8081)) {  

            System.out.println("서버가 시작되었습니다. 포트 8081에서 기다리는 중...");
            


            System.out.println("▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶");
            System.out.println("URL-Input");
            System.out.println("ㄴlocalhost:8081");
            System.out.println("ㄴ172.21.96.1:8081");


            
            while (true) {
                try (Socket clientSocket = serverSocket.accept()) {
                    // 클라이언트의 요청을 받기 위한 입력 스트림
                    BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                    // 클라이언트로 응답을 보내기 위한 출력 스트림
                    OutputStream out = clientSocket.getOutputStream();

                    String line;
                    while ((line = in.readLine()) != null && !line.isEmpty()) {
                        System.out.println(line); // 요청 헤더 출력
                    }

                    // HTTP 응답 작성
                    String response = "HTTP/1.1 200 OK\r\n"
                            + "Content-Type: text/html; charset=UTF-8\r\n"
                            + "\r\n"
                            + "<html><body><h1>안녕하세요, Java HTTP 서버!</h1></body></html>";


                    out.write(response.getBytes("UTF-8"));
                    out.flush();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
