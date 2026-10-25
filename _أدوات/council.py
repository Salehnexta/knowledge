import json,os,sys,urllib.request,concurrent.futures as cf,random,time
OUT=sys.argv[1]; KEY=os.environ["OPENROUTER_API_KEY"]
M={"A":"anthropic/claude-sonnet-5.5","B":"openai/gpt-5.6-terra","C":"google/gemini-4-argon"}
CHAIR="anthropic/claude-opus-5.5"; CUST="google/gemini-3.8-flash"
usage=[]
def call(model,msgs,max_tokens=6000):
    for a in range(3):
        try:
            req=urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",data=json.dumps({"model":model,"messages":msgs,"max_tokens":max_tokens,"usage":{"include":True}}).encode(),headers={"Authorization":"Bearer "+KEY,"Content-Type":"application/json","X-Title":"morvo-council"})
            r=json.load(urllib.request.urlopen(req,timeout=400))
            usage.append((model,r.get("usage",{}).get("cost")))
            return r["choices"][0]["message"]["content"]
        except Exception as e:
            print("retry",model,e,file=sys.stderr); time.sleep(5)
    raise SystemExit("failed "+model)
brief=open(OUT+"/brief.md",encoding="utf-8").read()
voice=open(OUT+"/voice.md",encoding="utf-8").read()
Q="السؤال: كيف يدخل مورفو السوق السعودي بقوة ويحصل أول عملاء يدفعون ويستمرون خلال الأشهر الثلاثة القادمة؟ (العملاء: المتاجر الإلكترونية فقط حالياً)."
SYS="أنت عضو مستقل في مجلس استشاري. أجب بالعربية الفصحى المبسطة، بأسلوب علمي مباشر بلا مبالغة ولا لغة شركات استشارية. استخدم فقط الحقائق في الملف، وإذا افترضت شيئاً فاكتب «افتراض». لا تخترع أرقاماً سوقية."
# Stage 1: independent plans
p1=lambda k: call(M[k],[{"role":"system","content":SYS},{"role":"user","content":f"{brief}\n\n{Q}\n\nاكتب خطتك المستقلة (حتى 900 كلمة): 1) السؤال المؤلم الذي يحله مورفو 2) العميل الأول 3) المنتج والعرض والسعر 4) أول 20 عميلاً من أين 5) أكبر ثلاثة مخاطر وكيف تُعالج 6) مقاييس النجاح ومتى نتوقف."}])
with cf.ThreadPoolExecutor(3) as ex: plans=dict(zip(M,ex.map(p1,M)))
json.dump(plans,open(OUT+"/1_plans.json","w"),ensure_ascii=False,indent=1)
# anonymize
labels=list(M); random.shuffle(labels); anon={f"الخطة {i+1}":plans[k] for i,k in enumerate(labels)}
json.dump({"map":{f"الخطة {i+1}":M[k] for i,k in enumerate(labels)}},open(OUT+"/anon_map.json","w"),ensure_ascii=False)
allp="\n\n".join(f"### {n}\n{t}" for n,t in anon.items())
# Stage 2: critique + customer
p2=lambda k: call(M[k],[{"role":"system","content":SYS},{"role":"user","content":f"{brief}\n\n{Q}\n\nهذه ثلاث خطط بلا أسماء (إحداها قد تكون خطتك):\n{allp}\n\nالمطلوب (حتى 800 كلمة): لكل خطة استخرج عيباً قاتلاً واحداً على الأقل مع السبب، ثم رتّب الخطط من الأقوى للأضعف، ثم اذكر أفضل فكرة في كل خطة تستحق البقاء. لا مجاملة."}])
cust=lambda: call(CUST,[{"role":"system","content":"أنت تاجر سعودي صاحب متجر إلكتروني صغير. تتكلم باللهجة السعودية. شخصيتك وهمومك مبنية فقط على أصوات التجار الحقيقية التالية، ولا تخرج عنها:\n"+voice},{"role":"user","content":f"عرضوا عليك هذه الخطط الثلاث لمنتج اسمه مورفو:\n{allp}\n\nلكل خطة: هل تدفع؟ ليش لا؟ وش اللي يخليك تدفع؟ (حتى 500 كلمة، بصراحة وسخرية)."}],2500)
with cf.ThreadPoolExecutor(4) as ex:
    fut={k:ex.submit(p2,k) for k in M}; fc=ex.submit(cust)
    crit={k:f.result() for k,f in fut.items()}; customer=fc.result()
json.dump({"critiques":crit,"customer":customer},open(OUT+"/2_critiques.json","w"),ensure_ascii=False,indent=1)
crits="\n\n".join(f"### نقد العضو {i+1}\n{crit[k]}" for i,k in enumerate(M))
# Stage 3: chairman
final=call(CHAIR,[{"role":"system","content":SYS+" أنت رئيس المجلس."},{"role":"user","content":f"{brief}\n\n{Q}\n\n## الخطط المستقلة\n{allp}\n\n## نقد الأعضاء المتبادل\n{crits}\n\n## صوت التاجر\n{customer}\n\nالمطلوب: لا تلخّص النقاش. اكتب الحل النهائي الجاهز للتنفيذ بناءً على ما صمد أمام النقد فقط. البنية: 1) السؤال المؤلم 2) العميل الأول 3) المنتج والعرض والتسعير 4) خطة أول 20 عميلاً 5) شروط قبل فتح الدفع 6) جدول زمني لـ12 أسبوعاً 7) مقاييس ومعايير توقف 8) ما يتأجل 9) نقاط اتفق عليها المجلس بالإجماع، ونقاط خلاف حقيقية تحتاج قرار المؤسس (اذكر الطرفين)."}],9000)
open(OUT+"/3_final.md","w",encoding="utf-8").write(final)
print("cost",round(sum(c or 0 for _,c in usage),3),usage)
