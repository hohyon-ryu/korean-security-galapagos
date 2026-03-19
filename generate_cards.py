#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
카드뉴스 생성 — 한국 결제·보안 시스템 분석
Facebook용 1080x1080 카드 이미지
"""

import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARD_DIR = os.path.join(BASE_DIR, "cardnews")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(CARD_DIR, exist_ok=True)

COMMON_STYLE = """
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    width: 1080px;
    height: 1080px;
    overflow: hidden;
  }
  body {
    font-family: -apple-system, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;
    color: #1a1a1a;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .card {
    width: 1080px;
    height: 1080px;
    padding: 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
  }
  .card::after {
    content: '';
    position: absolute;
    bottom: 30px;
    left: 80px;
    right: 80px;
    height: 1px;
    background: rgba(0,0,0,0.08);
  }
  .badge {
    display: inline-block;
    font-size: 18px;
    font-weight: 700;
    padding: 8px 20px;
    border-radius: 6px;
    margin-bottom: 30px;
    letter-spacing: 1px;
    width: fit-content;
  }
  .page-num {
    position: absolute;
    bottom: 40px;
    right: 80px;
    font-size: 16px;
    color: #999;
    font-weight: 500;
  }
  .logo {
    position: absolute;
    bottom: 38px;
    left: 80px;
    font-size: 14px;
    color: #bbb;
    font-weight: 500;
  }
  h1 { font-size: 52px; font-weight: 800; line-height: 1.35; margin-bottom: 24px; }
  h2 { font-size: 40px; font-weight: 800; line-height: 1.35; margin-bottom: 20px; }
  h3 { font-size: 30px; font-weight: 700; line-height: 1.4; margin-bottom: 16px; }
  p { font-size: 24px; line-height: 1.65; margin-bottom: 12px; color: #444; }
  .big { font-size: 28px; line-height: 1.6; }
  .accent { color: #DC2626; }
  .accent-blue { color: #2563EB; }
  .accent-green { color: #16A34A; }
  .muted { color: #888; font-size: 20px; }
  .em { font-weight: 700; color: #111; }
  .stat-row {
    display: flex;
    gap: 30px;
    margin: 20px 0;
  }
  .stat-box {
    flex: 1;
    background: #F8FAFC;
    border-radius: 16px;
    padding: 28px 24px;
    text-align: center;
  }
  .stat-box .num {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 8px;
  }
  .stat-box .label {
    font-size: 18px;
    color: #666;
  }
  .vs-row {
    display: flex;
    gap: 20px;
    margin: 20px 0;
  }
  .vs-box {
    flex: 1;
    padding: 28px;
    border-radius: 16px;
  }
  .vs-box h3 { font-size: 22px; margin-bottom: 14px; }
  .vs-box p { font-size: 20px; margin-bottom: 8px; }
  .vs-bad { background: #FEF2F2; border: 2px solid #FECACA; }
  .vs-good { background: #F0FDF4; border: 2px solid #BBF7D0; }
  .item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 18px;
    font-size: 24px;
    line-height: 1.5;
  }
  .item .icon {
    font-size: 28px;
    min-width: 36px;
    text-align: center;
    margin-top: 2px;
  }
  .divider {
    width: 60px;
    height: 4px;
    background: #DC2626;
    margin: 20px 0;
    border-radius: 2px;
  }
  .quote-box {
    background: #1E293B;
    color: #E2E8F0;
    padding: 32px;
    border-radius: 16px;
    margin: 20px 0;
    font-size: 22px;
    line-height: 1.6;
  }
  .quote-box strong { color: #FCA5A5; }
  .diagram-box {
    background: #F8FAFC;
    border: 2px solid #E2E8F0;
    border-radius: 16px;
    padding: 32px;
    margin: 16px 0;
    font-size: 22px;
    line-height: 1.8;
    text-align: center;
  }
  .diagram-box .arrow { color: #DC2626; font-weight: 700; }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 20px;
  }
  th {
    background: #1E293B;
    color: #fff;
    padding: 14px 16px;
    text-align: left;
    font-weight: 600;
  }
  td {
    padding: 12px 16px;
    border-bottom: 1px solid #E5E7EB;
  }
  tr:nth-child(even) { background: #F9FAFB; }
</style>
"""

TOTAL = 8

def logo_and_page(n):
    return f'<span class="logo">옥소폴리틱스</span><span class="page-num">{n} / {TOTAL}</span>'


cards = []

# ─── Card 1: Cover ───
cards.append(f"""
<div class="card" style="background: linear-gradient(160deg, #0F172A 0%, #1E293B 100%); color: #fff;">
  <div class="badge" style="background: #DC2626; color: #fff;">POLICY BRIEF</div>
  <h1 style="color: #fff; font-size: 48px;">
    왜 한국에서만<br>
    은행 업무를 하려면<br>
    <span style="color: #FCA5A5;">이상한 프로그램</span>을<br>
    깔아야 할까?
  </h1>
  <div class="divider" style="background: #DC2626;"></div>
  <p style="color: #94A3B8; font-size: 22px;">보이스피싱을 막겠다고 만든 시스템이<br>왜 북한 해커에게 문을 열어줬는가</p>
  <span class="logo" style="color: #64748B;">옥소폴리틱스</span>
  <span class="page-num" style="color: #64748B;">1 / {TOTAL}</span>
</div>
""")

# ─── Card 2: 출발점 ───
cards.append(f"""
<div class="card" style="background: #fff;">
  <div class="badge" style="background: #FEF2F2; color: #DC2626;">출발점</div>
  <h2>보이스피싱 피해가<br>진짜 심각하긴 했다</h2>
  <div class="stat-row">
    <div class="stat-box">
      <div class="num accent">1조 965억</div>
      <div class="label">2023년 보이스피싱 피해액</div>
    </div>
    <div class="stat-box">
      <div class="num accent">하루 30억</div>
      <div class="label">매일 사기로 빠져나가는 돈</div>
    </div>
  </div>
  <div class="divider"></div>
  <p class="big">그래서 정부가 만든 대책:</p>
  <div class="item"><span class="icon">🔒</span><span>키보드 보안 프로그램 (TouchEn nxKey)</span></div>
  <div class="item"><span class="icon">🛡️</span><span>방화벽 프로그램 (AhnLab Safe Transaction)</span></div>
  <div class="item"><span class="icon">📋</span><span>공인인증서, 보안카드, OTP</span></div>
  <p class="muted" style="margin-top: 16px;">출발점은 이해할 수 있다. 문제는 다음 장에.</p>
  {logo_and_page(2)}
</div>
""")

# ─── Card 3: 못 막는다 ───
cards.append(f"""
<div class="card" style="background: #fff;">
  <div class="badge" style="background: #FEF2F2; color: #DC2626;">핵심 문제</div>
  <h2>그런데 이 프로그램들은<br><span class="accent">보이스피싱을 못 막는다</span></h2>
  <p class="big" style="margin-bottom:20px;">보이스피싱의 실제 수법:</p>
  <div class="diagram-box" style="text-align:left; font-size:21px;">
    사기범이 전화한다 ("검찰입니다")<br>
    <span class="arrow">↓</span> 피해자가 속는다<br>
    <span class="arrow">↓</span> 피해자가 <strong>직접</strong> 돈을 보낸다<br>
    <span class="arrow">↓</span> 끝.
  </div>
  <p class="big" style="margin-top: 20px;">
    피해자가 <span class="em">직접 이체 버튼을 누르는데</span>,<br>
    키보드 보안 프로그램이 무슨 소용?
  </p>
  <div class="divider"></div>
  <p class="muted">비유: 도둑이 "택배입니다" 하고 현관문을 두드리면,<br>집주인이 직접 문을 열어준다. 창문에 강화유리를 달아봤자 소용없다.</p>
  {logo_and_page(3)}
</div>
""")

# ─── Card 4: 프로그램 정체 ───
cards.append(f"""
<div class="card" style="background: #fff;">
  <div class="badge" style="background: #EFF6FF; color: #2563EB;">프로그램의 정체</div>
  <h2>은행이 깔라는 프로그램은<br><span class="accent">사실상 스파이웨어</span></h2>
  <table>
    <tr><th>프로그램</th><th>명목</th><th>실제로 하는 일</th></tr>
    <tr><td><strong>TouchEn nxKey</strong></td><td>키보드 보안</td><td>모든 키보드 입력을 가로챔<br><span class="muted">평점 1.3/5, 취약점 7개</span></td></tr>
    <tr><td><strong>IPinside</strong></td><td>IP 확인</td><td>HDD 시리얼, 프로그램 목록,<br>시스템 정보 전부 수집</td></tr>
    <tr><td><strong>AhnLab</strong></td><td>방화벽</td><td>PC의 모든 네트워크<br>트래픽을 감시</td></tr>
    <tr><td><strong>Veraport</strong></td><td>설치 관리</td><td>암호화 없이(HTTP)<br>프로그램 다운로드</td></tr>
  </table>
  <div class="quote-box">
    "이것은 <strong>의무 설치 스파이웨어</strong>다"<br>
    — Wladimir Palant, 보안 연구자
  </div>
  {logo_and_page(4)}
</div>
""")

# ─── Card 5: CCTV 비유 + 실제 해킹 ───
cards.append(f"""
<div class="card" style="background: #fff;">
  <div class="badge" style="background: #FEF2F2; color: #DC2626;">실제 피해</div>
  <h2><span class="accent">북한 해커</span>가<br>이 프로그램을 뚫고 들어왔다</h2>
  <div class="item"><span class="icon" style="font-size:24px;">🇰🇵</span><span><strong>2020년</strong> — 라자루스 그룹이 Veraport를 해킹해<br>악성코드를 <span class="em">보안 프로그램인 척</span> 배포</span></div>
  <div class="item"><span class="icon" style="font-size:24px;">🇰🇵</span><span><strong>2023년</strong> — MagicLine4NX 취약점으로 기업 내부 침투<br><span class="em">영국+한국 정보기관 공동 경보</span> 발령</span></div>
  <div class="item"><span class="icon" style="font-size:24px;">🇰🇵</span><span><strong>2023년</strong> — TouchEn nxKey로 <span class="em">전 국민 키보드</span>를<br>엿볼 수 있는 취약점 발견</span></div>
  <div class="divider"></div>
  <div class="diagram-box" style="font-size: 24px; background: #FFFBEB; border-color: #FDE68A;">
    비유: 은행이 보안을 위해 당신 집에 CCTV를 설치했다.<br>
    거실, 침실, 화장실 전부.<br>
    <strong>"아, 그리고 CCTV 시야 확보를 위해<br>대문도 열어놔야 합니다."</strong>
  </div>
  {logo_and_page(5)}
</div>
""")

# ─── Card 6: 규제가 만든 밥그릇 ───
cards.append(f"""
<div class="card" style="background: #fff;">
  <div class="badge" style="background: #FFFBEB; color: #92400E;">구조적 문제</div>
  <h2>왜 안 바뀌나?<br><span class="accent">규제가 만든 이권</span></h2>
  <div class="diagram-box" style="text-align: left; font-size: 20px; line-height: 2;">
    ① 금감원이 "보안 프로그램 설치하라" 규정<br>
    <span class="arrow">&nbsp;&nbsp;&nbsp;↓</span><br>
    ② 은행이 규정 따르려고 특정 업체 프로그램 구매<br>
    <span class="arrow">&nbsp;&nbsp;&nbsp;↓</span><br>
    ③ 업체는 규제가 보장하는 안정 수입<br>
    &nbsp;&nbsp;&nbsp;(라온시큐어 2024 매출 <strong>533억, 전년 대비 52.6%↑</strong>)<br>
    <span class="arrow">&nbsp;&nbsp;&nbsp;↓</span><br>
    ④ 보안 구멍 발견 → 긴급 패치 계약 → 매출 증가<br>
    <span class="arrow">&nbsp;&nbsp;&nbsp;↓</span><br>
    ⑤ 바꿀 인센티브가 아무에게도 없다 → ①로 반복
  </div>
  <div class="divider"></div>
  <p><span class="em">금감원</span>: 바꾸면 비난 위험 &nbsp;|&nbsp; <span class="em">은행</span>: 면책 확보됨</p>
  <p><span class="em">보안업체</span>: 매출 보장 &nbsp;|&nbsp; <span class="em">퇴직 공무원</span>: 업체 임원으로 이동</p>
  <p class="muted" style="margin-top:12px;">→ 규제 포획(Regulatory Capture): 규제가 시민이 아니라<br>피규제 업체의 이익을 위해 작동하는 현상</p>
  {logo_and_page(6)}
</div>
""")

# ─── Card 7: 다른 나라 비교 ───
cards.append(f"""
<div class="card" style="background: #fff;">
  <div class="badge" style="background: #F0FDF4; color: #16A34A;">글로벌 비교</div>
  <h2>다른 나라는<br><span class="accent-green">프로그램 0개</span>로 더 안전하다</h2>
  <div class="vs-row">
    <div class="vs-box vs-bad">
      <h3>🇰🇷 한국</h3>
      <p>보안 프로그램 <strong>5~9개</strong> 설치</p>
      <p>사고 나면 <strong>사용자 책임</strong></p>
      <p>PC가 위험하니 <strong>통제하겠다</strong></p>
      <p style="margin-top:8px; font-size:18px; color:#999;">결과: 공격 면적 증가, 북한에 뚫림</p>
    </div>
    <div class="vs-box vs-good">
      <h3>🇺🇸🇪🇺 미국·유럽</h3>
      <p>프로그램 설치 <strong>0개</strong></p>
      <p>사고 나면 <strong>은행 책임</strong></p>
      <p>PC는 통제 불가, <strong>서버에서 막겠다</strong></p>
      <p style="margin-top:8px; font-size:18px; color:#999;">토큰화, 3D Secure, FIDO2 지문인증</p>
    </div>
  </div>
  <div class="divider"></div>
  <table style="font-size: 19px;">
    <tr><th>하려는 일</th><th>한국</th><th>미국·유럽</th></tr>
    <tr><td>온라인 결제</td><td>프로그램 5개 + 인증서 + 가상키패드</td><td>카드번호 입력 → 끝</td></tr>
    <tr><td>은행 이체</td><td>프로그램 5개 + OTP + 보안카드</td><td>앱에서 지문 → 끝</td></tr>
  </table>
  {logo_and_page(7)}
</div>
""")

# ─── Card 8: 해결책 / CTA ───
cards.append(f"""
<div class="card" style="background: linear-gradient(160deg, #0F172A 0%, #1E293B 100%); color: #fff;">
  <div class="badge" style="background: #16A34A; color: #fff;">해결책</div>
  <h2 style="color: #fff;">해결책은 간단하다</h2>
  <p style="color: #94A3B8; font-size: 26px; margin-bottom: 30px;">다른 나라처럼 하면 된다.</p>
  <div class="item"><span class="icon">1</span><span style="color:#E2E8F0;"><strong style="color:#FCA5A5;">프로그램 강제 설치 폐지</strong><br>글로벌 표준 충족 시 면제</span></div>
  <div class="item"><span class="icon">2</span><span style="color:#E2E8F0;"><strong style="color:#FCA5A5;">금융사고 책임을 은행으로</strong><br>"프로그램 안 깔았으니 네 책임" 종료</span></div>
  <div class="item"><span class="icon">3</span><span style="color:#E2E8F0;"><strong style="color:#FCA5A5;">지문·얼굴 인증으로 전환</strong><br>인증서·보안카드에서 해방</span></div>
  <div class="item"><span class="icon">4</span><span style="color:#E2E8F0;"><strong style="color:#FCA5A5;">PC 감시 범위 제한</strong><br>내 HDD 시리얼까지 수집하는 건 스파이웨어</span></div>
  <div style="margin-top:30px; padding: 24px; border: 2px solid #334155; border-radius: 12px; text-align:center;">
    <p style="color: #94A3B8; font-size: 20px; margin:0;">핵심은 하나:</p>
    <p style="color: #fff; font-size: 28px; font-weight: 800; margin: 8px 0 0 0;">
      보안의 책임을<br>사용자 PC에서 은행 서버로 옮긴다.
    </p>
  </div>
  <span class="logo" style="color: #64748B;">옥소폴리틱스</span>
  <span class="page-num" style="color: #64748B;">{TOTAL} / {TOTAL}</span>
</div>
""")

# Generate each card
for i, card_html in enumerate(cards):
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8">{COMMON_STYLE}</head>
<body>{card_html}</body>
</html>"""

    html_path = os.path.join(CARD_DIR, f"card_{i+1}.html")
    png_path = os.path.join(CARD_DIR, f"card_{i+1}.png")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={png_path}",
        "--window-size=1080,1080",
        "--default-background-color=00000000",
        "--force-device-scale-factor=2",
        html_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode == 0:
        print(f"✓ card_{i+1}.png")
    else:
        print(f"✗ card_{i+1}.png: {result.stderr[:100]}")

    # Clean up HTML
    os.remove(html_path)

print(f"\n완료: {CARD_DIR}/")
