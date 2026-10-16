import sys,csv,json,collections
csv.field_size_limit(10**9)
src,out=sys.argv[1],sys.argv[2]
A=collections.defaultdict(lambda:[0,0])
for r in csv.DictReader(open(src,encoding='utf-8',newline='')):
    k=(r["Ward Name"] or "Unknown",r["Department Name"],r["Complaint Type"])
    A[k][0]+=1
    if r["Last Action"]=="Resolved":A[k][1]+=1
wards=sorted({k[0] for k in A});depts=sorted({k[1] for k in A});types=sorted({k[2] for k in A})
wi={w:i for i,w in enumerate(wards)};di={d:i for i,d in enumerate(depts)};ti={t:i for i,t in enumerate(types)}
rows=[[wi[w],di[d],ti[t],v[0],v[1]] for (w,d,t),v in A.items()]
data=json.dumps({"wards":wards,"depts":depts,"types":types,"rows":rows},ensure_ascii=False,separators=(",",":"))
html=open(sys.argv[3],encoding='utf-8').read().replace("__DATA__",data)
open(out,"w",encoding='utf-8').write(html)
print(len(rows),"cells")
