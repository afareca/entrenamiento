// Flujo de Vigor o Amplitud: chequeo de hipertensión, sesión, rotación y aviso de semana 13. Uso: node pruebas/mayores.js vigor|amplitud
const {JSDOM}=require('jsdom');
const [,,app]=process.argv;
const html=require('fs').readFileSync(require('path').join(__dirname,'..',app+'.html'),'utf8');
const errs=[],voz=[];
function mk(st){return new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://x.io/'+app+'.html',beforeParse(w){
 if(st) w.localStorage.setItem(app+'.v1',JSON.stringify(st));
 const si=w.setInterval.bind(w),so=w.setTimeout.bind(w); w.setInterval=(f,ms)=>si(f,Math.max(1,ms/300)); w.setTimeout=(f,ms)=>so(f,Math.max(1,(ms||0)/300));
 function n(){return{connect(){},start(){},stop(){},frequency:{setValueAtTime(){}},gain:{setValueAtTime(){},exponentialRampToValueAtTime(){}}}}
 w.AudioContext=function(){return{currentTime:0,state:'running',destination:{},resume(){},createOscillator:n,createGain:n}};
 w.speechSynthesis={getVoices:()=>[{lang:'es-MX'}],speak(u){if(u.text.trim())voz.push(u.text)},cancel(){}};w.SpeechSynthesisUtterance=function(t){this.text=t};
 w.confirm=()=>true;w.alert=()=>{};w.requestAnimationFrame=f=>so(()=>f(Date.now()),16);w.cancelAnimationFrame=()=>{};
 w.addEventListener('error',e=>errs.push(e.message));}});}
const wait=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 let dom=mk();let w=dom.window,d=w.document,$=i=>d.getElementById(i),cl=e=>e.dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
 await wait(100);
 console.log('1 inicio  :',d.querySelector('h1').textContent,'|',$('i-fase').textContent,'|',$('i-dia').textContent,'|',$('i-dur').textContent,'|',$('i-aviso').textContent.slice(0,60));
 cl($('b-empezar')); cl(d.querySelector('[data-k="peso"] [data-v="1"]'));
 console.log('2 alarma  :',$('c-nota').textContent.slice(0,60),'| botón:',$('b-ir').textContent); cl($('b-ir')); console.log('  vuelve a:',d.querySelector('.pant.on').id);
 cl($('b-empezar')); cl(d.querySelector('[data-k="escape"] [data-v="1"]')); console.log('3 sin med :',$('c-nota').textContent.slice(0,110));
 cl(d.querySelector('[data-k="escape"] [data-v="0"]')); cl($('b-ir'));
 for(let k=0;k<6000&&d.querySelector('.pant.on').id==='player';k++) await wait(3);
 console.log('4 fin     :',$('f-resumen').textContent,'| pregunta:',d.querySelector('#fin .preg p').textContent);
 console.log('  voz     :',voz.filter(v=>/vuelta 2/.test(v)).length,'anuncios de vuelta 2 ·',voz.filter(v=>/Cambia/.test(v)).length,'cambios de lado');
 cl($('b-guardar')); console.log('5 después :',$('i-dia').textContent,'| sesiones',$('s-total').textContent);
 const hace=n=>{const x=new Date();x.setDate(x.getDate()-n);return x.getFullYear()+'-'+String(x.getMonth()+1).padStart(2,'0')+'-'+String(x.getDate()).padStart(2,'0')};
 dom=mk({inicio:hace(90),fase:3,sesiones:[{f:hace(1),dia:'A',fase:3}],pos:1,voz:1,nombre:'',fman:0,tests:[]});w=dom.window;d=w.document;await wait(100);
 console.log('6 semana 13:',d.getElementById('i-semana').textContent,'|',d.getElementById('i-aviso').textContent.slice(0,70));
 console.log('errores   :',errs.length?errs:'ninguno');process.exit(0);
})();
