// Flujo de Núcleo (core.html): rotación, cambio de día, sesión de movilidad y guardado. Uso: node pruebas/nucleo.js
const {JSDOM}=require('jsdom');
const html=require('fs').readFileSync(require('path').join(__dirname,'..','core.html'),'utf8');
const errs=[],voz=[];
function mk(st){return new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://x.io/core.html',beforeParse(w){
 if(st) w.localStorage.setItem('nucleo.v2',JSON.stringify(st));
 const si=w.setInterval.bind(w),so=w.setTimeout.bind(w); w.setInterval=(f,ms)=>si(f,Math.max(1,ms/200)); w.setTimeout=(f,ms)=>so(f,Math.max(1,(ms||0)/200));
 function n(){return{connect(){},start(){},stop(){},frequency:{setValueAtTime(){}},gain:{setValueAtTime(){},exponentialRampToValueAtTime(){}}}}
 w.AudioContext=function(){return{currentTime:0,state:'running',destination:{},resume(){},createOscillator:n,createGain:n}};
 w.speechSynthesis={getVoices:()=>[{lang:'es-MX'}],speak(u){if(u.text.trim())voz.push(u.text)},cancel(){}};w.SpeechSynthesisUtterance=function(t){this.text=t};
 w.confirm=()=>true;w.alert=()=>{};w.requestAnimationFrame=f=>so(()=>f(Date.now()),16);w.cancelAnimationFrame=()=>{};
 w.addEventListener('error',e=>errs.push(e.message));}});}
const wait=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 let dom=mk({inicio:null,fase:1,sesiones:[],voz:1,nombre:'',fman:0,tests:[{f:'2026-10-14',dedos:1,firme:1}]});let w=dom.window,d=w.document,$=i=>d.getElementById(i),cl=e=>e.dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
 await wait(100);
 console.log('1 hoy     :',$('i-dia').textContent,'|',$('i-manana').textContent,'|',$('i-dur').textContent,'| chips:',[...d.querySelectorAll('#i-dias button')].map(b=>b.textContent+(b.className?'*':'')).join(' '));
 cl(d.querySelectorAll('#i-dias button')[3]);
 console.log('2 cambio D:',$('i-dia').textContent,'|',$('i-dur').textContent);
 cl($('b-ver')); console.log('3 ver     :',$('v-t').textContent,'|',[...d.querySelectorAll('#v-lista .ej')].map(x=>x.children[0].textContent).join(', '));
 cl(d.querySelector('[data-ir="inicio"]'));
 cl($('b-empezar')); cl($('b-ir'));
 let vist=[];for(let k=0;k<3000&&d.querySelector('.pant.on').id==='player';k++){ const m=d.querySelector('#escena .media,#escena .orbe-wrap'); const nm=d.querySelector('#escena .nombre');
   if(m&&nm&&!d.querySelector('#escena.trans')){const t=nm.textContent+':'+(d.querySelector('#escena .hoja')?'hoja':d.querySelector('#escena .media img')?'gif':d.querySelector('#escena .espera')?'orbe':'figura'); if(!vist.includes(t))vist.push(t);} await wait(5);}
 console.log('4 sesión D:',vist.join(' · '));
 console.log('5 fin     :',$('f-resumen').textContent); cl($('b-guardar'));
 console.log('6 después :',$('i-dia').textContent,'| sesiones',$('s-total').textContent,'| guardado dia:',JSON.parse(w.localStorage.getItem('nucleo.v2')).sesiones[0].dia);
 // fase 2 día A y C
 const hace=n=>{const x=new Date();x.setDate(x.getDate()-n);return x.getFullYear()+'-'+String(x.getMonth()+1).padStart(2,'0')+'-'+String(x.getDate()).padStart(2,'0')};
 dom=mk({inicio:hace(40),fase:2,sesiones:[1,2].map(n=>({f:hace(n),dia:'A',fase:2})),voz:1,nombre:'',fman:0,tests:[{}]});w=dom.window;d=w.document;await wait(100);
 console.log('7 fase2   :',d.getElementById('i-fase').textContent,'| hoy:',d.getElementById('i-dia').textContent);
 console.log('errores   :',errs.length?errs:'ninguno');process.exit(0);
})();
