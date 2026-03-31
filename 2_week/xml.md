# 🧱 MJCF 전체 기본 구조

가장 기본 뼈대는 이 형태입니다.

```xml
<mujoco model="simple_arm">
    <worldbody>
        <body name="base">
            <joint name="joint1" type="hinge"/>
            <geom type="capsule"/>
            
            <body name="link2">
                <joint name="joint2" type="hinge"/>
                <geom type="capsule"/>
            </body>
        </body>
    </worldbody>

    <actuator>
        <motor joint="joint1"/>
        <motor joint="joint2"/>
    </actuator>

    <sensor>
        <jointpos joint="joint1"/>
    </sensor>
</mujoco>
```

---

# 1) `<mujoco>`

최상위 루트입니다.

```xml
<mujoco model="simple_arm">
```

Unity로 비유하면:

> **하나의 Scene / Robot Prefab 전체**

---

# 2) `<worldbody>`

월드 안에 존재하는 모든 오브젝트의 시작점입니다.

```xml
<worldbody>
```

쉽게 말하면:

> **씬에 배치되는 실제 로봇 본체 시작 위치**

Unity에서는:

> Hierarchy 최상단 부모 오브젝트

---

# ⭐ 3) `<body>` ← 가장 중요

이게 진짜 핵심입니다.

```xml
<body name="base">
```

`body`는 로봇의 링크(뼈대)입니다.

Unity로 비유하면:

> **GameObject / Bone / 부모-자식 Transform 구조**

예시:

```xml
<body name="base">
    <body name="link2">
```

이렇게 들어가면:

> base의 자식으로 link2가 붙음

즉 로봇 팔처럼 연결됩니다.

---

## 🔥 Unity 비유 (제일 중요)

```text
Robot
 └─ Base
     └─ Link1
         └─ Link2
```

MJCF도 완전히 동일합니다.

```xml
<body name="base">
    <body name="link1">
        <body name="link2">
```

당신은 Unity 경험 덕분에 이 부분을 **가장 빠르게 이해할 수 있습니다.**

---

# ⚙️ 4) `<joint>`

관절입니다.

```xml
<joint name="joint1" type="hinge"/>
```

이 body가 **어떻게 움직이는지 규칙 정의**합니다.

---

## joint 종류

### hinge

회전 관절

```xml
<joint type="hinge"/>
```

예:

* 로봇 팔 회전
* 문 열기
* 바퀴 회전

---

### slide

직선 이동

```xml
<joint type="slide"/>
```

예:

* 엘리베이터
* 리니어 액추에이터

---

### ball

자유 회전

```xml
<joint type="ball"/>
```

예:

* 어깨
* 드론 짐벌

---

# 🧩 5) `<geom>`

눈에 보이는 형태 + 충돌체입니다.

```xml
<geom type="capsule" size="0.03 0.3"/>
```

역할:

* 모양
* 충돌
* 질량 계산

Unity로 비유하면:

> **Mesh Renderer + Collider 합친 느낌**

---

## geom 자주 쓰는 타입

* box
* sphere
* capsule
* cylinder
* mesh

---

# 🔋 6) `<actuator>`

모터입니다.

```xml
<actuator>
    <motor joint="joint1"/>
</actuator>
```

joint를 **실제로 움직이는 힘 입력 장치**

Unity 느낌:

> Input → Rigidbody.AddTorque()

즉 joint는 **움직일 수 있는 구조**, actuator는 **실제로 움직이는 엔진**

---

# 👀 7) `<sensor>`

상태 읽기입니다.

```xml
<sensor>
    <jointpos joint="joint1"/>
</sensor>
```

읽을 수 있는 값:

* joint 각도
* 속도
* 힘
* 터치
* IMU
* 카메라

강화학습에서는 거의 필수입니다.

---

# 📷 8) `<camera>`

시뮬레이터 시점입니다.

```xml
<camera name="top" pos="0 0 3"/>
```

역할:

* 로봇 시점
* top-down
* tracking
* vision input

---

# 🎯 핵심 구조 흐름 한 번에 보기

이 순서로 이해하면 됩니다.

```text
mujoco
 └─ worldbody
     └─ body
         ├─ joint
         ├─ geom
         └─ child body
 └─ actuator
 └─ sensor
 └─ camera
```

---

# 💡 당신 기준 초핵심 이해 포인트

게임 개발자 관점으로 보면 이렇게 외우면 가장 쉽습니다.

> **body = GameObject**
>
> **joint = 움직임 제한 Transform**
>
> **geom = Collider + Mesh**
>
> **actuator = 입력으로 움직이는 Motor**
>
> **sensor = 상태값 읽기**
>
> **camera = 시점**

---

# 🚀 오늘 학습 목표 (딱 이것만)

오늘은 아래 3개만 완벽히 되면 성공입니다.

### ✅ 1

XML에서 부모-자식 body 구조 읽기

### ✅ 2

joint가 어느 body를 움직이는지 보기

### ✅ 3

geom이 모양이라는 것 이해


