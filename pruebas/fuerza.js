// Flujo completo de Fuerza (index.html) con temporizadores acelerados, audio y voz simulados. Uso: node pruebas/fuerza.js
const {JSDOM}=require('jsdom');
const html=require('fs').readFileSync(require('path').join(__dirname,'..','index.html'),'utf8');
const errs=[],voz=[],tonos=[];
function mk(st){return new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://afareca.github.io/entrenamiento/',
 beforeParse(w){
  if(st) w.localStorage.setItem('fuerza.v2',JSON.stringify(st));
  const si=w.setInterval.bind(w),so=w.setTimeout.bind(w);
  w.setInterval=(f,ms)=>si(f,Math.max(1,ms/250)); w.setTimeout=(f,ms)=>so(f,Math.max(1,(ms||0)/250));
  function n(){return{connect(){},start(){},stop(){},frequency:{setValueAtTime(v){tonos.push(v)}},gain:{setValueAtTime(){},exponentialRampToValueAtTime(){}}}}
  w.AudioContext=function(){return{currentTime:0,state:'running',destination:{},resume(){},createOscillator:n,createGain:n}};
  w.speechSynthesis={getVoices:()=>[{lang:'es-MX'}],speak(u){if(u.text.trim())voz.push(u.text)},cancel(){}};
  w.SpeechSynthesisUtterance=function(t){this.text=t}; w.confirm=()=>true;
  w.addEventListener('error',e=>errs.push(e.message));}});}
const wait=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 let dom=mk(); let w=dom.window,d=w.document,$=i=>d.getElementById(i),cl=e=>e.dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
 await wait(100);
 console.log('1 inicio :',$('i-fase').textContent,'|',$('i-sem').textContent,'|',$('p-nom').textContent,'|',$('p-chips').textContent,'|',$('p-dur').textContent);
 console.log('  lista  :',[...d.querySelectorAll('#p-lista div')].map(x=>x.textContent).join(' ; '));
 cl($('b-empezar')); cl(d.querySelector('#semaf [data-v="ambar"]'));
 console.log('2 ámbar  :',$('c-ajuste').textContent);
 cl(d.querySelector('#semaf [data-v="verde"]')); cl($('b-ir'));
 console.log('3 pasos  :',$('lomo').children.length,'| primero:',d.querySelector('.nom').textContent);
 // recorrer: en ejercicios de reps pulsar Hecho
 let guard=0, vistos=new Set();
 while(d.querySelector('.pant.on').id==='player' && guard<400){ guard++;
   const b=$('b-hecho'); if(b){ vistos.add(d.querySelector('.nom').textContent+' | '+d.querySelector('.dosis').textContent); cl(b); }
   await wait(20); }
 console.log('4 final  :',d.querySelector('.pant.on').id,'|',$('f-res').textContent);
 console.log('  ejercicios vistos:',[...vistos].join(' ; '));
 console.log('  voz ejemplos:',voz.filter(v=>v.includes('Sigue')).slice(0,2),voz.find(v=>v.includes('Swing')), '| cambia lado:',voz.filter(v=>v.includes('Cambia')).length);
 console.log('  tonos 880/660:',tonos.filter(t=>t==880).length,tonos.filter(t=>t==660).length);
 cl(d.querySelector('#rpe button:nth-child(3)')); cl($('b-guardar'));
 console.log('5 guardado:',$('s-tot').textContent,$('s-sem').textContent,'RPE',$('s-rpe').textContent,'| próxima:',$('p-nom').textContent,'| espina ok:',d.querySelectorAll('.espina i.ok').length);
 // semana 7
 const h=new Date();h.setDate(h.getDate()-45);
 dom=mk({inicio:h.toISOString().slice(0,10),sesiones:[],voz:1,med:{}}); w=dom.window;d=w.document;await wait(100);
 console.log('6 semana 7:',d.getElementById('i-fase').textContent,'|',d.getElementById('i-sem').textContent,'|',d.getElementById('p-chips').textContent,'|',[...d.querySelectorAll('#p-lista div')].slice(0,1).map(x=>x.textContent)[0]);
 d.getElementById('b-cambiar').dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
 console.log('  sesión B:',[...d.querySelectorAll('#p-lista div')].map(x=>x.textContent).slice(0,2).join(' ; '));
 // rojo
 d.getElementById('b-empezar').dispatchEvent(new w.MouseEvent('click',{bubbles:true})); d.querySelector('#semaf [data-v="rojo"]').dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
 console.log('7 rojo    :',d.getElementById('c-ajuste').textContent);
 console.log('errores  :',errs.length?errs:'ninguno');
 process.exit(0);
})();
