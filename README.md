# notion-tools
노션문서 일괄처리를 위한 유틸리티 레포

#### 사전 준비

1. [Notion Integration](https://www.notion.so/profile/integrations) 생성 → `ntn_` 으로 시작하는 토큰 발급
2. 대상 데이터베이스 id 찾기
3. 대상 데이터베이스에서 **⋯ → 연결 추가** 로 Integration 연결

   
#### Database ID 찾기

브라우저에서 Notion 데이터베이스를 열면 URL이 다음과 같은 형태입니다:

```
https://www.notion.so/{workspace}/{database_id}?v={view_id}
```

예시:

```
https://www.notion.so/junseokahn/6fdd8bfbc3df4f53a0fc197469d5111b?v=2e6ec8c2a6e743aebb358fa94a241835
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                 이 32자리 hex 문자열이 Database ID
