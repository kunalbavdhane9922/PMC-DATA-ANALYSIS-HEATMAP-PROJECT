import sys,csv,json,collections,statistics
from datetime import datetime as D
csv.field_size_limit(10**9)
src,out,tpl=sys.argv[1:4]
F="%Y-%m-%d %H:%M:%S.%f"
def p(s):
    return D.strptime(s,F)
class Cell:
    __slots__=("n","res","days","sla","breach")
    def __init__(s):s.n=0;s.res=0;s.days=[];s.sla=0;s.breach=0
V={k:collections.defaultdict(Cell) for k in("ward_dept","dept_type","month_type","wd_hour")}
tot={k:collections.Counter() for k in("ward","dept","type")}
for r in csv.DictReader(open(src,encoding='utf-8',newline='')):
    w=r["Ward Name"] or "Unknown";d=r["Department Name"];t=r["Complaint Type"]
    cd=p(r["Complaint Date"])
    tot["ward"][w]+=1;tot["dept"][d]+=1;tot["type"][t]+=1
    res=r["Last Action"]=="Resolved"
    days=None;breach=None
    if res:
        end=p(r["Complaint close date"] or r["Last Action Date"])
        days=(end-cd).total_seconds()/86400
        if r["Expected Complaint Date"]:breach=end>p(r["Expected Complaint Date"])
    keys={"ward_dept":(w,d),"dept_type":(d,t),"month_type":(t,cd.strftime("%Y-%m")),"wd_hour":(cd.strftime("%a"),cd.hour)}
    for k,key in keys.items():
        c=V[k][key];c.n+=1
        if res:
            c.res+=1;c.days.append(days)
            if breach is not None:
                c.sla+=1;c.breach+=breach
# axis orders
def order(keys,vol):return sorted(keys,key=lambda x:-vol[x])
wards=order(tot["ward"],tot["ward"]);depts=order(tot["dept"],tot["dept"]);types=order(tot["type"],tot["type"])
months=sorted({m for (_,m) in V["month_type"]})
wdays=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];hours=list(range(24))
axes={"ward_dept":(wards,depts),"dept_type":(depts,types),"month_type":(types,months),"wd_hour":(wdays,hours)}
res={}
for k,(ra,ca) in axes.items():
    ri={x:i for i,x in enumerate(ra)};ci={x:i for i,x in enumerate(ca)}
    cells=[]
    for (a,b),c in V[k].items():
        med=round(statistics.median(c.days),1) if c.days else None
        cells.append([ri[a],ci[b],c.n,c.res,med,len(c.days),c.breach,c.sla])
    res[k]={"rows":[str(x) for x in ra],"cols":[str(x) for x in ca],"cells":cells}
data=json.dumps(res,ensure_ascii=False,separators=(",",":"))
open(out,"w",encoding="utf-8").write(open(tpl,encoding="utf-8").read().replace("__DATA__",data))
print({k:len(v["cells"]) for k,v in res.items()})
