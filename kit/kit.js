// Shared helpers for WellKeptDesk widgets. Params: URL fragment first (never sent to the server), query string as fallback.
(function(){
  var raw = location.hash.length > 1 ? location.hash.slice(1) : location.search.slice(1);
  var P = new URLSearchParams(raw);
  var PALETTES = ["serein", "lavender-oat", "linen-sage", "espresso", "sea-glass", "olive", "champagne", "porcelain", "terracotta", "honey", "midnight", "sky-ledger", "lavender-haze", "ink-brass"];
  var STYLES = ['editorial','soft','minimal','ledger'];
  function pick(name, allowed, fallback){ var v = P.get(name); return allowed.indexOf(v) > -1 ? v : fallback; }
  function num(name){ var v = parseFloat(P.get(name)); return isFinite(v) ? v : null; }
  function text(name, fallback, max){ var v = P.get(name); if(!v) return fallback; return v.replace(/[\u0000-\u001f]/g,'').slice(0, max || 40); }
  function date(name){ var v = P.get(name); if(!v || !/^\d{4}-\d{2}-\d{2}$/.test(v)) return null; var p=v.split('-').map(Number); var d=new Date(p[0],p[1]-1,p[2]); return (d.getMonth()===p[1]-1) ? d : null; }
  var root = document.documentElement;
  root.setAttribute('data-theme', pick('theme',['light','dark','auto'],'auto'));
  root.setAttribute('data-palette', pick('palette', PALETTES, 'serein'));
  root.setAttribute('data-style', pick('style', STYLES, 'editorial'));
  function startOfDay(d){ return new Date(d.getFullYear(), d.getMonth(), d.getDate()); }
  function daysBetween(a,b){ return Math.round((startOfDay(b)-startOfDay(a))/86400000); } // DST-safe via rounding
  function onNewMinute(fn){ var last=''; setInterval(function(){ if(document.visibilityState!=='visible') return; var n=new Date(); var k=n.getHours()+':'+n.getMinutes(); if(k!==last){ last=k; fn(n); } }, 1000); }
  function isoWeek(d){ var t=new Date(d.getFullYear(),d.getMonth(),d.getDate()); var day=(t.getDay()+6)%7; t.setDate(t.getDate()-day+3); var y=t.getFullYear(); var j=new Date(y,0,4); return {week:1+Math.round(((t-j)/86400000-3+((j.getDay()+6)%7))/7), year:y}; }
  function el(tag,cls,txt){ var e=document.createElement(tag); if(cls) e.className=cls; if(txt!=null) e.textContent=txt; return e; }
  window.WK = { P:P, isoWeek:isoWeek, el:el, pick:pick, num:num, text:text, date:date, daysBetween:daysBetween, startOfDay:startOfDay, onNewMinute:onNewMinute,
    reduced: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches };
})();
