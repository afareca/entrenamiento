/* Figuras animadas propias para los ejercicios sin GIF.
   Una figura de articulaciones que interpola entre poses al ritmo de la respiración. */
var FIG=(function(){
  var NS='http://www.w3.org/2000/svg';
  /* lado cercano: N · lado lejano: F.  sh hombro, el codo, ha mano, hi cadera, kn rodilla, an tobillo, to punta */
  var SUP={ head:[42,110], sh:[62,116], hi:[124,118],
    elN:[86,128], haN:[110,129], elF:[86,124], haF:[110,125],
    knN:[154,84], anN:[178,124], toN:[192,124],
    knF:[150,86], anF:[172,123], toF:[186,123], rib:9, pf:0, pfa:.35, neck:[52,113] };
  function P(base,cambios){ var o={}; for(var k in base) o[k]=base[k]; for(var c in cambios) o[c]=cambios[c]; return o; }

  var CUAD={ head:[62,89], neck:[72,84], sh:[80,78], hi:[156,80],
    elN:[82,104], haN:[82,126], elF:[88,103], haF:[88,125],
    knN:[158,126], anN:[192,126], toN:[200,122],
    knF:[164,125], anF:[198,125], toF:[206,121], rib:0, pf:0, pfa:0 };

  var POSES={
    supina:SUP,
    inhala:P(SUP,{rib:14}),
    exhala:P(SUP,{rib:8}),
    pfArriba:P(SUP,{rib:8,pf:-7,pfa:1}),
    pfSuelta:P(SUP,{rib:11,pf:0,pfa:.3}),
    talonN:P(SUP,{rib:8,knN:[168,118],anN:[206,124],toN:[218,118]}),
    talonF:P(SUP,{rib:8,knF:[164,117],anF:[200,123],toF:[212,117]}),
    cuad:CUAD,
    /* brazo lejano adelante + pierna cercana atrás */
    birdA:P(CUAD,{elF:[55,75],haF:[29,73],knN:[186,80],anN:[218,80],toN:[226,74]}),
    /* brazo cercano adelante + pierna lejana atrás */
    birdB:P(CUAD,{elN:[55,76],haN:[29,74],knF:[188,79],anF:[220,78],toF:[228,72]})
  };

  /* secuencias: [ms, pose, texto] */
  var SEQ={
    respira:[[4000,'inhala','Inhala · costillas a los lados'],[6000,'exhala','Exhala largo']],
    piso:[[5000,'pfArriba','Exhala · aprieta y sube'],[5000,'pfSuelta','Suelta del todo']],
    rapido:[[700,'pfArriba','Aprieta'],[900,'pfSuelta','Suelta']],
    talon:[[3000,'talonN','Exhala · desliza'],[3000,'supina','Inhala · vuelve'],[3000,'talonF','Exhala · la otra'],[3000,'supina','Inhala · vuelve']],
    bird:[[3000,'birdA','Exhala · extiende'],[2500,'cuad','Inhala · vuelve'],[3000,'birdB','Exhala · al otro lado'],[2500,'cuad','Inhala · vuelve']]
  };

  function el(tag,at,padre){ var e=document.createElementNS(NS,tag); for(var k in at) e.setAttribute(k,at[k]); if(padre) padre.appendChild(e); return e; }
  function suave(t){ return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2; }
  function mezcla(a,b,t){ var o={}; for(var k in a){ var x=a[k],y=b[k];
      o[k]=Array.isArray(x)?[x[0]+(y[0]-x[0])*t,x[1]+(y[1]-x[1])*t]:x+(y-x)*t; } return o; }

  function crear(cont,tipo,pausadoFn){
    var seq=SEQ[tipo]||SEQ.respira, cuad=(tipo==='bird');
    cont.innerHTML='';
    var svg=el('svg',{viewBox:cuad?'14 50 220 92':'12 68 216 74',width:'100%',height:'100%','aria-hidden':'true'},cont);
    el('rect',{x:14,y:cuad?128:128,width:212,height:7,rx:3.5,fill:'#EADFD2'},svg);           /* colchoneta */
    var C={lej:'#E3B9A7',cuerpo:'#B9654A',cerca:'#9C4F37',piel:'#B9654A'};
    function linea(col,w){ return el('path',{fill:'none',stroke:col,'stroke-width':w,'stroke-linecap':'round','stroke-linejoin':'round'},svg); }
    var bL=linea(C.lej,9), pL=linea(C.lej,11);                                          /* brazo y pierna lejanos */
    var torso=linea(C.cuerpo,20), cuello=linea(C.cuerpo,8);
    var rib=el('ellipse',{fill:'#E7C9B9',opacity:.9},svg);
    var pierna=linea(C.cerca,12), brazo=linea(C.cerca,10);                              /* cercanos */
    var pf=el('ellipse',{fill:'#7E9A73'},svg);
    var flecha=el('path',{fill:'none',stroke:'#7E9A73','stroke-width':3,'stroke-linecap':'round','stroke-linejoin':'round'},svg);
    var cab=el('circle',{r:11,fill:C.cuerpo},svg);
    var pelo=el('path',{fill:'#5A2E22'},svg);
    var etiq=document.createElement('div'); etiq.className='orbe-txt'; cont.appendChild(etiq);

    function dibujar(p){
      function L(){ var a=arguments,d='M'+a[0][0]+' '+a[0][1]; for(var i=1;i<a.length;i++) d+=' L'+a[i][0]+' '+a[i][1]; return d; }
      bL.setAttribute('d',L(p.sh,p.elF,p.haF));
      pL.setAttribute('d',L(p.hi,p.knF,p.anF,p.toF));
      torso.setAttribute('d',L(p.sh,p.hi));
      var nk=p.neck||p.sh; cuello.setAttribute('d',L(p.head,nk));
      pierna.setAttribute('d',L(p.hi,p.knN,p.anN,p.toN));
      brazo.setAttribute('d',L(p.sh,p.elN,p.haN));
      cab.setAttribute('cx',p.head[0]); cab.setAttribute('cy',p.head[1]);
      /* moño: le da lectura de figura femenina sin detalle */
      var hx=p.head[0], hy=p.head[1];
      pelo.setAttribute('d','M'+(hx-11)+' '+(hy-1)+' A11 11 0 0 1 '+(hx+9)+' '+(hy-6)+' L'+(hx+2)+' '+(hy-3)+' Z M'+(hx-15)+' '+(hy-4)+' a6 6 0 1 0 0.1 0 Z');
      if(cuad){ rib.setAttribute('rx',0); pf.setAttribute('rx',0); flecha.setAttribute('d',''); return; }
      var cx=(p.sh[0]+p.hi[0])/2-14, cy=(p.sh[1]+p.hi[1])/2-1;
      rib.setAttribute('cx',cx); rib.setAttribute('cy',cy); rib.setAttribute('rx',22); rib.setAttribute('ry',p.rib*.55);
      var px=p.hi[0]-4, py=p.hi[1]+5+p.pf*.5;
      pf.setAttribute('cx',px); pf.setAttribute('cy',py); pf.setAttribute('rx',9); pf.setAttribute('ry',4.5); pf.setAttribute('opacity',p.pfa);
      var fa=Math.max(0,(p.pfa-.35)/.65);
      flecha.setAttribute('d','M'+px+' '+(py-8)+' L'+px+' '+(py-20)+' M'+(px-5)+' '+(py-15)+' L'+px+' '+(py-20)+' L'+(px+5)+' '+(py-15));
      flecha.setAttribute('opacity',fa);
    }

    var k=0, desde=POSES[cuad?'cuad':'supina'], hasta, t0=0, dur=1, raf=null, vivo=true, acum=0, ult=0;
    function siguiente(){ var s=seq[k%seq.length]; hasta=POSES[s[1]]; dur=s[0]; etiq.textContent=s[2]; acum=0; k++; }
    function cuadro(ts){
      if(!vivo) return;
      if(!ult) ult=ts; var dt=ts-ult; ult=ts;
      if(!(pausadoFn&&pausadoFn())) acum+=dt;
      var t=Math.min(1,acum/dur); dibujar(mezcla(desde,hasta,suave(t)));
      if(t>=1){ desde=hasta; siguiente(); }
      raf=requestAnimationFrame(cuadro);
    }
    dibujar(desde); siguiente(); raf=requestAnimationFrame(cuadro);
    return { parar:function(){ vivo=false; cancelAnimationFrame(raf); },
             pose:function(nombre){ vivo=false; cancelAnimationFrame(raf); dibujar(POSES[nombre]); } };
  }
  return {crear:crear, POSES:POSES};
})();
