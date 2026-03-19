#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
인증서 추가 슬라이드 → 프레젠테이션 스타일 PDF 생성
HTML + CSS → Chrome headless → PDF
"""

import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_HTML = os.path.join(BASE_DIR, "cert_slides.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "인증서_추가슬라이드.pdf")

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

html_content = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>인증서 추가 슬라이드</title>
<style>
  @page {
    size: 1280px 720px;
    margin: 0;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: -apple-system, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: #ffffff;
    background: #1a1b2e;
  }

  .slide {
    width: 1280px;
    height: 720px;
    padding: 50px 70px 60px 70px;
    position: relative;
    page-break-after: always;
    overflow: hidden;
  }
  .slide:last-child {
    page-break-after: auto;
  }

  /* Tag badge */
  .tag {
    display: inline-block;
    background: rgba(91,181,240,0.15);
    color: #5bb5f0;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 12px;
    border: 1px solid rgba(91,181,240,0.3);
    margin-bottom: 14px;
  }
  .tag.red {
    background: rgba(220,38,38,0.15);
    color: #f87171;
    border-color: rgba(220,38,38,0.3);
  }

  /* Title */
  .slide-title {
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 16px;
    line-height: 1.3;
  }

  .body-text {
    font-size: 17px;
    color: #cbd5e1;
    margin-bottom: 14px;
    line-height: 1.7;
  }

  /* Info box */
  .info-box {
    background: rgba(255,255,255,0.05);
    border-left: 3px solid #5bb5f0;
    padding: 14px 18px;
    border-radius: 0 6px 6px 0;
    font-family: 'SF Mono', 'Menlo', 'Consolas', monospace;
    font-size: 13px;
    line-height: 1.65;
    color: #e2e8f0;
    white-space: pre-wrap;
    margin-bottom: 14px;
  }

  /* Comparison boxes */
  .compare {
    display: flex;
    gap: 14px;
    margin-bottom: 14px;
  }
  .compare > div {
    flex: 1;
    padding: 14px 16px;
    border-radius: 8px;
    font-size: 13px;
    line-height: 1.6;
    color: #e2e8f0;
  }
  .compare .bad {
    background: rgba(220,38,38,0.1);
    border: 1px solid rgba(220,38,38,0.4);
    border-left: 3px solid #DC2626;
  }
  .compare .good {
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.4);
    border-left: 3px solid #22c55e;
  }
  .compare h4 {
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 6px;
  }
  .compare .bad h4 { color: #f87171; }
  .compare .good h4 { color: #4ade80; }

  /* Highlight quote */
  .highlight-quote {
    background: rgba(91,181,240,0.1);
    border-left: 4px solid #5bb5f0;
    padding: 10px 16px;
    border-radius: 0 6px 6px 0;
    font-size: 13px;
    color: #cbd5e1;
    line-height: 1.6;
    margin-top: 8px;
  }
  .highlight-quote.red {
    background: rgba(220,38,38,0.1);
    border-left-color: #DC2626;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin-bottom: 12px;
  }
  thead th {
    background: #2a2b3e;
    color: #ffffff;
    font-weight: 600;
    padding: 7px 12px;
    text-align: left;
    border-bottom: 2px solid #3b3c52;
  }
  tbody td {
    padding: 6px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    color: #e2e8f0;
    vertical-align: top;
  }
  tbody tr:nth-child(even) {
    background: rgba(255,255,255,0.03);
  }

  strong { color: #ffffff; }
  .accent { color: #5bb5f0; }

  /* Footer */
  .footer {
    position: absolute;
    bottom: 20px;
    left: 70px;
    right: 70px;
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: #666;
  }

  /* Special backgrounds */
  .slide-dark-red {
    background: linear-gradient(135deg, #2a1520 0%, #1a1b2e 100%);
  }
  .slide-conclusion {
    background: #141828;
  }

  /* Compact variants for dense slides */
  .body-text-sm {
    font-size: 15px;
    color: #cbd5e1;
    margin-bottom: 10px;
    line-height: 1.6;
  }
  .info-box-sm {
    background: rgba(255,255,255,0.05);
    border-left: 3px solid #5bb5f0;
    padding: 10px 16px;
    border-radius: 0 6px 6px 0;
    font-family: 'SF Mono', 'Menlo', 'Consolas', monospace;
    font-size: 12px;
    line-height: 1.55;
    color: #e2e8f0;
    white-space: pre-wrap;
    margin-bottom: 10px;
  }
  table.compact {
    font-size: 13px;
    margin-bottom: 10px;
  }
  table.compact thead th {
    padding: 5px 10px;
  }
  table.compact tbody td {
    padding: 4px 10px;
  }
  table.compact-sm {
    font-size: 12px;
    margin-bottom: 10px;
  }
  table.compact-sm thead th {
    padding: 5px 10px;
    font-size: 12px;
  }
  table.compact-sm tbody td {
    padding: 4px 10px;
  }
  .highlight-quote-sm {
    background: rgba(91,181,240,0.1);
    border-left: 4px solid #5bb5f0;
    padding: 8px 14px;
    border-radius: 0 6px 6px 0;
    font-size: 12px;
    color: #cbd5e1;
    line-height: 1.5;
    margin-top: 6px;
  }
  .highlight-quote-sm.red {
    background: rgba(220,38,38,0.1);
    border-left-color: #DC2626;
  }

  /* Side-by-side tables */
  .tables-row {
    display: flex;
    gap: 16px;
    margin-bottom: 10px;
  }
  .tables-row > div {
    flex: 1;
  }
  .tables-row h4 {
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 6px;
  }
  .tables-row h4.red { color: #f87171; }
  .tables-row h4.green { color: #4ade80; }
</style>
</head>
<body>

<!-- ==================== SLIDE 1 ==================== -->
<div class="slide">
  <div class="tag">전자서명법의 근본 문제</div>
  <div class="slide-title">왜 한국만 사용자에게 개인키를 줬나</div>
  <div class="body-text">1999년 전자서명법의 핵심 논리:</div>

  <div class="info-box">한국 정부의 사고방식:
  "거래 당사자가 나중에 '내가 안 했다'고 부인하지 못하게 해야 한다"
  → "부인 방지에는 전자서명이 필요하다"
  → "전자서명에는 개인키가 필요하다"
  → "개인키를 사용자에게 줘야 한다"
  → 사용자가 USB/PC에 파일로 보관하고 직접 관리</div>

  <div class="compare">
    <div class="bad">
      <h4>한국 (1999년)</h4>
      법이 특정 기술(PKI 인증서)을 유일한 전자서명 수단으로 지정<br>
      사용자가 개인키를 파일로 보관<br>
      분실, 유출, 갱신을 사용자가 책임
    </div>
    <div class="good">
      <h4>글로벌</h4>
      "거래 부인 방지"는 서버측 로그 + 다중인증으로 해결<br>
      은행이 거래 기록을 보관하면 법적 효력 충분<br>
      사용자에게 개인키를 줄 이유가 없다
    </div>
  </div>

  <div class="highlight-quote">다른 나라는 "내가 안 했다"는 주장에 대해 서버 로그와 인증 기록으로 대응한다. 한국만 "사용자가 직접 전자서명을 했으니 부인할 수 없다"는 구조를 선택했다.</div>

  <div class="footer"><span>유호현 · 옥소폴리틱스</span><span>1</span></div>
</div>

<!-- ==================== SLIDE 2 ==================== -->
<div class="slide">
  <div class="tag">핵심 개념</div>
  <div class="slide-title">다른 나라에는 사용자 개인키가 없다</div>
  <div class="body-text">전 세계 표준 방식에서 일반 사용자에게 개인키를 발급하지 않는다.</div>

  <div class="info-box">[한국 공인인증서 모델]
  서버 개인키 → 서버가 관리 (HTTPS 암호화용)
  사용자 개인키 → 사용자가 관리  ← <strong style="color:#f87171">한국만 이렇게 한다</strong>

[글로벌 표준 모델]
  서버 개인키 → 서버가 관리 (HTTPS 암호화용)
  사용자 인증 → 비밀번호 + MFA (개인키 없음)</div>

  <table>
    <thead><tr><th>계층</th><th>방식</th><th>누가 관리</th></tr></thead>
    <tbody>
      <tr><td>통신 암호화</td><td>TLS (서버 인증서)</td><td>서버</td></tr>
      <tr><td>본인 확인</td><td>ID/비밀번호</td><td>서버가 해시 저장</td></tr>
      <tr><td>추가 인증</td><td>OTP, 생체인증</td><td>서버 + 사용자 기기</td></tr>
      <tr><td>거래 보호</td><td>이상거래탐지(FDS)</td><td>서버</td></tr>
      <tr><td>부인 방지</td><td>서버 로그 + 감사 추적</td><td>서버</td></tr>
    </tbody>
  </table>

  <div class="highlight-quote">패스키(FIDO2)는 개인키를 사용하지만, 기기의 보안 칩에 저장되어 사용자가 존재 자체를 모른다. 지문이나 얼굴로 자동 사용. 한국 공인인증서와 같은 "개인키"지만 사용자 경험은 정반대다.</div>

  <div class="footer"><span>유호현 · 옥소폴리틱스</span><span>2</span></div>
</div>

<!-- ==================== SLIDE 3 ==================== -->
<div class="slide slide-dark-red">
  <div class="tag red">2020년 이후</div>
  <div class="slide-title">인증서 춘추전국시대</div>
  <div class="body-text">2020년 공인인증서 독점은 폐지됐다. 하지만 "인증서"라는 틀 자체는 유지됐다.</div>

  <table style="font-size:14px;">
    <thead><tr><th>인증서</th><th>운영 주체</th><th>동기</th></tr></thead>
    <tbody>
      <tr><td><strong>카카오 인증서</strong></td><td>카카오</td><td>4,700만 사용자 → 인증 시장 선점, 데이터 확보</td></tr>
      <tr><td><strong>네이버 인증서</strong></td><td>네이버</td><td>카카오에 뺏기면 안 됨</td></tr>
      <tr><td><strong>PASS 인증서</strong></td><td>SKT/KT/LGU+</td><td>본인인증(SMS) 시장 사수</td></tr>
      <tr><td><strong>토스 인증서</strong></td><td>토스</td><td>금융 플랫폼 확장</td></tr>
      <tr><td><strong>KB모바일 인증서</strong></td><td>국민은행</td><td>고객 이탈 방지</td></tr>
      <tr><td><strong>국민인증서</strong></td><td>행정안전부</td><td>공공서비스용</td></tr>
      <tr><td><strong>공동인증서</strong></td><td>금융결제원</td><td>기존 수익원 사수</td></tr>
    </tbody>
  </table>

  <div class="highlight-quote red"><strong>결과:</strong> 사용자는 서비스마다 다른 인증서를 발급받아야 한다. 은행 갈 때 하나, 정부 민원 때 하나, 카카오 또 하나. 인증서가 1개에서 7개 이상으로 늘었을 뿐, 사용자의 부담은 오히려 증가했다.</div>

  <div class="footer"><span>유호현 · 옥소폴리틱스</span><span>3</span></div>
</div>

<!-- ==================== SLIDE 4 ==================== -->
<div class="slide">
  <div class="tag">근본 진단</div>
  <div class="slide-title">마차 독점을 풀었을 뿐, 자동차로 바꾸지 않았다</div>

  <div class="compare" style="margin-top: 6px;">
    <div class="bad">
      <h4>한국의 진단: "독점이 문제다"</h4>
      공인인증서 6개 기관 독점 → 폐지<br>
      → 누구나 인증서를 발급할 수 있게<br>
      → 인증서가 7개 이상으로 증가<br>
      → 마차가 1종류에서 10종류가 됨
    </div>
    <div class="good">
      <h4>실제 문제: "인증서라는 개념 자체"</h4>
      글로벌: 비밀번호 + MFA → 끝<br>
      별도의 "인증서"라는 개체가 불필요<br>
      방법의 경쟁 (지문, 얼굴, OTP)<br>
      자동차로 전환
    </div>
  </div>

  <div class="info-box">[한국]   "본인임을 증명하는 특별한 파일(인증서)"이 필요하다
         → 누가 그 파일을 발급하느냐의 경쟁

[글로벌]  "본인임을 증명하는 방법"이 있으면 된다
         → 비밀번호, 지문, 얼굴, OTP 등 방법의 경쟁
         → 별도의 "인증서"라는 개체 자체가 불필요</div>

  <div class="highlight-quote">공인인증서 폐지는 "독점을 깼을 뿐, 패러다임을 바꾸지 못했다." 한국은 "인증서가 필요하다"는 전제 자체를 의심하지 않았다.</div>

  <div class="footer"><span>유호현 · 옥소폴리틱스</span><span>4</span></div>
</div>

<!-- ==================== SLIDE 5 ==================== -->
<div class="slide slide-dark-red">
  <div class="tag red">한국만의 구조</div>
  <div class="slide-title" style="font-size:32px;">휴대폰 없으면 아무것도 할 수 없는 나라</div>
  <div class="body-text-sm">한국은 모든 온라인 서비스에 휴대폰 본인인증을 요구한다. 미국은 이메일이면 충분하다.</div>

  <table class="compact">
    <thead><tr><th>상황</th><th>한국</th><th>미국</th></tr></thead>
    <tbody>
      <tr><td>쇼핑몰 회원가입</td><td>휴대폰 본인인증 필수</td><td>이메일만 있으면 됨</td></tr>
      <tr><td>게임 계정 생성</td><td>휴대폰 본인인증 필수</td><td>이메일만 있으면 됨</td></tr>
      <tr><td>비밀번호 찾기</td><td>휴대폰 인증</td><td>이메일 링크</td></tr>
      <tr><td>커뮤니티 댓글</td><td>휴대폰 인증 필수</td><td>익명 가능</td></tr>
      <tr><td>은행 이체</td><td>휴대폰 인증 + 인증서</td><td>로그인 + 서버 FDS</td></tr>
      <tr><td>휴대폰 없으면?</td><td><strong style="color:#f87171">아무것도 못 함</strong></td><td>이메일로 대체 가능</td></tr>
    </tbody>
  </table>

  <div class="info-box-sm">주민등록번호 수집 금지 (2014년)
  → 대체 수단 필요
  → 통신사가 "우리가 하겠다"
  → 통신사가 주민번호와 휴대폰 번호를 연결해 놨으니까
  → 휴대폰 인증 = 실명 확인
  → 통신사가 모든 온라인 서비스의 관문을 장악</div>

  <div class="highlight-quote-sm red">미국에서 SSN을 웹사이트 회원가입에 입력하라고 하면 100% 사기다. 한국에서는 2014년까지 모든 웹사이트가 주민등록번호를 수집했다. 지금은 주민번호 대신 휴대폰 인증이 그 역할을 하고 있을 뿐이다.</div>

  <div class="footer"><span>유호현 · 옥소폴리틱스</span><span>5</span></div>
</div>

<!-- ==================== SLIDE 6 ==================== -->
<div class="slide">
  <div class="tag">여권의 비유</div>
  <div class="slide-title" style="font-size:32px;">주민등록번호가 문제가 아니라 남용이 문제다</div>
  <div class="body-text-sm">한국, 독일, 일본, 스웨덴 전부 국민 ID가 있다. 차이는 어디까지 요구하느냐다.</div>

  <div class="compare" style="margin-bottom:10px;">
    <div class="bad" style="padding:12px 14px;">
      <h4>적절한 사용 (모든 나라)</h4>
      은행 계좌 개설 (자금세탁 방지)<br>
      증권 거래 (내부자 거래 감시)<br>
      정부 민원 (세금, 복지)<br>
      통신사 후불 계약
    </div>
    <div class="bad" style="padding:12px 14px;">
      <h4>한국만 요구하는 곳</h4>
      온라인 쇼핑몰 회원가입 · 게임 계정 생성<br>
      커뮤니티/SNS 가입 · 배달 앱 가입<br>
      OTT 서비스 가입 · 와이파이 가입
    </div>
  </div>

  <div class="info-box-sm">비유: 주민등록번호 = 여권

다른 나라: 여권은 출입국과 은행에서만 보여준다.
한국: 편의점 들어갈 때도 여권을 보여줘야 한다.
      2014년에 "여권 직접 제시"는 금지됐지만,
      대신 "여권 번호를 아는 통신사가 대신 확인해줌"으로 바뀜.
      본질은 같다.</div>

  <div class="highlight-quote-sm">EU GDPR의 "데이터 최소화 원칙" — 서비스에 꼭 필요한 정보만 수집해야 한다. 쇼핑몰이 주민번호를 수집하면 불법이다. 한국은 정반대 방향으로 가고 있다.</div>

  <div class="footer"><span>유호현 · 옥소폴리틱스</span><span>6</span></div>
</div>

<!-- ==================== SLIDE 7 ==================== -->
<div class="slide slide-conclusion">
  <div class="tag">종합</div>
  <div class="slide-title" style="font-size:30px; margin-bottom:12px;">문제의 핵심: 보안의 책임을 사용자에게 떠넘기는 구조</div>
  <div class="body-text-sm" style="margin-bottom:8px;">지금까지 다룬 모든 문제를 관통하는 하나의 구조가 있다.</div>

  <div class="tables-row">
    <div>
      <h4 class="red">한국</h4>
      <table class="compact-sm">
        <thead><tr><th>영역</th><th>방법</th><th>책임</th></tr></thead>
        <tbody>
          <tr><td>암호화</td><td>사용자 PC에 프로그램 설치</td><td style="color:#f87171">사용자</td></tr>
          <tr><td>인증</td><td>사용자가 인증서(개인키) 관리</td><td style="color:#f87171">사용자</td></tr>
          <tr><td>본인확인</td><td>사용자가 매번 증명</td><td style="color:#f87171">사용자</td></tr>
          <tr><td>사고 시</td><td>"프로그램 안 깔았으니 네 잘못"</td><td style="color:#f87171">사용자</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <h4 class="green">글로벌</h4>
      <table class="compact-sm">
        <thead><tr><th>영역</th><th>방법</th><th>책임</th></tr></thead>
        <tbody>
          <tr><td>암호화</td><td>서버에서 TLS 처리</td><td style="color:#4ade80">서비스 제공자</td></tr>
          <tr><td>인증</td><td>서버가 MFA+FDS로 판단</td><td style="color:#4ade80">서비스 제공자</td></tr>
          <tr><td>본인확인</td><td>서버가 행동 패턴으로 판단</td><td style="color:#4ade80">서비스 제공자</td></tr>
          <tr><td>사고 시</td><td>"서버 보안 부족이면 은행 잘못"</td><td style="color:#4ade80">서비스 제공자</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="info-box-sm" style="font-size:11.5px; line-height:1.5; padding:8px 14px;">뿌리 1: 국민 관리 사상 (1968~)
  주민등록제도 → 인터넷 실명제 → 휴대폰 본인인증

뿌리 2: 책임 회피 규제 (1999~)
  전자서명법 → 보안프로그램 의무화 → 면책 구조

뿌리 3: 규제가 만든 이권 (2005~)
  보안프로그램 업체 → 인증기관 → 통신사 본인인증</div>

  <div class="highlight-quote-sm" style="font-size:12px;"><strong>한국 IT 보안의 근본 문제는 기술이 아니라 철학이다.</strong> "보안의 책임이 누구에게 있는가"에 대해 한국은 사용자를, 세계는 서비스 제공자를 지목한다. 이 하나의 차이에서 인증서, 보안프로그램, 휴대폰 인증, 면책 구조가 전부 갈라진다.</div>

  <div class="footer"><span>유호현 · 옥소폴리틱스</span><span>7</span></div>
</div>

</body>
</html>"""

# Write HTML
with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML 생성: {OUTPUT_HTML}")

# Generate PDF via Chrome headless
cmd = [
    CHROME,
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--print-to-pdf=" + OUTPUT_PDF,
    "--no-pdf-header-footer",
    "file://" + OUTPUT_HTML,
]

result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
if result.returncode == 0:
    print(f"PDF 생성 완료: {OUTPUT_PDF}")
else:
    print(f"PDF 생성 실패: {result.stderr}")
