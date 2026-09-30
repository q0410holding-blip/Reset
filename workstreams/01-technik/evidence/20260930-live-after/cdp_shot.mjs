// Read-only: open URL in headless Chrome via CDP, optional mobile emulation, screenshots at given delays.
import { spawn } from 'node:child_process';
import { writeFileSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
const [,, url, prefix, mode='desktop', delays='2,5,12', full='0'] = process.argv;
const port = 9300 + Math.floor(Math.random()*500);
const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ['--headless=new','--disable-gpu','--hide-scrollbars',`--remote-debugging-port=${port}`,
   `--user-data-dir=${mkdtempSync(tmpdir()+'/cdp')}`,'about:blank'], {stdio:'ignore'});
const sleep = ms => new Promise(r=>setTimeout(r,ms));
let ws; for (let i=0;i<50;i++){ try{ const l=await (await fetch(`http://127.0.0.1:${port}/json`)).json(); const p=l.find(t=>t.type==='page'); if(p){ws=new WebSocket(p.webSocketDebuggerUrl);break;} }catch{} await sleep(200); }
await new Promise(r=>ws.onopen=r);
let id=0; const pend=new Map(); ws.onmessage=e=>{const m=JSON.parse(e.data); if(m.id&&pend.has(m.id)){pend.get(m.id)(m);pend.delete(m.id);}};
const send=(method,params={})=>new Promise(r=>{const i=++id;pend.set(i,r);ws.send(JSON.stringify({id:i,method,params}));});
await send('Page.enable'); await send('Runtime.enable');
if (mode==='mobile') {
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:2,mobile:true});
  await send('Emulation.setUserAgentOverride',{userAgent:'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1'});
  await send('Emulation.setTouchEmulationEnabled',{enabled:true});
} else await send('Emulation.setDeviceMetricsOverride',{width:1280,height:900,deviceScaleFactor:1,mobile:false});
const t0=Date.now(); await send('Page.navigate',{url});
const info = async () => (await send('Runtime.evaluate',{returnByValue:true,expression:`(()=>{const h=document.querySelector('h1');let op=[];let e=h;while(e&&e!==document.body){op.push(getComputedStyle(e).opacity);e=e.parentElement;}return {href:location.href,innerW:innerWidth,scrollW:document.documentElement.scrollWidth,h1:h&&h.innerText.slice(0,60),h1Top:h&&Math.round(h.getBoundingClientRect().top),h1Opacities:op.join(','),readyState:document.readyState}})()`})).result.result.value;
for (const d of delays.split(',').map(Number)) {
  const wait = d*1000 - (Date.now()-t0); if (wait>0) await sleep(wait);
  const i = await info();
  let params={format:'png'};
  if (full==='1'){ const {result}=await send('Page.getLayoutMetrics'); params={format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:result.cssContentSize.width,height:result.cssContentSize.height,scale:1}}; }
  const shot = await send('Page.captureScreenshot',params);
  const f=`${prefix}-${d}s.png`; writeFileSync(f, Buffer.from(shot.result.data,'base64'));
  console.log(JSON.stringify({file:f,t:d,...i}));
}
ws.close(); chrome.kill();
