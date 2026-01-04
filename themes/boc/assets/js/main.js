// Bank of Canada Theme - Main JavaScript

(function () {
  "use strict";

  // Dropdown Menu Toggle (Click-based for Desktop)
  function initDropdownMenus() {
    const mainNav = document.getElementById("main-nav");
    if (!mainNav) return;

    const dropdownParents = mainNav.querySelectorAll(".has-dropdown");

    dropdownParents.forEach(function (parent) {
      const link = parent.querySelector("a");

      // Add click handler for dropdown toggle
      link.addEventListener("click", function (e) {
        // On desktop, prevent default and toggle dropdown
        if (window.innerWidth > 768) {
          e.preventDefault();

          // Close all other dropdowns
          dropdownParents.forEach(function (otherParent) {
            if (otherParent !== parent) {
              otherParent.classList.remove("dropdown-open");
            }
          });

          // Toggle this dropdown
          parent.classList.toggle("dropdown-open");
        } else {
          // On mobile, toggle mobile-open class
          e.preventDefault();
          parent.classList.toggle("mobile-open");
          console.log(
            "Mobile dropdown toggled:",
            parent.classList.contains("mobile-open"),
          );
        }
      });
    });

    // Close dropdowns when clicking outside
    document.addEventListener("click", function (e) {
      if (!mainNav.contains(e.target)) {
        dropdownParents.forEach(function (parent) {
          parent.classList.remove("dropdown-open");
          parent.classList.remove("mobile-open");
        });
      }
    });

    // Close dropdowns on Escape key
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        dropdownParents.forEach(function (parent) {
          parent.classList.remove("dropdown-open");
          parent.classList.remove("mobile-open");
        });
      }
    });
  }

  // Mobile Menu Toggle
  function initMobileMenu() {
    const mobileToggle = document.getElementById("mobile-menu-toggle");
    const navContainer = document.querySelector(".nav-container");
    const mainNav = document.getElementById("main-nav");

    if (!mobileToggle || !navContainer) return;

    mobileToggle.addEventListener("click", function (e) {
      e.stopPropagation();
      navContainer.classList.toggle("mobile-open");

      // Update aria-expanded for accessibility
      const isExpanded = navContainer.classList.contains("mobile-open");
      mobileToggle.setAttribute("aria-expanded", isExpanded);

      // Change icon
      mobileToggle.textContent = isExpanded ? "✕" : "☰";

      // Toggle body class to prevent scrolling
      if (isExpanded) {
        document.body.classList.add("mobile-menu-open");
      } else {
        document.body.classList.remove("mobile-menu-open");
      }
    });

    // Close mobile menu when clicking outside
    document.addEventListener("click", function (e) {
      if (
        !navContainer.contains(e.target) &&
        !mobileToggle.contains(e.target)
      ) {
        navContainer.classList.remove("mobile-open");
        mobileToggle.setAttribute("aria-expanded", "false");
        mobileToggle.textContent = "☰";
        document.body.classList.remove("mobile-menu-open");
      }
    });
  }

  // Keyboard Navigation for Dropdowns
  function initKeyboardNav() {
    const dropdownParents = document.querySelectorAll(".has-dropdown");

    dropdownParents.forEach(function (parent) {
      const link = parent.querySelector("a");
      const dropdown = parent.querySelector("ul");

      if (!dropdown) return;

      // Handle keyboard navigation
      link.addEventListener("keydown", function (e) {
        // Open dropdown on Enter or Space
        if (e.key === "Enter" || e.key === " ") {
          if (window.innerWidth > 768) {
            e.preventDefault();
            const firstChild = dropdown.querySelector("a");
            if (firstChild) firstChild.focus();
          }
        }

        // Close on Escape
        if (e.key === "Escape") {
          link.focus();
        }
      });

      // Handle arrow keys within dropdown
      const dropdownLinks = dropdown.querySelectorAll("a");
      dropdownLinks.forEach(function (dropdownLink, index) {
        dropdownLink.addEventListener("keydown", function (e) {
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

  // Search Toggle (placeholder functionality)
  function initSearch() {
    const searchToggle = document.querySelector(".search-toggle");

    if (!searchToggle) return;

    searchToggle.addEventListener("click", function () {
      alert("Search functionality - to be implemented");
      // You can implement actual search functionality here
    });
  }

  // Language Toggle (placeholder functionality)
  function initLanguageToggle() {
    const langToggle = document.querySelector(".lang-toggle");

    if (!langToggle) return;

    langToggle.addEventListener("click", function () {
      // Toggle between EN and FR
      const currentLang = this.textContent.trim();
      this.textContent = currentLang === "FR" ? "EN" : "FR";

      // You can implement actual language switching here
      console.log("Language toggle clicked - to be implemented");
    });
  }

  // Theme Toggle (Dark/Light Mode)
  function initThemeToggle() {
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = themeToggle?.querySelector(".theme-icon");

    if (!themeToggle) return;

    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", currentTheme);

    // Update icon based on current theme
    if (themeIcon) {
      themeIcon.textContent = currentTheme === "dark" ? "☀️" : "🌙";
    }

    themeToggle.addEventListener("click", function () {
      // Get current theme
      const theme = document.documentElement.getAttribute("data-theme");

      // Toggle theme
      const newTheme = theme === "dark" ? "light" : "dark";

      // Update DOM
      document.documentElement.setAttribute("data-theme", newTheme);

      // Update icon
      if (themeIcon) {
        themeIcon.textContent = newTheme === "dark" ? "☀️" : "🌙";
      }

      // Save to localStorage
      localStorage.setItem("theme", newTheme);

      console.log("Theme switched to:", newTheme);
    });
  }

  // Smooth Scroll for Skip Link
  function initSmoothScroll() {
    const skipLink = document.querySelector(".skip-link");

    if (!skipLink) return;

    skipLink.addEventListener("click", function (e) {
      const target = document.querySelector("#main-content");
      if (target) {
        e.preventDefault();
        target.focus();
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  }

  // Add scroll behavior to header
  function initStickyHeader() {
    const header = document.querySelector("header");
    let lastScroll = 0;

    if (!header) return;

    window.addEventListener("scroll", function () {
      const currentScroll = window.pageYOffset;

      // Add shadow when scrolled
      if (currentScroll > 0) {
        header.style.boxShadow = "0 2px 8px rgba(0, 0, 0, 0.15)";
      } else {
        header.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.1)";
      }

      lastScroll = currentScroll;
    });
  }

  // Handle window resize
  function initResizeHandler() {
    let resizeTimer;

    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () {
        const navContainer = document.querySelector(".nav-container");
        const mobileToggle = document.getElementById("mobile-menu-toggle");

        // Reset mobile menu on desktop
        if (window.innerWidth > 768 && navContainer) {
          navContainer.classList.remove("mobile-open");
          document.body.classList.remove("mobile-menu-open");
          if (mobileToggle) {
            mobileToggle.setAttribute("aria-expanded", "false");
            mobileToggle.textContent = "☰";
          }
        }
      }, 250);
    });
  }

  // Initialize all functionality when DOM is ready
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

  // Run initialization
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
