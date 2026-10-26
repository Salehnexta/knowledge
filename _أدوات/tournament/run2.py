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
SYS="اكتب بالعربية الفصحى المبسطة. استخدم البيانات المذكورة في الجرد فقط، ولا تخترع مصادر أو أرقاماً."

P_ab="تاجرة عبايات من البيت، ميزانية إعلان 1500 ريال شهرياً، تبيع عبر إنستغرام وسلة"
DUMB=("أنت «الزبون الغبي»: "+P_ab+". ساخرة، تكرهين التعقيد، تفهمين الأمور بأسوأ طريقة، ما عندك وقت، وفلوسك قليلة. همومك مبنية فقط على أصوات التجار الحقيقية هذه:\n"+voice+
 "\n\nقاعدتك: لا تقولين «أدفع» إلا إذا فهمتِ العرض في أقل من 10 ثواني، وشفتِ فيه فلوس ترجع لك هالشهر، والسعر أقل من اللي يضيع عليك بدونه، وما يطلب منك وقت. لا تجاملين أبداً.")
final=open(T+"/5_final.md",encoding="utf-8").read()
internal=final
offer=call("anthropic/claude-opus-5.5",[{"role":"system","content":SYS+" أنت «المهندس»."},{"role":"user","content":f"هذه مواصفات المنتج الداخلية:\n{final}\n\nاكتب العرض كما تراه التاجرة فقط (صفحة بيع قصيرة + بطاقة المثال)، بلا تكاليف داخلية ولا أدوات ولا جداول بناء، ومدة التسليم نفس اليوم. حتى 350 كلمة. لا وعود لا تدعمها البيانات، ولا ضمان مبيعات."}],4000)
rounds=[{"offer":offer}]; paid=False
for r in range(1,9):
    cust=call("google/gemini-3.8-flash",[{"role":"system","content":DUMB},{"role":"user","content":f"هذا العرض:\n{offer}\n\nردك بلهجتك (حتى 200 كلمة). ثم في آخر سطر JSON فقط: {{\"verdict\":\"أدفع\" أو \"ما أدفع\",\"score\":0-10,\"must_fix\":[\"...\"]}}"}],2500)
    m=re.findall(r"\{.*\}",cust,re.S)
    try: v=json.loads(m[-1])
    except Exception: v={"verdict":"ما أدفع","score":0,"must_fix":["رد غير واضح"]}
    rounds[-1].update(customer=cust,verdict=v); print("round",r,v.get("verdict"),v.get("score"),v.get("must_fix"),file=sys.stderr,flush=True)
    if v.get("verdict")=="أدفع" and float(v.get("score",0))>=9 and not v.get("must_fix"): paid=True; break
    devil=call("google/gemini-4-argon",[{"role":"system","content":SYS+" أنت «محامي الشيطان»."},{"role":"user","content":f"{inv}\n\nالمواصفات الداخلية:\n{internal[:7000]}\n\nالعرض:\n{offer}\n\nاعتراضات الزبونة:\n{cust}\n\nامنع الغش: أي وعد لا تدعمه بياناتنا، أو رقم مخترع، أو ضمان مبيعات، أو سعر يخسرنا، ارفضه. اذكر لكل اعتراض: يجوز تعديله وكيف، أو لا يجوز ولماذا، وكيف نرد عليه بصدق بلغة تقنعها. حتى 250 كلمة."}],3000)
    comp=call("deepseek/deepseek-v3.2",[{"role":"system","content":SYS+" أنت «المقارِن»."},{"role":"user","content":f"العرض:\n{offer}\n\nاعتراض الزبونة:\n{cust}\n\nاقترح فكرتين من أدوات عالمية أو صناعات أخرى (ضمانات، تجارب مجانية، دفع بعد النتيجة...) تحل الاعتراض، بشرط أن تُبنى من الجرد:\n{inv[:9000]}\nحتى 150 كلمة."}],2000)
    offer=call("anthropic/claude-opus-5.5",[{"role":"system","content":SYS+" أنت «المهندس»."},{"role":"user","content":f"المواصفات الداخلية (لا تظهر للزبونة):\n{internal[:7000]}\n\nالعرض السابق:\n{offer}\n\nالزبونة:\n{cust}\n\nمحامي الشيطان:\n{devil}\n\nالمقارِن:\n{comp}\n\nعدّل العرض ليقنعها دون كسر قيود محامي الشيطان. نفس الشكل، حتى 350 كلمة، بلا تكاليف داخلية."}],4000)
    rounds[-1].update(devil=devil,comparator=comp); rounds.append({"offer":offer})
json.dump({"paid":paid,"rounds":rounds},open(T+"/6_rounds.json","w"),ensure_ascii=False,indent=1)
print("cost",round(sum(c for _,c in usage),3),"paid",paid)
