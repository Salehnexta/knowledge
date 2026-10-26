import json,os,sys,re,itertools,urllib.request,concurrent.futures as cf,time,random
T=sys.argv[1]; KEY=os.environ["OPENROUTER_API_KEY"]; usage=[]
def call(model,msgs,mt=6000,js=False):
    for a in range(3):
        try:
            body={"model":model,"messages":msgs,"max_tokens":mt+6000,"usage":{"include":True}}
            if "flash" not in model: body["reasoning"]={"effort":"low"}
            r=json.load(urllib.request.urlopen(urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",data=json.dumps(body).encode(),headers={"Authorization":"Bearer "+KEY,"Content-Type":"application/json","X-Title":"morvo-tournament"}),timeout=400))
            usage.append((model,r.get("usage",{}).get("cost") or 0)); t=r["choices"][0]["message"].get("content") or ""
            if not t.strip(): raise ValueError("empty")
            if js:
                m=re.search(r"```(?:json)?\s*(.*?)```",t,re.S); t=m.group(1) if m else t[t.find(next(c for c in t if c in "[{")):]
                return json.loads(t)
            return t
        except Exception as e: print("retry",model,repr(e)[:200],file=sys.stderr); time.sleep(5)
    raise SystemExit("fail "+model)
inv=open(T+"/inventory.md",encoding="utf-8").read(); voice=open(T+"/voice.md",encoding="utf-8").read()
SYS="اكتب بالعربية الفصحى المبسطة. استخدم البيانات المذكورة في الجرد فقط، ولا تخترع مصادر أو أرقاماً. ما تفترضه اكتب بجانبه (افتراض)."
GOAL="الهدف: ميزة تنافسية لمورفو يستفيد منها التاجر السعودي (متجر إلكتروني) مباشرة، مبنية على تجميع البيانات الكثيرة التي نملكها، ويصعب على أدوات أخرى أو على ChatGPT تقليدها."
# Stage 1: divergent lenses
L={"anthropic/claude-sonnet-5.5":"عالم بيانات: ابحث عن إشارات لا يجمعها أحد معاً (مثلاً عمر الإعلان + الزيارات + التعليقات + الأسعار + ساما) لتنتج معلومة جديدة.",
"openai/gpt-5.6-terra":"تاجر سعودي متمرس صار مستشاراً: ما الذي يوفر على التاجر فلوساً أو وقتاً هذا الأسبوع؟ فكّر في قرارات يومية (ماذا أعلن، بأي سعر، أي قصة، متى).",
"google/gemini-4-argon":"استراتيجي ميزة تنافسية: ما الذي يتراكم مع الوقت ويصعب نسخه (التاريخ الأسبوعي، المعايير المحلية، الشبكة)؟",
"deepseek/deepseek-v3.2":"المقارِن: قارن بأدوات عالمية (Similarweb، Jungle Scout، Helium 10، Pathmatics، Foreplay، Triple Whale، Google Trends) وما تفعله لبائعيها، ثم اقترح ما يُنقل للسوق السعودي ويتفوق عليها محلياً، واذكر المقارنة صراحة.",
"x-ai/grok-4.7":"المبتكر الدخيل من صناعات أخرى (منصات تداول الأسهم، تحليلات الرياضة، الأرصاد): انقل فكرة ناجحة هناك إلى تجارة المتاجر السعودية."}
FMT='أعد JSON فقط: قائمة من 5 عناصر، كل عنصر {"name":..., "merchant_question":"سؤال التاجر بلهجته", "what_merchant_sees":"مثال بطاقة بأرقام من لقطة العبايات الحقيقية", "data_used":[...], "why_hard_to_copy":..., "risk":...}'
s1=lambda m: call(m,[{"role":"system","content":SYS},{"role":"user","content":f"{inv}\n\n{GOAL}\n\nأنت عضو في لجنة. شخصيتك ودورك: {L[m]}\n\nعدستك: {L[m]}\n\n{FMT}"}],5000,True)
with cf.ThreadPoolExecutor(5) as ex: raw=dict(zip(L,ex.map(s1,L)))
json.dump(raw,open(T+"/1_raw.json","w"),ensure_ascii=False,indent=1)
pool=[dict(i,src=m) for m,v in raw.items() for i in v]
# Stage 2: merge
cand=call("anthropic/claude-sonnet-5.5",[{"role":"system","content":SYS},{"role":"user","content":f"هذه {len(pool)} فكرة من أربعة مصادر:\n{json.dumps(pool,ensure_ascii=False)}\n\nادمج المكرر، واحذف ما يكرر أفكاراً مسجلة سابقاً بلا زاوية جديدة (القائمة في الجرد):\n{inv[-4000:]}\n\nأعد JSON فقط: قائمة حتى 12 فكرة مميزة بنفس الحقول مع حقل id (C1..C12) وحقل sources (أي مصادر اقترحتها)."}],9000,True)
json.dump(cand,open(T+"/2_candidates.json","w"),ensure_ascii=False,indent=1)
C=json.dumps(cand,ensure_ascii=False)
# Stage 3: stress tests + merchant panel
feas=lambda: call("openai/gpt-5.6-terra",[{"role":"system","content":SYS},{"role":"user","content":f"{inv}\n\nالأفكار:\n{C}\n\nأنت مهندس بيانات. لكل فكرة قيّم: feasibility (0-10: هل تُبنى بالبيانات والأدوات الموجودة الآن خلال أسبوعين)، accuracy_risk (0-10: خطر أن تعطي رقماً مضللاً للتاجر، 10=خطر عال)، note. أعد JSON فقط: {{\"C1\":{{...}},...}}"}],4000,True)
moat=lambda: call("google/gemini-4-argon",[{"role":"system","content":SYS},{"role":"user","content":f"{inv}\n\nالأفكار:\n{C}\n\nأنت «محامي الشيطان»: ناقد شرس مهمته تدمير الافتراضات. لكل فكرة: copyability (0-10: 10=يصعب جداً نسخها من منافس أو ChatGPT أو أداة عالمية)، fatal_flaw (عيب قاتل بجملة). أعد JSON فقط: {{\"C1\":{{...}},...}}"}],4000,True)
P={"عبايات":"تاجرة عبايات من البيت، ميزانية إعلان 1500 ريال شهرياً، تبيع عبر إنستغرام وسلة","عطور":"صاحب متجر عطور متوسط، 3 موظفين، يعلن في سناب وتيك توك، يعاني من المنافسة السعرية","مكملات":"صاحب متجر مكملات جديد، عمره 4 أشهر، زيارات بلا طلبات"}
merch=lambda k: call("google/gemini-3.8-flash",[{"role":"system","content":f"أنت «الزبون الغبي»: مستخدم ساخر يكره التعقيد ويفهم الأمور بأسوأ طريقة ممكنة. أنت {P[k]}. تتكلم باللهجة السعودية. همومك مبنية فقط على أصوات التجار الحقيقية هذه:\n{voice}"},{"role":"user","content":f"هذه أفكار لميزات في منتج اسمه مورفو:\n{C}\n\nلكل فكرة: pay (0-10 كم أنت مستعد تدفع عليها شهرياً)، quote (جملة بلهجتك). أعد JSON فقط: {{\"C1\":{{\"pay\":..,\"quote\":..}},...}}"}],4000,True)
with cf.ThreadPoolExecutor(5) as ex:
    f1=ex.submit(feas); f2=ex.submit(moat); fm={k:ex.submit(merch,k) for k in P}
    F=f1.result(); Mo=f2.result(); Me={k:f.result() for k,f in fm.items()}
json.dump({"feas":F,"moat":Mo,"merchants":Me},open(T+"/3_scores.json","w"),ensure_ascii=False,indent=1)
def sc(c):
    i=c["id"]; g=lambda d,k,dv=5: float((d.get(i) or {}).get(k,dv))
    pay=sum(g(Me[k],"pay") for k in P)/len(P)
    return round(0.4*pay+0.25*g(F,"feasibility")+0.2*g(Mo,"copyability")+0.15*(10-g(F,"accuracy_risk")),2)
for c in cand: c["score"]=sc(c)
top=sorted(cand,key=lambda c:-c["score"])[:5]
# Stage 4: pairwise tournament, two judges, both orders
wins={c["id"]:0 for c in top}; log=[]
def duel(a,b,j):
    r=call(j,[{"role":"system","content":SYS},{"role":"user","content":f"{GOAL}\n\nأصوات التجار (مختصر):\n{voice[:6000]}\n\nالفكرة A:\n{json.dumps(a,ensure_ascii=False)}\n\nالفكرة B:\n{json.dumps(b,ensure_ascii=False)}\n\nأيهما أقوى كميزة تنافسية يدفع عليها التاجر ويصعب نسخها ونقدر نبنيها بدقة؟ أعد JSON فقط: {{\"winner\":\"A\" أو \"B\",\"why\":\"جملة\"}}"}],800,True)
    return (a["id"] if r["winner"]=="A" else b["id"]),r.get("why","")
jobs=[(a,b,j) for a,b in itertools.permutations(top,2) for j in ["anthropic/claude-sonnet-5.5","openai/gpt-5.6-terra"] if a["id"]<b["id"] or True]
jobs=[(a,b,j) for (a,b,j) in jobs]  # both orders × 2 judges = 40 duels
with cf.ThreadPoolExecutor(8) as ex:
    for (a,b,j),(w,why) in zip(jobs,ex.map(lambda x:duel(*x),jobs)):
        wins[w]+=1; log.append({"A":a["id"],"B":b["id"],"judge":j,"winner":w,"why":why})
json.dump({"top":top,"wins":wins,"duels":log},open(T+"/4_tournament.json","w"),ensure_ascii=False,indent=1)
rank=sorted(top,key=lambda c:-wins[c["id"]])
# Stage 5: committee loop until the dumb customer pays
DUMB=("أنت «الزبون الغبي»: "+P["عبايات"]+". ساخر، تكره التعقيد، تفهم الأمور بأسوأ طريقة، ما عندك وقت، وفلوسك قليلة. "
 "همومك مبنية فقط على أصوات التجار الحقيقية هذه:\n"+voice+
 "\n\nقاعدتك: لا تقول «أدفع» إلا إذا فهمت المنتج في أقل من 10 ثواني، وشفت فيه فلوس ترجع لك هالشهر، والسعر أقل من اللي يضيع عليك بدونه، وما يطلب منك وقت. لا تجامل أبداً.")
spec=call("anthropic/claude-opus-5.5",[{"role":"system","content":SYS+" أنت «المهندس» في اللجنة."},{"role":"user","content":f"{inv}\n\n{GOAL}\n\nفازت هذه الأفكار في البطولة (بعدد الانتصارات):\n{json.dumps([dict(c,wins=wins[c['id']]) for c in rank],ensure_ascii=False)}\n\nتقييمات محامي الشيطان والمهندس والزبائن:\n{json.dumps({'feas':F,'moat':Mo,'merchants':Me},ensure_ascii=False)}\n\nابنِ من الفائز (ويمكن دمج الثاني) منتجاً واحداً يُعرض على تاجرة عبايات: الاسم، وما تراه بالضبط (بطاقة بأرقام لقطة العبايات الحقيقية فقط)، والسعر الشهري، والضمان. حتى 450 كلمة، بلغة بسيطة."}],5000)
rounds=[{"spec":spec}]
for r in range(1,9):
    cust=call("google/gemini-3.8-flash",[{"role":"system","content":DUMB},{"role":"user","content":f"هذا العرض:\n{spec}\n\nردك بلهجتك (حتى 200 كلمة). ثم في آخر سطر JSON فقط: {{\"verdict\":\"أدفع\" أو \"ما أدفع\",\"score\":0-10,\"must_fix\":[\"...\"]}}"}],2500)
    m=re.findall(r"\{.*\}",cust,re.S); v=json.loads(m[-1]) if m else {"verdict":"ما أدفع","score":0,"must_fix":["رد غير واضح"]}
    rounds[-1].update(customer=cust,verdict=v)
    print("round",r,v.get("verdict"),v.get("score"),file=sys.stderr)
    if v.get("verdict")=="أدفع" and float(v.get("score",0))>=9 and not v.get("must_fix"): break
    devil=call("google/gemini-4-argon",[{"role":"system","content":SYS+" أنت «محامي الشيطان»."},{"role":"user","content":f"{inv}\n\nالعرض الحالي:\n{spec}\n\nاعتراضات الزبون:\n{cust}\n\nمهمتك: امنع الغش. أي تعديل يرضي الزبون بوعد لا تدعمه بياناتنا، أو برقم مخترع، أو بضمان مبيعات، أو بسعر يخسرنا، ارفضه. اذكر: ما يجوز تعديله، وما لا يجوز، وعيباً قاتلاً واحداً باقياً في العرض. حتى 250 كلمة."}],3000)
    new=call("deepseek/deepseek-v3.2",[{"role":"system","content":SYS+" أنت «المقارِن»."},{"role":"user","content":f"العرض:\n{spec}\n\nاعتراض الزبون:\n{cust}\n\nاقترح فكرتين جديدتين من أدوات عالمية أو صناعات أخرى تحل اعتراض الزبون، بشرط أن تُبنى من الجرد:\n{inv[:9000]}\nحتى 150 كلمة."}],2000)
    spec=call("anthropic/claude-opus-5.5",[{"role":"system","content":SYS+" أنت «المهندس»."},{"role":"user","content":f"{inv}\n\nالعرض السابق:\n{spec}\n\nالزبون الغبي:\n{cust}\n\nمحامي الشيطان:\n{devil}\n\nالمقارِن:\n{new}\n\nعدّل العرض ليقنع الزبون دون كسر قيود محامي الشيطان. نفس الشكل، حتى 450 كلمة."}],5000)
    rounds[-1].update(devil=devil,comparator=new); rounds.append({"spec":spec})
json.dump(rounds,open(T+"/5_rounds.json","w"),ensure_ascii=False,indent=1)
final=call("anthropic/claude-opus-5.5",[{"role":"system","content":SYS+" أنت «المايسترو»."},{"role":"user","content":f"{inv}\n\nمسار التفاوض كاملاً بين المهندس والزبون الغبي ومحامي الشيطان والمقارِن:\n{json.dumps(rounds,ensure_ascii=False)}\n\nلا تلخّص. اكتب المنتج النهائي الجاهز للبناء كما وصل إليه آخر عرض: 1) الاسم وسؤال التاجر 2) ما يراه التاجر: بطاقة مثال كاملة بأرقام العبايات الحقيقية فقط 3) كيف تُحسب من البيانات 4) لماذا يصعب نسخه (قارن بالأدوات العالمية) 5) ما قد يضلل وكيف نحميه 6) السعر والضمان 7) البناء بالأسابيع والتكلفة 8) هل دفع الزبون الغبي فعلاً، وفي أي جولة، وما الذي أقنعه. بلا مقدمات."}],9000)
open(T+"/5_final.md","w",encoding="utf-8").write(final)
print("cost",round(sum(c for _,c in usage),3)); print("wins",wins); print([(c["id"],c["name"],c["score"]) for c in cand])
