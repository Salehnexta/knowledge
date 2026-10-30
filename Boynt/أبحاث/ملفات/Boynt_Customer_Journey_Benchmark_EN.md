# Boynt: journey and design benchmark

Date: 2026-10-30. Method: standard web search plus primary docs where they were reachable. Evidence grades: **P** = vendor's own docs or launch post, **R** = peer-reviewed or institutional research, **S** = secondary (trade press, partner blog, review site). Most vendor numbers are self-reported.

## 1. Product benchmark (17 products)

### A. Agentic chat + canvas

| Product | Journey and first screen | Approval | What keeps people coming back | Evidence |
|---|---|---|---|---|
| Layla.ai | Landing page says "now it takes one sentence". Five stages: AI plans, a human expert gets to know you, plan finalised in 48h, booking in under 1h, 24/7 on call. Shows ready-made trip cards that can be "remixed". | The user approves the final plan. A human expert reviews it before booking. | A complete result from the first prompt, plus a human backstop. | P [layla.ai](https://layla.ai); map plus chat layout from S only [screensdesign](https://screensdesign.com/showcase/layla-ai-trip-planner) |
| ChatGPT Canvas | The canvas opens on the right when the output is long. You can select a passage and ask for an edit to it. | Inline suggestions that you accept or ignore. "Show changes", plus back arrows to restore a version. | Versioned co-editing. | P [help.openai.com](https://help.openai.com/en/articles/9930697) |
| ChatGPT Agent | Long multi-step runs with visible browsing. | Pauses for personal data and asks before submitting. NN/g calls these gates the best-working part. | Not observed. NN/g rated it "slow" and "shaky". | R/S [NN/g](https://www.nngroup.com/articles/impressions-chatgpt-agent/) |
| Claude artifacts | The artifact opens in a dedicated window beside the chat. Each publish is a version that can be shared. | Not applicable. | Shareable, versioned outputs. | P [support.claude.com](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) |
| Perplexity Labs | Every project has tabs: Tasks (the steps taken), Assets (CSV, charts), App (dashboards), Sources. | Not applicable. | The process and its sources stay inspectable next to the output. | S [InfoQ](https://www.infoq.com/news/2025/06/perplexity-labs), [The Register](https://www.theregister.com/2025/05/30/perplexity_labs_ai_agent/) |
| D365 SCM Procurement Agent | Reads supplier emails and PDFs, classifies them (confirmation, quantity, price, date change) and matches them to the PO line. It also drafts follow-ups for unconfirmed POs (for example after 7 days) or late ones. | Follow-ups are either sent automatically or saved as drafts for human review. Each detected change is summarised as old vs new value and flagged for buyer approval. | Removes repetitive work from the inbox. | P [Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-agent-supplier-com-overview) |
| Salesforce Agentforce | One primary agent is the "single point of contact" and routes work to specialist agents behind the scenes. The guidance is to connect no more than 7 subagents. | Not covered. | One conversation for everything. | P [salesforce.com](https://www.salesforce.com/agentforce/multi-agent-orchestration/), [admin blog](https://admin.salesforce.com/blog/2026/what-is-soma-and-when-to-build-a-super-agent-or-a-single-agent) |
| Copilot Studio | Connected agents' results are merged into one answer. Whether a connected agent is visible in the conversation is a configuration choice. | Not covered. | Not covered. | P [Microsoft blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-multi-agent-orchestration-connected-experiences-and-faster-prompt-iteration/) |
| Glean Assistant | The Home page has cards. The 2026 assistant "brings priority work to you" before you ask. | Not covered. | Proactive, role-based feed. | P [Glean press](https://www.glean.com/press/gleans-latest-ai-assistant-moves-every-employee-from-insight-to-execution), [docs](https://docs.glean.com/administration/management/customization/home-page) |
| Decagon / Sierra | A supervisor model checks responses in real time. Flagged conversations feed a regular review of the agent's operating procedures. A handoff to a human states what the customer wants and what the AI already tried. | Escalation to a human. | The procedures improve from reviewed cases. | P/S [Decagon](https://decagon.ai/blog/from-sops-to-agent-operating-procedures), [Featurebase](https://www.featurebase.app/blog/decagon-vs-sierra.md) |

### B. Control towers and inventory planning

| Product | Journey and first screen | Approval | What keeps people coming back | Evidence |
|---|---|---|---|---|
| Kinaxis Maestro Agents (Oct 2025) and Agent Studio (Feb 2026) | Agents sit inside the planning environment. They flag issues and recommend the "next-best action". | Human-in-the-loop guardrails. Orchestrator agents are planned. | Decisions are made where the data already is. | P [BusinessWire](https://www.businesswire.com/news/home/20251017746583/en/Kinaxis-Accelerates-Agentic-Era-for-Supply-Chain-Orchestration-with-the-Launch-of-Maestro-Agents) |
| Blue Yonder Inventory Ops Agent (ICON 2025) | Diagnoses supply/demand mismatches and their root causes, then proposes fixes (alternate source, demand swap). Works on a see, analyze, decide, act loop. Agent activation is quoted at 6–12 weeks. | Routine decisions are automated. Critical ones are "flagged for human approval". | Graduated autonomy. | S/P [SupplyChainDigital](https://supplychaindigital.com/technology/blue-yonder-unveils-five-ai-agents) |
| o9 | Control tower with root-cause analysis, recommended actions and what-if scenarios with their financial trade-offs. | Not covered. | Every decision is costed. | S [01net](https://www.01net.it/o9-solutions-named-a-leader-in-2026-nucleus-research-control-tower-technology-value-matrix/) |
| Netstock | Data load, then validation, then an onboarding specialist reviews the *suggested orders* with you. Live in "90 days or less". Its "Prioritized Dashboard" shows where action is needed, and an executive dashboard shows inventory health and supplier service. | Suggested orders go out as POs. | Claims of 70% less planning time and ordering cut "from hours to minutes". | P/S [netstock.com](https://www.netstock.com/customer-success/), [softwareconnect](https://softwareconnect.com/reviews/netstock/) |
| Inventory Planner (Cin7) | Connect with an API key. The first sync pulls products, sales history, vendors and past POs, then refreshes every 24h. You set lead time and days of stock, and get purchase and transfer recommendations per location. | You edit the PO, and it syncs back to the ERP. | Daily reorder list. | P [help.inventory-planner.com](https://help.inventory-planner.com/en/articles/3408341-cin7-core-dear-integration) |
| Odoo Inventory | Replenishment report. Manual rules *suggest* orders and automatic rules *create* them. | No approval step before the RFQ in standard Odoo, so a third-party app exists to add one. | It is the ERP itself. | P/S [Odoo apps](https://apps.odoo.com/apps/modules/18.0/fal_replenishment_approval), [cleverence](https://www.cleverence.com/articles/odoo-documentation/reordering-rules-odoo-documentation-2735/) |
| Lokad | One ranked list of purchase lines ordered by economic score. Buyers buy "from the top until the budget is exhausted". Recommendations are described as "justified and can be challenged". | Buyers execute the list. | A simple decision artifact. | P [docs.lokad.com](https://docs.lokad.com/how-to/economic-purchase-prioritization/) |

### C. Agent builders

| Product | Approval and visibility pattern | Evidence |
|---|---|---|
| Relevance AI | A Task View with tabs for Approvals, Escalated (the agent asks a question) and Errors. An escalated task is highlighted and shows the agent's stated reason. A manager agent can decide whether to run on its own or ask for approval. | P [relevanceai.com docs](https://relevanceai.com/docs/build/agents/give-your-agent-tasks/tasks-page) |
| Lindy | An "Ask for confirmation" setting on each action. Reported per-integration settings: "Always allow / Require approval / Don't offer". Reads are never gated. | P [lindy.ai](https://lindy.ai/academy-lessons/ai-agents); S [automationatlas](https://automationatlas.io/guides/moxo-vs-lindy-2026/) |
| Zapier Agents | A Human-in-the-Loop step pauses the run. Approval requests arrive by email or Slack. | P [help.zapier.com](https://help.zapier.com/hc/en-us/articles/41776074420493) |
| n8n | Approval can gate a single tool call, and the reviewer sees the tool's name and parameters. Approval works over Slack, email or WhatsApp buttons, with timeouts and fallback actions. | S [growwstacks](https://growwstacks.com/blog/human-in-the-loop-n8n-guide), [nordflux](https://nordflux.de/es/guias/human-in-the-loop-pasos-de-aprobacion-para-agentes) |

### What the leaders do across these products

- **Time to value:** The fastest products show a useful object on the first session: Layla's plan, Inventory Planner's reorder list after the first sync, Netstock's suggested orders. Enterprise tools take 6–12 weeks (Blue Yonder) to 90 days (Netstock).
- **Onboarding:** It is a data sync followed by a few parameters (lead time, days of stock), then a guided review of the first recommendations. Netstock assigns a specialist for that review.
- **Daily loop:** The pattern is a prioritised exception list (Netstock, Lokad, Relevance Approvals tab) plus a proactive feed (Glean). Agents do the inbox work (D365).
- **Approvals:** The pattern is graduated (Blue Yonder, D365 auto-send vs draft, Lindy per-integration). The approval card shows an old→new diff and a reason, and approval is possible from outside the app (Zapier, n8n via Slack/WhatsApp).
- **Escalation:** Explicit "Escalated/Errors" states (Relevance). Handoff notes say what the AI already tried (Decagon). A human expert stays behind the AI (Layla).
- **Weekly loop:** Executive health dashboards and KPIs track "real-world impact of decisions" (Netstock, Lokad). This is thinly documented across vendors.

## 2. Multi-agent visibility

**Vendor pattern.** The large platforms default to *one front door*. Agentforce has a single primary agent with specialists behind it. Copilot Studio merges results into one answer, with connected-agent visibility left optional. Kinaxis plans orchestrator agents. The products that show agents openly are builder tools (Relevance, Lindy), whose users design the agents themselves.

**Research.**
- When a single assistant was compared with a team of four expert chatbots, users reached their goals equally well. Users of the team version predicted agent behaviour better, with no extra coordination cost ([arXiv 1808.08157](https://arxiv.org/abs/1808.08157)). R
- In another study, a multi-agent setup raised perceived warmth, helpfulness and persuasion ([arXiv 1904.05248](https://arxiv.org/pdf/1904.05248)). Persuasion is a risk when the goal is calibrated trust. R
- Findings on how much a human-like agent affects trust are mixed. A 2025 survey says research on trust in multi-agent systems is "largely unexplored" ([arXiv 2503.09648](https://arxiv.org/pdf/2503.09648)). R
- In a user study of multi-agent LLM interfaces, the transparency people needed depended on the task and on the user's expertise ([synapsesocial listing](https://www.synapsesocial.com/papers/6a18262eaeefdf6d9c136abe)). R, abstract only
- Microsoft's design principles for agents say connections between agents should be "transparent and customizable", background agents need "a user-facing way to view and control their actions", and "agent status… clearly visible at all times". They also ask designers to reduce cognitive load and to "nudge more than notify" ([microsoft.design](https://microsoft.design/articles/ux-design-for-agents/)). P
- The HAX guideline G11 asks products to "make clear why the system did what it did" ([HAX toolkit](https://www.microsoft.com/en-us/haxtoolkit/library/pattern/)). PAIR says trust should be calibrated, not maximised ([PAIR](https://pair.withgoogle.com/chapter/explainability-trust/)). R/P

**Trade-offs.**
- **Named agent team:** It shows the system's scope and gives each alert a clear owner. Against it: more to learn, it can persuade more than it should, and people start to anthropomorphise the agents.
- **One hidden assistant:** It is simpler to use. Against it: users cannot tell which module produced an alert, and accountability is unclear.

**Recommendation: hybrid.** Keep one assistant in the chat as the only voice. Put a small *functional* badge on each alert, approval and canvas item: "Inventory", "Supplier", "Quality", "Planning". Use icons, not faces or human names. Add an "Agents" view that shows each agent's status, its last actions and its autonomy setting. This follows the platform default, Microsoft's visibility principle and the scope-clarity finding. It also avoids the persuasion effect.

For Saudi SMB and mid-market users, a single Arabic-speaking assistant is the easier mental model. Function labels match their department structure (purchasing, warehouse, quality).

## 3. Chat + live canvas patterns

1. **Canvas follows chat.** Each answer focuses the canvas: open the warehouse rack, highlight a lot, filter the network. Selecting something on the canvas sets the chat context, as ChatGPT Canvas does with selected text ([OpenAI](https://help.openai.com/en/articles/9930697)).
2. **Diffs, not prose.** Show proposed changes as old→new fields, as D365 does for supplier changes, with "Show changes" and version restore as in Canvas.
3. **Traceability.** Every number links to its source: the ERP record, the supplier message or the forecast run. Perplexity's Tasks and Sources tabs are the model. Lokad shows that recommendations should be "justified and can be challenged".
4. **"Why" on every recommendation.** Give a local explanation and a what-if (HAX G11 patterns), plus a confidence level (Microsoft's "show certainty").
5. **Undo and reversibility.** Gate only irreversible or external actions: sending to a supplier, issuing a PO. Leave reads and drafts ungated (Lindy; NN/g warns that too many gates destroy the value).
6. **Progress visibility.** Show which step the agent is on and flag any substitution prominently (NN/g).
7. **Mobile.** Approvals must work outside the canvas, as Slack/email buttons do in Zapier and n8n. For Boynt that means WhatsApp.

## 4. Saudi and GCC context

- **WhatsApp:** It is the most-used app among Saudi adults (national poll, n=1,220; [Arab News](https://arabnews.com/node/2054631/)). Penetration is about 80%, and business WhatsApp use in Saudi Arabia, the UAE and Qatar grew 43%→82% (Infobip via [CampaignMe](https://campaignme.com/messaging-in-mena-is-entering-a-new-phase-and-marketers-must-adapt-fast/), S). Note that SAMA bars banks from contacting customers over WhatsApp. That rule does not cover B2B supplier messages, but it is a signal for anything touching payments.
- **Hierarchy:** Saudi Arabia's power-distance score is reported as 95, which suggests centralised decisions ([koreascience](https://koreascience.or.kr/article/JAKO202221643444556.pdf), S). A survey of 230 Saudi ERP users found that power distance did *not* predict resistance to ERP, while uncertainty avoidance did ([UNE](https://rune.une.edu.au/web/handle/1959.11/16836?mode=full), R). In practice, build in owner or manager approval thresholds and reduce uncertainty: show why, show the source, allow undo.
- **ZATCA e-invoicing:** Phase 2 is reaching smaller firms. Wave 24 (SAR 375k–750k turnover) was due by 30 June 2026, and Wave 25 goes live in Feb 2027 ([EY](https://globaltaxnews.ey.com/news/2026-1705-saudi-arabia-announces-25th-wave-of-phase-2-e-invoicing-integration)). Structured supplier invoices make PO, receipt and invoice matching feasible.
- **Gaps:** I found no Saudi-specific survey of B2B buyer WhatsApp use and no data on Arabic UI preference. Validate both in customer interviews.

## 5. Ranked recommendations for Boynt

1. **First value inside session one.** Connect Odoo, sync, then show the Control Tower with the top 5 reorder or expiry exceptions and a draft PO. Do not show an empty canvas. *Evidence:* Inventory Planner's first sync, Netstock's suggested-order review, Layla's one sentence to a full plan.
2. **One assistant, function badges, and an Agents status page.** No persona avatars. *Evidence:* Agentforce and Copilot Studio defaults, Microsoft's visibility principle, scope clarity in arXiv 1808.08157, persuasion risk in 1904.05248.
3. **A morning brief as a ranked exception list.** Order it by money or risk (stockout cost, expiring value) and let users work it from the top. *Evidence:* Lokad's prioritised list, Netstock's Prioritized Dashboard, Glean's proactive Home.
4. **Graduated autonomy per action type.** Settings: auto, draft-for-review, never. Supplier reminders could start as drafts. *Evidence:* D365 auto-send vs draft, Lindy per-integration settings, Blue Yonder routine vs critical.
5. **The approval card is a diff plus a why plus a source.** Show old→new quantity, price or date, the reason, the confidence and a link to the supplier message or record. *Evidence:* D365 change summaries, HAX G11, Perplexity Sources, Microsoft's certainty principle.
6. **Approve from WhatsApp.** Send a one-tap Approve or Dismiss with a deep link to the canvas, and set a timeout with escalation to the next approver. *Evidence:* Zapier and n8n approvals outside the app, Saudi WhatsApp penetration.
7. **Approval thresholds by role and amount.** Fill the gap Odoo leaves, since it has no native pre-RFQ approval. *Evidence:* the fal_replenishment_approval module, high power distance (reported score 95).
8. **Explicit Escalated and Errors states.** Each handoff note states what the agent already tried. *Evidence:* Relevance AI Task View, Decagon handoff guidance.
9. **The canvas reacts to chat, and the chat reacts to selection, with version restore.** *Evidence:* ChatGPT Canvas, Claude artifacts, NN/g progress visibility.
10. **A weekly "decisions and impact" report.** Cover approved vs dismissed actions, the outcome of each (avoided stockouts, write-offs), and agent accuracy. Use dismissals to tune the rules. *Evidence:* Lokad's impact KPIs, Decagon's review loop, PAIR's trust calibration over time.
