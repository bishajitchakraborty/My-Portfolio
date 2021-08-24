///button
const hb=document.querySelector(".hbtn");
const ab = document.querySelector(".abtn");
const cb = document.querySelector(".cbtn");
const sb = document.querySelector(".sbtn");
const pb = document.querySelector(".pbtn");
const skb = document.querySelector(".skbtn");
const exb = document.querySelector(".exbtn");
const edb = document.querySelector(".edbtn");


////pagename
const hp = document.querySelector(".home");
const ap = document.querySelector(".about");
const cp = document.querySelector(".contact");
const sp = document.querySelector(".services");
const pp = document.querySelector(".projects");
const skp = document.querySelector(".skills");
const exp = document.querySelector(".experience");
const edp = document.querySelector(".education");


hb.addEventListener('click',function(){
   hp.classList.add("active")
   ap.classList.remove("active")
   cp.classList.remove("active")
   sp.classList.remove("active")
   pp.classList.remove("active")
})
ab.addEventListener('click', function(){
    hp.classList.remove("active")
    ap.classList.add("active")
    cp.classList.remove("active")
    sp.classList.remove("active")
    pp.classList.remove("active")
})
cb.addEventListener('click', function(){
    hp.classList.remove("active")
    ap.classList.remove("active")
    cp.classList.add("active")
    sp.classList.remove("active")
    pp.classList.remove("active")
})
sb.addEventListener('click', function () {
    hp.classList.remove("active")
    ap.classList.remove("active")
    cp.classList.remove("active")
    sp.classList.add("active")
    pp.classList.remove("active")
})
pb.addEventListener('click', function () {
    hp.classList.remove("active")
    ap.classList.remove("active")
    cp.classList.remove("active")
    sp.classList.remove("active")
    pp.classList.add("active")
})
skb.addEventListener('click', function () {
    skp.classList.add("active")
    exp.classList.remove("active")
    edp.classList.remove("active")
    
})
exb.addEventListener('click', function () {
    skp.classList.remove("active")
    exp.classList.add("active")
    edp.classList.remove("active")
    
})
edb.addEventListener('click', function () {
    skp.classList.remove("active")
    exp.classList.remove("active")
    edp.classList.add("active")
    
})
