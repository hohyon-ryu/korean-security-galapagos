# 한국 보안의 갈라파고스

### 어디서부터 잘못됐나 — ActiveX에서 AI까지, 25년의 역사

---

> 은행 홈페이지 들어갔더니 **프로그램 5개 깔라고?**
>
> 외국에선 지문 찍으면 끝인데, 한국만 25년째 이러고 있다.
>
> **도대체 왜?**

---

## 한눈에 보기

| 한국 | 세계 |
|---|---|
| 프로그램 5개 설치 | 설치할 것 없음 |
| 공동인증서 + OTP + 보안카드 | 지문 한 번 |
| 해킹당하면 **사용자 책임** | 해킹당하면 **은행 책임** |
| Windows + IE 종속 | 모든 브라우저, 모든 OS |
| 보안 프로그램이 해킹 통로가 됨 | 서버에서 보안 처리 |

---

## 타임라인

```
1999  미국 암호화 수출 금지 → 한국, SEED + ActiveX로 독자 해결
      전자서명법 제정 → 공인인증서만 법적 효력
2000  미국 수출 제한 해제 → 한국만 돌아오지 못함
2005  최초 인터넷뱅킹 해킹 → 보안프로그램 의무화 시작
2008  Chrome 출시 (샌드박스) → 세계는 브라우저 격리로 전환
2020  북한 라자루스, Veraport로 악성코드 배포
      공인인증서 폐지 (21년 만에)
2023  TouchEn nxKey 취약점 발견 (전 국민 키로거 위험)
      북한 해커, MagicLine4NX로 기업 침입
2026  한국 시민은 여전히 프로그램 5개를 깔고 있다
```

---

## 핵심 발견

### 1. 보안 프로그램은 보이스피싱을 못 막는다

보이스피싱의 핵심: **피해자가 속아서 직접 돈을 보낸다.**
키보드 보안, 방화벽, 공인인증서 — 이 중 어느 것도 이걸 막지 못한다.
연간 피해액: **1조 965억 원.**

### 2. 보안 프로그램의 진짜 역할은 은행 면책용이다

- 한국: "보안 프로그램 깔라고 했잖아" → 해킹당해도 **은행 면책**
- EU: "서버 보안을 제대로 했나?" → 해킹당하면 **은행 책임** (PSD2)

### 3. 보안 프로그램이 오히려 해킹 통로가 됐다

- **2020**: 북한이 Veraport로 악성코드 배포 (ESET 보고)
- **2023**: MagicLine4NX 취약점으로 기업 침입 (영국 NCSC + 한국 NIS 공동 경보)
- **2023**: TouchEn nxKey에서 전 국민 키보드 엿볼 수 있는 취약점 (Wladimir Palant)

### 4. AI 시대에 더 큰 문제가 된다

- AI 에이전트가 은행 업무를 대신하는데 "프로그램 5개 설치"를 AI가 할 수 있나?
- Windows가 아니면 은행 업무가 힘들고, Linux는 아예 불가
- 글로벌 AI 서비스가 한국 결제를 붙일 수 없다

---

## 자료 구성

### 분석 문서

| 파일 | 설명 |
|---|---|
| [`한국_결제보안_갈라파고스_분석.md`](한국_결제보안_갈라파고스_분석.md) | 전체 분석 원문 — 10개 챕터 |
| [`정책제언_국가AI전략위원회.md`](정책제언_국가AI전략위원회.md) | 국가인공지능전략위원회 발표용 정책 제언 |

### 발표 슬라이드 (PDF)

| 파일 | 설명 |
|---|---|
| [`한국보안_갈라파고스_발표자료_유호현_v2.1.pdf`](한국보안_갈라파고스_발표자료_유호현_v2.1.pdf) | 최신 발표 슬라이드 (20페이지) |
| [`한국_결제보안_갈라파고스_분석_옥소폴리틱스.pdf`](한국_결제보안_갈라파고스_분석_옥소폴리틱스.pdf) | 분석 보고서 PDF |

### 인스타그램 카드뉴스

최종 버전: **[`instagram_v6/`](instagram_v6/)** (10장)

| 슬라이드 | 내용 |
|---|---|
| 01 | 은행 홈페이지 들어갔더니 프로그램 5개 깔라고? |
| 02 | 한국은 세계 1등이었다 → 1년 차이로 돌아오지 못함 |
| 03 | 정부가 법으로 못 박아버렸다 |
| 04 | 미국: 지문 찍기. 끝. / 한국: 5단계 |
| 05 | 이 프로그램 5개 깔아도 보이스피싱 못 막는다 |
| 06 | 왜 깔라고 하나 → 은행 면책용이다 |
| 07 | 이 보안 프로그램으로 북한이 해킹했다 |
| 08 | 다른 나라는 아무것도 안 깔아도 된다 |
| 09 | 이대로면 AI 시대에 뒤처진다 |
| 10 | 바꿀 수 있다, 지금 당장 |

### 기타 자료

| 폴더/파일 | 설명 |
|---|---|
| `cardnews/` | 카드뉴스 이미지 |
| `shorts/` | 숏폼 영상 |
| `slides_images/` | 발표 슬라이드 개별 이미지 |
| `generate_*.py` | 이미지 생성 스크립트 (Python + Pillow) |
| `facebook_post.md` | 페이스북 게시글 |
| `instagram_post.md` | 인스타그램 게시글 |

---

## 출처

### 보안 연구

- [Wladimir Palant, "South Korea's online security dead end" (2023)](https://palant.info/2023/01/02/south-koreas-online-security-dead-end/)
- [Palant, "TouchEn nxKey: The keylogging anti-keylogger solution" (2023)](https://palant.info/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/)
- [Palant, "IPinside: Korea's mandatory spyware" (2023)](https://palant.info/2023/01/25/ipinside-koreas-mandatory-spyware/)
- [KAIST / USENIX Security 2025, "Too Much of a Good Thing"](https://syssec.kaist.ac.kr/pub/2025/Too_Much_Good.pdf)

### 해킹 사례

- [ESET, "Lazarus supply-chain attack in South Korea" (2020)](https://www.welivesecurity.com/2020/11/16/lazarus-supply-chain-attack-south-korea/)
- [BleepingComputer, "North Korean hackers exploited MagicLine4NX zero-day" (2023)](https://www.bleepingcomputer.com/news/security/uk-and-south-korea-hackers-use-zero-day-in-supply-chain-attack/)

### 규제 및 시장

- [The Register, "South Korea kills ActiveX-based certificate service" (2020)](https://www.theregister.com/2020/12/10/south_korea_activex_certs_dead/)

---

## 라이선스

이 자료는 자유롭게 공유, 인용, 활용할 수 있습니다. 출처 표기를 부탁드립니다.

---

*2026년 3월*
