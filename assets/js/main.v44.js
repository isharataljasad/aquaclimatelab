/* AquaClimate Lab — interactions (vanilla, no dependencies) */
(function () {
  "use strict";

  /* ---------- Mobile navigation (single source of truth) ----------
     Robust against (a) running before the DOM exists and (b) being
     bound twice. A dataset flag makes binding idempotent, so even if
     this file is ever included more than once the toggle never gets
     two listeners (which would open-then-close on a single tap). */
  function initMobileNav() {
    var navToggle = document.querySelector("button.nav-toggle, .nav-toggle");
    var navMenu = document.querySelector("ul#nav-menu, #nav-menu");
    if (!navToggle || !navMenu) return;
    if (navToggle.dataset.navBound === "true") return;
    navToggle.dataset.navBound = "true";

    function closeMenu() {
      navToggle.setAttribute("aria-expanded", "false");
      navMenu.classList.remove("open");
    }
    function openMenu() {
      navToggle.setAttribute("aria-expanded", "true");
      navMenu.classList.add("open");
    }

    navToggle.addEventListener("click", function () {
      if (navMenu.classList.contains("open")) closeMenu();
      else openMenu();
    });

    navMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && navMenu.classList.contains("open")) {
        closeMenu();
        navToggle.focus();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initMobileNav);
  } else {
    initMobileNav();
  }

  /* ---------- Footer year ---------- */
  var yearEl = document.querySelector("#year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---------- Floating back-to-top button (all pages) ---------- */
  (function () {
    var style = document.createElement("style");
    style.textContent =
      ".floating-top{position:fixed;inset-inline-start:18px;bottom:18px;z-index:60;" +
      "width:46px;height:46px;border-radius:14px;border:1px solid rgba(255,255,255,.25);" +
      "background:rgba(12,42,67,.92);color:#EAF6FB;cursor:pointer;display:grid;place-items:center;" +
      "box-shadow:0 10px 26px rgba(12,42,67,.30);backdrop-filter:blur(8px);" +
      "opacity:0;visibility:hidden;transform:translateY(8px);" +
      "transition:opacity .2s ease,transform .2s ease,visibility .2s,background .2s}" +
      ".floating-top.show{opacity:1;visibility:visible;transform:translateY(0)}" +
      ".floating-top:hover,.floating-top:focus-visible{background:#0E84A8}" +
      ".floating-top svg{width:20px;height:20px}" +
      "@media (prefers-reduced-motion:reduce){.floating-top{transition:none}}";
    document.head.appendChild(style);

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "floating-top";
    btn.setAttribute("aria-label", "العودة إلى أعلى الصفحة");
    btn.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg>';
    document.body.appendChild(btn);

    function onScroll() {
      btn.classList.toggle("show", window.scrollY > 480);
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    btn.addEventListener("click", function () {
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
      var main = document.querySelector("#main") || document.body;
      if (main) main.focus && main.focus({ preventScroll: true });
    });
  })();

  /* ---------- Interactive water-quality demo ---------- */
  var ph = document.querySelector("#ph");
  var tds = document.querySelector("#tds");
  var hard = document.querySelector("#hard");
  var sal = document.querySelector("#sal");

  var phOut = document.querySelector("#phOut");
  var tdsOut = document.querySelector("#tdsOut");
  var hardOut = document.querySelector("#hardOut");
  var salOut = document.querySelector("#salOut");

  var box = document.querySelector("#signalBox");
  var title = document.querySelector("#signalTitle");
  var body = document.querySelector("#signalBody");

  function update() {
    if (!ph || !tds || !hard || !sal || !box) return;

    var phV = Number(ph.value);
    var tdsV = Number(tds.value);
    var hardV = Number(hard.value);
    var salV = Number(sal.value);

    if (phOut) phOut.textContent = phV.toFixed(1);
    if (tdsOut) tdsOut.textContent = String(Math.round(tdsV));
    if (hardOut) hardOut.textContent = String(Math.round(hardV));
    if (salOut) salOut.textContent = salV.toFixed(1);

    // Priority-ordered, simple educational interpretation.
    var state = "ok";
    var t = "عيّنة تعليمية متوازنة";
    var b = "القيم الحالية ضمن نطاق تعليمي متوازن. غيّر المؤشرات لرؤية كيف تتبدّل القراءة.";

    if (phV < 6.5 || phV > 8.5) {
      state = "watch";
      t = "إشارة pH خارج النطاق المتوازن";
      b = "الحموضة خارج النطاق التعليمي المتوازن (6.5–8.5)؛ تحتاج تفسيرًا حسب مصدر العينة وسياقها.";
    } else if (salV > 10) {
      state = "watch";
      t = "إشارة ملوحة مرتفعة";
      b = "الملوحة مرتفعة وتقترب من المياه قليلة الملوحة (brackish)؛ ترتبط غالبًا بالمصدر أو التبخّر في المناطق الجافة.";
    } else if (tdsV > 1000) {
      state = "watch";
      t = "إشارة أملاح ذائبة مرتفعة";
      b = "ارتفاع TDS يشير إلى أملاح ذائبة أعلى، ويحتاج ربطًا بالمصدر ونوع المعالجة المطلوبة.";
    } else if (hardV > 300) {
      state = "watch";
      t = "إشارة عسر مرتفع";
      b = "العسر العالي يرتبط عادةً بالكالسيوم والمغنيسيوم، وقد يؤثر على الاستخدامات المنزلية والصناعية.";
    }

    box.setAttribute("data-state", state);
    if (title) title.textContent = t;
    if (body) body.textContent = b;
  }

  [ph, tds, hard, sal].forEach(function (el) {
    if (el) el.addEventListener("input", update);
  });
  update();
})();
