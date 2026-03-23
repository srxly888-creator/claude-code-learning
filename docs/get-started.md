# 開始使用 Claude

> 進行您的第一次 Claude API 呼叫並建立一個簡單的網路搜尋助手

---

## 先決條件

- • 一個 Anthropic Console 帳戶
- • 一個 API 金鑰

---

## 呼叫 API

### 1. 設定您的 API 金鑰

在 [Claude Console](https://console.anthropic.com/settings/keys) 取得您的 API 金鑰並將其設定為環境變數：

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### 2. 進行您的第一次 API 呼叫

執行此命令以建立一個簡單的網路搜尋助手：

#### cURL

```bash
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
  "model": "claude-opus-4-6",
  "max_tokens": 1000,
  "messages": [
    {
      "role": "user",
      "content": "What should I search for to find the latest developments in renewable energy?"
    }
  ]
}'
```

#### Python

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?"
        }
    ]
)

print(message.content)
```

#### TypeScript

```typescript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const msg = await anthropic.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1000,
  messages: [
    {
      role: "user",
      content: "What should I search for to find the latest developments in renewable energy?",
    },
  ],
});

console.log(msg);
```

#### Java

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;

AnthropicClient client = AnthropicOkHttpClient.create();

MessageCreateParams params = MessageCreateParams.builder()
    .model("claude-opus-4-6")
    .maxTokens(1000L)
    .addUserMessage("What should I search for to find the latest developments in renewable energy?")
    .build();

Message message = client.messages().create(params);

System.out.println(message.content());
```

---

### 範例輸出

```json
{
  "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Check:\n\n**News & Industry Sites:**\n- Renewable Energy World\n- GreenTech Media (now Wood Mackenzie)\n- Energy Storage News\n- CleanTechnica\n- PV Magazine (for solar)\n- WindPower Engineering & Development..."
    }
  ],
  "model": "claude-opus-4-6",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 21,
    "output_tokens": 305
  }
}
```

---

## 後續步驟

現在您已經完成了第一次 Claude API 請求，是時候探索更多可能性了：

### 1. 使用 Messages

學習 Messages API 的常見模式。

**路徑：** `/docs/zh-TW/build-with-claude/working-with-messages`

### 2. 功能概覽

探索 Claude 的進階功能與能力。

**路徑：** `/docs/zh-TW/api/overview`

### 3. 客戶端 SDK

探索 Anthropic 客戶端程式庫。

**路徑：** `/docs/zh-TW/api/client-sdks`

### 4. Claude Cookbook

透過互動式 Jupyter 筆記本學習。

**路徑：** `https://platform.claude.com/cookbooks`

---

## 相關連結

### Solutions
- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners
- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn
- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company
- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Help and security
- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies
- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)

---

**文檔來源：** https://platform.claude.com/docs/zh-TW/get-started  
**整理時間：** 2026-03-23  
**整理者：** Assistant (OpenClaw)
