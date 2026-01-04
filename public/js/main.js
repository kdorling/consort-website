(() => {
  // <stdin>
  (function() {
    "use strict";
    function initDropdownMenus() {
      const mainNav = document.getElementById("main-nav");
      if (!mainNav) return;
      const dropdownParents = mainNav.querySelectorAll(".has-dropdown");
      dropdownParents.forEach(function(parent) {
        const link = parent.querySelector("a");
        link.addEventListener("click", function(e) {
          if (window.innerWidth > 768) {
            e.preventDefault();
            dropdownParents.forEach(function(otherParent) {
              if (otherParent !== parent) {
                otherParent.classList.remove("dropdown-open");
              }
            });
            parent.classList.toggle("dropdown-open");
          } else {
            e.preventDefault();
            parent.classList.toggle("mobile-open");
            console.log(
              "Mobile dropdown toggled:",
              parent.classList.contains("mobile-open")
            );
          }
        });
      });
      document.addEventListener("click", function(e) {
        if (!mainNav.contains(e.target)) {
          dropdownParents.forEach(function(parent) {
            parent.classList.remove("dropdown-open");
            parent.classList.remove("mobile-open");
          });
        }
      });
      document.addEventListener("keydown", function(e) {
        if (e.key === "Escape") {
          dropdownParents.forEach(function(parent) {
            parent.classList.remove("dropdown-open");
            parent.classList.remove("mobile-open");
          });
        }
      });
    }
    function initMobileMenu() {
      const mobileToggle = document.getElementById("mobile-menu-toggle");
      const mainNav = document.getElementById("main-nav");
      if (!mobileToggle || !mainNav) return;
      mobileToggle.addEventListener("click", function(e) {
        e.stopPropagation();
        mainNav.classList.toggle("mobile-open");
        const isExpanded = mainNav.classList.contains("mobile-open");
        mobileToggle.setAttribute("aria-expanded", isExpanded);
        mobileToggle.textContent = isExpanded ? "\u2715" : "\u2630";
        if (isExpanded) {
          document.body.classList.add("mobile-menu-open");
        } else {
          document.body.classList.remove("mobile-menu-open");
        }
      });
      document.addEventListener("click", function(e) {
        if (!mainNav.contains(e.target) && !mobileToggle.contains(e.target)) {
          mainNav.classList.remove("mobile-open");
          mobileToggle.setAttribute("aria-expanded", "false");
          mobileToggle.textContent = "\u2630";
          document.body.classList.remove("mobile-menu-open");
        }
      });
    }
    function initKeyboardNav() {
      const dropdownParents = document.querySelectorAll(".has-dropdown");
      dropdownParents.forEach(function(parent) {
        const link = parent.querySelector("a");
        const dropdown = parent.querySelector("ul");
        if (!dropdown) return;
        link.addEventListener("keydown", function(e) {
          if (e.key === "Enter" || e.key === " ") {
            if (window.innerWidth > 768) {
              e.preventDefault();
              const firstChild = dropdown.querySelector("a");
              if (firstChild) firstChild.focus();
            }
          }
          if (e.key === "Escape") {
            link.focus();
          }
        });
        const dropdownLinks = dropdown.querySelectorAll("a");
        dropdownLinks.forEach(function(dropdownLink, index) {
          dropdownLink.addEventListener("keydown", function(e) {
            if (e.key === "ArrowDown") {
              e.preventDefault();
              const next = dropdownLinks[index + 1] || dropdownLinks[0];
              next.focus();
            } else if (e.key === "ArrowUp") {
              e.preventDefault();
              const prev = dropdownLinks[index - 1] || link;
              prev.focus();
            } else if (e.key === "Escape") {
              e.preventDefault();
              link.focus();
            }
          });
        });
      });
    }
    function initSearch() {
      const searchToggle = document.querySelector(".search-toggle");
      if (!searchToggle) return;
      searchToggle.addEventListener("click", function() {
        alert("Search functionality - to be implemented");
      });
    }
    function initLanguageToggle() {
      const langToggle = document.querySelector(".lang-toggle");
      if (!langToggle) return;
      langToggle.addEventListener("click", function() {
        const currentLang = this.textContent.trim();
        this.textContent = currentLang === "FR" ? "EN" : "FR";
        console.log("Language toggle clicked - to be implemented");
      });
    }
    function initThemeToggle() {
      const themeToggle = document.getElementById("theme-toggle");
      const themeIcon = themeToggle?.querySelector(".theme-icon");
      if (!themeToggle) return;
      const currentTheme = localStorage.getItem("theme") || "light";
      document.documentElement.setAttribute("data-theme", currentTheme);
      if (themeIcon) {
        themeIcon.textContent = currentTheme === "dark" ? "\u2600\uFE0F" : "\u{1F319}";
      }
      themeToggle.addEventListener("click", function() {
        const theme = document.documentElement.getAttribute("data-theme");
        const newTheme = theme === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", newTheme);
        if (themeIcon) {
          themeIcon.textContent = newTheme === "dark" ? "\u2600\uFE0F" : "\u{1F319}";
        }
        localStorage.setItem("theme", newTheme);
        console.log("Theme switched to:", newTheme);
      });
    }
    function initSmoothScroll() {
      const skipLink = document.querySelector(".skip-link");
      if (!skipLink) return;
      skipLink.addEventListener("click", function(e) {
        const target = document.querySelector("#main-content");
        if (target) {
          e.preventDefault();
          target.focus();
          target.scrollIntoView({ behavior: "smooth" });
        }
      });
    }
    function initStickyHeader() {
      const header = document.querySelector("header");
      let lastScroll = 0;
      if (!header) return;
      window.addEventListener("scroll", function() {
        const currentScroll = window.pageYOffset;
        if (currentScroll > 0) {
          header.style.boxShadow = "0 2px 8px rgba(0, 0, 0, 0.15)";
        } else {
          header.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.1)";
        }
        lastScroll = currentScroll;
      });
    }
    function initResizeHandler() {
      let resizeTimer;
      window.addEventListener("resize", function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
          const mainNav = document.getElementById("main-nav");
          const mobileToggle = document.getElementById("mobile-menu-toggle");
          if (window.innerWidth > 768 && mainNav) {
            mainNav.classList.remove("mobile-open");
            document.body.classList.remove("mobile-menu-open");
            if (mobileToggle) {
              mobileToggle.setAttribute("aria-expanded", "false");
              mobileToggle.textContent = "\u2630";
            }
          }
        }, 250);
      });
    }
    function init() {
      initDropdownMenus();
      initMobileMenu();
      initKeyboardNav();
      initSearch();
      initLanguageToggle();
      initThemeToggle();
      initSmoothScroll();
      initStickyHeader();
      initResizeHandler();
      console.log("Bank of Canada theme initialized");
    }
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", init);
    } else {
      init();
    }
  })();
})();
