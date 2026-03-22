# Notion 데이터베이스 페이지의 "생성 일시"(created_time) 메타데이터를 "날짜"속성(date)에 일괄 복사합니다.
import requests
import time

NOTION_TOKEN = "your-secret"
DATABASE_ID = "your-database-id"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

# 1. 모든 페이지 조회
pages = []
payload = {"page_size": 100}
while True:
    res = requests.post(
        f"https://api.notion.com/v1/databases/{DATABASE_ID}/query",
        headers=HEADERS, json=payload
    ).json()
    pages.extend(res["results"])
    if not res.get("has_more"):
        break
    payload["start_cursor"] = res["next_cursor"]
    time.sleep(0.4)

print(f"총 {len(pages)}개 페이지")

# 2. 일괄 업데이트 (딜레이 + 재시도)
for i, page in enumerate(pages):
    created = page["created_time"][:10]
    for attempt in range(3):
        try:
            resp = requests.patch(
                f"https://api.notion.com/v1/pages/{page['id']}",
                headers=HEADERS,
                json={"properties": {"날짜": {"date": {"start": created}}}}
            )
            if resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", 1))
                print(f"  Rate limited, waiting {retry_after}s...")
                time.sleep(retry_after)
                continue
            resp.raise_for_status()
            print(f"[{i+1}/{len(pages)}] Updated: {page['id']} → {created}")
            break
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
            time.sleep(2)
    time.sleep(0.4)  # 초당 3 요청 미만 유지