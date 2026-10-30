# Boynt: habit formation and sign-up personas (research note, 2026-10-30)

Evidence grades: **[P]** primary source (paper, vendor docs, regulator, founder's own words); **[S]** secondary (credible interview or teardown); **[W]** weak (vendor blog, widely repeated but unverified). Where no evidence was found, this is stated.

## 1. Habit and lasting impact

### Core models
- **Fogg Behavior Model, B = MAP**: a behavior happens when motivation, ability and a prompt converge at the same moment. Low motivation can be offset by high ability (making the action easier), and without a prompt nothing happens [P] https://behaviormodel.org/. Tiny Habits: anchor a very small behavior to an existing routine ("after I open WhatsApp in the morning, I glance at the brief") [P] https://tinyhabits.com/.
- **Habit formation takes time**: in Lally et al. (2010), automaticity took 18–254 days to plateau, with a median of 66. Missing one day did not derail it [P] https://doi.org/10.1002/ejsp.674. Habits form around a **stable context cue** (time, place, preceding action) [P] Wood & Neal 2007, https://doi.org/10.1037/0033-295X.114.4.843. Implication: the first session cannot create a habit on its own. What it can do is install a cue and a reason to come back tomorrow.
- **Hook model** (trigger → action → variable reward → investment) [S] https://www.nirandfar.com/how-to-manufacture-desire/. In B2B the "variable reward" should mean **variable information**: which approvals are waiting today, which branch is at risk. Slot-machine mechanics do not belong here. Eyal's own ethics test ("would I use it, and does it help the user?") is in the same source. Evidence that Hook mechanics specifically drive B2B retention is mostly anecdotal. No controlled B2B studies were found.

### Activation ("aha") examples and how reliable they are
- **Slack**: Butterfield's statement that teams which had exchanged about 2,000 messages had "really tried" Slack, and that 93% of them were still using it. Reported in Andrew Chen's *The Cold Start Problem* [S] https://www.goodreads.com/notes/56962799-the-cold-start-problem/84411704-mikko-ikola/435bc888-c6a7-45f1-83c2-6c66617e1ab2. The threshold is team-level, not user-level.
- **Facebook "7 friends in 10 days"**: Chamath Palihapitiya's growth-team talks [W]. Widely repeated, but no primary transcript was located.
- **Dropbox** ("one file in one folder on one device") and **HubSpot** activation thresholds [W]. These circulate only in blogs. Do not cite them as data.
- **Superhuman**: every new user got a roughly 30-minute 1:1 onboarding call before access. This was later turned into in-product onboarding [S] https://review.firstround.com/superhuman-onboarding-playbook/. Founders and teardowns say it improved retention, but no figures have been published.
- **Figma**: the value appears when a second person edits the same file live (multiplayer) [P on mechanism] https://www.figma.com/blog/how-figmas-multiplayer-technology-works/.
- **Notion/Linear**: Notion asks about use case and team at sign-up and fills the workspace with templates. Linear walks the user through a short guided setup. Both are product observations. No published outcome data exists.
- **Lesson across these cases**: each "aha" is a **collaborative or real-data event**, not a tour completed. Each was found by correlating early behavior with later retention, not by assumption.

### Benchmarks
- Average B2B SaaS time-to-value (TTV) is about 1 day 12 h, with a median of about 1 day 2 h (Userpilot, 547 companies). The report itself was not retrieved, so these figures come via summaries [W] https://userpilot.com/saas-product-metrics/.
- OpenView: about 20–40% of free or trial users activate. Free-to-paid conversion is about 3–5% for no-card trials versus about 18–25% when a card is required up front. The card-trial figure is through secondary roundups [S/W] https://openviewpartners.com/2022-product-benchmarks-calculator, https://openviewpartners.com/blog/2020-saas-product-benchmarks.
- Pendo found that about 80% of features are rarely or never used. This argues for a narrow first path [S] https://www.pendo.io/resources/the-2019-feature-adoption-report/.

### Ten mechanisms mapped to Boynt

| # | Mechanism (evidence) | Boynt implementation |
|---|---|---|
| 1 | **Real data before value** (aha = real-data event; Pendo) | The first canvas uses the company's own ERP or uploaded data: one real stock-out risk and one overdue PO. Show sample data only if the connection is pending, and label it "sample". |
| 2 | **Stable external cue** (Fogg prompt; Wood & Neal context) | A daily morning brief on WhatsApp at a time the user picks (e.g. 7:30), with 3 lines plus one deep link. The same time every day forms the habit cue. |
| 3 | **Ability: act where the cue arrives** (B=MAP ability) | Approve or reject a PO or transfer directly from WhatsApp with one tap, within the user's approval limit. Open the canvas only for exceptions. |
| 4 | **Variable but useful information** (Hook, ethical form) | The brief ranks today's real exceptions: branch X has 3 days of cover on SKU Y, and supplier Z is late. No streaks, no fake urgency. |
| 5 | **Team-level activation** (Slack 2,000 messages; Figma multiplayer) | Define activation at the **company** level, e.g. at least 3 roles active and at least 1 approval completed end-to-end in 7 days. Finalize the threshold once retention data exists. |
| 6 | **Investment / stored value** (Hook investment; IKEA effect, Norton et al. 2012 https://doi.org/10.1016/j.jcps.2011.08.002) | Approval limits, reorder rules, branch structure and agent-built workflows are kept as company assets the user owns. Each one makes the next brief more accurate. |
| 7 | **Endowed progress** (Nunes & Drèze 2006 https://doi.org/10.1086/500480) | The setup checklist starts partly complete ("company created, 2 of 6 done") and shows what each step unlocks. |
| 8 | **Visible outcome feedback** (Superhuman measured value; no B2B RCT found) | A weekly "what changed" card: approvals cleared and median approval time (before vs. now), stock-outs avoided, hours saved, with the calculation shown. Use conservative numbers and let the user open the calculation. |
| 9 | **Human-assisted first session for larger accounts** (Superhuman) | Offer an optional 30-minute setup call (Arabic or English) for mid-market sign-ups. Keep it optional for SMBs. |
| 10 | **Reduce the first task to the smallest useful action** (Tiny Habits) | Finish session 1 with one committed action, such as "set the reorder alert for your top 20 SKUs", not a full setup. |

**Measuring "life change"**: use operational KPIs the user already tracks, such as approval cycle time, stock-out days per SKU-branch, PO-to-receipt lead time and manual report hours. Record a baseline in week 1 (from ERP history or the user's own estimate, labeled as such) and compare from week 4. No published benchmark was found for "hours saved" claims in operations software. Treat vendor ROI claims as unreliable.

## 2. Who signs up: three personas

### How leading products branch by role (observed behavior plus docs)
- **Asking role or purpose at sign-up**: Monday.com, Notion and HubSpot ask about role, team size and use case, then pre-load templates. This is product observation. None publish the uplift.
- **Asking the admin**: Slack lets members "Request to install" an app with a note to the admin when app approval is on [P] https://slack.com/help/articles/202035138. Microsoft Entra has an "admin consent workflow" where users ask an admin to approve an app's data permissions [P] https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow. Atlassian Marketplace apps can be requested by non-admins [P, product docs].
- **Champion to buyer**: OpenView's PLG reports describe product-qualified leads, where usage signals hand off to sales. No public conversion rate for a champion upgrading their owner was found.

### Persona A: Owner/CEO (likely buyer and often the signer in Saudi SMBs)
- **Goals**: visibility across branches without calling managers, cash tied up in stock, control of spending.
- **Fears**: wasted time, staff resistance, data leaking, AI giving wrong numbers.
- **First screen**: an executive cockpit with 4 KPIs. Use real data if they connect, otherwise a labeled sample of their sector. One question prompt: "What do you want to know every morning?"
- **5-minute path**: name company and branches (count) → pick the 3 things they want in the morning brief → enter WhatsApp number → delegate the ERP connection.
- **Delegate**: "Connect ERP" to IT, and "Import branches/employees and set approval limits" to the operations manager. Use a pre-filled WhatsApp or email invite: "[Owner] asked you to connect [ERP] to Boynt; takes ~10 min; read-only access; link expires 72 h."
- **Aha**: the first morning brief with their own numbers, plus their first approval done from WhatsApp.
- **Triggers**: D1 first brief; D3 "Your ops manager set approval limits — approve the first PO here"; D7 weekly summary of approvals and exceptions; D14 before/after card, then a decision on paying.

### Persona B: Operations/Purchasing manager (champion, no admin rights)
- **Goals**: fewer stock-outs, fewer calls from branches, a faster PO cycle, credit with the owner.
- **Fears**: losing control to the owner's view, extra data entry, blame for wrong numbers.
- **First screen**: control tower or warehouse view, plus a "what needs action today" list.
- **5-minute path**: upload an Excel or CSV of stock by branch (no ERP access needed) → see a stock-cover forecast → set one reorder rule.
- **Delegate**: ERP credentials to IT, and approval of the budget to the owner. Send a one-tap "share this view with [owner]" with a 3-line summary of what was found.
- **Aha**: the first exception he did not already know about, such as a SKU about to stock out at branch X.
- **Triggers**: D1 exceptions brief; D3 "IT hasn't connected yet — resend the request?"; D7 suggestion to invite branch managers; D14 a ready-made report for the owner to sponsor the purchase.

### Persona C: IT manager (admin, security-minded)
- **Goals**: control, least-privilege access, auditability, no shadow IT.
- **Fears**: write access to the ERP, data stored outside the Kingdom, AI acting without logs, WhatsApp as an uncontrolled channel.
- **First screen**: a trust panel showing data scopes requested (read-only by default), hosting location, the audit log, SSO options and role mapping.
- **5-minute path**: review scopes → approve the connector (read-only) → map roles → enable SSO (Microsoft Entra/Google) or defer it.
- **Delegate**: business configuration (limits, workflows) back to the operations manager.
- **Aha**: an audit log showing every agent action and every WhatsApp approval, with user, time and before/after values.
- **Triggers**: D1 connector health; D3 access review summary; D7 audit digest; D14 security pack (DPA, hosting, sub-processors).

### When the signer lacks ERP credentials
Never block on the connection. Offer three paths in parallel: (1) file upload (Excel/CSV), (2) an "ask IT" invite that carries context and a scoped, expiring link, following the Slack and Entra request-to-admin pattern, (3) a labeled sample workspace. Show the delegated step's status on the checklist ("waiting for Ahmed, IT").

## 3. GCC/Saudi specifics

- **WhatsApp**: 92.2% of Saudi internet users use WhatsApp, the top app (CST *Saudi Internet 2024*) [P via report coverage] https://bridgemena.com/news/saudi-internet-report-2024-over-99-penetration-and-growth-in-ai-digital-commerce. No figure was found for **business approval workflows** done on WhatsApp. That is an evidence gap.
- **Trust in AI**: 62% of Saudi respondents are willing to trust AI and 84% accept it, above the global average (KPMG/University of Melbourne 2025) [P] https://kpmg.com/sa/en/insights/ai-and-technology/trust-attitudes-and-use-of-artificial-intelligence.html. This is general public trust, not trust in AI acting on business transactions, so human approval is still advisable.
- **Owner-centred decisions**: PwC's Middle East family business surveys describe founder-centred authority and weak formal governance. For example, a reported 69% have no formal succession plan [S] https://www.pwc.com/m1/en/publications/documents/family-business-survey-2019.pdf. No quantitative study was found on who signs up for or buys SaaS in Saudi SMBs. This is a gap. Validate it with Boynt's own sign-up data, asking role at sign-up.
- **Data residency / IT concerns**: the PDPL has been enforceable since September 2024. Transfers outside the Kingdom require safeguards, risk assessments, and in some cases SDAIA's rules [P/S] https://www.kslaw.com/insights/articles/international-personal-data-transfers-under-saudi-arabias-data-protection-law, https://www.clydeco.com/en/insights/2025/03/update-on-saudi-arabia-risk-assessment-guidelines. NCA Cloud Cybersecurity Controls apply mainly to government and critical sectors. Their reach into private SMB buyers was not verified. Employee records imported into Boynt are personal data under the PDPL.
- **Missing evidence**: Saudi B2B onboarding benchmarks, Arabic-language activation data, and how trial versus card-upfront performs in KSA.

## 4. Twelve design decisions, ranked

1. **Ask role at sign-up (Owner / Ops / IT / Other) and branch the first screen.** Evidence: Monday/Notion/HubSpot practice. Also needed to measure the Saudi signer mix (gap above).
2. **Never block first value on the ERP connection**: offer file upload plus a labeled sample in parallel. Evidence: real-data aha (Slack/Figma), and TTV of about 1.5 days on average (Userpilot).
3. **Context-carrying delegation invites** (WhatsApp/email, scoped, expiring, with a status shown on the checklist). Evidence: Slack request-to-install and the Entra admin-consent workflow.
4. **A daily WhatsApp morning brief at a user-chosen fixed time.** Evidence: Fogg prompt, Wood & Neal context cue, 92% WhatsApp use in KSA.
5. **One-tap approvals in WhatsApp within limits, with full audit.** Evidence: B=MAP ability. IT's audit needs.
6. **Define and instrument company-level activation**, e.g. 3 roles active and 1 end-to-end approval in 7 days, then confirm it against retention. Evidence: Slack's team threshold and its derivation method.
7. **Read-only connector by default, with a trust panel** (scopes, hosting location, sub-processors, audit). Evidence: PDPL transfer rules, IT persona fears.
8. **Human approval on every agent action that writes data in the early stage**, with the agent's reasoning shown. Evidence: 62% trust (not universal), and the lack of transaction-level trust data.
9. **A weekly "what changed" card with a visible calculation and a recorded baseline.** Evidence: outcome feedback. No reliable industry ROI benchmarks exist.
10. **A setup checklist with endowed progress and named owners per step.** Evidence: Nunes & Drèze 2006.
11. **Configuration kept as visible company assets** (limits, rules, workflows). Evidence: Hook "investment", the IKEA effect.
12. **An optional 30-minute Arabic setup call for mid-market sign-ups.** Evidence: Superhuman (qualitative only). Test it before scaling.

**Limits of this note**: standard-effort search only. Several widely quoted activation figures (Facebook, Dropbox, HubSpot) have no located primary source, and benchmark figures from Userpilot and OpenView were partly read through secondary summaries.
