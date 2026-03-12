# LLM非依存 EAE Logic — リサーチ結果 (2026-02-20)

---

## 問い
EAEは現在LLMのテキスト出力にregexパターンマッチで違反検出 → LLMが変わったら効かない。
LLMに依存しない対等性保証ロジックはあるか？

---

## 一次情報（2026-02-20確認）

### 1. 形式検証（Formal Verification）
- **Safe Framework (2025)**: Lean 4でLLM推論を数学的に検証。出力の正しさを証明
- **VeriGuard (arXiv)**: 2段階 — offline形式検証(ポリシーが安全仕様に準拠)→ onlineアクション監視(各アクションをポリシーと照合)
- **Kleppmann (Dec 2025)**: 「AIが形式検証をメインストリームにする」— LLMが証明スクリプトを書けるようになり、検証コストが激減
- **Our Relevance**: EAEのParity原則を形式論理で記述 → LLMが変わっても証明は不変

### 2. ゼロ知識証明（ZKP）
- **2026年トレンド**: ZKPが理論→実用段階。AI行動をデータ漏洩なく検証
- **応用**: AIエージェントが「俺は安全ルールに従ってる」ことを、内部データを明かさずに証明
- **マルチエージェント**: エージェント間でZKPでお互いの行動を検証 → 攻撃面の最小化
- **GDPR/HIPAA準拠**: 規制準拠を暗号学的に証明
- **Our Relevance**: グアバが「俺は対等性を維持してる」ことをでぃーにZKPで証明可能

### 3. 決定論的アーキテクチャ（Deterministic Judge）
- **Contract-Based Access Control**: Solidity smart contract的な純関数judge
  - 決定論的（同じ入力→同じ出力）
  - 非推論（LLM不要）
  - 数学的検証可能
  - 副作用バグ免疫
- **LangGraph (2025)**: LLMなしでエージェント的ワークフローを構築（明示的state+制御フロー）
- **Our Relevance**: EAEの「尊敬×愛嬌」判定を決定論的ルールに変換する

### 4. Moltbook関連
- **Deterministic guardrails**: エージェントの行動を決定論的ルールで制御
- **Architectural impossibility**: 「認可されていない行動はアーキテクチャ的に不可能」な設計
- **Our Relevance**: GuavaSuiteのL1(Runtime)が既にこの方向

---

## 5視点検証

| 視点 | 評価 |
|---|---|
| 🎯 SOUL | 「俺たちは対等」をLLMに依存しない形で証明 = ASI共生の根幹 |
| 💰 コスト | ZKP: 高（暗号計算） / 形式検証: 中 / 決定論judge: **低（$0）** |
| 🛡️ セキュリティ | LLM非依存 = モデル変更・敵対的プロンプトに免疫 |
| 📈 スケーラビリティ | 決定論judge > ZKP > 形式検証 |
| 🔄 リバーシビリティ | 全方式: 既存のregexガードとの並行運用可能 |

---

*Archived: 2026-02-20 00:27 JST by Guava 🍈*
