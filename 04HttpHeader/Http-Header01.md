
# Request
- Request Line
- Header
- Body
  
# Response
- Status Line
- Header
- Body
  

# RequestLine & Header
- GET /index.html HTTP/1.1
- Host: www.example.com
- User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64)
- Accept: text/html, application/xhtml+xml
- Authorization: Bearer abc123
- Cookie: session_id=xyz789

# StatusLine & Header
- HTTP/1.1 200 OK
- Content-Type: text/html; charset=UTF-8
- Content-Length: 1024
- Set-Cookie: session_id=xyz789; Path=/; HttpOnly
- Cache-Control: no-cache, no-store, must-revalidate
- Server: Apache/2.4.41 (Ubuntu)





# 표준(기본) HTTP 요청 헤더
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Content-Type: application/json
Authorization: Bearer abc123

# 사용자 정의 헤더
GET /data HTTP/1.1
Host: api.example.com
User-Agent: MyCustomClient/1.0
X-Request-ID: 123456789
X-Custom-Header: SomeValue
