# 大六壬神课 · iOS 版（汉基）

> 传统三式之一「大六壬」的电子罗盘：天地盘、四课、九宗门取三传、十二天将、六亲、旬空驿马日禄，附八段详细断语解析。
> **全部计算在本机完成，App 不联网、不上传任何数据。**

本仓库是 iOS 侧的壳工程 + 云端自动构建 IPA 的流水线。安卓版见隔壁的 APK（另一渠道发布）。

---

## 一、这里有什么

| 路径 | 说明 |
|---|---|
| `Resources/index.html` | 完整应用本体（单文件，排盘引擎 + 七彩罗盘 + 断语），约 42 KB |
| `Sources/LiuRenApp.swift` | SwiftUI + WKWebView 外壳，加载本地 index.html |
| `Sources/Info.plist` | 应用信息（名称「大六壬神课」、竖屏、深色状态栏） |
| `project.yml` | XcodeGen 描述文件，云端据此生成 .xcodeproj |
| `.github/workflows/build-ipa.yml` | macOS 云端编译 → 打包 IPA → 发布到 Release |
| `Resources/Assets.xcassets` | App 图标（1024×1024） |

---

## 二、拿 IPA 的三种方式

### 方式 1（本仓库已配好）：直接下 Release 里的 IPA

每次推送代码，GitHub 的 macOS 机器会自动编译并重新发布：

👉 **Releases → `latest` → 下载 `LiuRen-unsigned.ipa`**

这是**未签名**的 IPA（GitHub 机器没有你的苹果证书，签不了名）。iPhone 不认未签名包，必须用下一步签名，这是苹果的规矩，绕不过去。

> ⚠️ **首次构建若在 Actions 里显示 `cancelled`（没有执行任何步骤）**：不是代码问题，是本账号的 macOS 执行器没开通。
> 两种解法（任选其一）：
> 1. **GitHub 侧**：Settings → Billing → 添加支付方式（公共仓库的 macOS 分钟不扣费，只作身份核验），回到 Actions 点 `Re-run all jobs`；
> 2. **Codemagic 侧（免信用卡，每月 500 分钟）**：用 GitHub 账号登录 [codemagic.io](https://codemagic.io) → Add application → 选本仓库 → 构建配置选 `codemagic.yaml` → Start new build，产物 `LiuRen-unsigned.ipa` 直接下载。本仓库已内置 `codemagic.yaml`，可直接用。

### 方式 2：Windows 上用 Sideloadly 签名安装（推荐，无需 Mac）

1. 下载安装 [Sideloadly](https://sideloadly.io/)（Windows 版）；
2. 用数据线连 iPhone，解锁并点「信任此电脑」；
3. 打开 Sideloadly，把 `LiuRen-unsigned.ipa` 拖进窗口；
4. `Apple ID` 填你的 Apple 账号（免费的即可），点 **Start**，按提示在手机上输入 Apple ID 密码；
5. 首次安装后，手机「设置 → 通用 → VPN与设备管理」里**信任**你的开发者证书，即可打开。

> 免费 Apple ID 签名的有效期是 **7 天**，到期用 Sideloadly 重新签一次即可；开发者账号（$99/年）可延长到 1 年。
> 若提示 `Unable to install`，先确认 iPhone 已开启「开发者模式」（iOS 16+：设置 → 隐私与安全性 → 开发者模式）。

### 方式 3：有 Mac 就用 Xcode

```bash
brew install xcodegen
xcodegen generate
open LiuRen.xcodeproj
```

选自己的 iPhone → Run。要上架就走 Product → Archive。

---

## 三、想改点东西

- 改界面 / 断语：直接编辑 `Resources/index.html`（纯 HTML+JS，无需编译环境，改完推上去就自动出新 IPA）；
- 改应用名 / Bundle ID / 图标：`Sources/Info.plist`、`project.yml`、`Resources/Assets.xcassets`；
- 想让 IPA 直接可装（不签名）：做不到，iOS 强制签名，任何声称「免签直接装」的方式都是企业证书滥用，随时封。

---

## 四、技术要点

- 月将按太阳黄经定中气换将；月将加占时起天盘（可选真太阳时，按经度差 + 均时差校正）；
- 十干寄宫 → 四课 → 九宗门（贼克 / 比用 / 涉害 / 遥克 / 昴星 / 别责 / 八专 / 伏吟 / 返吟）取三传；
- 贵人分昼夜起、临亥至辰顺行、临巳至戌逆行，布十二天将；
- 辅以旬空、驿马、日禄、刑冲合；断语按课体、三传生克、神将象义、类神逐层生成。

不同流派判语有出入，本项目取通行一说，并在断语中注明取用依据。

---

## 五、免责

术数为传统象数文化模型，未经科学验证，仅供研读与文化体验，不可替代医疗、法律、财务等现实决策。

© 汉基科技
