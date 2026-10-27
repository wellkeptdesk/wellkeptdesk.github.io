import os,sys
# Builds the Linen Vows widget files from _base.html: python3 build.py <this folder>
D=sys.argv[1]
base=open(os.path.join(D,'_base.html')).read()
W={}
W['clock']=dict(title='Clock & date',maxw=240,pad='12px 16px 12px',css='''
.card{display:flex;align-items:center;gap:12px}
.s{width:30px;height:30px;flex:none}
.t{font-size:30px;font-weight:600;line-height:1;color:var(--ink)} .t small{font-size:14px;font-weight:500;color:var(--mute);margin-left:3px;font-family:Inter,system-ui,sans-serif;letter-spacing:.04em}
.d{font-size:11.5px;color:var(--mute);margin-top:5px;letter-spacing:.02em}''',
html='''<div class="card"><svg class="s" viewBox="0 0 40 40"><path id="sp" fill="var(--main)" filter="url(#rough)"/><circle cx="20" cy="20" r="8.5" fill="none" stroke="var(--bg)" stroke-width="1.4"/><path d="M20 14.5c2.6 2.4 2.6 8.6 0 11-2.6-2.4-2.6-8.6 0-11z" fill="var(--bg)" opacity=".9"/></svg><div><div class="t serif" id="t"></div><div class="d" id="d"></div></div></div>''',
js='''document.getElementById('sp').setAttribute('d',seal(20,20,18,16,14));
function tick(){const n=new Date();let h=n.getHours(),m=String(n.getMinutes()).padStart(2,'0'),ap=h<12?'am':'pm';h=h%12||12;
document.getElementById('t').innerHTML=h+':'+m+'<small>'+ap+'</small>';document.getElementById('d').textContent=fmtDate(n,{weekday:'long',day:'numeric',month:'long'})}
tick();setInterval(tick,1000*5);''')

cd_css='''.card{text-align:center}
svg.main{width:100%;max-width:190px;height:auto;display:block;margin:0 auto}
.lab{margin-top:2px}.dt{font-size:11.5px;color:var(--mute);margin-top:3px}
.empty{padding:18px 6px}.empty .btn{margin-top:10px}'''
def cd(idn,label,deflabel,title):
    return dict(title=title,maxw=230,pad='12px 12px 12px',css=cd_css,html=f'''<div class="card"><button class="gear" id="g"></button>
<div id="view"></div>
<form class="set" id="set"><label>Label<input id="fl" maxlength="28" placeholder="{deflabel}"></label><label>{label}<input type="date" id="fd" required></label><label>Planning started<input type="date" id="fs"></label><div class="row"><button class="btn" type="submit">Save</button><button class="btn ghost" type="button" id="cx">Cancel</button></div></form></div>''',
    js=f'''const V=document.getElementById('view'),S=document.getElementById('set');let st=store.get();
function draw(){{const d=parseD(st.date),lab=st.label||'{deflabel}';
if(!d){{V.innerHTML='<div class="empty"><div class="cap">'+lab+'</div><div class="serif" style="font-size:20px;margin-top:8px">Set your date</div><button class="btn" id="go">Add date</button></div>';document.getElementById('go').onclick=open;return}}
const now=new Date(),left=dayDiff(now,d),start=parseD(st.start)||parseD(st.saved)||now,tot=Math.max(1,dayDiff(start,d)),p=left<=0?1:Math.min(1,Math.max(0.02,1-left/tot));
const R=46,C=2*Math.PI*R;let big,sub;if(left>0){{big=left;sub=left==1?'DAY TO GO':'DAYS TO GO'}}else if(left==0){{big='Today';sub='THE DAY IS HERE'}}else{{big=-left;sub=-left==1?'DAY MARRIED':'DAYS MARRIED'}}
V.innerHTML=`<svg class="main" viewBox="0 0 160 150"><path d="${{seal(80,72,66,61,22)}}" fill="var(--band)" filter="url(#rough)"/><circle cx="80" cy="72" r="${{R}}" fill="none" stroke="var(--card)" stroke-width="7"/><circle cx="80" cy="72" r="${{R}}" fill="none" stroke="var(--main)" stroke-width="7" stroke-linecap="round" stroke-dasharray="${{C*p}} ${{C}}" transform="rotate(-90 80 72)" filter="url(#wash)"/><text x="80" y="${{typeof big=='number'?80:78}}" text-anchor="middle" class="serif" font-family="Cormorant Garamond,Georgia,serif" font-weight="600" font-size="${{typeof big=='number'&&big>999?28:34}}" fill="var(--deep)">${{big}}</text><text x="80" y="96" text-anchor="middle" font-size="7.5" letter-spacing="1.6" font-weight="600" fill="var(--mute)" font-family="Inter,system-ui,sans-serif">${{sub}}</text></svg><div class="cap lab">${{lab}}</div><div class="dt">${{fmtDate(d)}}</div>`}}
function open(){{document.getElementById('fl').value=st.label||'';document.getElementById('fd').value=st.date||'';document.getElementById('fs').value=st.start||'';S.classList.add('on')}}
document.getElementById('g').onclick=open;document.getElementById('cx').onclick=()=>S.classList.remove('on');
S.onsubmit=e=>{{e.preventDefault();const n=new Date();st={{label:document.getElementById('fl').value.trim(),date:document.getElementById('fd').value,start:document.getElementById('fs').value,saved:st.saved||`${{n.getFullYear()}}-${{n.getMonth()+1}}-${{n.getDate()}}`}};store.set(st);S.classList.remove('on');draw()}};
draw();setInterval(draw,6e4);''')
W['countdown']=cd('countdown','Wedding date','Days to I do','Countdown')
W['honeymoon-countdown']=cd('honeymoon','Departure date','Until we fly','Honeymoon countdown')

W['focus']=dict(title="This month's focus",maxw=300,pad='14px 16px 14px',css='''
.ph{font-size:22px;font-weight:600;line-height:1.1;margin:4px 0 8px;color:var(--deep)}
.trail{display:flex;gap:4px;margin:2px 0 10px}.trail i{flex:1;height:4px;border-radius:3px;background:var(--band)}.trail i.on{background:var(--main)}.trail i.past{background:var(--acc);opacity:.55}
ul{list-style:none}li{display:flex;gap:9px;align-items:center;font-size:12.5px;padding:6px 0;border-top:1px solid var(--line);cursor:pointer;user-select:none}
li svg{width:16px;height:16px;flex:none}li.done span{color:var(--mute);text-decoration:line-through;text-decoration-color:var(--acc)}
.empty .btn{margin-top:10px}''',
html='''<div class="card"><button class="gear" id="g"></button><div id="view"></div>
<form class="set" id="set"><label>Wedding date<input type="date" id="fd" required></label><div class="row"><button class="btn" type="submit">Save</button><button class="btn ghost" type="button" id="cx">Cancel</button></div><div class="hint">Tick items off as you go. Your full task list lives in Checklist.</div></form></div>''',
js='''const P=[[99999,366,'12+ months out',['Agree on a total budget','Draft the guest list','Tour and book the venue']],
[365,270,'12–9 months out',['Book photographer and videographer','Book caterer or confirm menu style','Ask your wedding party']],
[269,180,'9–6 months out',['Send save-the-dates','Book florist and music','Start shopping for attire']],
[179,120,'6–4 months out',['Order invitations','Plan the honeymoon','Book a hair and makeup trial']],
[119,60,'4–2 months out',['Send invitations','Cake tasting','First attire fitting']],
[59,30,'2–1 months out',['Chase missing RSVPs','Finalise the menu','Collect the rings']],
[29,8,'The final month',['Finish the seating plan','Make final payments','Confirm vendor arrival times']],
[7,1,'Wedding week',['Pack the day-of kit','Share the run of show','Rest, eat well, drink water']],
[0,0,'The day itself',['Breathe','Hold hands often','Enjoy every minute']],
[-1,-99999,'After the wedding',['Write thank-you notes','Return rentals','Update your name and documents']]];
const V=document.getElementById('view'),S=document.getElementById('set');let st=store.get();st.done=st.done||{};
const leaf='<path d="M8 2.5c3.2 2.6 3.2 8.4 0 11-3.2-2.6-3.2-8.4 0-11z" fill="var(--bg)"/>';
function draw(){const d=parseD(st.date);if(!d){V.innerHTML='<div class="empty"><div class="cap">This month\\'s focus</div><div class="ph serif">Add your wedding date</div><div class="hint">The three things that matter most right now.</div><button class="btn" id="go">Add date</button></div>';document.getElementById('go').onclick=open;return}
const left=dayDiff(new Date(),d),i=P.findIndex(p=>left<=p[0]&&left>=p[1]),ph=P[i];
V.innerHTML=`<div class="cap">This month's focus</div><div class="ph serif">${ph[2]}</div><div class="trail">${P.map((p,j)=>`<i class="${j<i?'past':j==i?'on':''}"></i>`).join('')}</div><ul>${ph[3].map((t,k)=>{const id=i+'-'+k,on=st.done[id];return `<li data-id="${id}" class="${on?'done':''}"><svg viewBox="0 0 16 16"><path d="${seal(8,8,7.6,6.6,10)}" fill="${on?'var(--main)':'none'}" stroke="var(--main)" stroke-width="1" filter="url(#rough)"/>${on?leaf:''}</svg><span>${t}</span></li>`}).join('')}</ul>`;
V.querySelectorAll('li').forEach(li=>li.onclick=()=>{const id=li.dataset.id;st.done[id]=!st.done[id];store.set(st);draw()})}
function open(){document.getElementById('fd').value=st.date||'';S.classList.add('on')}
document.getElementById('g').onclick=open;document.getElementById('cx').onclick=()=>S.classList.remove('on');
S.onsubmit=e=>{e.preventDefault();st.date=document.getElementById('fd').value;store.set(st);S.classList.remove('on');draw()};draw();setInterval(draw,36e5);''')

CITIES=[('Amsterdam',52.37,4.90,'Europe/Amsterdam'),('Athens',37.98,23.73,'Europe/Athens'),('Auckland',-36.85,174.76,'Pacific/Auckland'),('Austin',30.27,-97.74,'America/Chicago'),('Bali',-8.65,115.22,'Asia/Makassar'),('Barcelona',41.39,2.17,'Europe/Madrid'),('Boston',42.36,-71.06,'America/New_York'),('Cancún',21.16,-86.85,'America/Cancun'),('Cape Town',-33.92,18.42,'Africa/Johannesburg'),('Charleston',32.78,-79.93,'America/New_York'),('Chicago',41.88,-87.63,'America/Chicago'),('Dubai',25.20,55.27,'Asia/Dubai'),('Dublin',53.35,-6.26,'Europe/Dublin'),('Dubrovnik',42.65,18.09,'Europe/Zagreb'),('Edinburgh',55.95,-3.19,'Europe/London'),('Florence',43.77,11.26,'Europe/Rome'),('Istanbul',41.01,28.98,'Europe/Istanbul'),('Lake Como',45.99,9.26,'Europe/Rome'),('Lisbon',38.72,-9.14,'Europe/Lisbon'),('London',51.51,-0.13,'Europe/London'),('Los Angeles',34.05,-118.24,'America/Los_Angeles'),('Melbourne',-37.81,144.96,'Australia/Melbourne'),('Mexico City',19.43,-99.13,'America/Mexico_City'),('Miami',25.76,-80.19,'America/New_York'),('Napa Valley',38.30,-122.29,'America/Los_Angeles'),('Nashville',36.16,-86.78,'America/Chicago'),('New York',40.71,-74.01,'America/New_York'),('Paris',48.86,2.35,'Europe/Paris'),('Provence',43.95,4.81,'Europe/Paris'),('Rome',41.90,12.50,'Europe/Rome'),('San Francisco',37.77,-122.42,'America/Los_Angeles'),('Santorini',36.39,25.46,'Europe/Athens'),('Seattle',47.61,-122.33,'America/Los_Angeles'),('Sydney',-33.87,151.21,'Australia/Sydney'),('Tuscany',43.32,11.33,'Europe/Rome'),('Toronto',43.65,-79.38,'America/Toronto'),('Vancouver',49.28,-123.12,'America/Vancouver')]
copts=''.join(f'<option value="{c[0]}">{c[0]}</option>' for c in CITIES)
cjs='const CITIES={'+','.join(f'"{c[0]}":[{c[1]},{c[2]},"{c[3]}"]' for c in CITIES)+'};'
W['golden-hour']=dict(title='Golden hour',maxw=280,pad='12px 14px 12px',css='''
svg.arc{width:100%;height:auto;display:block}
.big{font-size:21px;font-weight:600;color:var(--deep);text-align:center;margin-top:-2px}
.meta{display:flex;justify-content:space-between;font-size:11px;color:var(--mute);margin-top:6px;border-top:1px solid var(--line);padding-top:6px}
.empty{text-align:center;padding:14px 4px}.empty .btn{margin-top:10px}''',
html=f'''<div class="card"><button class="gear" id="g"></button><div id="view"></div>
<form class="set" id="set"><label>Wedding date<input type="date" id="fd" required></label><label>Place<select id="fc"><option value="">Other (enter below)</option>{copts}</select></label><div class="row"><label>Latitude<input id="flat" inputmode="decimal" placeholder="51.5"></label><label>Longitude<input id="flon" inputmode="decimal" placeholder="-0.1"></label></div><div class="row"><button class="btn" type="submit">Save</button><button class="btn ghost" type="button" id="cx">Cancel</button></div></form></div>''',
js=cjs+'''
const rad=Math.PI/180;
function elev(t,lat,lon){const d=t/864e5-10957.5,g=(357.529+.98560028*d)*rad,q=280.459+.98564736*d,L=(q+1.915*Math.sin(g)+.02*Math.sin(2*g))*rad,e=(23.439-3.6e-7*d)*rad,ra=Math.atan2(Math.cos(e)*Math.sin(L),Math.cos(L)),dec=Math.asin(Math.sin(e)*Math.sin(L)),gmst=(18.697374558+24.06570982441908*d)%24,ha=(gmst*15+lon)*rad-ra;return Math.asin(Math.sin(lat*rad)*Math.sin(dec)+Math.cos(lat*rad)*Math.cos(dec)*Math.cos(ha))/rad}
function cross(t0,lat,lon,deg){let prev=elev(t0,lat,lon);for(let k=1;k<=900;k++){const t=t0+k*6e4,e=elev(t,lat,lon);if(prev>=deg&&e<deg)return t;prev=e}return null}
const V=document.getElementById('view'),S=document.getElementById('set');let st=store.get();
function draw(){const d=parseD(st.date);if(!d||st.lat==null){V.innerHTML='<div class="empty"><div class="cap">Golden hour</div><div class="serif" style="font-size:19px;margin-top:6px">Your best photo light</div><div class="hint" style="margin-top:4px">Add the date and place to see it.</div><button class="btn" id="go">Set up</button></div>';document.getElementById('go').onclick=open;return}
const noon=Date.UTC(d.getFullYear(),d.getMonth(),d.getDate(),12)-st.lon/15*36e5,a=cross(noon,st.lat,st.lon,6),ss=cross(noon,st.lat,st.lon,-.833),b=cross(noon,st.lat,st.lon,-4);
const f=t=>t?new Date(t).toLocaleTimeString('en-US',{hour:'numeric',minute:'2-digit',timeZone:st.tz||undefined}).toLowerCase().replace(' ',' '):'—';
const pos=x=>{const an=Math.PI*(1-x);return [100+80*Math.cos(an),64-46*Math.sin(an)]},A=pos(.80),B=pos(.97),Su=pos(.86);
V.innerHTML=`<div class="cap" style="text-align:center">Golden hour</div><svg class="arc" viewBox="0 6 200 64"><path d="M20 64 A80 46 0 0 1 180 64" fill="none" stroke="var(--line)" stroke-width="2.2" stroke-dasharray="1 5" stroke-linecap="round"/><path d="M${A[0]} ${A[1]} A80 46 0 0 1 ${B[0]} ${B[1]}" fill="none" stroke="var(--acc)" stroke-width="5" stroke-linecap="round" opacity=".9"/><path d="${seal(Su[0],Su[1],7.5,6.5,12)}" fill="var(--main)" filter="url(#rough)"/><line x1="8" y1="64" x2="192" y2="64" stroke="var(--deep)" stroke-width="1" opacity=".3"/></svg><div class="big serif">${f(a)} – ${f(b)}</div><div class="meta"><span>Sunset ${f(ss)}</span><span>${st.city||'Custom place'} · ${d.toLocaleDateString('en-GB',{day:'numeric',month:'short'})}</span></div>`}
function open(){document.getElementById('fd').value=st.date||'';document.getElementById('fc').value=st.city||'';document.getElementById('flat').value=st.city?'':(st.lat??'');document.getElementById('flon').value=st.city?'':(st.lon??'');S.classList.add('on')}
document.getElementById('g').onclick=open;document.getElementById('cx').onclick=()=>S.classList.remove('on');
S.onsubmit=e=>{e.preventDefault();const c=document.getElementById('fc').value;st.date=document.getElementById('fd').value;if(c){const v=CITIES[c];st.city=c;st.lat=v[0];st.lon=v[1];st.tz=v[2]}else{const la=parseFloat(document.getElementById('flat').value),lo=parseFloat(document.getElementById('flon').value);if(isNaN(la)||isNaN(lo))return;st.city='';st.lat=la;st.lon=lo;st.tz=''}store.set(st);S.classList.remove('on');draw()};draw();''')

W['vow-card']=dict(title='Vow card',maxw=320,pad='14px 18px 14px',css='''
.q{font-size:19px;font-style:italic;line-height:1.35;min-height:52px;outline:none;margin-top:6px;color:var(--ink)}
.q:empty::before{content:attr(data-ph);color:var(--mute)}
.ft{display:flex;justify-content:space-between;align-items:center;margin-top:8px}.ft svg{width:26px;height:26px}
.sv{font-size:10.5px;color:var(--mute);opacity:0;transition:opacity .4s}.sv.on{opacity:1}''',
html='''<div class="card"><div class="cap">A line for my vows</div><div class="q serif" id="q" contenteditable="true" spellcheck="true" data-ph="I promise to…"></div><div class="ft"><span class="sv" id="sv">Saved</span><svg viewBox="0 0 30 30"><path id="sp" fill="var(--acc)" filter="url(#rough)"/><path d="M15 9.5c2.8 2.2 2.8 8.8 0 11-2.8-2.2-2.8-8.8 0-11z" fill="var(--bg)"/></svg></div></div>''',
js='''document.getElementById('sp').setAttribute('d',seal(15,15,13.5,12,14));const q=document.getElementById('q'),sv=document.getElementById('sv');let st=store.get();q.textContent=st.t||'';let tm;
q.addEventListener('input',()=>{clearTimeout(tm);tm=setTimeout(()=>{st.t=q.textContent.slice(0,400);store.set(st);sv.classList.add('on');setTimeout(()=>sv.classList.remove('on'),1200)},400)});''')

W['thank-you-tally']=dict(title='Thank-you tally',maxw=300,pad='14px 16px 14px',css='''
.n{font-size:30px;font-weight:600;color:var(--deep);line-height:1;margin-top:6px}.n small{font-size:15px;color:var(--mute);font-weight:500}
.dots{display:grid;grid-template-columns:repeat(20,1fr);gap:3px;margin:10px 0}.dots svg{width:100%;height:auto;display:block}
.ft{display:flex;justify-content:space-between;align-items:center}.pm{display:flex;gap:6px}.pm button{width:30px;height:30px;border-radius:50%;background:var(--band);font-size:17px;line-height:1;color:var(--deep)}.pm button.add{background:var(--main);color:var(--bg)}''',
html='''<div class="card"><button class="gear" id="g"></button><div class="cap">Thank-you notes sent</div><div id="view"></div>
<form class="set" id="set"><label>Notes to send in total<input type="number" min="1" max="999" id="ft" required></label><div class="row"><button class="btn" type="submit">Save</button><button class="btn ghost" type="button" id="cx">Cancel</button></div></form></div>''',
js='''const V=document.getElementById('view'),S=document.getElementById('set');let st=store.get();st.n=st.n||0;st.total=st.total||80;
function draw(){const p=Math.min(1,st.n/st.total),on=Math.round(p*20);
V.innerHTML=`<div class="n serif">${st.n} <small>/ ${st.total}</small></div><div class="dots">${Array.from({length:20},(_,i)=>`<svg viewBox="0 0 12 10"><rect x=".6" y=".6" width="10.8" height="8.8" rx="1.4" fill="${i<on?'var(--main)':'none'}" stroke="${i<on?'var(--main)':'var(--line)'}" stroke-width="1"/><path d="M1 1.4 6 5.6 11 1.4" fill="none" stroke="${i<on?'var(--bg)':'var(--line)'}" stroke-width="1"/></svg>`).join('')}</div><div class="ft"><span class="hint">${st.n>=st.total?'All sent. Lovely.':(st.total-st.n)+' to go'}</span><div class="pm"><button id="m" aria-label="One less">−</button><button id="p" class="add" aria-label="One more">+</button></div></div>`;
document.getElementById('m').onclick=()=>{st.n=Math.max(0,st.n-1);store.set(st);draw()};document.getElementById('p').onclick=()=>{st.n=Math.min(st.total,st.n+1);store.set(st);draw()}}
document.getElementById('g').onclick=()=>{document.getElementById('ft').value=st.total;S.classList.add('on')};document.getElementById('cx').onclick=()=>S.classList.remove('on');
S.onsubmit=e=>{e.preventDefault();st.total=Math.max(1,parseInt(document.getElementById('ft').value)||80);store.set(st);S.classList.remove('on');draw()};draw();''')

W['date']=dict(title='Date card',maxw=240,pad='12px 14px 12px',css='''
.card{display:flex;align-items:center;gap:14px}
.cal{position:relative;width:64px;height:68px;flex:none}
.cal svg{width:100%;height:100%;display:block}
.dn{position:absolute;left:0;right:0;top:20px;text-align:center;font-size:30px;font-weight:600;line-height:1;color:var(--deep)}
.mo{position:absolute;left:0;right:0;top:8px;text-align:center;font-size:8.5px;letter-spacing:.2em;color:var(--card);font-weight:600;text-transform:uppercase}
.wd{font-size:19px;font-weight:600;line-height:1.1}.sub{font-size:11px;color:var(--mute);margin-top:4px;letter-spacing:.02em}
.bar{height:4px;border-radius:3px;background:var(--band);margin-top:8px;overflow:hidden}.bar i{display:block;height:100%;background:var(--main);border-radius:3px}''',
html='''<div class="card"><div class="cal"><svg viewBox="0 0 64 68"><path id="sp" d="" fill="var(--band)" filter="url(#rough)"/><rect x="6" y="8" width="52" height="54" rx="8" fill="var(--card)" stroke="var(--line)"/><path d="M6 16a8 8 0 0 1 8-8h36a8 8 0 0 1 8 8v8H6z" fill="var(--main)"/></svg><div class="mo" id="mo"></div><div class="dn serif" id="dn"></div></div>
<div><div class="wd serif" id="wd"></div><div class="sub" id="sub"></div><div class="bar"><i id="bar"></i></div></div></div>''',
js='''document.getElementById('sp').setAttribute('d',seal(32,34,31,28,16));
function tick(){const n=new Date(),y0=new Date(n.getFullYear(),0,0),doy=dayDiff(y0,n),len=(n.getFullYear()%4==0&&(n.getFullYear()%100!=0||n.getFullYear()%400==0))?366:365;
const t=new Date(Date.UTC(n.getFullYear(),n.getMonth(),n.getDate()));const dn=t.getUTCDay()||7;t.setUTCDate(t.getUTCDate()+4-dn);const wk=Math.ceil(((t-Date.UTC(t.getUTCFullYear(),0,1))/864e5+1)/7);
document.getElementById('mo').textContent=n.toLocaleDateString('en-GB',{month:'short'});document.getElementById('dn').textContent=n.getDate();
document.getElementById('wd').textContent=n.toLocaleDateString('en-GB',{weekday:'long'});
document.getElementById('sub').textContent='Week '+wk+' \u00b7 day '+doy+'/'+len;document.getElementById('bar').style.width=(doy/len*100)+'%'}
tick();setInterval(tick,6e4);''')

W['moon']=dict(title='Moon phase',maxw=240,pad='12px 14px 12px',css='''
.card{display:flex;align-items:center;gap:14px}.m{width:60px;height:60px;flex:none}.m svg{width:100%;height:100%;display:block}
.nm{font-size:19px;font-weight:600;line-height:1.1}.sub{font-size:11px;color:var(--mute);margin-top:4px;line-height:1.4}''',
html='''<div class="card"><div class="m"><svg viewBox="0 0 60 60"><defs><clipPath id="cp"><circle cx="30" cy="30" r="25"/></clipPath></defs><circle cx="30" cy="30" r="25" fill="var(--line)" opacity=".7"/><path id="lit" fill="var(--main)" clip-path="url(#cp)" filter="url(#rough)"/></svg></div>
<div><div class="cap">Tonight\u2019s moon</div><div class="nm serif" id="nm"></div><div class="sub" id="sub"></div></div></div>''',
js='''const SYN=29.530588853,REF=Date.UTC(2000,0,6,18,14);
function tick(){const n=new Date();let a=((n-REF)/864e5/SYN)%1;if(a<0)a+=1;
const ill=(1-Math.cos(a*2*Math.PI))/2,names=['New moon','Waxing crescent','First quarter','Waxing gibbous','Full moon','Waning gibbous','Last quarter','Waning crescent'];
const nm=names[Math.floor(a*8+.5)%8];document.getElementById('nm').textContent=nm;
const nextFull=a<.5?(.5-a)*SYN:(1.5-a)*SYN,nextNew=(1-a)*SYN;
document.getElementById('sub').textContent=Math.round(ill*100)+'% lit \u00b7 '+(a>.47&&a<.56?'around its fullest':'full in '+Math.round(nextFull)+' days');
const R=25,cx=30,cy=30,k=Math.cos(a*2*Math.PI),rx=Math.abs(k)*R,waxing=a<.5;
const outer=waxing?1:0,sweepOuter=outer,term=k>0?(waxing?0:1):(waxing?1:0);
let d;if(a<.015||a>.985)d='';else{const x=cx+(waxing?1:-1)*0;d='M'+cx+' '+(cy-R)+' A'+R+' '+R+' 0 0 '+sweepOuter+' '+cx+' '+(cy+R)+' A'+rx+' '+R+' 0 0 '+term+' '+cx+' '+(cy-R)+'Z'}
document.getElementById('lit').setAttribute('d',d)}
tick();setInterval(tick,36e5);''')

for k,w in W.items():
    h=base
    for a,b in [('__TITLE__',w['title']),('__MAXW__',str(w['maxw'])),('__PAD__',w['pad']),('__CSS__',w['css']),('__HTML__',w['html']),('__JS__',w['js']),('__ID__',k)]:
        h=h.replace(a,b)
    open(os.path.join(D,k+'.html'),'w').write(h)
print(list(W))
