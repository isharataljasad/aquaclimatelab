/* ============================================================
   AquaClimate Lab × إشارات الجسد — Mobile UX helpers (v44)
   Tiny, dependency-free, fully optional. Nothing here is
   required for the page to work; it only refines behaviour.
   ============================================================ */
(function () {
  "use strict";

  /* 1) Mark the current page in the top navigation (aria-current).
        v44 understands clean URLs (/career-os), .html URLs, and
        folder-index fallbacks (/career-os/). */
  function normalizePathForNav(value) {
    try {
      var url = new URL(value || "/", window.location.origin);
      var path = url.pathname || "/";
      path = path.replace(/\/index\.html$/i, "/");
      path = path.replace(/\.html$/i, "");
      path = path.replace(/\/$/, "") || "/";
      return path;
    } catch (e) {
      return "";
    }
  }
  try {
    var here = normalizePathForNav(window.location.href);
    document.querySelectorAll(".nav-menu a[href]").forEach(function (a) {
      var href = a.getAttribute("href") || "";
      var target = normalizePathForNav(href.split("#")[0] || "/");
      if (target && target === here) {
        a.setAttribute("aria-current", "page");
      }
    });
  } catch (e) { /* no-op */ }

  /* 2) Add a subtle "swipe horizontally" hint to tables that actually
        overflow on small screens, then keep it accurate on resize. */
  function tagScrollableTables() {
    var wraps = document.querySelectorAll(".table-wrap");
    wraps.forEach(function (w) {
      var scrollable = w.scrollWidth > w.clientWidth + 4;
      w.classList.toggle("is-scrollable", scrollable);
    });
  }

  /* 3) Book Tools, mobile only: the ten "READY TO USE" tables default to
        open, which alone adds thousands of pixels at 390px. On small
        screens we start them collapsed — every tool's summary card above
        already lists the tool names, and one tap re-opens the table.
        Desktop is untouched; without JS they simply stay open (safe). */
  function collapseBookToolTablesOnMobile() {
    try {
      if (window.innerWidth > 760) return;
      var root = document.querySelector("#book-derived-tools");
      if (!root) return;
      root.querySelectorAll(".module-card details[open]").forEach(function (d) {
        d.removeAttribute("open");
      });
    } catch (e) { /* no-op */ }
  }

  var resizeTimer = null;
  function onResize() {
    if (resizeTimer) clearTimeout(resizeTimer);
    resizeTimer = setTimeout(tagScrollableTables, 150);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      collapseBookToolTablesOnMobile();
      tagScrollableTables();
    });
  } else {
    collapseBookToolTablesOnMobile();
    tagScrollableTables();
  }
  window.addEventListener("resize", onResize, { passive: true });
  window.addEventListener("load", tagScrollableTables);
})();
