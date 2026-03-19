#!/usr/bin/env python3
"""Instagram carousel v4 - 한국 보안의 갈라파고스. Spring palette, 10 slides."""

from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUTPUT_DIR = "/Users/will_ryu/workspace/personal/korean_it/결제보안/instagram_v4"
TOTAL = 10

def font(size, weight="bold"):
    idx = {"regular": 0, "medium": 2, "semibold": 4, "bold": 6, "light": 8}
    return ImageFont.truetype(FONT_PATH, size, index=idx.get(weight, 6))

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Spring palette ──
# Backgrounds
BG_CREAM = (255, 251, 245)
BG_MINT = (235, 250, 245)
BG_PEACH = (255, 243, 235)
BG_LAVENDER = (242, 238, 252)
BG_WARM_WHITE = (252, 249, 244)
BG_SAGE = (230, 242, 232)
BG_ROSE = (252, 238, 238)
BG_CORAL_DEEP = (210, 82, 72)
BG_SOFT_NAVY = (42, 52, 68)

# Text
T_DARK = "#2A2A2A"
T_BODY = "#4A4A4A"
T_MUTED = "#7A7A7A"
T_WHITE = "#FFFFFF"

# Accents
A_CORAL = "#E8706A"
A_MINT = "#3DB88C"
A_SAGE = "#6B9E7A"
A_LAVENDER = "#8B78C8"
A_PEACH = "#E8956A"
A_ROSE = "#D4707A"
A_WARM_YELLOW = "#E8C84A"
A_SKY = "#5AABE8"
A_SOFT_RED = "#D65A5A"


def lerp(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def gradient_bg(c1, c2, direction="vertical"):
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        for x in range(W):
            t = y / H if direction == "vertical" else x / W
            px[x, y] = lerp(c1, c2, t)
    return img


def soft_glow(img, cx, cy, radius, color, alpha=40):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -3):
        a = int(alpha * (1 - (r / radius) ** 1.5))
        if a < 1:
            continue
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color + (a,))
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def accent_line(draw, x, y, length, color, width=4):
    draw.rounded_rectangle((x, y, x + length, y + width), radius=2, fill=color)


def pill_tag(draw, pos, text, bg, fg="#FFFFFF"):
    f = font(24, "semibold")
    bb = f.getbbox(text)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    px, py = 20, 10
    x, y = pos
    draw.rounded_rectangle((x, y, x + tw + px * 2, y + th + py * 2), radius=24, fill=bg)
    draw.text((x + px, y + py - 2), text, fill=fg, font=f)
    return y + th + py * 2 + 10


def dots(draw, current):
    r = 5
    gap = 16
    tw = TOTAL * r * 2 + (TOTAL - 1) * gap
    sx = (W - tw) // 2
    y = H - 46
    for i in range(TOTAL):
        x = sx + i * (r * 2 + gap)
        draw.ellipse((x, y, x + r * 2, y + r * 2), fill=T_DARK if i == current - 1 else "#D0D0D0")


def rounded_box(draw, xy, fill, radius=16, border=None, border_width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill)
    if border:
        draw.rounded_rectangle(xy, radius=radius, outline=border, width=border_width)


# ═══════════════════════════════════════
# SLIDES
# ═══════════════════════════════════════

def slide_01_cover():
    img = gradient_bg(BG_CREAM, BG_PEACH)
    img = soft_glow(img, 850, 250, 400, (232, 150, 120), 30)
    img = soft_glow(img, 150, 800, 350, (100, 200, 160), 20)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 90), "국가인공지능전략위원회 발표자료", A_PEACH)
    accent_line(draw, 80, 170, 60, A_CORAL)

    draw.text((80, 200), "한국 보안의", fill=T_DARK, font=font(86, "bold"))
    draw.text((80, 308), "갈라파고스", fill=T_DARK, font=font(86, "bold"))

    draw.text((80, 440), "어디서부터", fill=A_CORAL, font=font(70, "bold"))
    draw.text((80, 530), "잘못됐나", fill=A_CORAL, font=font(70, "bold"))

    draw.text((80, 660), "ActiveX에서 AI까지 — 세계와 다른 길을 걸은 25년", fill=T_MUTED, font=font(28, "regular"))

    draw.text((80, 740), "유호현 · (주)옥소폴리틱스 대표", fill=T_MUTED, font=font(26, "medium"))
    draw.text((80, 778), "2026년 3월", fill="#999999", font=font(24, "regular"))

    dots(draw, 1)
    img.save(f"{OUTPUT_DIR}/01_cover.png", quality=95)


def slide_02_problem():
    img = gradient_bg(BG_MINT, BG_WARM_WHITE)
    img = soft_glow(img, 540, 300, 400, (80, 200, 140), 25)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 80), "25년의 역사", A_MINT)
    accent_line(draw, 80, 145, 50, A_SAGE)

    draw.text((80, 175), "1999년, 한국은", fill=T_DARK, font=font(60, "bold"))
    draw.text((80, 255), "세계 최고의", fill=A_MINT, font=font(60, "bold"))
    draw.text((80, 335), "IT 강국이었다", fill=A_MINT, font=font(60, "bold"))

    y = 440
    draw.text((80, y), "초고속 인터넷 보급률", fill=T_MUTED, font=font(26, "regular"))
    draw.text((80, y + 34), "세계 1위", fill=A_SAGE, font=font(50, "bold"))
    draw.text((80, y + 100), "UN 전자정부 순위", fill=T_MUTED, font=font(26, "regular"))
    draw.text((80, y + 134), "3회 연속 세계 1위", fill=A_SAGE, font=font(50, "bold"))

    y2 = y + 225
    draw.line((80, y2, W - 80, y2), fill="#C8D8C8", width=1)
    y2 += 25
    draw.text((80, y2), "그런데 2026년,", fill=T_DARK, font=font(42, "bold"))
    y2 += 56
    draw.text((80, y2), "은행 접속하려면", fill=T_DARK, font=font(42, "bold"))
    y2 += 56
    draw.text((80, y2), "프로그램 5개를 깔아야 한다", fill=A_SOFT_RED, font=font(42, "bold"))

    dots(draw, 2)
    img.save(f"{OUTPUT_DIR}/02_problem.png", quality=95)


def slide_03_origin():
    img = gradient_bg(BG_PEACH, BG_CREAM)
    img = soft_glow(img, 200, 650, 400, (232, 170, 100), 25)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 80), "1999년", A_PEACH)
    accent_line(draw, 80, 145, 50, A_PEACH)

    draw.text((80, 178), "미국이 암호화", fill=T_DARK, font=font(58, "bold"))
    draw.text((80, 255), "수출을 금지했다", fill=T_DARK, font=font(58, "bold"))

    y = 365
    f = font(32, "medium")
    for line in ["128비트 SSL을 쓸 수 없었던 한국",
                 "→  SEED 암호화를 직접 개발",
                 "→  브라우저가 SEED를 지원 안 함",
                 "→  ActiveX로 설치해서 해결"]:
        draw.text((80, y), line, fill=T_BODY, font=f)
        y += 50

    y += 25
    draw.text((80, y), "당시에는", fill=T_DARK, font=font(44, "bold"))
    y += 58
    draw.text((80, y), "합리적인 선택이었다", fill=A_MINT, font=font(44, "bold"))

    y += 85
    rounded_box(draw, (60, y, W - 60, y + 120), fill="#FFF5E8", radius=16, border="#E8C080")
    accent_line(draw, 60, y, 4, A_PEACH, width=120)
    draw.text((84, y + 16), "그런데 1년 후, 미국이 수출 제한을 풀었다.", fill="#A06020", font=font(30, "bold"))
    draw.text((84, y + 56), "한국은 이미 ActiveX 위에 인프라를 올려놓은 뒤였다.", fill="#A06020", font=font(28, "medium"))

    dots(draw, 3)
    img.save(f"{OUTPUT_DIR}/03_origin.png", quality=95)


def slide_04_law():
    img = gradient_bg(BG_ROSE, BG_CREAM)
    img = soft_glow(img, 540, 350, 450, (220, 100, 100), 22)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 80), "전자서명법 1999", A_ROSE)
    accent_line(draw, 80, 145, 50, A_ROSE)

    draw.text((80, 178), "법 한 줄이", fill=T_DARK, font=font(66, "bold"))
    draw.text((80, 265), "21년간", fill=A_SOFT_RED, font=font(66, "bold"))
    draw.text((80, 352), "인터넷을 가뒀다", fill=A_SOFT_RED, font=font(66, "bold"))

    y = 470
    f = font(30, "medium")
    items = [
        "공인인증서 = PKI 인증서만 법적 효력",
        "공인인증서 → ActiveX 필수",
        "ActiveX → IE에서만 작동",
        "→ 모든 금융·공공 = Internet Explorer 전용",
        "→ Chrome, Safari, Mac, Linux 전부 불가",
    ]
    for item in items:
        draw.text((80, y), item, fill=T_BODY, font=f)
        y += 46

    y += 25
    rounded_box(draw, (60, y, W - 60, y + 50), fill="#FFF0F0", radius=10, border="#E0B0B0")
    draw.text((80, y + 12), "이 법은 2020년 12월에야 폐지됐다", fill=T_MUTED, font=font(26, "semibold"))

    dots(draw, 4)
    img.save(f"{OUTPUT_DIR}/04_law.png", quality=95)


def slide_05_privatekey():
    img = gradient_bg(BG_WARM_WHITE, BG_LAVENDER)
    img = soft_glow(img, 270, 550, 300, (220, 100, 110), 20)
    img = soft_glow(img, 810, 550, 300, (80, 200, 140), 20)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 80), "핵심 차이", A_LAVENDER)
    accent_line(draw, 80, 145, 50, A_LAVENDER)

    draw.text((80, 178), "다른 나라에는", fill=T_DARK, font=font(58, "bold"))
    draw.text((80, 258), "사용자 개인키가", fill=T_DARK, font=font(58, "bold"))
    draw.text((80, 338), "없다", fill=A_SOFT_RED, font=font(58, "bold"))

    y = 440
    bh = 230
    # Korea
    rounded_box(draw, (60, y, 520, y + bh), fill="#FFF0EE", radius=16, border="#E8BBBB")
    draw.text((80, y + 16), "한국 (1999년)", fill=A_SOFT_RED, font=font(28, "bold"))
    draw.text((80, y + 54), "사용자가 개인키를 파일로 보관", fill=T_BODY, font=font(24, "regular"))
    draw.text((80, y + 86), "분실, 유출, 갱신 = 사용자 책임", fill=T_BODY, font=font(24, "regular"))
    draw.text((80, y + 130), "결국 비밀번호 수준", fill=A_SOFT_RED, font=font(27, "bold"))
    draw.text((80, y + 165), "보안으로 전락", fill=A_SOFT_RED, font=font(27, "bold"))

    # Global
    rounded_box(draw, (560, y, W - 60, y + bh), fill="#EEFAF2", radius=16, border="#B8DCC8")
    draw.text((580, y + 16), "글로벌", fill=A_MINT, font=font(28, "bold"))
    draw.text((580, y + 54), "서버 로그 + 다중인증으로 해결", fill=T_BODY, font=font(24, "regular"))
    draw.text((580, y + 86), "사용자에게 개인키를 줄 이유 없음", fill=T_BODY, font=font(24, "regular"))
    draw.text((580, y + 130), "잃어버릴 것 없음", fill=A_MINT, font=font(27, "bold"))
    draw.text((580, y + 165), "관리할 것 없음", fill=A_MINT, font=font(27, "bold"))

    dots(draw, 5)
    img.save(f"{OUTPUT_DIR}/05_privatekey.png", quality=95)


def slide_06_parking():
    img = gradient_bg(BG_SAGE, BG_WARM_WHITE)
    img = soft_glow(img, 540, 500, 400, (100, 180, 120), 20)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 80), "세대 비교", A_SAGE)
    accent_line(draw, 80, 145, 50, A_SAGE)

    draw.text((80, 175), "한국 주차장은 3세대", fill=T_DARK, font=font(50, "bold"))
    draw.text((80, 242), "한국 은행은 1세대", fill=A_SOFT_RED, font=font(50, "bold"))

    y = 335
    rounded_box(draw, (60, y, W - 60, y + 48), fill=A_SAGE, radius=8)
    hf = font(24, "bold")
    draw.text((80, y + 12), "세대", fill=T_WHITE, font=hf)
    draw.text((210, y + 12), "주차장", fill=T_WHITE, font=hf)
    draw.text((460, y + 12), "한국 금융", fill=T_WHITE, font=hf)
    draw.text((750, y + 12), "글로벌 금융", fill=T_WHITE, font=hf)

    rows = [
        ("1세대", "물리 주차권", "공인인증서(USB)", "비밀번호", False),
        ("2세대", "앱 주차권", "카카오/PASS", "비밀번호+MFA", False),
        ("3세대", "번호판 자동인식", "아직 2세대 멈춤", "FIDO2/패스키", True),
    ]
    cf = font(24, "regular")
    cbf = font(24, "bold")
    for i, (gen, park, kr, gl, hl) in enumerate(rows):
        ry = y + 60 + i * 58
        draw.line((60, ry, W - 60, ry), fill="#C0D0C0", width=1)
        draw.text((80, ry + 14), gen, fill=A_MINT if hl else T_DARK, font=cbf)
        draw.text((210, ry + 14), park, fill=T_BODY, font=cf)
        draw.text((460, ry + 14), kr, fill=A_SOFT_RED if hl else T_BODY, font=cbf if hl else cf)
        draw.text((750, ry + 14), gl, fill=T_BODY, font=cf)

    y2 = y + 250
    draw.text((80, y2), "같은 나라에서", fill=T_DARK, font=font(38, "bold"))
    y2 += 52
    draw.text((80, y2), "주차장은 번호판 자동인식인데", fill=T_DARK, font=font(38, "bold"))
    y2 += 52
    draw.text((80, y2), "은행은 아직 1999년에 멈춰있다", fill=A_SOFT_RED, font=font(38, "bold"))

    y3 = y2 + 75
    rounded_box(draw, (60, y3, W - 60, y3 + 60), fill="#F0FAF2", radius=12, border="#B0D8B8")
    draw.text((80, y3 + 15), "같은 기술 철학을 은행에 적용하면 된다. 새로 발명할 것이 없다.", fill=A_SAGE, font=font(26, "semibold"))

    dots(draw, 6)
    img.save(f"{OUTPUT_DIR}/06_parking.png", quality=95)


def slide_07_vishing():
    """Merged: 보이스피싱 + 보안프로그램이 못 막는 이유"""
    img = gradient_bg(BG_CORAL_DEEP, (180, 60, 55))
    img = soft_glow(img, 200, 200, 400, (255, 200, 150), 25)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 75), "보이스피싱", "#8B2020")

    draw.text((80, 140), "1조", fill=T_WHITE, font=font(100, "bold"))
    draw.text((80, 260), "965억 원", fill=T_WHITE, font=font(80, "bold"))

    draw.text((80, 370), "2023년 연간 피해액  |  하루 평균 30억 원", fill="#FFD0C8", font=font(28, "medium"))

    y = 430
    accent_line(draw, 80, y, W - 160, "#FFFFFF", width=1)
    y += 22
    steps = ["1. 전화가 온다 \"검찰입니다\"",
             "2. 피해자가 속는다",
             "3. 피해자가 직접 돈을 보낸다"]
    for s in steps:
        draw.text((100, y), s, fill="#FFD0C8", font=font(30, "medium"))
        y += 44

    y += 15
    draw.text((80, y), "핵심: 피해자가 속아서", fill=T_WHITE, font=font(36, "bold"))
    y += 48
    draw.text((80, y), "자기 손으로 직접 하는 것이다", fill=A_WARM_YELLOW, font=font(36, "bold"))

    y += 60
    accent_line(draw, 80, y, W - 160, "#FFFFFF", width=1)
    y += 18
    draw.text((80, y), "키보드 보안, 방화벽, 공인인증서 —", fill="#FFD0C8", font=font(28, "semibold"))
    y += 40
    draw.text((80, y), "이 중 어느 것도 보이스피싱을 막지 못한다", fill=T_WHITE, font=font(32, "bold"))
    y += 45
    draw.text((80, y), "PC 보안프로그램으로 막을 수 있는 문제가 아니다", fill=A_WARM_YELLOW, font=font(28, "bold"))

    dots(draw, 7)
    img.save(f"{OUTPUT_DIR}/07_vishing.png", quality=95)


def slide_08_solution():
    """Merged: 샌드박스 + 서버 해결책"""
    img = gradient_bg(BG_MINT, BG_SAGE)
    img = soft_glow(img, 540, 500, 450, (80, 200, 140), 25)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 75), "진짜 해결책", A_MINT)
    accent_line(draw, 80, 140, 50, A_SAGE)

    draw.text((80, 165), "세계는 서버에서 막고", fill=T_DARK, font=font(50, "bold"))
    draw.text((80, 232), "한국은 PC에 깔라고 한다", fill=A_SOFT_RED, font=font(50, "bold"))

    # Two small boxes for contrast
    y = 320
    bh = 120
    rounded_box(draw, (60, y, 520, y + bh), fill="#FFF0EE", radius=12, border="#E8BBBB")
    draw.text((80, y + 14), "한국: ActiveX 방식", fill=A_SOFT_RED, font=font(26, "bold"))
    draw.text((80, y + 48), "웹사이트가 PC에 프로그램 설치", fill=T_BODY, font=font(24, "regular"))
    draw.text((80, y + 78), "보안의 벽이 없다", fill=A_SOFT_RED, font=font(24, "bold"))

    rounded_box(draw, (560, y, W - 60, y + bh), fill="#EEFAF2", radius=12, border="#B8DCC8")
    draw.text((580, y + 14), "세계: 샌드박스 방식", fill=A_MINT, font=font(26, "bold"))
    draw.text((580, y + 48), "브라우저 안에 격리", fill=T_BODY, font=font(24, "regular"))
    draw.text((580, y + 78), "PC에 접근 불가", fill=A_MINT, font=font(24, "bold"))

    # Solution table
    y2 = y + bh + 30
    rounded_box(draw, (60, y2, W - 60, y2 + 42), fill=A_SAGE, radius=8)
    hf = font(23, "bold")
    draw.text((80, y2 + 8), "효과 있는 대책", fill=T_WHITE, font=hf)
    draw.text((380, y2 + 8), "작동 방식", fill=T_WHITE, font=hf)
    draw.text((830, y2 + 8), "위치", fill=T_WHITE, font=hf)

    solutions = [
        ("이상거래탐지(FDS)", "이상 패턴 → 자동 차단", "은행 서버"),
        ("지연이체", "큰 금액 30분 후 실행", "은행 서버"),
        ("AI 통화 분석", "\"검찰\" 감지 → 경고", "통신사 서버"),
        ("패스키(FIDO2)", "지문/얼굴로 인증", "기기 보안칩"),
    ]
    cf = font(22, "regular")
    cbf = font(22, "semibold")
    for i, (name, desc, where) in enumerate(solutions):
        ry = y2 + 52 + i * 48
        draw.line((60, ry, W - 60, ry), fill="#C0D8C0", width=1)
        draw.text((80, ry + 10), name, fill=T_DARK, font=cbf)
        draw.text((380, ry + 10), desc, fill=T_BODY, font=cf)
        draw.text((830, ry + 10), where, fill=A_MINT, font=cbf)

    y3 = y2 + 52 + len(solutions) * 48 + 25
    draw.text((80, y3), "이 중 어느 것도", fill=T_DARK, font=font(40, "bold"))
    y3 += 54
    draw.text((80, y3), "PC에 프로그램을 설치할 필요가 없다", fill=A_MINT, font=font(40, "bold"))

    dots(draw, 8)
    img.save(f"{OUTPUT_DIR}/08_solution.png", quality=95)


def slide_09_ai():
    """AI 시대 + 클라이언트 다양성"""
    img = gradient_bg(BG_LAVENDER, BG_WARM_WHITE)
    img = soft_glow(img, 540, 300, 450, (160, 130, 220), 25)
    img = soft_glow(img, 200, 800, 300, (232, 150, 100), 18)
    draw = ImageDraw.Draw(img)

    pill_tag(draw, (80, 80), "AI 시대", A_LAVENDER)
    accent_line(draw, 80, 145, 50, A_LAVENDER)

    draw.text((80, 178), "AI 시대에", fill=T_DARK, font=font(62, "bold"))
    draw.text((80, 260), "왜 더 큰 문제가", fill=A_LAVENDER, font=font(62, "bold"))
    draw.text((80, 342), "되는가", fill=A_LAVENDER, font=font(62, "bold"))

    y = 450
    problems = [
        ("AI 에이전트가 은행 업무를 대신할 때", T_DARK, "bold"),
        ("\"프로그램 5개 설치\"를 AI가 할 수 있나?", A_SOFT_RED, "semibold"),
        ("", "", ""),
        ("AI 보이스피싱은 목소리까지 복제한다", T_DARK, "bold"),
        ("키보드 보안으로 막을 수 있는 영역이 아니다", A_SOFT_RED, "semibold"),
        ("", "", ""),
        ("윈도우가 아니면 은행 업무가 힘들고", T_DARK, "bold"),
        ("리눅스는 아예 불가 — 클라이언트 다양성에 역행", A_SOFT_RED, "semibold"),
        ("", "", ""),
        ("글로벌 AI 서비스가 한국 결제를 붙일 수 없다", T_DARK, "bold"),
        ("한국만의 독자 규격이 AI 생태계를 차단한다", A_SOFT_RED, "semibold"),
    ]
    for text, color, weight in problems:
        if text:
            draw.text((100, y), text, fill=color, font=font(26, weight))
            y += 38
        else:
            y += 14

    dots(draw, 9)
    img.save(f"{OUTPUT_DIR}/09_ai.png", quality=95)


def slide_10_cta():
    """Merged: 타이밍 + CTA"""
    img = gradient_bg(BG_CREAM, BG_PEACH)
    img = soft_glow(img, 540, 400, 500, (232, 180, 130), 25)
    img = soft_glow(img, 800, 200, 300, (100, 200, 160), 18)
    draw = ImageDraw.Draw(img)

    accent_line(draw, 80, 90, 60, A_CORAL)

    draw.text((80, 115), "1년만 늦게", fill=T_DARK, font=font(56, "bold"))
    draw.text((80, 188), "시작했으면", fill=T_DARK, font=font(56, "bold"))
    draw.text((80, 275), "SEED도 ActiveX도", fill=A_CORAL, font=font(52, "bold"))
    draw.text((80, 345), "공인인증서도", fill=A_CORAL, font=font(52, "bold"))
    draw.text((80, 415), "필요 없었다", fill=A_CORAL, font=font(52, "bold"))

    y = 510
    draw.text((80, y), "그런데 지금이 최적의 타이밍이다", fill=T_DARK, font=font(36, "bold"))

    y += 60
    reasons = [
        ("01", "공인인증서 폐지(2020)로 법적 장벽 제거", A_MINT),
        ("02", "FIDO2/패스키가 모든 기기에 내장 완료", A_LAVENDER),
        ("03", "AI 시대 전환에 글로벌 호환 필수", A_PEACH),
    ]
    for num, text, color in reasons:
        draw.text((80, y), num, fill=color, font=font(34, "bold"))
        draw.text((145, y + 3), text, fill=T_BODY, font=font(28, "medium"))
        y += 50

    y += 25
    draw.line((80, y, W - 80, y), fill="#D8C8B8", width=1)
    y += 20
    draw.text((80, y), "25년의 기술 부채를", fill=T_DARK, font=font(46, "bold"))
    y += 60
    draw.text((80, y), "이제는 청산할 때다", fill=A_CORAL, font=font(46, "bold"))

    y += 80
    draw.text((80, y), "유호현 · (주)옥소폴리틱스 대표", fill=T_MUTED, font=font(24, "medium"))
    y += 35
    draw.text((80, y), "국가인공지능전략위원회 발표자료  |  2026년 3월", fill="#999999", font=font(22, "regular"))

    dots(draw, 10)
    img.save(f"{OUTPUT_DIR}/10_cta.png", quality=95)


if __name__ == "__main__":
    funcs = [
        slide_01_cover, slide_02_problem, slide_03_origin, slide_04_law,
        slide_05_privatekey, slide_06_parking, slide_07_vishing,
        slide_08_solution, slide_09_ai, slide_10_cta,
    ]
    print(f"Generating {len(funcs)} slides (v4 spring)...")
    for i, fn in enumerate(funcs, 1):
        fn()
        print(f"  {i}/{len(funcs)} {fn.__name__}")
    print(f"\nDone! → {OUTPUT_DIR}/")
