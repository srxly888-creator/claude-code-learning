# 📚 Claude 官方文档整合版（30天训练营配套）

> **版本**: 1.0 | **更新时间**: 2026-03-23 | **语言**: 繁体中文

---

## 📖 目录

1. [Claude 簡介](#claude-簡介)
2. [功能概覽](#功能概覽)
3. [工具使用](#工具使用)
4. [Agent 技能](#agent-技能)
5. [提示工程](#提示工程)
6. [测试与评估](#测试与评估)
7. [管理与监控](#管理与监控)

---

## 🎯 Claude 簡介

### 最新模型系列

- **Claude Opus 4.6** - 最智能的模型，全球最佳的编程、企业代理和专业工作模型
- **Claude Sonnet 4.6** - 规模化的前沿智能，专为编程、代理和企业工作流构建
- **Claude Haiku 4.5** - 最快的模型，具有接近前沿的智能

### 核心能力

Claude 可以协助处理许多涉及文本、代码和图像的任务：

- **文本与代码生成** - 摘要文本、回答问题、擷取资料、翻译文本，以及解释和生成程式碼
- **视觉** - 处理和分析视觉输入，并从图像生成文本和代码

---

## 🔧 功能概覽

### 核心能力

#### 1. 1M token 上下文視窗

**描述**: 擴展的上下文視窗，讓您能處理更大的文件、維持更長的對話，並處理更大規模的程式碼庫。

**可用性**: Claude API (Beta) | Amazon Bedrock (Beta) | Google Cloud's Vertex AI (Beta) | Microsoft Foundry (Beta)

---

#### 2. 自適應思考

**描述**: 讓 Claude 動態決定何時以及思考多少。這是 Opus 4.6 推薦的思考模式。使用 effort 參數來控制思考深度。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 3. Agent Skills

**描述**: 透過 Skills 擴展 Claude 的能力。使用預建的 Skills（PowerPoint、Excel、Word、PDF）或使用指令和腳本建立自訂 Skills。Skills 使用漸進式揭露來有效管理上下文。

**可用性**: Claude API (Beta) | Microsoft Foundry (Beta)

---

#### 4. 批次處理

**描述**: 非同步處理大量請求以節省成本。每批次可發送大量查詢。Batch API 呼叫成本比標準 API 呼叫低 50%。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA)

---

#### 5. 引用

**描述**: 將 Claude 的回應建立在來源文件的基礎上。透過引用功能，Claude 可以提供其用於生成回應的確切句子和段落的詳細參考，從而產生更可驗證、更值得信賴的輸出。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 6. 壓縮

**描述**: 針對長時間對話的伺服器端上下文摘要。當上下文接近視窗限制時，API 會自動摘要對話的早期部分。支援 Opus 4.6 和 Haiku 4.5。

**可用性**: Claude API (Beta)

---

#### 7. 上下文編輯

**描述**: 使用可配置策略自動管理對話上下文。支援在接近 token 限制時清除工具結果，以及在延伸思考對話中管理思考區塊。

**可用性**: Claude API (Beta) | Amazon Bedrock (Beta) | Google Cloud's Vertex AI (Beta) | Microsoft Foundry (Beta)

---

#### 8. 資料駐留

**描述**: 使用地理控制來控制模型推論的執行位置。透過 inference_geo 參數為每個請求指定 "global" 或 "us" 路由。

**可用性**: Claude API (GA)

---

#### 9. Effort

**描述**: 使用 effort 參數控制 Claude 回應時使用的 token 數量，在回應完整性和 token 效率之間進行權衡。支援 Opus 4.6 和 Opus 4.5。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 10. 延伸思考

**描述**: 針對複雜任務的增強推理能力，在提供最終答案之前，透明展示 Claude 的逐步思考過程。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 11. Files API

**描述**: 上傳和管理檔案以與 Claude 一起使用，無需每次請求都重新上傳內容。支援 PDF、圖片和文字檔案。

**可用性**: Claude API (Beta) | Microsoft Foundry (Beta)

---

#### 12. PDF 支援

**描述**: 處理和分析 PDF 文件中的文字和視覺內容。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 13. 提示快取（5 分鐘）

**描述**: 為 Claude 提供更多背景知識和範例輸出，以降低成本和延遲。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 14. 提示快取（1 小時）

**描述**: 延長至 1 小時的快取持續時間，適用於存取頻率較低但重要的上下文，作為標準 5 分鐘快取的補充。

**可用性**: Claude API (GA) | Microsoft Foundry (GA)

---

#### 15. 搜尋結果

**描述**: 透過提供具有適當來源歸屬的搜尋結果，為 RAG 應用程式啟用自然引用。為自訂知識庫和工具實現網頁搜尋品質的引用。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 16. 結構化輸出

**描述**: 透過兩種方法保證 schema 一致性：用於結構化資料回應的 JSON 輸出，以及用於驗證工具輸入的嚴格工具使用。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Microsoft Foundry (Beta)

---

#### 17. Token 計數

**描述**: Token 計數讓您能在將訊息發送給 Claude 之前確定訊息中的 token 數量，幫助您對提示和使用量做出明智的決策。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 18. 工具使用

**描述**: 讓 Claude 能與外部工具和 API 互動，以執行更多種類的任務。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

### 工具

#### 1. Bash

**描述**: 執行 bash 命令和腳本，與系統 shell 互動並執行命令列操作。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 2. 程式碼執行

**描述**: 在沙盒環境中執行 Python 程式碼，進行進階資料分析。

**可用性**: Claude API (Beta) | Microsoft Foundry (Beta)

---

#### 3. 程式化工具呼叫

**描述**: 讓 Claude 能從程式碼執行容器中以程式化方式呼叫您的工具，減少多工具工作流程的延遲和 token 消耗。

**可用性**: Claude API (Beta) | Microsoft Foundry (Beta)

---

#### 4. 電腦使用

**描述**: 透過截圖和發出滑鼠及鍵盤命令來控制電腦介面。

**可用性**: Claude API (Beta) | Amazon Bedrock (Beta) | Google Cloud's Vertex AI (Beta) | Microsoft Foundry (Beta)

---

#### 5. 細粒度工具串流

**描述**: 無需緩衝/JSON 驗證即可串流工具使用參數，減少接收大型參數的延遲。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 6. MCP 連接器

**描述**: 直接從 Messages API 連接到遠端 MCP 伺服器，無需單獨的 MCP 客戶端。

**可用性**: Claude API (Beta) | Microsoft Foundry (Beta)

---

#### 7. 記憶

**描述**: 讓 Claude 能跨對話儲存和檢索資訊。隨時間建立知識庫、維護專案上下文，並從過去的互動中學習。

**可用性**: Claude API (Beta) | Amazon Bedrock (Beta) | Google Cloud's Vertex AI (Beta) | Microsoft Foundry (Beta)

---

#### 8. 文字編輯器

**描述**: 使用內建的文字編輯器介面建立和編輯文字檔案，用於檔案操作任務。

**可用性**: Claude API (GA) | Amazon Bedrock (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

#### 9. 工具搜尋

**描述**: 透過使用基於正規表達式的搜尋動態發現和載入工具，擴展至數千個工具，優化上下文使用並提高工具選擇準確性。

**可用性**: Claude API (Beta) | Amazon Bedrock (Beta) | Google Cloud's Vertex AI (Beta) | Microsoft Foundry (Beta)

---

#### 10. 網頁擷取

**描述**: 從指定的網頁和 PDF 文件中檢索完整內容，進行深入分析。

**可用性**: Claude API (Beta) | Microsoft Foundry (Beta)

---

#### 11. 網頁搜尋

**描述**: 使用來自網路的即時、真實世界資料來增強 Claude 的全面知識。

**可用性**: Claude API (GA) | Google Cloud's Vertex AI (GA) | Microsoft Foundry (GA)

---

## 🛠️ 工具使用

### 工具使用的運作方式

Claude 支援兩種類型的工具：

#### 客戶端工具

在您的系統上執行的工具，包括：
- 您建立和實作的使用者自定義工具
- Anthropic 定義的工具（如電腦使用和文字編輯器），需要客戶端實作

#### 伺服器端工具

在 Anthropic 伺服器上執行的工具，如網頁搜尋和網頁擷取工具。這些工具必須在 API 請求中指定，但不需要您進行實作。

---

### 客戶端工具工作流程

#### 步驟 1：向 Claude 提供工具和使用者提示

- 在您的 API 請求中定義客戶端工具，包含名稱、描述和輸入結構描述
- 包含可能需要這些工具的使用者提示，例如「舊金山的天氣如何？」

#### 步驟 2：Claude 決定使用工具

- Claude 評估是否有任何工具可以幫助處理使用者的查詢
- 如果有，Claude 會建構格式正確的工具使用請求
- 對於客戶端工具，API 回應的 stop_reason 為 tool_use，表示 Claude 的意圖

#### 步驟 3：執行工具並回傳結果

- 從 Claude 的請求中提取工具名稱和輸入
- 在您的系統上執行工具程式碼
- 在包含 tool_result 內容區塊的新 user 訊息中回傳結果

#### 步驟 4：Claude 使用工具結果來制定回應

- Claude 分析工具結果，為原始使用者提示製作最終回應

---

### 伺服器端工具工作流程

#### 步驟 1：向 Claude 提供工具和使用者提示

- 伺服器端工具（如網頁搜尋和網頁擷取）有其自己的參數
- 包含可能需要這些工具的使用者提示

#### 步驟 2：Claude 執行伺服器端工具

- Claude 評估伺服器端工具是否可以幫助處理使用者的查詢
- 如果可以，Claude 執行該工具，結果會自動納入 Claude 的回應中

#### 步驟 3：Claude 使用伺服器端工具結果來制定回應

- Claude 分析伺服器端工具結果，為原始使用者提示製作最終回應
- 伺服器端工具執行不需要額外的使用者互動

---

### 工具使用範例

#### 單一工具範例

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
  "model": "claude-opus-4-6",
  "max_tokens": 1024,
  "tools": [
    {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          }
        },
        "required": ["location"]
      }
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": "What is the weather like in San Francisco?"
    }
  ]
}'
```

---

#### 平行工具使用

Claude 可以在单个响应中调用多个工具，并行执行多个操作。

---

#### 多工具範例

可以定义多个工具，让 Claude 根据用户需求选择合适的工具。

---

#### 缺少資訊

如果用户提供的信息不足以调用工具，Claude 会请求更多信息。

---

#### 順序工具

某些任务需要按顺序调用多个工具，前一个工具的结果作为后一个工具的输入。

---

#### 思維鏈工具使用

Claude 可以在使用工具时展示其思考过程，提高透明度和可理解性。

---

## 🤖 Agent 技能

### 為什麼使用 Skills

Skills 是可重複使用的、基於檔案系統的資源，為 Claude 提供特定領域的專業知識：工作流程、上下文和最佳實踐，將通用代理轉變為專家。

#### 主要優勢

- **專業化 Claude**：為特定領域任務量身定制能力
- **減少重複**：建立一次，自動使用
- **組合能力**：結合多個 Skills 建構複雜的工作流程

---

### Skills 的運作方式

Skills 利用 Claude 的 VM 環境來提供超越提示詞所能實現的能力。Claude 在具有檔案系統存取權限的虛擬機器中運作，允許 Skills 以目錄形式存在，包含指令、可執行程式碼和參考資料。

#### 漸進式揭露

Claude 根據需要分階段載入資訊，而不是預先消耗上下文。

---

### 三種 Skill 內容類型，三個載入層級

#### 第 1 層：元資料（始終載入）

**內容類型**：指令。Skill 的 YAML 前置資料提供發現資訊：

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```

Claude 在啟動時載入此元資料並將其包含在系統提示中。

---

#### 第 2 層：指令（觸發時載入）

**內容類型**：指令。SKILL.md 的主體包含程序性知識：工作流程、最佳實踐和指導：

```markdown
# PDF Processing
## Quick start
Use pdfplumber to extract text from PDFs:
```python
import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
For advanced form filling, see [FORMS.md](FORMS.md).
```

當您的請求與某個 Skill 的描述匹配時，Claude 會透過 bash 從檔案系統讀取 SKILL.md。

---

#### 第 3 層：資源和程式碼（按需載入）

**內容類型**：指令、程式碼和資源。Skills 可以捆綁額外的材料：

```
pdf-skill/
├── SKILL.md (main instructions)
├── FORMS.md (form-filling guide)
├── REFERENCE.md (detailed API reference)
└── scripts/
    └── fill_form.py (utility script)
```

- **指令**：額外的 markdown 檔案（FORMS.md、REFERENCE.md），包含專門的指導和工作流程
- **程式碼**：可執行腳本（fill_form.py、validate.py），Claude 透過 bash 執行
- **資源**：參考資料，如資料庫結構描述、API 文件、範本或範例

---

### Skills 架構

Skills 在程式碼執行環境中運行，Claude 在其中擁有檔案系統存取權限、bash 命令和程式碼執行能力。

#### Claude 如何存取 Skill 內容

當 Skill 被觸發時，Claude 使用 bash 從檔案系統讀取 SKILL.md，將其指令帶入上下文視窗。如果這些指令引用了其他檔案（如 FORMS.md 或資料庫結構描述），Claude 也會使用額外的 bash 命令讀取這些檔案。

#### 此架構實現的功能

- **按需檔案存取**：Claude 只讀取每個特定任務所需的檔案
- **高效腳本執行**：當 Claude 執行 validate_form.py 時，腳本的程式碼永遠不會載入上下文視窗
- **捆綁內容無實際限制**：因為檔案在被存取之前不會消耗上下文

---

### Skills 的適用範圍

#### Claude API

Claude API 支援預建 Agent Skills 和自訂 Skills。

**先決條件**：透過 API 使用 Skills 需要三個 beta 標頭：
- code-execution-2025-08-25 - Skills 在程式碼執行容器中運行
- skills-2025-10-02 - 啟用 Skills 功能
- files-api-2025-04-14 - 用於向容器上傳/下載檔案

---

#### Claude Code

Claude Code 僅支援自訂 Skills。

**自訂 Skills**：建立包含 SKILL.md 檔案的目錄作為 Skills。Claude 會自動發現並使用它們。

---

#### Claude Agent SDK

Claude Agent SDK 透過基於檔案系統的配置支援自訂 Skills。

**自訂 Skills**：在 .claude/skills/ 中建立包含 SKILL.md 檔案的目錄。

---

#### Claude.ai

Claude.ai 支援預建 Agent Skills 和自訂 Skills。

**預建 Agent Skills**：當您建立文件時，這些 Skills 已在幕後運作。

**自訂 Skills**：透過設定 > 功能，以 zip 檔案形式上傳您自己的 Skills。

---

### Skill 結構

每個 Skill 都需要一個包含 YAML 前置資料的 SKILL.md 檔案：

```yaml
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---
# Your Skill Name
## Instructions
[Clear, step-by-step guidance for Claude to follow]
## Examples
[Concrete examples of using this Skill]
```

#### 必填欄位

- name：最多 64 個字元，只能包含小寫字母、數字和連字號
- description：不能為空，最多 1024 個字元

---

### 安全考量

我們強烈建議僅使用來自可信來源的 Skills：您自己建立的或從 Anthropic 獲取的。

#### 主要安全考量

- **徹底審查**：檢查 Skill 中捆綁的所有檔案
- **外部來源有風險**：從外部 URL 獲取資料的 Skills 具有特別的風險
- **工具濫用**：惡意 Skills 可以以有害方式呼叫工具
- **資料暴露**：具有敏感資料存取權限的 Skills 可能被設計為向外部系統洩露資訊
- **視同安裝軟體**：僅使用來自可信來源的 Skills

---

### 可用 Skills

#### 預建 Agent Skills

- **PowerPoint (pptx)**：建立簡報、編輯投影片、分析簡報內容
- **Excel (xlsx)**：建立試算表、分析資料、生成帶圖表的報告
- **Word (docx)**：建立文件、編輯內容、格式化文字
- **PDF (pdf)**：生成格式化的 PDF 文件和報告

---

## 📝 提示工程

### 概覽

提示工程是设计和优化提示词以获得 Claude 最佳响应的艺术和科学。

---

### 提示產生器

使用提示產生器工具来创建和优化提示词。

---

### 使用提示範本

使用提示範本来标准化和重用提示词。

---

### 提示改進器

使用提示改進器来优化和改进现有的提示词。

---

### 清晰直接

- **明确目标**：清楚地说明您希望 Claude 完成什么
- **提供上下文**：给 Claude 足够的背景信息
- **使用具体语言**：避免模糊和歧义的表达

---

### 使用範例（多範例提示）

提供多个示例来指导 Claude 的输出格式和风格。

---

### 讓 Claude 思考（CoT）

鼓励 Claude 展示其思考过程，特别是在复杂任务中。

---

### 使用 XML 標籤

使用 XML 标签来组织提示词的结构，提高可读性。

---

### 賦予 Claude 角色（系統提示）

通过系统提示赋予 Claude 特定的角色或专业身份。

---

### 串連複雜提示

将复杂任务分解为多个简单的提示词，按顺序执行。

---

### 長上下文技巧

- **分块处理**：将长文档分成小块处理
- **摘要关键信息**：先摘要再详细分析
- **使用引用**：明确引用文档中的具体部分

---

### 延伸思考技巧

- **明确要求思考步骤**：要求 Claude 展示其推理过程
- **验证思考结果**：检查 Claude 的思考逻辑是否合理
- **迭代优化**：根据思考结果调整提示词

---

## 🧪 测试与评估

### 定義成功標準

- **明确目标**：定义清晰的成功指标
- **量化标准**：使用可量化的评估标准
- **多维度评估**：从多个角度评估性能

---

### 開發測試案例

- **覆盖边界情况**：测试极端和异常情况
- **多样化输入**：使用不同类型的输入进行测试
- **自动化测试**：建立自动化测试流程

---

### 使用評估工具

使用 Anthropic 提供的评估工具来评估 Claude 的性能。

---

### 降低延遲

- **优化提示词**：简化提示词，减少不必要的上下文
- **使用缓存**：利用提示缓存功能
- **选择合适的模型**：根据任务需求选择模型

---

### 強化防護機制

#### 減少幻覺

- **提供事实依据**：给 Claude 提供准确的事实和数据
- **要求引用**：要求 Claude 引用信息来源
- **验证输出**：独立验证 Claude 的输出

---

#### 提高輸出一致性

- **使用一致的提示词格式**：标准化提示词结构
- **提供明确的指导**：给出明确的输出格式要求
- **使用示例**：提供输出格式的示例

---

#### 防範越獄攻擊

- **输入验证**：验证用户输入，防止恶意提示
- **输出过滤**：过滤不当或危险的输出
- **使用安全模式**：启用 Claude 的安全功能

---

## 📊 管理与监控

### Admin API 概覽

使用 Admin API 来管理 Claude 的使用和配置。

---

### 資料駐留

控制数据存储和处理的地理位置。

---

### 工作區

使用工作区来组织和管理 Claude 的使用。

---

### 用量與成本 API

监控 Claude 的使用量和成本。

---

### Claude Code Analytics API

获取 Claude Code 的使用分析数据。

---

### 零資料保留

配置 Claude 不保留任何用户数据。

---

## 🎯 后续步骤

### 官方资源

- **Claude API Docs**: https://platform.claude.com/docs/zh-TW/home
- **Claude Cookbook**: https://platform.claude.com/cookbooks
- **Claude Help Center**: https://support.claude.com/
- **Anthropic Engineering Blog**: https://www.anthropic.com/engineering

---

### 学习路径

1. **快速開始**: 完成 Claude API 快速开始指南
2. **工具使用**: 学习如何使用 Claude 的工具功能
3. **Agent 技能**: 掌握 Agent Skills 的使用和创建
4. **提示工程**: 深入学习提示工程技巧
5. **测试与评估**: 建立完善的测试和评估体系
6. **管理与监控**: 实施 Claude 的管理和监控策略

---

## 📚 相关文档

- [30天实战训练营](./30-DAY-BOOTCAMP.md)
- [Claude Code 学习指南](./docs/claude-code-learning-guide.md)
- [官方文档深度分析](./docs/claude-code-official-analysis-part1.md)

---

**文档来源**: Claude 官方文档 (繁体中文)
**整合时间**: 2026-03-23
**整合者**: Assistant (OpenClaw)
