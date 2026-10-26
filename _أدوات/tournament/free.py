import json,sys,os,urllib.request
T=sys.argv[1]; K=os.environ["OPENROUTER_API_KEY"]
def call(m,msgs,mt=3000):
    b={"model":m,"messages":msgs,"max_tokens":mt+4000,"usage":{"include":True}}
    if "flash" not in m: b["reasoning"]={"effort":"low"}
    x=json.load(urllib.request.urlopen(urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",data=json.dumps(b).encode(),headers={"Authorization":"Bearer "+K,"Content-Type":"application/json"}),timeout=300))
    return x["choices"][0]["message"]["content"]
page="""نص صفحة المنتج كما هو (sadal-ksa.com، عباية رهاج T900):
السعر 204 (قبل 219). رقم الموديل T900. تصنيف المنتج نص كلوش. الوصف: القماش: انترنت - مريح، عملي، غير شفاف. القصة: نص كلوش. الملحقات: يوجد معها طرحة ساده بطرف من نفس قماش العباية. مقفله بطقطق. يمكنك التأكد من المقاس من جدول المقاسات المرفق. مده التنفيذ من 1-3 يوم قبل الشحن. لايوجد تعديل حالياً. (لا يوجد في نص الصفحة: الأطوال بالأرقام، مدة الشحن، تكلفة الشحن، المناسبة)."""
ad="""نص إعلان نفس المتجر على ميتا (شغّال منذ 2024-09-20، 765 يوماً): «عباية عمليه جداً وتناسب الدوام والطلعات وقماشها إنترنت الغني عن التعريف مقفله بطقطق ويوجد معها طرحه ساده من نفس قماش العبايه اسمها بالموقع (رهاج) رقمها T900 سعرها :184 ريال»"""
msg=call("anthropic/claude-opus-5.5",[{"role":"system","content":"اكتب رسالة واتساب «الفحص المجاني» لتاجرة عبايات: أول نقص واحد فقط، من الحقائق المعطاة حرفياً، بلهجة سعودية بسيطة، حتى 90 كلمة، مع سطر جاهز للنسخ. لا تخترع شيئاً."},{"role":"user","content":page+"\n\n"+ad}])
open(T+"/free_msg.md","w",encoding="utf-8").write(msg)
voice=open(T+"/voice.md",encoding="utf-8").read(); offer=open(T+"/final_offer.md",encoding="utf-8").read()
DUMB="أنت «الزبون الغبي»: تاجرة عبايات، ميزانية إعلان 1500 ريال شهرياً. ساخرة، تكرهين التعقيد، ما عندك وقت، وفلوسك قليلة. لا تجاملين. همومك من أصوات التجار هذه:\n"+voice
out=[]
for i in range(3):
    out.append(call("google/gemini-3.8-flash",[{"role":"system","content":DUMB},{"role":"user","content":f"العرض اللي شفتيه:\n{offer}\n\nأرسلتِ رابط عبايتك (رهاج T900) وإعلانك، ووصلتك بعد دقائق هذي الرسالة المجانية:\n{msg}\n\nوالحين وصلك رابط دفع 49 ريال بأبل باي. تدفعين بدون نقاش؟ ردي بلهجتك في 3 أسطر، ثم آخر سطر JSON فقط: {{\"pay_now\":true أو false,\"why\":\"...\"}}"}],1200))
json.dump({"free_msg":msg,"answers":out},open(T+"/10_free_check.json","w"),ensure_ascii=False,indent=1)
print(msg); print("======")
for o in out: print(o,"\n---")
