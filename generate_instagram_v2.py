#!/usr/bin/env python3
"""Instagram carousel image generator for 한국 보안의 갈라파고스 presentation."""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# Constants
W, H = 1080, 1080
FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUTPUT_DIR = "/Users/will_ryu/workspace/personal/korean_it/결제보안/instagram_v2"

# Font indices: 0=Regular, 2=Medium, 4=SemiBold, 6=Bold, 8=Light
def font(size, weight="bold"):
    idx = {"regular": 0, "medium": 2, "semibold": 4, "bold": 6, "light": 8}
    return ImageFont.truetype(FONT_PATH, size, index=idx.get(weight, 6))

# Colors
DARK_BG = "#0F1724"
BLUE_BG = "#1A2744"
RED_BG = "#C62828"
ACCENT_BLUE = "#64B5F6"
ACCENT_GREEN = "#66BB6A"
ACCENT_RED = "#EF5350"
ACCENT_YELLOW = "#FFD54F"
WHITE = "#FFFFFF"
GRAY = "#9E9E9E"
LIGHT_GRAY = "#BDBDBD"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def draw_rounded_rect(draw, xy, fill, radius=20):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def draw_tag(draw, pos, text, bg_color="#2196F3", text_color=WHITE):
    f = font(28, "semibold")
    bbox = f.getbbox(text)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    px, py = 16, 8
    x, y = pos
    draw_rounded_rect(draw, (x, y, x + tw + px * 2, y + th + py * 2), fill=bg_color, radius=8)
    draw.text((x + px, y + py - 2), text, fill=text_color, font=f)


def wrap_text(text, max_chars):
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        words = paragraph.split()
        current = ""
        for word in words:
            test = f"{current} {word}".strip() if current else word
            if len(test) <= max_chars:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_multiline(draw, pos, text, f, fill=WHITE, max_chars=20, line_spacing=1.4):
    lines = wrap_text(text, max_chars)
    x, y = pos
    for line in lines:
        if line:
            draw.text((x, y), line, fill=fill, font=f)
        bbox = f.getbbox("가")
        h = bbox[3] - bbox[1]
        y += int(h * line_spacing)
    return y


def card_cover():
    """Slide 1: Cover"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 120), "국가인공지능전략위원회 발표자료", bg_color="#37474F")

    # Title - big
    y = 220
    title_f = font(82, "bold")
    draw.text((80, y), "한국 보안의", fill=WHITE, font=title_f)
    y += 100
    draw.text((80, y), "갈라파고스", fill=WHITE, font=title_f)

    y += 140
    sub_f = font(68, "bold")
    draw.text((80, y), "어디서부터", fill=ACCENT_BLUE, font=sub_f)
    y += 90
    draw.text((80, y), "잘못됐나", fill=ACCENT_BLUE, font=sub_f)

    y += 160
    desc_f = font(36, "regular")
    draw.text((80, y), "ActiveX에서 AI까지", fill=LIGHT_GRAY, font=desc_f)
    y += 55
    draw.text((80, y), "한국이 세계와 다른 길을 걸은 25년의 역사", fill=LIGHT_GRAY, font=desc_f)

    y += 120
    author_f = font(32, "medium")
    draw.text((80, y), "유호현 · (주)옥소폴리틱스 대표", fill=GRAY, font=author_f)
    y += 48
    draw.text((80, y), "2026년 3월", fill=GRAY, font=author_f)

    # Page indicator
    draw_page_indicator(draw, 1, 10)

    img.save(os.path.join(OUTPUT_DIR, "01_cover.png"), quality=95)


def draw_page_indicator(draw, current, total):
    dot_size = 10
    gap = 20
    total_w = total * dot_size + (total - 1) * gap
    start_x = (W - total_w) // 2
    y = H - 50
    for i in range(total):
        x = start_x + i * (dot_size + gap)
        color = WHITE if i == current - 1 else "#3E4A5C"
        draw.ellipse((x, y, x + dot_size, y + dot_size), fill=color)


def card_problem():
    """Slide 2: 25년 전 같은 출발선 → 지금은?"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "25년의 역사")

    title_f = font(64, "bold")
    draw.text((80, 180), "1999년, 한국은", fill=WHITE, font=title_f)
    draw.text((80, 260), "세계 최고의", fill=ACCENT_BLUE, font=title_f)
    draw.text((80, 340), "IT 강국이었다", fill=ACCENT_BLUE, font=title_f)

    # Stats
    y = 470
    stat_f = font(44, "bold")
    label_f = font(30, "regular")

    draw.text((80, y), "초고속 인터넷 보급률", fill=LIGHT_GRAY, font=label_f)
    y += 45
    draw.text((80, y), "세계 1위", fill=ACCENT_GREEN, font=stat_f)

    y += 80
    draw.text((80, y), "UN 전자정부 순위", fill=LIGHT_GRAY, font=label_f)
    y += 45
    draw.text((80, y), "3회 연속 세계 1위", fill=ACCENT_GREEN, font=stat_f)

    # Divider
    y += 100
    draw.line((80, y, W - 80, y), fill="#2A3A50", width=2)

    y += 40
    now_f = font(44, "bold")
    draw.text((80, y), "그런데 2026년,", fill=WHITE, font=now_f)
    y += 65
    draw.text((80, y), "은행 접속하려면", fill=WHITE, font=now_f)
    y += 65
    draw.text((80, y), "프로그램 5개를", fill=ACCENT_RED, font=now_f)
    y += 65
    draw.text((80, y), "깔아야 한다", fill=ACCENT_RED, font=now_f)

    draw_page_indicator(draw, 2, 10)
    img.save(os.path.join(OUTPUT_DIR, "02_problem.png"), quality=95)


def card_origin():
    """Slide 3: 왜 ActiveX를 썼나"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "1999년")

    title_f = font(58, "bold")
    draw.text((80, 170), "미국이 암호화", fill=WHITE, font=title_f)
    draw.text((80, 250), "수출을 금지했다", fill=WHITE, font=title_f)

    y = 370
    body_f = font(36, "medium")
    draw.text((80, y), "128비트 SSL을 쓸 수 없었던 한국", fill=LIGHT_GRAY, font=body_f)
    y += 55
    draw.text((80, y), "→ SEED 암호화를 직접 개발", fill=LIGHT_GRAY, font=body_f)
    y += 55
    draw.text((80, y), "→ 브라우저가 SEED를 지원 안 함", fill=LIGHT_GRAY, font=body_f)
    y += 55
    draw.text((80, y), "→ ActiveX로 설치해서 해결", fill=LIGHT_GRAY, font=body_f)

    y += 90
    highlight_f = font(42, "bold")
    draw.text((80, y), "당시에는", fill=WHITE, font=highlight_f)
    y += 60
    draw.text((80, y), "합리적인 선택이었다", fill=ACCENT_GREEN, font=highlight_f)

    # But...
    y += 110
    draw_rounded_rect(draw, (60, y, W - 60, y + 140), fill="#1A2744", radius=12)
    but_f = font(36, "bold")
    draw.text((80, y + 20), "그런데 1년 후, 미국이 암호화 수출", fill=ACCENT_YELLOW, font=but_f)
    draw.text((80, y + 65), "제한을 풀었다. 한국만 돌아오지 못했다.", fill=ACCENT_YELLOW, font=but_f)

    draw_page_indicator(draw, 3, 10)
    img.save(os.path.join(OUTPUT_DIR, "03_origin.png"), quality=95)


def card_law():
    """Slide 4: 법으로 기술을 고정"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "전자서명법 1999")

    title_f = font(56, "bold")
    draw.text((80, 170), "법 한 줄이", fill=WHITE, font=title_f)
    draw.text((80, 245), "21년간 한국의", fill=WHITE, font=title_f)
    draw.text((80, 320), "인터넷을 가뒀다", fill=ACCENT_RED, font=title_f)

    y = 430
    body_f = font(34, "medium")
    lines = [
        "공인인증서 = PKI 기반 인증서만 법적 효력",
        "",
        "공인인증서를 쓰려면 → ActiveX 필수",
        "ActiveX는 IE에서만 작동",
        "",
        "→ 모든 금융·공공 서비스가",
        "   Internet Explorer 전용이 됨",
        "",
        "→ Chrome, Firefox, Safari 불가",
        "→ 맥, 리눅스에서도 불가",
    ]
    for line in lines:
        if line:
            draw.text((80, y), line, fill=LIGHT_GRAY, font=body_f)
        y += 48

    y += 20
    note_f = font(30, "semibold")
    draw.text((80, y), "이 법은 2020년 12월에야 폐지됐다", fill=GRAY, font=note_f)

    draw_page_indicator(draw, 4, 10)
    img.save(os.path.join(OUTPUT_DIR, "04_law.png"), quality=95)


def card_private_key():
    """Slide 5: 왜 한국만 사용자에게 개인키를 줬나"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "핵심 차이")

    title_f = font(54, "bold")
    draw.text((80, 170), "다른 나라에는", fill=WHITE, font=title_f)
    draw.text((80, 245), "사용자 개인키가", fill=WHITE, font=title_f)
    draw.text((80, 320), "없다", fill=ACCENT_RED, font=title_f)

    # Korea box
    y = 430
    draw_rounded_rect(draw, (60, y, 520, y + 260), fill="#2A1A1A", radius=16)
    box_title_f = font(32, "bold")
    box_f = font(28, "regular")
    draw.text((80, y + 15), "한국 (1999년)", fill=ACCENT_RED, font=box_title_f)
    draw.text((80, y + 60), "사용자가 개인키를", fill=LIGHT_GRAY, font=box_f)
    draw.text((80, y + 95), "파일로 보관", fill=LIGHT_GRAY, font=box_f)
    draw.text((80, y + 140), "분실, 유출, 갱신을", fill=LIGHT_GRAY, font=box_f)
    draw.text((80, y + 175), "사용자가 책임", fill=LIGHT_GRAY, font=box_f)
    draw.text((80, y + 215), "= 비밀번호 수준 보안", fill=ACCENT_RED, font=box_f)

    # Global box
    draw_rounded_rect(draw, (560, y, W - 60, y + 260), fill="#1A2A1A", radius=16)
    draw.text((580, y + 15), "글로벌", fill=ACCENT_GREEN, font=box_title_f)
    draw.text((580, y + 60), "서버 로그 + 다중인증", fill=LIGHT_GRAY, font=box_f)
    draw.text((580, y + 95), "으로 부인 방지 해결", fill=LIGHT_GRAY, font=box_f)
    draw.text((580, y + 140), "사용자에게 개인키를", fill=LIGHT_GRAY, font=box_f)
    draw.text((580, y + 175), "줄 이유가 없다", fill=LIGHT_GRAY, font=box_f)
    draw.text((580, y + 215), "= 잃어버릴 것 없음", fill=ACCENT_GREEN, font=box_f)

    # Bottom quote
    y2 = y + 300
    quote_f = font(32, "semibold")
    draw.text((80, y2), "비유: \"주차권이 비밀번호보다", fill=ACCENT_YELLOW, font=quote_f)
    draw.text((80, y2 + 45), "안전하니까 국민에게 나눠주자\"", fill=ACCENT_YELLOW, font=quote_f)
    draw.text((80, y2 + 95), "→ 결국 비밀번호 수준으로 전락", fill=LIGHT_GRAY, font=font(28, "regular"))

    draw_page_indicator(draw, 5, 10)
    img.save(os.path.join(OUTPUT_DIR, "05_private_key.png"), quality=95)


def card_parking():
    """Slide 6: 한국 주차장은 3세대, 한국 은행은 1세대"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "세대 비교")

    title_f = font(50, "bold")
    draw.text((80, 170), "한국 주차장은 3세대", fill=WHITE, font=title_f)
    draw.text((80, 240), "한국 은행은 1세대", fill=ACCENT_RED, font=title_f)

    # Table header
    y = 340
    hdr_f = font(30, "bold")
    cell_f = font(28, "regular")
    cell_bf = font(28, "bold")

    # Header
    draw_rounded_rect(draw, (60, y, W - 60, y + 50), fill="#1A2744", radius=8)
    draw.text((80, y + 10), "세대", fill=ACCENT_BLUE, font=hdr_f)
    draw.text((240, y + 10), "주차장", fill=ACCENT_BLUE, font=hdr_f)
    draw.text((500, y + 10), "한국 금융", fill=ACCENT_BLUE, font=hdr_f)
    draw.text((780, y + 10), "글로벌 금융", fill=ACCENT_BLUE, font=hdr_f)

    rows = [
        ("1세대", "물리 주차권", "공인인증서(USB)", "비밀번호"),
        ("2세대", "앱 주차권", "카카오/PASS", "비밀번호+MFA"),
        ("3세대", "번호판 자동인식", "아직 2세대 멈춤", "FIDO2/패스키"),
    ]

    for i, (gen, park, kr, glob) in enumerate(rows):
        ry = y + 70 + i * 65
        draw.line((60, ry - 5, W - 60, ry - 5), fill="#2A3A50", width=1)

        gen_color = ACCENT_GREEN if i == 2 else WHITE
        kr_color = ACCENT_RED if i == 2 else LIGHT_GRAY

        draw.text((80, ry + 5), gen, fill=gen_color, font=cell_bf)
        draw.text((240, ry + 5), park, fill=LIGHT_GRAY, font=cell_f)
        draw.text((500, ry + 5), kr, fill=kr_color, font=cell_bf if i == 2 else cell_f)
        draw.text((780, ry + 5), glob, fill=LIGHT_GRAY, font=cell_f)

    # Bottom insight
    y2 = 620
    insight_f = font(38, "bold")
    draw.text((80, y2), "같은 나라에서", fill=WHITE, font=insight_f)
    y2 += 55
    draw.text((80, y2), "주차장은 번호판 자동인식인데", fill=WHITE, font=insight_f)
    y2 += 55
    draw.text((80, y2), "은행은 아직 1999년에 멈춰있다", fill=ACCENT_RED, font=insight_f)

    # Bottom note
    y3 = y2 + 90
    draw_rounded_rect(draw, (60, y3, W - 60, y3 + 100), fill="#1A2744", radius=12)
    ana_f = font(30, "semibold")
    draw.text((80, y3 + 15), "같은 기술 철학을 은행에 적용하면 된다.", fill=ACCENT_YELLOW, font=ana_f)
    draw.text((80, y3 + 55), "새로 발명할 것이 없다.", fill=LIGHT_GRAY, font=ana_f)

    draw_page_indicator(draw, 6, 10)
    img.save(os.path.join(OUTPUT_DIR, "06_parking.png"), quality=95)


def card_vishing():
    """Slide 7: 보이스피싱 - 보안프로그램으로 못 막는다"""
    img = Image.new("RGB", (W, H), RED_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "보이스피싱", bg_color="#B71C1C")

    title_f = font(72, "bold")
    draw.text((80, 180), "1조 965억 원", fill=WHITE, font=title_f)

    sub_f = font(36, "medium")
    draw.text((80, 280), "2023년 연간 피해액 (경찰청 통계)", fill="#FFCDD2", font=sub_f)
    draw.text((80, 330), "하루 평균 30억 원이 사기로 빠져나간다", fill="#FFCDD2", font=sub_f)

    # How it works
    y = 430
    how_f = font(44, "bold")
    draw.text((80, y), "보이스피싱은 이렇게 작동한다", fill=WHITE, font=how_f)

    y += 70
    step_f = font(34, "medium")
    steps = [
        "1. 전화가 온다 \"검찰입니다\"",
        "2. 피해자가 속는다",
        "3. 피해자가 직접 돈을 보낸다",
        "4. 돈이 빠져나간다",
    ]
    for step in steps:
        draw.text((80, y), step, fill="#FFCDD2", font=step_f)
        y += 52

    # Key insight
    y += 30
    key_f = font(40, "bold")
    draw.text((80, y), "핵심: 피해자가 속아서", fill=WHITE, font=key_f)
    y += 55
    draw.text((80, y), "자기 손으로 직접 하는 것이다", fill=ACCENT_YELLOW, font=key_f)

    y += 80
    conc_f = font(34, "semibold")
    draw.text((80, y), "PC에 보안프로그램을 깔아서", fill="#FFCDD2", font=conc_f)
    y += 50
    draw.text((80, y), "막을 수 있는 문제가 아니다", fill=WHITE, font=font(38, "bold"))

    draw_page_indicator(draw, 7, 10)
    img.save(os.path.join(OUTPUT_DIR, "07_vishing.png"), quality=95)


def card_sandbox():
    """Slide 8: ActiveX vs 샌드박스"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "정반대 방향")

    title_f = font(54, "bold")
    draw.text((80, 170), "세계는 브라우저를 닫고", fill=WHITE, font=title_f)
    draw.text((80, 245), "한국은 브라우저를 열었다", fill=ACCENT_RED, font=title_f)

    # ActiveX box (red)
    y = 370
    draw_rounded_rect(draw, (60, y, 520, y + 280), fill="#2A1A1A", radius=16)
    box_title_f = font(36, "bold")
    box_f = font(30, "regular")
    draw.text((80, y + 15), "ActiveX 방식 (한국)", fill=ACCENT_RED, font=box_title_f)
    draw.text((80, y + 65), "웹사이트가 PC에", fill=LIGHT_GRAY, font=box_f)
    draw.text((80, y + 100), "프로그램을 설치하고", fill=LIGHT_GRAY, font=box_f)
    draw.text((80, y + 135), "실행할 수 있다", fill=LIGHT_GRAY, font=box_f)
    draw.text((80, y + 185), "PC의 모든 것에", fill=WHITE, font=font(30, "bold"))
    draw.text((80, y + 220), "접근 가능", fill=WHITE, font=font(30, "bold"))

    # Sandbox box (green)
    draw_rounded_rect(draw, (560, y, W - 60, y + 280), fill="#1A2A1A", radius=16)
    draw.text((580, y + 15), "샌드박스 방식 (세계)", fill=ACCENT_GREEN, font=box_title_f)
    draw.text((580, y + 65), "웹사이트는 브라우저", fill=LIGHT_GRAY, font=box_f)
    draw.text((580, y + 100), "라는 상자 안에", fill=LIGHT_GRAY, font=box_f)
    draw.text((580, y + 135), "갇혀 있다", fill=LIGHT_GRAY, font=box_f)
    draw.text((580, y + 185), "PC에 접근 불가", fill=WHITE, font=font(30, "bold"))
    draw.text((580, y + 220), "보안의 벽이 있다", fill=WHITE, font=font(30, "bold"))

    # Bottom quote
    y2 = y + 320
    quote_f = font(34, "bold")
    draw.text((80, y2), "세계:", fill=ACCENT_GREEN, font=quote_f)
    draw.text((160, y2), "\"프로그램 설치 자체가 위험\"", fill=LIGHT_GRAY, font=font(34, "medium"))
    y2 += 55
    draw.text((80, y2), "한국:", fill=ACCENT_RED, font=quote_f)
    draw.text((160, y2), "\"보안을 위해 프로그램을 더 깔아라\"", fill=LIGHT_GRAY, font=font(34, "medium"))

    y2 += 75
    draw.text((80, y2), "→ 정반대였다", fill=ACCENT_YELLOW, font=font(40, "bold"))

    draw_page_indicator(draw, 8, 10)
    img.save(os.path.join(OUTPUT_DIR, "08_sandbox.png"), quality=95)


def card_real_solution():
    """Slide 9: 진짜 효과 있는 대책은 서버에서 한다"""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "진짜 해결책")

    title_f = font(52, "bold")
    draw.text((80, 170), "효과 있는 대책은", fill=WHITE, font=title_f)
    draw.text((80, 245), "전부 서버에서 한다", fill=ACCENT_GREEN, font=title_f)

    # Solutions table
    y = 370
    solutions = [
        ("이상거래탐지 (FDS)", "평소와 다른 패턴 → 자동 차단", "은행 서버"),
        ("지연이체", "큰 금액 30분~1시간 후 실행", "은행 서버"),
        ("AI 통화 분석", "\"검찰\" \"계좌 동결\" 감지 → 경고", "통신사 서버"),
        ("다중인증 (MFA)", "비밀번호 + 생체인증", "서버 + 기기"),
        ("패스키 (FIDO2)", "지문/얼굴로 자동 사용", "기기 보안칩"),
    ]

    hdr_f = font(28, "bold")
    draw_rounded_rect(draw, (60, y, W - 60, y + 45), fill="#1A2744", radius=8)
    draw.text((80, y + 8), "대책", fill=ACCENT_BLUE, font=hdr_f)
    draw.text((400, y + 8), "작동 방식", fill=ACCENT_BLUE, font=hdr_f)
    draw.text((860, y + 8), "위치", fill=ACCENT_BLUE, font=hdr_f)

    cell_f = font(25, "regular")
    cell_bf = font(25, "semibold")
    for i, (name, desc, where) in enumerate(solutions):
        ry = y + 60 + i * 60
        draw.line((60, ry, W - 60, ry), fill="#2A3A50", width=1)
        draw.text((80, ry + 12), name, fill=WHITE, font=cell_bf)
        draw.text((400, ry + 12), desc, fill=LIGHT_GRAY, font=cell_f)
        draw.text((860, ry + 12), where, fill=ACCENT_GREEN, font=cell_bf)

    # Key insight
    y2 = y + 60 + len(solutions) * 60 + 40
    big_f = font(46, "bold")
    draw.text((80, y2), "이 중 어느 것도", fill=WHITE, font=big_f)
    y2 += 65
    draw.text((80, y2), "사용자 PC에 프로그램을", fill=WHITE, font=big_f)
    y2 += 65
    draw.text((80, y2), "설치할 필요가 없다", fill=ACCENT_GREEN, font=big_f)

    draw_page_indicator(draw, 9, 10)
    img.save(os.path.join(OUTPUT_DIR, "09_solution.png"), quality=95)


def card_cta():
    """Slide 10: 마무리 CTA"""
    img = Image.new("RGB", (W, H), BLUE_BG)
    draw = ImageDraw.Draw(img)

    title_f = font(56, "bold")
    y = 180
    draw.text((80, y), "1년만 늦게 시작했으면", fill=WHITE, font=title_f)
    y += 80
    draw.text((80, y), "SEED도 ActiveX도", fill=ACCENT_BLUE, font=title_f)
    y += 80
    draw.text((80, y), "공인인증서도", fill=ACCENT_BLUE, font=title_f)
    y += 80
    draw.text((80, y), "필요 없었다", fill=ACCENT_BLUE, font=title_f)

    y += 120
    body_f = font(38, "medium")
    draw.text((80, y), "한국이 인터넷 강국이라서", fill=LIGHT_GRAY, font=body_f)
    y += 55
    draw.text((80, y), "세계보다 빨리 움직인 것이", fill=LIGHT_GRAY, font=body_f)
    y += 55
    draw.text((80, y), "역설적으로 갈라파고스의 원인이 됐다", fill=LIGHT_GRAY, font=body_f)

    y += 100
    cta_f = font(44, "bold")
    draw.text((80, y), "25년의 기술 부채를", fill=WHITE, font=cta_f)
    y += 65
    draw.text((80, y), "이제는 청산할 때다", fill=ACCENT_YELLOW, font=cta_f)

    y += 120
    author_f = font(30, "medium")
    draw.text((80, y), "유호현 · (주)옥소폴리틱스 대표", fill=GRAY, font=author_f)
    y += 45
    draw.text((80, y), "국가인공지능전략위원회 발표자료 | 2026년 3월", fill=GRAY, font=font(26, "regular"))

    draw_page_indicator(draw, 10, 10)
    img.save(os.path.join(OUTPUT_DIR, "10_cta.png"), quality=95)


if __name__ == "__main__":
    print("Generating Instagram carousel images...")
    card_cover()
    print("  1/10 cover")
    card_problem()
    print("  2/10 problem")
    card_origin()
    print("  3/10 origin")
    card_law()
    print("  4/10 law")
    card_private_key()
    print("  5/10 private_key")
    card_parking()
    print("  6/10 parking")
    card_vishing()
    print("  7/10 vishing")
    card_sandbox()
    print("  8/10 sandbox")
    card_real_solution()
    print("  9/10 solution")
    card_cta()
    print("  10/10 cta")
    print(f"\nDone! Images saved to {OUTPUT_DIR}/")
