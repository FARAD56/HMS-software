(function () {
  var root = document.documentElement;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function sleep(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }

  function currentTheme() {
    var set = root.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  document.querySelectorAll(".theme-toggle").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("mlr-theme", next); } catch (e) {}
    });
  });

  var nav = document.getElementById("nav");
  function onScroll() { nav.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  document.querySelectorAll(".copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(btn.getAttribute("data-copy")).then(function () {
        btn.textContent = "Copied";
        btn.classList.add("done");
        setTimeout(function () { btn.textContent = "Copy"; btn.classList.remove("done"); }, 1600);
      }, function () {});
    });
  });

  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el, i) { el.style.transitionDelay = (i % 4) * 80 + "ms"; io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  var card = document.querySelector(".chart-card");
  if (!card) return;

  var days = [
    { temp: "38.4", bp: "142/91", triage: "severe", label: "Severe", t: [4, 8], b: [4, 6], dash: 130, orders: 1 },
    { temp: "37.6", bp: "131/86", triage: "severe", label: "Severe", t: [60, 22], b: [60, 20], dash: 65, orders: 2 },
    { temp: "36.9", bp: "124/80", triage: "normal", label: "Normal", t: [116, 38], b: [116, 34], dash: 0, orders: 3 }
  ];
  var tempEl = card.querySelector(".v-temp");
  var bpEl = card.querySelector(".v-bp");
  var triageEl = card.querySelector(".triage");
  var dayEls = card.querySelectorAll(".day");
  var orderEls = card.querySelectorAll(".order");
  var lines = card.querySelectorAll(".spark-line");
  var dotT = card.querySelector(".d-temp");
  var dotB = card.querySelector(".d-bp");
  var vitalEls = card.querySelectorAll(".vital");

  function show(i) {
    var d = days[i];
    tempEl.textContent = d.temp;
    bpEl.textContent = d.bp;
    triageEl.setAttribute("data-state", d.triage);
    triageEl.textContent = d.label;
    dayEls.forEach(function (el, k) { el.classList.toggle("on", k === i); });
    orderEls.forEach(function (el, k) { el.classList.toggle("on", k < d.orders); });
    lines.forEach(function (l) { l.style.strokeDashoffset = d.dash; });
    dotT.setAttribute("cx", d.t[0]); dotT.setAttribute("cy", d.t[1]);
    dotB.setAttribute("cx", d.b[0]); dotB.setAttribute("cy", d.b[1]);
    vitalEls.forEach(function (v) { v.classList.toggle("hot", d.triage === "severe"); });
  }

  if (reduceMotion) { show(2); return; }

  var visible = true;
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (e) { visible = e[0].isIntersecting; }).observe(card);
  }
  show(0);
  (async function loop() {
    var i = 0;
    for (;;) {
      await sleep(i === 2 ? 4200 : 2400);
      if (!visible || document.hidden) continue;
      i = (i + 1) % 3;
      show(i);
    }
  })();
})();
