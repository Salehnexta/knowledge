import json,sys,os,urllib.request
T=sys.argv[1]; voice=open(T+"/voice.md",encoding="utf-8").read()
r=json.load(open(T+"/8_rounds.json"))["rounds"]; offer=r[-1]["offer"]; open(T+"/final_offer.md","w",encoding="utf-8").write(offer)
DUMB="أنت «الزبون الغبي»: تاجرة عبايات من البيت، ميزانية إعلان 1500 ريال شهرياً. ساخرة، تكرهين التعقيد، ما عندك وقت، وفلوسك قليلة. لا تجاملين. همومك من أصوات التجار هذه:\n"+voice
q=f"هذا العرض النهائي:\n{offer}\n\nسؤال واحد: لو وصلك رابط الدفع الحين، تدفعين 49 ريال بدون نقاش ولا شروط إضافية؟ جاوبي بلهجتك في 3 أسطر، ثم آخر سطر JSON فقط: {{\"pay_now\":true أو false,\"why\":\"...\"}}"
out=[]
for i in range(3):
    b={"model":"google/gemini-3.8-flash","messages":[{"role":"system","content":DUMB},{"role":"user","content":q}],"max_tokens":1500}
    x=json.load(urllib.request.urlopen(urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",data=json.dumps(b).encode(),headers={"Authorization":"Bearer "+os.environ["OPENROUTER_API_KEY"],"Content-Type":"application/json"}),timeout=200))
    out.append(x["choices"][0]["message"]["content"])
json.dump(out,open(T+"/9_final_ask.json","w"),ensure_ascii=False,indent=1)
for o in out: print(o,"\n---")
