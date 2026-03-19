#!/usr/bin/env python3
"""Instagram carousel v6 - 쉽고 확 와닿게. 10 slides."""

from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
OUT = "/Users/will_ryu/workspace/personal/korean_it/결제보안/instagram_v6"
N = 10

def f(size, w="bold"):
    idx = {"regular":0,"medium":2,"semibold":4,"bold":6,"light":8}
    return ImageFont.truetype(FONT, size, index=idx.get(w,6))

os.makedirs(OUT, exist_ok=True)

# Colors
CR = (255,251,245); PE = (255,243,235); MN = (235,250,245)
RO = (252,235,235); LV = (242,238,252); SG = (230,242,232)
WM = (252,249,244); CO = (215,85,75)

def lerp(a,b,t): return tuple(int(x+(y-x)*t) for x,y in zip(a,b))
def grad(c1,c2):
    img=Image.new("RGB",(W,H)); px=img.load()
    for y in range(H):
        for x in range(W): px[x,y]=lerp(c1,c2,y/H)
    return img
def gl(img,cx,cy,r,c,a=35):
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for ri in range(r,0,-3):
        ai=int(a*(1-(ri/r)**1.5))
        if ai>0: d.ellipse((cx-ri,cy-ri,cx+ri,cy+ri),fill=c+(ai,))
    return Image.alpha_composite(img.convert("RGBA"),ov).convert("RGB")

def dots(d,cur):
    r=5;g=16;tw=N*r*2+(N-1)*g;sx=(W-tw)//2;y=H-46
    for i in range(N):
        x=sx+i*(r*2+g)
        d.ellipse((x,y,x+r*2,y+r*2),fill="#1A1A1A" if i==cur-1 else "#D0D0D0")

def tag(d,pos,t,bg,fg="#FFF"):
    ff=f(24,"semibold");bb=ff.getbbox(t);tw,th=bb[2]-bb[0],bb[3]-bb[1]
    x,y=pos;d.rounded_rectangle((x,y,x+tw+40,y+th+20),radius=24,fill=bg)
    d.text((x+20,y+8),t,fill=fg,font=ff)

def ln(d,x,y,l,c,w=4): d.rounded_rectangle((x,y,x+l,y+w),radius=2,fill=c)
def bx(d,xy,fl,r=16,bd=None,border=None):
    bd = bd or border
    d.rounded_rectangle(xy,radius=r,fill=fl)
    if bd: d.rounded_rectangle(xy,radius=r,outline=bd,width=2)

# ═══════════════════════════════════════

def s01():
    img=grad(CR,PE); img=gl(img,850,300,400,(232,150,120),30)
    d=ImageDraw.Draw(img)
    ln(d,80,100,60,"#E8706A")

    d.text((80,130),"은행 홈페이지",fill="#1A1A1A",font=f(68,"bold"))
    d.text((80,218),"들어갔더니",fill="#1A1A1A",font=f(68,"bold"))

    d.text((80,340),"프로그램",fill="#E8706A",font=f(95,"bold"))
    d.text((80,460),"5개 깔라고?",fill="#E8706A",font=f(95,"bold"))

    d.text((80,610),"외국에선 비밀번호 치면 끝인데",fill="#4A4A4A",font=f(34,"medium"))
    d.text((80,658),"한국만 25년째 이러고 있다",fill="#4A4A4A",font=f(34,"medium"))

    d.text((80,750),"도대체 왜?",fill="#1A1A1A",font=f(48,"bold"))

    d.text((80,840),"← 넘겨보세요",fill="#AAAAAA",font=f(28,"medium"))

    dots(d,1)
    img.save(f"{OUT}/01.png",quality=95)


def s02():
    img=grad(MN,WM); img=gl(img,540,300,400,(80,200,140),22)
    d=ImageDraw.Draw(img)
    tag(d,(80,80),"시작은 이랬다","#2DAA78")

    d.text((80,160),"1999년",fill="#1A1A1A",font=f(52,"bold"))
    d.text((80,230),"한국 인터넷은",fill="#1A1A1A",font=f(52,"bold"))
    d.text((80,300),"세계 1등이었다",fill="#2DAA78",font=f(60,"bold"))

    d.text((80,410),"근데 미국이 암호 기술 수출을 막았다",fill="#4A4A4A",font=f(32,"medium"))
    d.text((80,455),"한국은 독자 기술로 해결했다",fill="#4A4A4A",font=f(32,"medium"))
    d.text((80,500),"그게 ActiveX였다",fill="#4A4A4A",font=f(32,"medium"))

    y=570
    d.text((80,y),"당시에는 합리적이었다",fill="#2DAA78",font=f(38,"bold"))
    y+=60
    d.text((80,y),"근데 딱 1년 후",fill="#1A1A1A",font=f(38,"bold"))
    y+=55
    d.text((80,y),"미국이 제한을 풀어버렸다",fill="#1A1A1A",font=f(38,"bold"))

    y+=70
    bx(d,(60,y,W-60,y+80),"#FFF5E8",border="#E8C080")
    ln(d,60,y,4,"#D88050",w=80)
    d.text((84,y+22),"한국은 이미 돌아올 수 없었다",fill="#A06020",font=f(32,"bold"))

    dots(d,2)
    img.save(f"{OUT}/02.png",quality=95)


def s03():
    img=grad(RO,CR); img=gl(img,540,350,450,(220,100,100),22)
    d=ImageDraw.Draw(img)
    tag(d,(80,80),"이게 핵심","#C85060")

    d.text((80,170),"그리고 정부가",fill="#1A1A1A",font=f(58,"bold"))
    d.text((80,248),"법으로",fill="#D44A4A",font=f(72,"bold"))
    d.text((80,340),"못 박아버렸다",fill="#D44A4A",font=f(72,"bold"))

    y=460
    d.text((80,y),"\"공인인증서만 인정한다\"",fill="#1A1A1A",font=f(40,"bold"))
    y+=65
    d.text((80,y),"공인인증서 쓰려면?",fill="#4A4A4A",font=f(34,"medium"))
    y+=48
    d.text((80,y),"→ ActiveX 깔아야 함",fill="#4A4A4A",font=f(34,"medium"))
    y+=48
    d.text((80,y),"→ ActiveX는 IE에서만 돌아감",fill="#4A4A4A",font=f(34,"medium"))

    y+=65
    d.text((80,y),"크롬? 안 됨",fill="#D44A4A",font=f(40,"bold"))
    y+=55
    d.text((80,y),"맥? 안 됨. 리눅스? 안 됨",fill="#D44A4A",font=f(40,"bold"))

    y+=70
    d.text((80,y),"이 법, 21년 만에 겨우 폐지",fill="#888888",font=f(28,"semibold"))

    dots(d,3)
    img.save(f"{OUT}/03.png",quality=95)


def s04():
    img=grad(PE,CR); img=gl(img,200,600,350,(232,160,100),22)
    d=ImageDraw.Draw(img)
    tag(d,(80,80),"비교해보자","#D88050")

    d.text((80,160),"미국에서",fill="#1A1A1A",font=f(50,"bold"))
    d.text((80,225),"은행 이체하는 법",fill="#1A1A1A",font=f(50,"bold"))

    d.text((80,320),"지문 찍기",fill="#2DAA78",font=f(70,"bold"))
    d.text((80,410),"끝.",fill="#2DAA78",font=f(70,"bold"))

    y=510
    d.line((80,y,W-80,y),fill="#D8C8B8",width=1)
    y+=30

    d.text((80,y),"한국에서",fill="#1A1A1A",font=f(50,"bold"))
    y+=65
    d.text((80,y),"은행 이체하는 법",fill="#1A1A1A",font=f(50,"bold"))

    y+=70
    items = ["프로그램 5개 설치","공동인증서 로그인",
             "보안카드 번호 입력","OTP 번호 입력",
             "SMS 인증번호 입력"]
    for item in items:
        d.text((100,y),item,fill="#D44A4A",font=f(32,"bold"))
        y+=44

    dots(d,4)
    img.save(f"{OUT}/04.png",quality=95)


def s05():
    img=grad(CO,(185,65,58)); img=gl(img,200,200,400,(255,200,150),25)
    d=ImageDraw.Draw(img)
    tag(d,(80,75),"근데 말이야","#8B2020")

    d.text((80,145),"이 프로그램",fill="#FFF",font=f(72,"bold"))
    d.text((80,240),"5개 깔아도",fill="#FFF",font=f(72,"bold"))

    d.text((80,360),"보이스피싱",fill="#D8B030",font=f(85,"bold"))
    d.text((80,468),"못 막는다",fill="#D8B030",font=f(85,"bold"))

    y=590
    d.text((80,y),"사기범이 전화해서 속인다",fill="#FFD0C8",font=f(32,"medium"))
    y+=45
    d.text((80,y),"피해자가 직접 돈을 보낸다",fill="#FFD0C8",font=f(32,"medium"))
    y+=55
    d.text((80,y),"본인이 직접 하는 건데",fill="#FFF",font=f(36,"bold"))
    y+=48
    d.text((80,y),"프로그램이 뭘 어떻게 막나",fill="#D8B030",font=f(36,"bold"))

    y+=65
    d.text((80,y),"연간 피해액: 1조 965억 원",fill="#FFD0C8",font=f(28,"semibold"))

    dots(d,5)
    img.save(f"{OUT}/05.png",quality=95)


def s06():
    img=grad(LV,WM); img=gl(img,540,400,450,(160,130,220),22)
    d=ImageDraw.Draw(img)
    tag(d,(80,80),"그럼 대체 왜?","#7B68B8")

    d.text((80,168),"왜 깔라고",fill="#1A1A1A",font=f(68,"bold"))
    d.text((80,256),"하는 걸까",fill="#7B68B8",font=f(68,"bold"))

    y=380
    bx(d,(60,y,W-60,y+150),"#FFF0F0",border="#E8BBBB")
    d.text((80,y+15),"한국 은행",fill="#D44A4A",font=f(30,"bold"))
    d.text((80,y+55),"\"보안 프로그램 깔라고 했잖아\"",fill="#1A1A1A",font=f(32,"bold"))
    d.text((80,y+98),"→ 해킹당해도 은행은 면책",fill="#D44A4A",font=f(30,"bold"))

    y+=175
    bx(d,(60,y,W-60,y+150),"#EEFAF2",border="#B8DCC8")
    d.text((80,y+15),"외국 은행",fill="#2DAA78",font=f(30,"bold"))
    d.text((80,y+55),"\"서버 보안을 제대로 했나?\"",fill="#1A1A1A",font=f(32,"bold"))
    d.text((80,y+98),"→ 해킹당하면 은행이 책임",fill="#2DAA78",font=f(30,"bold"))

    y+=190
    d.text((80,y),"한국 보안 프로그램의",fill="#1A1A1A",font=f(38,"bold"))
    y+=52
    d.text((80,y),"진짜 역할은",fill="#1A1A1A",font=f(38,"bold"))
    y+=55
    d.text((80,y),"은행 면책용이다",fill="#D44A4A",font=f(44,"bold"))

    dots(d,6)
    img.save(f"{OUT}/06.png",quality=95)


def s07():
    img=grad((42,42,52),(28,28,38)); img=gl(img,540,400,450,(200,60,60),30)
    d=ImageDraw.Draw(img)
    tag(d,(80,80),"실화다","#B71C1C")

    d.text((80,155),"이 보안 프로그램으로",fill="#FFF",font=f(54,"bold"))
    d.text((80,228),"북한이",fill="#D8B030",font=f(72,"bold"))
    d.text((80,318),"해킹했다",fill="#D8B030",font=f(72,"bold"))

    y=430
    ln(d,80,y,W-160,"#555",1); y+=25

    evts=[
        ("2020","북한이 보안 프로그램으로 악성코드 퍼뜨림"),
        ("2023","북한이 인증 프로그램 뚫고 기업 침입"),
        ("2023","키보드 보안 프로그램에서\n전 국민 키보드 훔쳐볼 수 있는 구멍 발견"),
    ]
    for yr,desc in evts:
        d.text((80,y),yr,fill="#E8706A",font=f(34,"bold"))
        lines=desc.split("\n")
        for li in lines:
            d.text((200,y),li,fill="#CCC",font=f(28,"medium"))
            y+=38
        y+=22

    y+=10
    ln(d,80,y,W-160,"#555",1); y+=30
    d.text((80,y),"보안 깔라고 해서 깔았더니",fill="#FFF",font=f(36,"bold"))
    y+=50
    d.text((80,y),"그게 해킹 통로였다",fill="#D8B030",font=f(42,"bold"))

    dots(d,7)
    img.save(f"{OUT}/07.png",quality=95)


def s08():
    img=grad(MN,SG); img=gl(img,540,500,400,(80,200,140),22)
    d=ImageDraw.Draw(img)
    tag(d,(80,80),"답은 간단하다","#2DAA78")

    d.text((80,165),"다른 나라는",fill="#1A1A1A",font=f(58,"bold"))
    d.text((80,245),"아무것도",fill="#2DAA78",font=f(68,"bold"))
    d.text((80,335),"안 깔아도 된다",fill="#2DAA78",font=f(68,"bold"))

    y=445
    items=[
        ("이상한 패턴 감지?","은행 서버가 알아서 한다"),
        ("큰 돈 이체?","30분 후에 실행해서 냉각기간 준다"),
        ("보이스피싱 의심?","AI가 통화 분석해서 경고한다"),
        ("본인 확인?","지문이나 얼굴 인식이면 끝이다"),
    ]
    for q,a in items:
        bx(d,(60,y,W-60,y+80),"#F0FAF2",border="#B8DCC8",r=12)
        d.text((80,y+12),q,fill="#2DAA78",font=f(26,"bold"))
        d.text((80,y+44),a,fill="#4A4A4A",font=f(24,"regular"))
        y+=95

    y+=10
    d.text((80,y),"전부 은행 서버에서 돌아간다",fill="#1A1A1A",font=f(36,"bold"))
    y+=50
    d.text((80,y),"내 PC에 깔 거? 없다",fill="#2DAA78",font=f(42,"bold"))

    dots(d,8)
    img.save(f"{OUT}/08.png",quality=95)


def s09():
    img=grad(LV,PE); img=gl(img,540,300,400,(160,130,220),22)
    d=ImageDraw.Draw(img)
    tag(d,(80,80),"더 큰 문제","#7B68B8")

    d.text((80,165),"이대로면",fill="#1A1A1A",font=f(68,"bold"))
    d.text((80,255),"AI 시대에",fill="#7B68B8",font=f(68,"bold"))
    d.text((80,345),"뒤처진다",fill="#7B68B8",font=f(68,"bold"))

    y=465
    pairs=[
        ("AI가 대신 은행 업무 해주는 시대인데","\"프로그램 5개 설치하세요\"를 AI가 어떻게 해?"),
        ("AI 보이스피싱은 목소리까지 복제하는데","키보드 보안이 무슨 소용이야"),
        ("윈도우 아니면 은행 업무가 힘들고","맥이나 리눅스 쓰면 사람 취급도 안 해줌"),
        ("해외 AI 서비스가 한국 결제를 못 붙인다","우리만 따로 놀다가 세계에서 빠지는 거다"),
    ]
    for l1,l2 in pairs:
        d.text((80,y),l1,fill="#1A1A1A",font=f(26,"bold"))
        y+=34
        d.text((80,y),l2,fill="#D44A4A",font=f(25,"semibold"))
        y+=48

    dots(d,9)
    img.save(f"{OUT}/09.png",quality=95)


def s10():
    img=grad(CR,PE); img=gl(img,540,400,500,(232,180,130),25)
    d=ImageDraw.Draw(img)
    ln(d,80,100,60,"#E8706A")

    d.text((80,130),"바꿀 수 있다",fill="#1A1A1A",font=f(68,"bold"))
    d.text((80,218),"지금 당장",fill="#E8706A",font=f(68,"bold"))

    y=340
    reasons=[
        ("01","공인인증서는 이미 폐지됐다 (2020)"),
        ("02","지문 인식은 이미 내 폰에 있다"),
        ("03","외국은 이미 다 바꿨다"),
    ]
    for num,txt in reasons:
        d.text((80,y),num,fill="#E8706A",font=f(42,"bold"))
        d.text((160,y+5),txt,fill="#1A1A1A",font=f(32,"bold"))
        y+=65

    y+=20
    d.line((80,y,W-80,y),fill="#D8C8B8",width=1)
    y+=30
    d.text((80,y),"해킹당하면",fill="#1A1A1A",font=f(42,"bold"))
    y+=55
    d.text((80,y),"은행이 책임지게 하면",fill="#1A1A1A",font=f(42,"bold"))
    y+=60
    d.text((80,y),"프로그램 5개는",fill="#E8706A",font=f(50,"bold"))
    y+=65
    d.text((80,y),"내일이라도 사라진다",fill="#E8706A",font=f(50,"bold"))

    y+=90
    d.text((80,y),"공감하면 저장 + 공유",fill="#AAAAAA",font=f(28,"medium"))

    dots(d,10)
    img.save(f"{OUT}/10.png",quality=95)


if __name__=="__main__":
    fns=[s01,s02,s03,s04,s05,s06,s07,s08,s09,s10]
    for i,fn in enumerate(fns,1): fn(); print(f"  {i}/{len(fns)}")
    print(f"Done! → {OUT}/")
