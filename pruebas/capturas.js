// Capturas a ancho de iPhone (390 px) del inicio de cada app. Uso: node pruebas/capturas.js [carpeta_salida]
// Chromium de Playwright no trae H.264: los videos se ven como su imagen de respaldo (poster). En Safari sí corren.
const {chromium}=require('playwright'), path=require('path'), fs=require('fs');
(async()=>{const out=process.argv[2]||path.join(__dirname,'capturas'); fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch(process.env.CHROMIUM?{executablePath:process.env.CHROMIUM}:{}); const errs=[];
 for(const f of ['index.html','core.html','vigor.html','amplitud.html']){
  const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2}); p.on('pageerror',e=>errs.push(f+': '+e.message));
  await p.addInitScript(()=>{window.speechSynthesis={getVoices:()=>[],speak(){},cancel(){}};});
  await p.goto('file://'+path.join(__dirname,'..',f)); await p.waitForTimeout(500);
  await p.screenshot({path:path.join(out,f.replace('.html','')+'_inicio.png'),fullPage:true});
  await p.click('#b-empezar'); await p.click('#b-ir'); for(let i=0;i<5;i++) await p.click('#c-sig');
  await p.waitForTimeout(800); await p.screenshot({path:path.join(out,f.replace('.html','')+'_sesion.png')}); }
 console.log('capturas en',out,'| errores:',errs.length?errs:'ninguno'); await b.close();})();
