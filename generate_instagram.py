#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
인스타그램 캐러셀 카드 생성 — 한국 결제·보안 시스템 분석
Instagram용 1080x1350 (4:5) 카드 이미지
"""

import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARD_DIR = os.path.join(BASE_DIR, "instagram")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(CARD_DIR, exist_ok=True)

COMMON_STYLE = """
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    width: 1080px;
    height: 1350px;
    overflow: hidden;
  }
  body {
    font-family: -apple-system, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;
    color: #ffffff;
    display: flex;
    flex-direction: column;
  }
  .card {
    width: 1080px;
    height: 1350px;
    padding: 80px 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    background: #1a1b2e;
  }
  .footer {
    position: absolute;
    bottom: 40px;
    left: 70px;
    font-size: 18px;
    color: #666;
    font-weight: 400;
  }
  h1 { font-size: 56px; font-weight: 800; line-height: 1.35; margin-bottom: 28px; color: #fff; }
  h2 { font-size: 44px; font-weight: 800; line-height: 1.35; margin-bottom: 24px; color: #fff; }
  h3 { font-size: 32px; font-weight: 700; line-height: 1.4; margin-bottom: 16px; color: #fff; }
  p { font-size: 26px; line-height: 1.65; margin-bottom: 14px; color: #ccc; }
  .blue { color: #5bb5f0; }
  .red { color: #f87171; }
  .green { color: #4ade80; }
  .bold { font-weight: 700; color: #fff; }
  .muted { color: #666; font-size: 20px; }
  .small { font-size: 22px; }
  .subtitle { font-size: 28px; color: #aaa; line-height: 1.5; margin-bottom: 20px; }
  .swipe {
    position: absolute;
    bottom: 80px;
    left: 70px;
    font-size: 24px;
    color: #5bb5f0;
    font-weight: 600;
  }
  .divider {
    width: 60px;
    height: 4px;
    background: #f87171;
    margin: 24px 0;
    border-radius: 2px;
  }
  .gen-row {
    margin-bottom: 28px;
  }
  .gen-label {
    font-size: 22px;
    color: #5bb5f0;
    font-weight: 700;
    margin-bottom: 8px;
  }
  .gen-item {
    font-size: 24px;
    color: #ccc;
    line-height: 1.6;
    padding-left: 16px;
  }
  .gen-item .here {
    color: #f87171;
    font-weight: 700;
  }
  .gen-item .check {
    color: #4ade80;
  }
  .bullet {
    font-size: 26px;
    color: #ccc;
    line-height: 1.7;
    margin-bottom: 8px;
    padding-left: 8px;
  }
  .bullet strong { color: #fff; }
  .compare-row {
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    font-size: 23px;
  }
  .compare-row .left { color: #ccc; flex: 1; }
  .compare-row .arrow-col { color: #5bb5f0; width: 50px; text-align: center; }
  .compare-row .kr { color: #f87171; flex: 1; text-align: center; }
  .compare-row .us { color: #4ade80; flex: 1; text-align: center; }
  .compare-header {
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 2px solid rgba(255,255,255,0.15);
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 4px;
  }
  .compare-header .left { flex: 1; color: #888; }
  .compare-header .arrow-col { width: 50px; }
  .compare-header .kr { flex: 1; text-align: center; color: #f87171; }
  .compare-header .us { flex: 1; text-align: center; color: #4ade80; }
  .quote-box {
    background: rgba(255,255,255,0.06);
    border-left: 4px solid #f87171;
    padding: 28px 32px;
    border-radius: 0 12px 12px 0;
    margin: 20px 0;
    font-size: 26px;
    line-height: 1.6;
    color: #ddd;
  }
  .quote-box strong { color: #f87171; }
  .highlight-box {
    background: rgba(248,113,113,0.1);
    border: 2px solid rgba(248,113,113,0.3);
    border-radius: 16px;
    padding: 28px 32px;
    margin: 20px 0;
    font-size: 26px;
    line-height: 1.6;
    color: #fff;
  }
  .center-text {
    text-align: center;
  }
  .big-statement {
    font-size: 36px;
    font-weight: 800;
    color: #fff;
    line-height: 1.5;
    margin: 20px 0;
  }
  .hashtags {
    font-size: 17px;
    color: #555;
    line-height: 1.6;
    margin-top: 16px;
  }
</style>
"""

TOTAL = 10

cards = []

# ─── Card 1: Cover ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h1 style="font-size: 64px; line-height: 1.3;">
    한국 주차장은 <span class="green">3세대</span><br>
    한국 은행은 <span class="red">1세대</span>
  </h1>
  <div class="divider"></div>
  <p class="subtitle" style="font-size: 30px; color: #999;">
    왜 한국에서만 은행에 접속하려면<br>프로그램을 5개씩 깔아야 할까?
  </p>
  <div class="swipe">넘겨보세요 →</div>
  <div class="footer">옥소폴리틱스 | 유호현</div>
</div>
""")

# ─── Card 2: 주차장 비유 표 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2>같은 나라, 다른 세대</h2>
  <div style="height: 20px;"></div>

  <div class="gen-row">
    <div class="gen-label">1세대 (1990년대)</div>
    <div class="gen-item">주차장: 물리 주차권</div>
    <div class="gen-item">은행: USB 인증서 <span class="here">← 아직 여기</span></div>
  </div>

  <div class="gen-row">
    <div class="gen-label">2세대 (2010년대)</div>
    <div class="gen-item">주차장: 앱 주차권</div>
    <div class="gen-item">은행: 카카오/PASS 인증서</div>
  </div>

  <div class="gen-row">
    <div class="gen-label">3세대 (2020년대)</div>
    <div class="gen-item">주차장: 번호판 자동 인식 <span class="check">✓</span></div>
    <div class="gen-item">은행: ???</div>
    <div class="gen-item">세계: 지문/얼굴 인식 <span class="check">✓</span></div>
  </div>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 3: 개인키 문제 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2>은행이 국민에게<br>주차권을 나눠줬다</h2>
  <div class="divider"></div>

  <p style="font-size: 26px; color: #ccc; line-height: 1.7;">
    1999년, 한국 정부는 국민 전체에게<br>
    <span class="bold">개인키(=주차권)</span>를 나눠줬다.
  </p>
  <p style="font-size: 26px; color: #999; line-height: 1.7;">
    SSH에 쓰는 것과 같은 기술을<br>
    할머니, 할아버지, 초등학생에게 관리하라고 한 것.
  </p>

  <div style="height: 16px;"></div>
  <p style="font-size: 24px; color: #5bb5f0; font-weight: 700; margin-bottom: 12px;">결과:</p>
  <div class="bullet">• 잃어버린다 → 재발급</div>
  <div class="bullet">• 복사된다 → 해킹</div>
  <div class="bullet">• 보관이 어렵다 → USB 구매</div>
  <div class="bullet">• 관리 프로그램 필요 → ActiveX 설치</div>

  <div style="height: 20px;"></div>
  <p class="big-statement" style="font-size: 30px; color: #4ade80;">
    주차권을 없애면 이 모든 게 필요 없다.
  </p>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 4: 주차권 난립 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2>주차권을 자꾸 잃어버리니까?</h2>
  <h3 style="color: #f87171;">더 많은 주차권을 만들었다</h3>
  <div class="divider"></div>

  <div style="height: 12px;"></div>
  <div class="bullet" style="font-size: 30px;">• 카카오 주차권</div>
  <div class="bullet" style="font-size: 30px;">• 네이버 주차권</div>
  <div class="bullet" style="font-size: 30px;">• PASS 주차권</div>
  <div class="bullet" style="font-size: 30px;">• 토스 주차권</div>
  <div class="bullet" style="font-size: 30px;">• KB 주차권</div>
  <div class="bullet" style="font-size: 30px;">• 국민 주차권</div>
  <div class="bullet" style="font-size: 30px;">• 공동 주차권</div>

  <div style="height: 24px;"></div>
  <p class="big-statement" style="font-size: 30px;">
    <span class="red">1개에서 7개로 늘었을 뿐.</span><br>
    <span class="green">글로벌은 주차권 자체를 없앴다.</span>
  </p>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 5: 휴대폰 없으면 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2>한국에서 휴대폰 없으면<br><span class="red">아무것도 못 한다</span></h2>
  <div class="divider"></div>

  <div style="height: 12px;"></div>
  <div class="compare-header">
    <span class="left"></span>
    <span class="arrow-col"></span>
    <span class="kr">한국</span>
    <span class="us">미국</span>
  </div>
  <div class="compare-row">
    <span class="left">쇼핑몰 가입</span>
    <span class="arrow-col"></span>
    <span class="kr">휴대폰 인증</span>
    <span class="us">이메일</span>
  </div>
  <div class="compare-row">
    <span class="left">게임 계정</span>
    <span class="arrow-col"></span>
    <span class="kr">휴대폰 인증</span>
    <span class="us">이메일</span>
  </div>
  <div class="compare-row">
    <span class="left">비번 찾기</span>
    <span class="arrow-col"></span>
    <span class="kr">휴대폰 인증</span>
    <span class="us">이메일 링크</span>
  </div>
  <div class="compare-row">
    <span class="left">커뮤니티</span>
    <span class="arrow-col"></span>
    <span class="kr">휴대폰 인증</span>
    <span class="us">익명 가능</span>
  </div>
  <div class="compare-row" style="border-bottom: none;">
    <span class="left" style="font-weight:700;">휴대폰 없으면</span>
    <span class="arrow-col"></span>
    <span class="kr" style="font-weight:700; font-size: 26px;">불가</span>
    <span class="us" style="font-weight:700;">이메일로 대체</span>
  </div>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 6: 보안프로그램의 진실 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2>보안프로그램의<br><span class="red">진짜 역할</span></h2>
  <div class="divider"></div>

  <p style="font-size: 30px; color: #fff; line-height: 1.6; margin-bottom: 24px;">
    보이스피싱을 막을 수 있나? <span class="red" style="font-weight:800;">못 막는다.</span>
  </p>

  <p style="font-size: 26px; color: #ccc; line-height: 1.7;">
    피해자가 속아서 직접 돈을 보낸다.<br>
    키보드 보안이 그걸 어떻게 막나.
  </p>

  <div style="height: 24px;"></div>
  <p style="font-size: 28px; color: #5bb5f0; font-weight: 700;">그럼 왜 깔라고 하나?</p>
  <div style="height: 12px;"></div>

  <div class="quote-box">
    은행의 <strong>면책 도구</strong>.<br><br>
    "우리는 프로그램 깔라고 했잖아요"<br>
    → 사고가 나면 <strong>사용자 책임</strong>
  </div>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 7: 해킹 사례 ───
cards.append("""
<div class="card" style="justify-content: center; border: 3px solid rgba(248,113,113,0.4);">
  <h2><span class="red">보안프로그램이<br>해킹 통로가 됐다</span></h2>
  <div class="divider" style="background: #f87171;"></div>

  <div style="height: 12px;"></div>
  <div class="bullet" style="font-size: 26px; line-height: 1.8; margin-bottom: 20px;">
    <span class="blue">2020년</span> — 북한이 Veraport로 악성코드 배포
  </div>
  <div class="bullet" style="font-size: 26px; line-height: 1.8; margin-bottom: 20px;">
    <span class="blue">2023년</span> — TouchEn으로 전 국민 키보드 엿볼 수 있었다
  </div>
  <div class="bullet" style="font-size: 26px; line-height: 1.8; margin-bottom: 20px;">
    <span class="blue">2023년</span> — 영국+한국 정보기관 공동 경보
  </div>

  <div class="highlight-box">
    <span class="bold" style="font-size: 28px;">
      보안을 위해 설치한 프로그램이<br>
      <span class="red">악성코드 배달부</span>가 됐다.
    </span>
  </div>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 8: AI 시대 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2>AI 시대에<br><span class="red">주차권을 나눠주는 나라</span></h2>
  <div class="divider"></div>

  <div style="height: 8px;"></div>
  <p style="font-size: 27px; color: #ccc; line-height: 1.8;">
    "AI야, 잔고 확인해줘"<br>
    → 보안프로그램 설치 팝업 → <span class="red" style="font-weight:700;">AI 접근 불가</span>
  </p>
  <div style="height: 16px;"></div>
  <p style="font-size: 27px; color: #ccc; line-height: 1.8;">
    "AI야, 결제해줘"<br>
    → 휴대폰 인증 필요 → <span class="red" style="font-weight:700;">사람만 가능</span>
  </p>

  <div style="height: 24px;"></div>
  <p style="font-size: 30px; color: #5bb5f0; font-weight: 700;">
    로봇에 보안프로그램을 설치할 건가?
  </p>

  <div style="height: 24px;"></div>
  <div class="quote-box" style="border-left-color: #4ade80;">
    <span class="green" style="font-weight: 700; font-size: 28px;">
      서버에서 처리하면<br>
      클라이언트가 뭐든 상관없다.
    </span>
  </div>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 9: 핵심 결론 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2 class="center-text">문제의 핵심은 하나다</h2>
  <div style="height: 24px;"></div>

  <div class="center-text">
    <p style="font-size: 32px; color: #ccc; line-height: 1.6;">보안의 책임을</p>
    <p class="big-statement" style="font-size: 44px; color: #f87171;">사용자에게 떠넘기는 구조</p>
  </div>

  <div style="height: 28px;"></div>
  <div style="background: rgba(255,255,255,0.05); border-radius: 16px; padding: 28px 32px;">
    <p style="font-size: 25px; color: #ccc; line-height: 1.7; margin-bottom: 16px;">
      <span class="red">한국:</span> 사용자가 증명하고, 설치하고, 관리한다.
    </p>
    <p style="font-size: 25px; color: #ccc; line-height: 1.7; margin-bottom: 0;">
      <span class="green">세계:</span> 서버가 판단하고, 처리하고, 책임진다.
    </p>
  </div>

  <div style="height: 28px;"></div>
  <p class="big-statement center-text" style="font-size: 28px; color: #4ade80; line-height: 1.6;">
    한국 주차장이 번호판 인식으로<br>
    전환하는 데 10년이 걸리지 않았다.<br>
    기술은 이미 있다. 결정만 하면 된다.
  </p>

  <div class="footer">유호현 · 옥소폴리틱스</div>
</div>
""")

# ─── Card 10: 마무리 ───
cards.append("""
<div class="card" style="justify-content: center;">
  <h2>새로 발명할 것이 없다</h2>
  <div class="divider"></div>

  <p style="font-size: 28px; color: #5bb5f0; font-weight: 700; line-height: 1.6; margin-bottom: 24px;">
    TLS, FDS, FIDO2, 3D Secure<br>
    <span style="color: #ccc; font-weight: 400;">— 전부 이미 검증된 글로벌 표준이다.</span>
  </p>

  <p style="font-size: 28px; color: #ccc; line-height: 1.7; margin-bottom: 28px;">
    한국 주차장은 진작에 바꿨다.<br>
    한국 은행만 아직도 주차권을 나눠주고 있다.
  </p>

  <div style="height: 20px;"></div>
  <div style="background: rgba(255,255,255,0.05); border-radius: 16px; padding: 28px 32px; text-align: center;">
    <p style="font-size: 22px; color: #999; margin-bottom: 8px;">자세한 내용</p>
    <p style="font-size: 30px; color: #5bb5f0; font-weight: 700; margin-bottom: 0;">oxopolitics.com</p>
  </div>

  <div style="height: 24px;"></div>
  <p style="font-size: 22px; color: #888; text-align: center; font-weight: 600;">옥소폴리틱스 | 유호현</p>

  <div class="hashtags" style="text-align: center; margin-top: 20px;">
    #결제보안 #인터넷뱅킹 #공인인증서 #FIDO2 #패스키<br>
    #금융규제 #규제개혁 #AI시대 #옥소폴리틱스
  </div>

  <div class="footer">유호현 · 옥소폴리틱스</div>
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
        "--window-size=1080,1350",
        "--default-background-color=00000000",
        "--force-device-scale-factor=2",
        f"file://{html_path}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode == 0:
        print(f"✓ card_{i+1}.png")
    else:
        print(f"✗ card_{i+1}.png: {result.stderr[:200]}")

    # Clean up HTML
    os.remove(html_path)

print(f"\n완료: {CARD_DIR}/")
