#!/usr/bin/env python3
"""Instagram carousel v3 - 한국 보안의 갈라파고스. Enhanced design."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

W, H = 1080, 1080
FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUTPUT_DIR = "/Users/will_ryu/workspace/personal/korean_it/결제보안/instagram_v3"
TOTAL = 12

# Font indices: 0=Regular, 2=Medium, 4=SemiBold, 6=Bold, 8=Light, 10=Heavy(if exists)
def font(size, weight="bold"):
    idx = {"regular": 0, "medium": 2, "semibold": 4, "bold": 6, "light": 8}
    return ImageFont.truetype(FONT_PATH, size, index=idx.get(weight, 6))


os.makedirs(OUTPUT_DIR, exist_ok=True)


# ── Gradient helpers ──

def lerp_color(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def gradient_bg(c1, c2, direction="vertical"):
    img = Image.new("RGB", (W, H))
    pixels = img.load()
    for y in range(H):
        for x in range(W):
            t = y / H if direction == "vertical" else x / W
            pixels[x, y] = lerp_color(c1, c2, t)
    return img


def radial_glow(img, cx, cy, radius, color, alpha=60):
    """Add a soft radial glow on the image."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -2):
        a = int(alpha * (r / radius) ** 0.5 * (1 - r / radius) ** 0.3)
        if a < 1:
            continue
        c = color + (a,)
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=c)
    img_rgba = img.convert("RGBA")
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    return img_rgba.convert("RGB")


def draw_accent_line(draw, x, y, length, color, width=4):
    draw.rounded_rectangle((x, y, x + length, y + width), radius=2, fill=color)


def draw_tag(draw, pos, text, bg_color, text_color="#FFFFFF"):
    f = font(26, "semibold")
    bbox = f.getbbox(text)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    px, py = 18, 10
    x, y = pos
    draw.rounded_rectangle((x, y, x + tw + px * 2, y + th + py * 2), radius=24, fill=bg_color)
    draw.text((x + px, y + py - 2), text, fill=text_color, font=f)
    return y + th + py * 2


def draw_dots(draw, current, total):
    dot_r = 5
    gap = 18
    total_w = total * dot_r * 2 + (total - 1) * gap
    sx = (W - total_w) // 2
    y = H - 48
    for i in range(total):
        x = sx + i * (dot_r * 2 + gap)
        color = "#FFFFFF" if i == current - 1 else "#3A4A60"
        draw.ellipse((x, y, x + dot_r * 2, y + dot_r * 2), fill=color)


# ── Color palettes ──
C_DARK1 = (12, 18, 30)
C_DARK2 = (20, 30, 55)
C_NAVY1 = (15, 25, 50)
C_NAVY2 = (30, 50, 90)
C_RED1 = (160, 30, 30)
C_RED2 = (100, 15, 15)
C_BLUE_GLOW = (80, 160, 255)
C_GREEN_GLOW = (80, 220, 140)
C_RED_GLOW = (255, 80, 80)
C_ORANGE_GLOW = (255, 160, 60)
C_PURPLE1 = (40, 20, 70)
C_PURPLE2 = (20, 12, 45)


def card_01_cover():
    img = gradient_bg(C_DARK1, C_DARK2)
    img = radial_glow(img, 200, 400, 500, C_BLUE_GLOW, alpha=35)
    img = radial_glow(img, 900, 800, 400, C_RED_GLOW, alpha=20)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 100), "국가인공지능전략위원회 발표자료", "#1E3A5F")

    draw_accent_line(draw, 80, 185, 60, "#64B5F6")

    y = 210
    draw.text((80, y), "한국 보안의", fill="#FFFFFF", font=font(88, "bold"))
    y += 110
    draw.text((80, y), "갈라파고스", fill="#FFFFFF", font=font(88, "bold"))

    y += 150
    draw.text((80, y), "어디서부터", fill="#64B5F6", font=font(72, "bold"))
    y += 95
    draw.text((80, y), "잘못됐나", fill="#64B5F6", font=font(72, "bold"))

    y += 140
    draw.text((80, y), "ActiveX에서 AI까지 — 세계와 다른 길을 걸은 25년", fill="#8899AA", font=font(30, "regular"))

    y += 80
    draw.text((80, y), "유호현 · (주)옥소폴리틱스 대표", fill="#667788", font=font(28, "medium"))
    y += 42
    draw.text((80, y), "2026년 3월", fill="#556677", font=font(26, "regular"))

    draw_dots(draw, 1, TOTAL)
    img.save(f"{OUTPUT_DIR}/01_cover.png", quality=95)


def card_02_problem():
    img = gradient_bg(C_DARK1, C_NAVY2)
    img = radial_glow(img, 540, 300, 450, C_GREEN_GLOW, alpha=25)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "25년의 역사", "#1B5E20")
    draw_accent_line(draw, 80, 140, 50, "#66BB6A")

    draw.text((80, 170), "1999년, 한국은", fill="#FFFFFF", font=font(62, "bold"))
    draw.text((80, 250), "세계 최고의", fill="#66BB6A", font=font(62, "bold"))
    draw.text((80, 330), "IT 강국이었다", fill="#66BB6A", font=font(62, "bold"))

    # Big stats
    y = 440
    draw.text((80, y), "초고속 인터넷 보급률", fill="#8899AA", font=font(28, "regular"))
    draw.text((80, y + 38), "세계 1위", fill="#A5D6A7", font=font(52, "bold"))
    draw.text((80, y + 110), "UN 전자정부 순위", fill="#8899AA", font=font(28, "regular"))
    draw.text((80, y + 148), "3회 연속 세계 1위", fill="#A5D6A7", font=font(52, "bold"))

    # Divider
    y2 = y + 240
    draw.line((80, y2, W - 80, y2), fill="#2A3A55", width=1)

    y2 += 30
    draw.text((80, y2), "그런데 2026년,", fill="#FFFFFF", font=font(44, "bold"))
    y2 += 60
    draw.text((80, y2), "은행 접속하려면", fill="#FFFFFF", font=font(44, "bold"))
    y2 += 60
    draw.text((80, y2), "프로그램 5개를 깔아야 한다", fill="#EF5350", font=font(44, "bold"))

    draw_dots(draw, 2, TOTAL)
    img.save(f"{OUTPUT_DIR}/02_problem.png", quality=95)


def card_03_origin():
    img = gradient_bg(C_DARK2, C_DARK1)
    img = radial_glow(img, 150, 600, 400, C_ORANGE_GLOW, alpha=25)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "1999년", "#E65100")
    draw_accent_line(draw, 80, 140, 50, "#FFB74D")

    draw.text((80, 175), "미국이 암호화", fill="#FFFFFF", font=font(60, "bold"))
    draw.text((80, 255), "수출을 금지했다", fill="#FFFFFF", font=font(60, "bold"))

    y = 370
    f_body = font(34, "medium")
    steps = [
        ("128비트 SSL을 쓸 수 없었던 한국", "#9AA8B8"),
        ("→  SEED 암호화를 직접 개발", "#9AA8B8"),
        ("→  브라우저가 SEED를 지원 안 함", "#9AA8B8"),
        ("→  ActiveX로 설치해서 해결", "#9AA8B8"),
    ]
    for text, color in steps:
        draw.text((80, y), text, fill=color, font=f_body)
        y += 52

    y += 30
    draw.text((80, y), "당시에는", fill="#FFFFFF", font=font(46, "bold"))
    y += 60
    draw.text((80, y), "합리적인 선택이었다", fill="#66BB6A", font=font(46, "bold"))

    # Warning box
    y += 100
    draw.rounded_rectangle((60, y, W - 60, y + 130), radius=16, fill="#1A2744")
    draw_accent_line(draw, 60, y, 4, "#FFD54F", width=130)
    draw.text((84, y + 18), "그런데 1년 후, 미국이 수출 제한을 풀었다.", fill="#FFD54F", font=font(32, "bold"))
    draw.text((84, y + 60), "한국은 이미 ActiveX 위에 전체 인프라를 올려놓은 뒤였다.", fill="#FFD54F", font=font(30, "medium"))

    draw_dots(draw, 3, TOTAL)
    img.save(f"{OUTPUT_DIR}/03_origin.png", quality=95)


def card_04_law():
    img = gradient_bg(C_DARK1, C_DARK2)
    img = radial_glow(img, 540, 350, 500, C_RED_GLOW, alpha=30)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "전자서명법 1999", "#B71C1C")
    draw_accent_line(draw, 80, 140, 50, "#EF5350")

    # Giant text
    draw.text((80, 175), "법 한 줄이", fill="#FFFFFF", font=font(68, "bold"))
    draw.text((80, 265), "21년간", fill="#EF5350", font=font(68, "bold"))
    draw.text((80, 355), "인터넷을 가뒀다", fill="#EF5350", font=font(68, "bold"))

    y = 480
    items = [
        "공인인증서 = PKI 인증서만 법적 효력",
        "공인인증서 → ActiveX 필수",
        "ActiveX → IE에서만 작동",
        "→ 모든 금융·공공 = IE 전용",
        "→ Chrome, Safari, Mac, Linux 불가",
    ]
    f = font(32, "medium")
    for item in items:
        draw.text((80, y), item, fill="#9AA8B8", font=f)
        y += 48

    y += 30
    draw.rounded_rectangle((60, y, W - 60, y + 55), radius=12, fill="#1A1A2A")
    draw.text((80, y + 12), "이 법은 2020년 12월에야 폐지됐다.", fill="#78909C", font=font(28, "semibold"))

    draw_dots(draw, 4, TOTAL)
    img.save(f"{OUTPUT_DIR}/04_law.png", quality=95)


def card_05_privatekey():
    img = gradient_bg(C_DARK2, C_DARK1)
    img = radial_glow(img, 270, 550, 350, C_RED_GLOW, alpha=25)
    img = radial_glow(img, 810, 550, 350, C_GREEN_GLOW, alpha=25)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "핵심 차이", "#0D47A1")
    draw_accent_line(draw, 80, 140, 50, "#64B5F6")

    draw.text((80, 175), "다른 나라에는", fill="#FFFFFF", font=font(60, "bold"))
    draw.text((80, 258), "사용자 개인키가", fill="#FFFFFF", font=font(60, "bold"))
    draw.text((80, 341), "없다", fill="#EF5350", font=font(60, "bold"))

    # Two boxes
    y = 450
    bh = 240
    # Korea
    draw.rounded_rectangle((60, y, 520, y + bh), radius=16, fill="#2A1515")
    draw_accent_line(draw, 60, y, 460, "#EF5350", width=3)
    draw.text((80, y + 20), "한국 (1999년)", fill="#EF5350", font=font(30, "bold"))
    draw.text((80, y + 62), "사용자가 개인키를 파일로 보관", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((80, y + 96), "분실, 유출, 갱신 = 사용자 책임", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((80, y + 145), "결국 비밀번호 수준 보안", fill="#EF9A9A", font=font(28, "bold"))
    draw.text((80, y + 185), "으로 전락", fill="#EF9A9A", font=font(28, "bold"))

    # Global
    draw.rounded_rectangle((560, y, W - 60, y + bh), radius=16, fill="#152A15")
    draw_accent_line(draw, 560, y, 460, "#66BB6A", width=3)
    draw.text((580, y + 20), "글로벌", fill="#66BB6A", font=font(30, "bold"))
    draw.text((580, y + 62), "서버 로그 + 다중인증으로 해결", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((580, y + 96), "사용자에게 개인키를 줄 이유 없음", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((580, y + 145), "잃어버릴 것 없음", fill="#A5D6A7", font=font(28, "bold"))
    draw.text((580, y + 185), "관리할 것 없음", fill="#A5D6A7", font=font(28, "bold"))

    draw_dots(draw, 5, TOTAL)
    img.save(f"{OUTPUT_DIR}/05_privatekey.png", quality=95)


def card_06_parking():
    img = gradient_bg(C_NAVY1, C_DARK2)
    img = radial_glow(img, 540, 500, 450, C_BLUE_GLOW, alpha=20)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "세대 비교", "#1565C0")
    draw_accent_line(draw, 80, 140, 50, "#64B5F6")

    draw.text((80, 170), "한국 주차장은 3세대", fill="#FFFFFF", font=font(52, "bold"))
    draw.text((80, 240), "한국 은행은 1세대", fill="#EF5350", font=font(52, "bold"))

    # Table
    y = 340
    draw.rounded_rectangle((60, y, W - 60, y + 48), radius=8, fill="#1A2744")
    hf = font(26, "bold")
    draw.text((80, y + 10), "세대", fill="#64B5F6", font=hf)
    draw.text((220, y + 10), "주차장", fill="#64B5F6", font=hf)
    draw.text((480, y + 10), "한국 금융", fill="#64B5F6", font=hf)
    draw.text((770, y + 10), "글로벌 금융", fill="#64B5F6", font=hf)

    rows = [
        ("1세대", "물리 주차권", "공인인증서(USB)", "비밀번호", False),
        ("2세대", "앱 주차권", "카카오/PASS", "비밀번호+MFA", False),
        ("3세대", "번호판 자동인식", "아직 2세대 멈춤", "FIDO2/패스키", True),
    ]
    cf = font(26, "regular")
    cbf = font(26, "bold")
    for i, (gen, park, kr, gl, highlight) in enumerate(rows):
        ry = y + 60 + i * 60
        draw.line((60, ry, W - 60, ry), fill="#1E2E45", width=1)
        gc = "#66BB6A" if highlight else "#FFFFFF"
        kc = "#EF5350" if highlight else "#9AA8B8"
        draw.text((80, ry + 12), gen, fill=gc, font=cbf)
        draw.text((220, ry + 12), park, fill="#9AA8B8", font=cf)
        draw.text((480, ry + 12), kr, fill=kc, font=cbf if highlight else cf)
        draw.text((770, ry + 12), gl, fill="#9AA8B8", font=cf)

    y2 = y + 260
    draw.text((80, y2), "같은 나라에서", fill="#FFFFFF", font=font(40, "bold"))
    y2 += 56
    draw.text((80, y2), "주차장은 번호판 자동인식인데", fill="#FFFFFF", font=font(40, "bold"))
    y2 += 56
    draw.text((80, y2), "은행은 아직 1999년에 멈춰있다", fill="#EF5350", font=font(40, "bold"))

    y3 = y2 + 80
    draw.rounded_rectangle((60, y3, W - 60, y3 + 65), radius=12, fill="#1A2744")
    draw.text((80, y3 + 16), "같은 기술 철학을 은행에 적용하면 된다. 새로 발명할 것이 없다.", fill="#FFD54F", font=font(28, "semibold"))

    draw_dots(draw, 6, TOTAL)
    img.save(f"{OUTPUT_DIR}/06_parking.png", quality=95)


def card_07_vishing():
    img = gradient_bg(C_RED1, C_RED2)
    img = radial_glow(img, 200, 250, 400, (255, 200, 150), alpha=30)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "보이스피싱", "#7F0000")

    # Giant number
    draw.text((80, 150), "1조", fill="#FFFFFF", font=font(110, "bold"))
    draw.text((80, 280), "965억 원", fill="#FFFFFF", font=font(90, "bold"))

    draw.text((80, 400), "2023년 연간 피해액  |  하루 평균 30억 원", fill="#FFCDD2", font=font(30, "medium"))

    # Steps
    y = 480
    draw_accent_line(draw, 80, y, W - 160, "#FFFFFF", width=1)
    y += 25
    draw.text((80, y), "보이스피싱은 이렇게 작동한다", fill="#FFFFFF", font=font(40, "bold"))
    y += 60
    steps = ["1. 전화가 온다 \"검찰입니다\"", "2. 피해자가 속는다", "3. 피해자가 직접 돈을 보낸다"]
    for s in steps:
        draw.text((100, y), s, fill="#FFCDD2", font=font(32, "medium"))
        y += 48

    y += 25
    draw.text((80, y), "핵심: 피해자가 속아서", fill="#FFFFFF", font=font(38, "bold"))
    y += 52
    draw.text((80, y), "자기 손으로 직접 하는 것이다", fill="#FFD54F", font=font(38, "bold"))

    y += 65
    draw.text((80, y), "PC 보안프로그램으로 막을 수 있는 문제가 아니다", fill="#FFCDD2", font=font(30, "semibold"))

    draw_dots(draw, 7, TOTAL)
    img.save(f"{OUTPUT_DIR}/07_vishing.png", quality=95)


def card_08_sandbox():
    img = gradient_bg(C_DARK1, C_DARK2)
    img = radial_glow(img, 270, 480, 350, C_RED_GLOW, alpha=25)
    img = radial_glow(img, 810, 480, 350, C_GREEN_GLOW, alpha=25)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "정반대 방향", "#4A148C")
    draw_accent_line(draw, 80, 140, 50, "#CE93D8")

    draw.text((80, 170), "세계는 브라우저를 닫고", fill="#FFFFFF", font=font(52, "bold"))
    draw.text((80, 242), "한국은 브라우저를 열었다", fill="#EF5350", font=font(52, "bold"))

    y = 350
    bh = 260
    # ActiveX
    draw.rounded_rectangle((60, y, 520, y + bh), radius=16, fill="#2A1515")
    draw_accent_line(draw, 60, y, 460, "#EF5350", width=3)
    draw.text((80, y + 18), "ActiveX 방식 (한국)", fill="#EF5350", font=font(30, "bold"))
    draw.text((80, y + 62), "웹사이트가 PC에 프로그램을", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((80, y + 94), "설치하고 실행할 수 있다", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((80, y + 148), "PC의 모든 것에 접근 가능", fill="#FFFFFF", font=font(28, "bold"))
    draw.text((80, y + 188), "보안의 벽이 없다", fill="#EF9A9A", font=font(28, "bold"))

    # Sandbox
    draw.rounded_rectangle((560, y, W - 60, y + bh), radius=16, fill="#152A15")
    draw_accent_line(draw, 560, y, 460, "#66BB6A", width=3)
    draw.text((580, y + 18), "샌드박스 방식 (세계)", fill="#66BB6A", font=font(30, "bold"))
    draw.text((580, y + 62), "웹사이트는 브라우저라는", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((580, y + 94), "상자 안에 갇혀 있다", fill="#9AA8B8", font=font(26, "regular"))
    draw.text((580, y + 148), "PC에 접근 불가", fill="#FFFFFF", font=font(28, "bold"))
    draw.text((580, y + 188), "보안의 벽이 있다", fill="#A5D6A7", font=font(28, "bold"))

    y2 = y + bh + 40
    draw.text((80, y2), "세계:", fill="#66BB6A", font=font(32, "bold"))
    draw.text((170, y2), "\"프로그램 설치 자체가 위험하다\"", fill="#9AA8B8", font=font(32, "medium"))
    y2 += 48
    draw.text((80, y2), "한국:", fill="#EF5350", font=font(32, "bold"))
    draw.text((170, y2), "\"보안을 위해 프로그램을 더 깔아라\"", fill="#9AA8B8", font=font(32, "medium"))

    y2 += 65
    draw.text((80, y2), "→ 정반대였다", fill="#FFD54F", font=font(42, "bold"))

    draw_dots(draw, 8, TOTAL)
    img.save(f"{OUTPUT_DIR}/08_sandbox.png", quality=95)


def card_09_solution():
    img = gradient_bg(C_DARK1, C_NAVY1)
    img = radial_glow(img, 540, 600, 450, C_GREEN_GLOW, alpha=25)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "진짜 해결책", "#1B5E20")
    draw_accent_line(draw, 80, 140, 50, "#66BB6A")

    draw.text((80, 175), "효과 있는 대책은", fill="#FFFFFF", font=font(54, "bold"))
    draw.text((80, 250), "전부 서버에서 한다", fill="#66BB6A", font=font(54, "bold"))

    y = 360
    draw.rounded_rectangle((60, y, W - 60, y + 45), radius=8, fill="#1A2744")
    hf = font(25, "bold")
    draw.text((80, y + 8), "대책", fill="#64B5F6", font=hf)
    draw.text((370, y + 8), "작동 방식", fill="#64B5F6", font=hf)
    draw.text((850, y + 8), "위치", fill="#64B5F6", font=hf)

    solutions = [
        ("이상거래탐지(FDS)", "평소와 다른 패턴 → 자동 차단", "은행 서버"),
        ("지연이체", "큰 금액 30분~1시간 후 실행", "은행 서버"),
        ("AI 통화 분석", "\"검찰\" \"계좌 동결\" 감지 → 경고", "통신사 서버"),
        ("다중인증(MFA)", "비밀번호 + 생체인증", "서버 + 기기"),
        ("패스키(FIDO2)", "지문/얼굴로 자동 사용", "기기 보안칩"),
    ]
    cf = font(24, "regular")
    cbf = font(24, "semibold")
    for i, (name, desc, where) in enumerate(solutions):
        ry = y + 58 + i * 55
        draw.line((60, ry, W - 60, ry), fill="#1E2E45", width=1)
        draw.text((80, ry + 12), name, fill="#FFFFFF", font=cbf)
        draw.text((370, ry + 12), desc, fill="#9AA8B8", font=cf)
        draw.text((850, ry + 12), where, fill="#66BB6A", font=cbf)

    y2 = y + 58 + len(solutions) * 55 + 40
    draw.text((80, y2), "이 중 어느 것도", fill="#FFFFFF", font=font(46, "bold"))
    y2 += 62
    draw.text((80, y2), "사용자 PC에 프로그램을", fill="#FFFFFF", font=font(46, "bold"))
    y2 += 62
    draw.text((80, y2), "설치할 필요가 없다", fill="#66BB6A", font=font(46, "bold"))

    draw_dots(draw, 9, TOTAL)
    img.save(f"{OUTPUT_DIR}/09_solution.png", quality=95)


def card_10_ai():
    """NEW: AI 시대에 왜 더 큰 문제가 되는가"""
    img = gradient_bg(C_PURPLE1, C_PURPLE2)
    img = radial_glow(img, 540, 300, 500, (180, 100, 255), alpha=30)
    img = radial_glow(img, 200, 800, 350, C_ORANGE_GLOW, alpha=20)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "AI 시대", "#6A1B9A")
    draw_accent_line(draw, 80, 140, 50, "#CE93D8")

    draw.text((80, 175), "AI 시대에", fill="#FFFFFF", font=font(64, "bold"))
    draw.text((80, 260), "왜 더 큰 문제가", fill="#CE93D8", font=font(64, "bold"))
    draw.text((80, 345), "되는가", fill="#CE93D8", font=font(64, "bold"))

    y = 460
    problems = [
        ("AI 에이전트가 은행 업무를 대신할 때", "#FFFFFF", "bold"),
        ("\"프로그램 5개 설치\"를 AI가 할 수 있나?", "#EF9A9A", "bold"),
        ("", "", ""),
        ("AI 보이스피싱은 목소리까지 복제한다", "#FFFFFF", "bold"),
        ("키보드 보안으로 막을 수 있는 영역이 아니다", "#EF9A9A", "bold"),
        ("", "", ""),
        ("윈도우가 아니면 은행 업무가 힘들고", "#FFFFFF", "bold"),
        ("리눅스는 아예 불가 — 클라이언트 다양성에 역행", "#EF9A9A", "bold"),
        ("", "", ""),
        ("글로벌 AI 서비스가 한국 결제를 붙일 수 없다", "#FFFFFF", "bold"),
        ("한국만의 독자 규격이 AI 생태계를 차단한다", "#EF9A9A", "bold"),
    ]

    for text, color, weight in problems:
        if text:
            draw.text((100, y), text, fill=color, font=font(27, weight))
            y += 40
        else:
            y += 15

    y += 25
    draw.rounded_rectangle((60, y, W - 60, y + 65), radius=12, fill="#1A1030")
    draw.text((80, y + 16), "ActiveX의 유산이 AI 전환의 가장 큰 걸림돌이 되고 있다", fill="#FFD54F", font=font(27, "semibold"))

    draw_dots(draw, 10, TOTAL)
    img.save(f"{OUTPUT_DIR}/10_ai.png", quality=95)


def card_11_timing():
    """NEW: 왜 지금이 좋은 타이밍인가"""
    img = gradient_bg((10, 30, 20), (15, 40, 30))
    img = radial_glow(img, 540, 400, 500, C_GREEN_GLOW, alpha=30)
    img = radial_glow(img, 900, 200, 300, C_BLUE_GLOW, alpha=20)
    draw = ImageDraw.Draw(img)

    draw_tag(draw, (80, 80), "왜 지금인가", "#2E7D32")
    draw_accent_line(draw, 80, 140, 50, "#66BB6A")

    draw.text((80, 175), "지금이", fill="#FFFFFF", font=font(64, "bold"))
    draw.text((80, 260), "최적의 타이밍인", fill="#66BB6A", font=font(64, "bold"))
    draw.text((80, 345), "3가지 이유", fill="#66BB6A", font=font(64, "bold"))

    y = 460
    reasons = [
        ("01", "공인인증서 폐지(2020)로 법적 장벽이 사라졌다", "규제 전환이 이미 시작됨"),
        ("02", "FIDO2/패스키가 모든 기기에 내장됐다", "기술이 이미 준비 완료"),
        ("03", "AI 시대 전환에 글로벌 호환이 필수가 됐다", "안 바꾸면 AI 생태계에서 배제"),
    ]

    for num, title, desc in reasons:
        # Number
        draw.text((80, y), num, fill="#66BB6A", font=font(42, "bold"))
        draw.text((160, y + 5), title, fill="#FFFFFF", font=font(30, "bold"))
        draw.text((160, y + 44), desc, fill="#78909C", font=font(26, "regular"))
        y += 105

    y += 15
    draw.rounded_rectangle((60, y, W - 60, y + 70), radius=12, fill="#0D2010")
    draw_accent_line(draw, 60, y, 4, "#66BB6A", width=70)
    draw.text((84, y + 18), "25년간 못 바꾼 것을 바꿀 조건이 처음으로 갖춰졌다", fill="#A5D6A7", font=font(28, "bold"))

    draw_dots(draw, 11, TOTAL)
    img.save(f"{OUTPUT_DIR}/11_timing.png", quality=95)


def card_12_cta():
    img = gradient_bg(C_NAVY1, C_NAVY2)
    img = radial_glow(img, 540, 400, 500, C_BLUE_GLOW, alpha=30)
    img = radial_glow(img, 200, 700, 300, C_ORANGE_GLOW, alpha=15)
    draw = ImageDraw.Draw(img)

    draw_accent_line(draw, 80, 130, 60, "#64B5F6")

    draw.text((80, 160), "1년만 늦게", fill="#FFFFFF", font=font(60, "bold"))
    draw.text((80, 240), "시작했으면", fill="#FFFFFF", font=font(60, "bold"))
    draw.text((80, 340), "SEED도 ActiveX도", fill="#64B5F6", font=font(56, "bold"))
    draw.text((80, 415), "공인인증서도", fill="#64B5F6", font=font(56, "bold"))
    draw.text((80, 490), "필요 없었다", fill="#64B5F6", font=font(56, "bold"))

    y = 590
    draw.text((80, y), "한국이 인터넷 강국이라서 세계보다 빨리 움직인 것이", fill="#8899AA", font=font(28, "medium"))
    y += 40
    draw.text((80, y), "역설적으로 갈라파고스의 원인이 됐다", fill="#8899AA", font=font(28, "medium"))

    y += 70
    draw_accent_line(draw, 80, y, W - 160, "#2A3A55", width=1)
    y += 25
    draw.text((80, y), "25년의 기술 부채를", fill="#FFFFFF", font=font(48, "bold"))
    y += 65
    draw.text((80, y), "이제는 청산할 때다", fill="#FFD54F", font=font(48, "bold"))

    y += 100
    draw.text((80, y), "유호현 · (주)옥소폴리틱스 대표", fill="#667788", font=font(26, "medium"))
    y += 38
    draw.text((80, y), "국가인공지능전략위원회 발표자료  |  2026년 3월", fill="#556677", font=font(24, "regular"))

    draw_dots(draw, 12, TOTAL)
    img.save(f"{OUTPUT_DIR}/12_cta.png", quality=95)


if __name__ == "__main__":
    funcs = [
        card_01_cover, card_02_problem, card_03_origin, card_04_law,
        card_05_privatekey, card_06_parking, card_07_vishing, card_08_sandbox,
        card_09_solution, card_10_ai, card_11_timing, card_12_cta,
    ]
    print(f"Generating {len(funcs)} Instagram carousel images (v3)...")
    for i, fn in enumerate(funcs, 1):
        fn()
        print(f"  {i}/{len(funcs)} {fn.__name__}")
    print(f"\nDone! → {OUTPUT_DIR}/")
