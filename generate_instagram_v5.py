#!/usr/bin/env python3
"""Instagram carousel v5 - 선동적/공감형. 10 slides, spring palette."""

from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUTPUT_DIR = "/Users/will_ryu/workspace/personal/korean_it/결제보안/instagram_v5"
TOTAL = 10

def font(size, weight="bold"):
    idx = {"regular": 0, "medium": 2, "semibold": 4, "bold": 6, "light": 8}
    return ImageFont.truetype(FONT_PATH, size, index=idx.get(weight, 6))

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Colors ──
BG_CREAM = (255, 251, 245)
BG_MINT = (235, 250, 245)
BG_PEACH = (255, 243, 235)
BG_LAVENDER = (242, 238, 252)
BG_WARM = (252, 249, 244)
BG_SAGE = (230, 242, 232)
BG_ROSE = (252, 235, 235)
BG_CORAL = (215, 85, 75)

T_BLACK = "#1A1A1A"
T_DARK = "#2A2A2A"
T_BODY = "#4A4A4A"
T_MUTED = "#888888"
T_WHITE = "#FFFFFF"

A_CORAL = "#E8706A"
A_MINT = "#2DAA78"
A_SAGE = "#5A9066"
A_LAVENDER = "#7B68B8"
A_PEACH = "#D88050"
A_ROSE = "#C85060"
A_RED = "#D44A4A"
A_YELLOW = "#D8B030"


def lerp(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))

def gradient(c1, c2):
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        for x in range(W):
            px[x, y] = lerp(c1, c2, y / H)
    return img

def glow(img, cx, cy, r, color, a=35):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for ri in range(r, 0, -3):
        ai = int(a * (1 - (ri / r) ** 1.5))
        if ai < 1: continue
        d.ellipse((cx-ri, cy-ri, cx+ri, cy+ri), fill=color+(ai,))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

def line(draw, x, y, length, color, w=4):
    draw.rounded_rectangle((x, y, x+length, y+w), radius=2, fill=color)

def tag(draw, pos, text, bg, fg="#FFFFFF"):
    f = font(24, "semibold")
    bb = f.getbbox(text)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    px, py = 20, 10
    x, y = pos
    draw.rounded_rectangle((x, y, x+tw+px*2, y+th+py*2), radius=24, fill=bg)
    draw.text((x+px, y+py-2), text, fill=fg, font=f)

def dots(draw, cur):
    r = 5; gap = 16
    tw = TOTAL*r*2 + (TOTAL-1)*gap
    sx = (W-tw)//2; y = H-46
    for i in range(TOTAL):
        x = sx + i*(r*2+gap)
        draw.ellipse((x, y, x+r*2, y+r*2), fill=T_BLACK if i==cur-1 else "#D0D0D0")

def box(draw, xy, fill, radius=16, border=None):
    draw.rounded_rectangle(xy, radius=radius, fill=fill)
    if border:
        draw.rounded_rectangle(xy, radius=radius, outline=border, width=2)


# ═══════════════════════════════════════

def s01():
    img = gradient(BG_CREAM, BG_PEACH)
    img = glow(img, 850, 300, 400, (232, 150, 120), 30)
    draw = ImageDraw.Draw(img)

    line(draw, 80, 120, 60, A_CORAL)

    draw.text((80, 150), "은행 접속하려면", fill=T_BLACK, font=font(72, "bold"))
    draw.text((80, 245), "프로그램", fill=A_CORAL, font=font(90, "bold"))
    draw.text((80, 358), "5개를 깔아라?", fill=A_CORAL, font=font(90, "bold"))

    y = 510
    draw.text((80, y), "세계 어느 나라도 이런 걸 요구하지 않는다", fill=T_BODY, font=font(32, "medium"))
    y += 55
    draw.text((80, y), "한국만 25년째 이러고 있다", fill=T_BODY, font=font(32, "medium"))

    y += 90
    draw.text((80, y), "어디서부터 잘못된 걸까?", fill=T_BLACK, font=font(40, "bold"))
    y += 55
    draw.text((80, y), "왜 아직도 안 바뀌는 걸까?", fill=T_BLACK, font=font(40, "bold"))

    y += 90
    draw.text((80, y), "← 넘겨서 확인하세요", fill=T_MUTED, font=font(28, "medium"))

    dots(draw, 1)
    img.save(f"{OUTPUT_DIR}/01.png", quality=95)


def s02():
    img = gradient(BG_MINT, BG_WARM)
    img = glow(img, 540, 350, 400, (80, 200, 140), 22)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 80), "1999년", A_MINT)
    line(draw, 80, 145, 50, A_SAGE)

    draw.text((80, 178), "한국은 원래", fill=T_DARK, font=font(56, "bold"))
    draw.text((80, 255), "세계 최고였다", fill=A_MINT, font=font(64, "bold"))

    y = 370
    draw.text((80, y), "초고속 인터넷", fill=T_MUTED, font=font(28, "regular"))
    draw.text((80, y+36), "세계 1위", fill=A_SAGE, font=font(56, "bold"))
    draw.text((80, y+108), "UN 전자정부", fill=T_MUTED, font=font(28, "regular"))
    draw.text((80, y+144), "3회 연속 세계 1위", fill=A_SAGE, font=font(56, "bold"))

    y2 = y + 245
    draw.line((80, y2, W-80, y2), fill="#C0D0C0", width=1)
    y2 += 30

    draw.text((80, y2), "그런데 너무 빨리 움직인 게 문제였다", fill=T_DARK, font=font(36, "bold"))
    y2 += 55
    draw.text((80, y2), "미국이 암호화 수출을 막던 시절,", fill=T_BODY, font=font(30, "medium"))
    y2 += 45
    draw.text((80, y2), "한국은 자체 암호화 + ActiveX로 해결했다", fill=T_BODY, font=font(30, "medium"))
    y2 += 50
    draw.text((80, y2), "1년 후 미국이 제한을 풀었지만", fill=A_RED, font=font(30, "bold"))
    y2 += 42
    draw.text((80, y2), "한국은 이미 돌아올 수 없었다", fill=A_RED, font=font(30, "bold"))

    dots(draw, 2)
    img.save(f"{OUTPUT_DIR}/02.png", quality=95)


def s03():
    img = gradient(BG_ROSE, BG_CREAM)
    img = glow(img, 540, 350, 450, (220, 100, 100), 22)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 80), "법으로 고정", A_ROSE)
    line(draw, 80, 145, 50, A_ROSE)

    draw.text((80, 178), "법 한 줄이", fill=T_BLACK, font=font(68, "bold"))
    draw.text((80, 268), "21년간 한국의", fill=A_RED, font=font(68, "bold"))
    draw.text((80, 358), "인터넷을 가뒀다", fill=A_RED, font=font(68, "bold"))

    y = 480
    f = font(34, "medium")
    draw.text((80, y), "1999년 전자서명법:", fill=T_DARK, font=font(34, "bold"))
    y += 55
    draw.text((80, y), "\"공인인증서만 법적 효력 있음\"", fill=T_BODY, font=f)
    y += 55
    draw.text((80, y), "공인인증서 → ActiveX 필수", fill=T_BODY, font=f)
    y += 48
    draw.text((80, y), "ActiveX → Internet Explorer에서만 작동", fill=T_BODY, font=f)

    y += 70
    draw.text((80, y), "Chrome 안 됨. Mac 안 됨.", fill=A_RED, font=font(36, "bold"))
    y += 50
    draw.text((80, y), "Linux 안 됨. 모바일 안 됨.", fill=A_RED, font=font(36, "bold"))

    y += 65
    draw.text((80, y), "이 법, 2020년에야 겨우 폐지됐다", fill=T_MUTED, font=font(28, "semibold"))

    dots(draw, 3)
    img.save(f"{OUTPUT_DIR}/03.png", quality=95)


def s04():
    img = gradient(BG_PEACH, BG_CREAM)
    img = glow(img, 200, 600, 350, (232, 160, 100), 22)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 80), "비교해보자", A_PEACH)
    line(draw, 80, 145, 50, A_PEACH)

    draw.text((80, 178), "외국에서 은행 이체하면", fill=T_DARK, font=font(48, "bold"))

    y = 270
    draw.text((80, y), "앱 열기 → 지문 찍기 → 끝", fill=A_MINT, font=font(44, "bold"))
    y += 60
    draw.text((80, y), "설치할 것: 없음", fill=A_MINT, font=font(36, "bold"))

    y += 80
    draw.line((80, y, W-80, y), fill="#D8C8B8", width=1)
    y += 30

    draw.text((80, y), "한국에서 은행 이체하면", fill=T_DARK, font=font(48, "bold"))
    y += 65
    items = [
        "1. 키보드 보안 프로그램 설치",
        "2. 방화벽 프로그램 설치",
        "3. 인증서 프로그램 설치",
        "4. IP 수집 프로그램 설치",
        "5. 설치 관리 프로그램 설치",
    ]
    for item in items:
        draw.text((100, y), item, fill=A_RED, font=font(32, "bold"))
        y += 46

    y += 15
    draw.text((80, y), "그리고 공동인증서 + OTP + 보안카드...", fill=T_BODY, font=font(30, "medium"))

    y += 60
    draw.text((80, y), "이걸 정상이라고 생각하는 나라는", fill=T_BLACK, font=font(36, "bold"))
    y += 48
    draw.text((80, y), "지구상에 한국밖에 없다", fill=A_RED, font=font(40, "bold"))

    dots(draw, 4)
    img.save(f"{OUTPUT_DIR}/04.png", quality=95)


def s05():
    """보이스피싱 - 이 프로그램들 소용없다"""
    img = gradient(BG_CORAL, (185, 65, 58))
    img = glow(img, 200, 200, 400, (255, 200, 150), 25)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 75), "충격적 사실", "#8B2020")

    draw.text((80, 135), "이 프로그램들", fill=T_WHITE, font=font(68, "bold"))
    draw.text((80, 225), "보이스피싱", fill=A_YELLOW, font=font(78, "bold"))
    draw.text((80, 325), "못 막는다", fill=A_YELLOW, font=font(78, "bold"))

    y = 440
    line(draw, 80, y, W-160, T_WHITE, 1)
    y += 22
    draw.text((80, y), "보이스피싱 피해액: 연간 1조 965억 원", fill="#FFD0C8", font=font(30, "medium"))

    y += 55
    draw.text((80, y), "사기범이 전화한다", fill=T_WHITE, font=font(34, "bold"))
    y += 45
    draw.text((80, y), "→ 피해자가 속는다", fill=T_WHITE, font=font(34, "bold"))
    y += 45
    draw.text((80, y), "→ 피해자가 직접 돈을 보낸다", fill=T_WHITE, font=font(34, "bold"))

    y += 60
    draw.text((80, y), "피해자가 직접 하는 건데", fill=T_WHITE, font=font(36, "bold"))
    y += 48
    draw.text((80, y), "키보드 보안 프로그램이", fill=A_YELLOW, font=font(36, "bold"))
    y += 48
    draw.text((80, y), "어떻게 막나?", fill=A_YELLOW, font=font(36, "bold"))

    y += 60
    draw.text((80, y), "현관문으로 도둑을 들이는데", fill="#FFD0C8", font=font(28, "semibold"))
    y += 38
    draw.text((80, y), "창문에 쇠창살 다는 격이다", fill="#FFD0C8", font=font(28, "semibold"))

    dots(draw, 5)
    img.save(f"{OUTPUT_DIR}/05.png", quality=95)


def s06():
    """그럼 이 프로그램들 왜 깔라고 하나"""
    img = gradient(BG_LAVENDER, BG_WARM)
    img = glow(img, 540, 400, 450, (160, 130, 220), 22)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 80), "진짜 이유", A_LAVENDER)
    line(draw, 80, 145, 50, A_LAVENDER)

    draw.text((80, 178), "그럼 왜", fill=T_BLACK, font=font(62, "bold"))
    draw.text((80, 260), "깔라고 하는 걸까?", fill=A_LAVENDER, font=font(62, "bold"))

    y = 380
    # Box 1
    box(draw, (60, y, W-60, y+140), fill="#F5F0FF", border="#D0C0E8")
    draw.text((80, y+15), "은행의 논리", fill=A_LAVENDER, font=font(28, "bold"))
    draw.text((80, y+52), "\"보안프로그램 설치하라고 했잖아요\"", fill=T_DARK, font=font(30, "bold"))
    draw.text((80, y+90), "→ 해킹당하면? 사용자 책임", fill=A_RED, font=font(28, "bold"))

    y += 165
    # Box 2
    box(draw, (60, y, W-60, y+140), fill="#F0FAF2", border="#B8DCC8")
    draw.text((80, y+15), "외국 은행의 논리 (EU PSD2)", fill=A_MINT, font=font(28, "bold"))
    draw.text((80, y+52), "\"서버 보안을 제대로 했나?\"", fill=T_DARK, font=font(30, "bold"))
    draw.text((80, y+90), "→ 해킹당하면? 은행 책임", fill=A_MINT, font=font(28, "bold"))

    y += 180
    draw.text((80, y), "한국 보안 프로그램의 진짜 역할:", fill=T_DARK, font=font(34, "bold"))
    y += 50
    draw.text((100, y), "해킹을 막는 것?  아니다", fill=T_BODY, font=font(30, "medium"))
    y += 45
    draw.text((100, y), "은행의 면책 근거를 만드는 것", fill=A_RED, font=font(34, "bold"))

    dots(draw, 6)
    img.save(f"{OUTPUT_DIR}/06.png", quality=95)


def s07():
    """북한 해커가 이걸로 뚫었다"""
    img = gradient((42, 42, 52), (28, 28, 38))
    img = glow(img, 540, 400, 450, (200, 60, 60), 30)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 80), "실제 사건", "#B71C1C")

    draw.text((80, 150), "보안 프로그램이", fill=T_WHITE, font=font(62, "bold"))
    draw.text((80, 235), "해킹 통로가 됐다", fill=A_YELLOW, font=font(62, "bold"))

    y = 350
    line(draw, 80, y, W-160, "#555555", 1)
    y += 25

    events = [
        ("2020", "북한 라자루스 그룹이", "Veraport를 이용해 악성코드 배포"),
        ("2023", "북한 해커가", "MagicLine4NX를 뚫고 기업 침입"),
        ("2023", "TouchEn nxKey에서", "전 국민 키보드 엿볼 수 있는 취약점 발견"),
    ]
    for year, l1, l2 in events:
        draw.text((80, y), year, fill=A_CORAL, font=font(32, "bold"))
        draw.text((200, y), l1, fill="#CCCCCC", font=font(28, "medium"))
        y += 38
        draw.text((200, y), l2, fill=T_WHITE, font=font(28, "bold"))
        y += 52

    y += 15
    line(draw, 80, y, W-160, "#555555", 1)
    y += 25
    draw.text((80, y), "보안을 위해 설치한 프로그램이", fill=T_WHITE, font=font(34, "bold"))
    y += 48
    draw.text((80, y), "오히려 해커에게 문을 열어줬다", fill=A_YELLOW, font=font(38, "bold"))

    y += 65
    draw.text((80, y), "키로거 막으려고 깐 프로그램이", fill="#AAAAAA", font=font(28, "medium"))
    y += 38
    draw.text((80, y), "전 국민 규모의 키로거 취약점을 만들었다", fill="#AAAAAA", font=font(28, "medium"))

    dots(draw, 7)
    img.save(f"{OUTPUT_DIR}/07.png", quality=95)


def s08():
    """진짜 해결책"""
    img = gradient(BG_MINT, BG_SAGE)
    img = glow(img, 540, 500, 400, (80, 200, 140), 22)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 80), "해결책은 간단하다", A_MINT)
    line(draw, 80, 145, 50, A_SAGE)

    draw.text((80, 178), "다른 나라처럼", fill=T_DARK, font=font(56, "bold"))
    draw.text((80, 255), "서버에서 막으면 된다", fill=A_MINT, font=font(56, "bold"))

    y = 360
    solutions = [
        ("이상거래탐지", "\"이 사람 평소 패턴이 아닌데?\" → 자동 차단"),
        ("지연이체", "큰 돈은 30분 후 실행 → 냉각기간"),
        ("AI 통화 분석", "통화 중 \"검찰\" \"계좌 동결\" 감지 → 경고"),
        ("패스키", "지문/얼굴인식 → 피싱에 원천 면역"),
    ]
    for name, desc in solutions:
        box(draw, (60, y, W-60, y+75), fill="#F0FAF2", border="#B8DCC8", radius=12)
        draw.text((80, y+10), name, fill=A_MINT, font=font(28, "bold"))
        draw.text((80, y+42), desc, fill=T_BODY, font=font(24, "regular"))
        y += 90

    y += 15
    draw.text((80, y), "이 중 어느 것도", fill=T_DARK, font=font(42, "bold"))
    y += 56
    draw.text((80, y), "PC에 뭘 깔 필요가 없다", fill=A_MINT, font=font(42, "bold"))

    y += 70
    draw.text((80, y), "전부 은행 서버에서 돌아간다", fill=T_BODY, font=font(30, "medium"))
    y += 42
    draw.text((80, y), "사용자가 할 일? 아무것도 없다", fill=T_BODY, font=font(30, "medium"))

    dots(draw, 8)
    img.save(f"{OUTPUT_DIR}/08.png", quality=95)


def s09():
    """AI 시대 + 클라이언트 다양성"""
    img = gradient(BG_LAVENDER, BG_PEACH)
    img = glow(img, 540, 300, 400, (160, 130, 220), 22)
    draw = ImageDraw.Draw(img)

    tag(draw, (80, 80), "AI 시대", A_LAVENDER)
    line(draw, 80, 145, 50, A_LAVENDER)

    draw.text((80, 178), "이대로 가면", fill=T_BLACK, font=font(62, "bold"))
    draw.text((80, 260), "AI 시대에서", fill=A_LAVENDER, font=font(62, "bold"))
    draw.text((80, 342), "낙오한다", fill=A_LAVENDER, font=font(62, "bold"))

    y = 450
    pairs = [
        ("AI가 은행 업무를 대신하는 시대에", "\"프로그램 5개 설치\"를 AI가 할 수 있나?", A_RED),
        ("AI 보이스피싱은 목소리까지 복제하는데", "키보드 보안으로 막겠다고?", A_RED),
        ("윈도우 아니면 은행 업무가 힘들고", "Mac, Linux는 아예 불가 수준", A_RED),
        ("글로벌 AI 서비스가 한국 결제를 못 붙인다", "한국만의 독자 규격이 AI 생태계를 차단", A_RED),
    ]
    for l1, l2, color in pairs:
        draw.text((80, y), l1, fill=T_DARK, font=font(26, "bold"))
        y += 34
        draw.text((80, y), l2, fill=color, font=font(26, "semibold"))
        y += 46

    dots(draw, 9)
    img.save(f"{OUTPUT_DIR}/09.png", quality=95)


def s10():
    """CTA"""
    img = gradient(BG_CREAM, BG_PEACH)
    img = glow(img, 540, 400, 500, (232, 180, 130), 25)
    img = glow(img, 800, 200, 300, (100, 200, 160), 18)
    draw = ImageDraw.Draw(img)

    line(draw, 80, 100, 60, A_CORAL)

    draw.text((80, 125), "바꿀 조건은", fill=T_BLACK, font=font(62, "bold"))
    draw.text((80, 210), "이미 갖춰졌다", fill=A_CORAL, font=font(62, "bold"))

    y = 330
    reasons = [
        ("01", "공인인증서 폐지 (2020)", "법적 장벽이 사라졌다"),
        ("02", "패스키가 모든 기기에 내장", "기술이 이미 준비됐다"),
        ("03", "AI 시대에 글로벌 호환 필수", "안 바꾸면 세계에서 배제된다"),
    ]
    for num, title, desc in reasons:
        draw.text((80, y), num, fill=A_CORAL, font=font(40, "bold"))
        draw.text((155, y+5), title, fill=T_BLACK, font=font(32, "bold"))
        draw.text((155, y+42), desc, fill=T_BODY, font=font(26, "medium"))
        y += 95

    y += 15
    draw.line((80, y, W-80, y), fill="#D8C8B8", width=1)
    y += 30

    draw.text((80, y), "은행이 서버 보안에 투자하게", fill=T_BLACK, font=font(40, "bold"))
    y += 55
    draw.text((80, y), "책임을 은행에 돌리면", fill=T_BLACK, font=font(40, "bold"))
    y += 55
    draw.text((80, y), "프로그램 5개는 내일이라도", fill=A_CORAL, font=font(42, "bold"))
    y += 55
    draw.text((80, y), "사라질 수 있다", fill=A_CORAL, font=font(42, "bold"))

    y += 75
    draw.text((80, y), "공감하면 저장하고 공유해주세요", fill=T_MUTED, font=font(26, "medium"))

    dots(draw, 10)
    img.save(f"{OUTPUT_DIR}/10.png", quality=95)


if __name__ == "__main__":
    funcs = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10]
    print(f"Generating {len(funcs)} slides (v5)...")
    for i, fn in enumerate(funcs, 1):
        fn()
        print(f"  {i}/{len(funcs)}")
    print(f"\nDone! → {OUTPUT_DIR}/")
