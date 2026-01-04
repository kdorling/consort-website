// Mega Menu Animation Debug Script
// Copy and paste this into your browser console (F12) to test the animation

console.log("🔍 Mega Menu Animation Debugger\n");

// 1. Check if main nav exists
const mainNav = document.getElementById("main-nav");
console.log("1. Main Nav Element:", mainNav ? "✅ Found" : "❌ Not found");

// 2. Find dropdown parents
const dropdownParents = mainNav
  ? mainNav.querySelectorAll(".has-dropdown")
  : [];
console.log(
  "2. Dropdown Menu Items:",
  dropdownParents.length,
  dropdownParents.length > 0 ? "✅" : "❌",
);

// 3. Check first dropdown menu
const firstDropdown = mainNav ? mainNav.querySelector("nav ul ul") : null;
if (firstDropdown) {
  const styles = getComputedStyle(firstDropdown);
  console.log("\n3. Dropdown CSS Properties:");
  console.log("   - Visibility:", styles.visibility);
  console.log("   - Opacity:", styles.opacity);
  console.log("   - Transform:", styles.transform);
  console.log("   - Transition:", styles.transition);
  console.log("   - Position:", styles.position);

  // Check if using display:none (bad for animation)
  if (styles.display === "none") {
    console.log("   ⚠️  WARNING: Using display:none will prevent animation!");
  } else {
    console.log("   ✅ Not using display:none");
  }

  // Check if transform is set correctly for scaleY
  if (styles.transform.includes("0, 0, 0")) {
    console.log("   ✅ Transform includes scaleY(0) - collapsed state");
  } else {
    console.log("   ⚠️  Transform might not be set correctly");
    console.log(
      "   Expected: matrix with scaleY(0) = matrix(1, 0, 0, 0, 0, 0)",
    );
  }

  // Check transform-origin
  if (styles.transformOrigin) {
    console.log("   - Transform Origin:", styles.transformOrigin);
    if (
      styles.transformOrigin.includes("0") ||
      styles.transformOrigin.includes("top")
    ) {
      console.log("   ✅ Transform origin set to top");
    }
  }

  // Check if transition is set
  if (
    styles.transition &&
    styles.transition.includes("opacity") &&
    styles.transition.includes("transform")
  ) {
    console.log("   ✅ Transitions configured");
  } else {
    console.log("   ⚠️  Transitions might not be set correctly");
  }
} else {
  console.log("\n3. Dropdown Menu: ❌ Not found");
}

// 4. Test animation function
console.log("\n4. Animation Test:");
console.log("   Run this command to test: testAnimation()");

window.testAnimation = function () {
  const parent = mainNav.querySelector(".has-dropdown");
  if (!parent) {
    console.log("❌ No dropdown found to test");
    return;
  }

  console.log("🎬 Opening dropdown...");
  parent.classList.add("dropdown-open");

  setTimeout(() => {
    const dropdown = parent.querySelector("ul");
    const styles = getComputedStyle(dropdown);
    console.log("   After opening:");
    console.log("   - Visibility:", styles.visibility);
    console.log("   - Opacity:", styles.opacity);
    console.log("   - Transform:", styles.transform);

    console.log("\n⏸️  Closing in 2 seconds...");

    setTimeout(() => {
      parent.classList.remove("dropdown-open");
      console.log("✅ Animation test complete!");
      console.log(
        "Did you see the menu GROW/EXPAND down and then shrink back up?",
      );
    }, 2000);
  }, 500);
};

// 5. Check JavaScript listeners
console.log("\n5. JavaScript Event Listeners:");
if (dropdownParents.length > 0) {
  const hasClickListener = true; // Can't directly check, assume it's there
  console.log(
    "   Click handlers should be attached to",
    dropdownParents.length,
    "menu items",
  );
  console.log("   Try clicking a menu item to test");
} else {
  console.log("   ⚠️  No dropdown menus found");
}

// 6. Browser info
console.log("\n6. Browser Information:");
console.log("   - User Agent:", navigator.userAgent.substring(0, 50) + "...");
console.log("   - Window Width:", window.innerWidth, "px");
console.log("   - Device:", window.innerWidth > 768 ? "Desktop" : "Mobile");
if (window.innerWidth <= 768) {
  console.log("   ℹ️  Note: Animations are disabled on mobile (<768px)");
}

// 7. CSS file check
console.log("\n7. CSS File Status:");
const cssLinks = document.querySelectorAll('link[rel="stylesheet"]');
console.log("   Stylesheets loaded:", cssLinks.length);
cssLinks.forEach((link, index) => {
  console.log(`   ${index + 1}. ${link.href}`);
});

// 8. Summary
console.log("\n📊 Summary:");
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");

const checks = [
  { name: "Main Nav", pass: !!mainNav },
  { name: "Dropdown Menus", pass: dropdownParents.length > 0 },
  { name: "CSS Loaded", pass: !!firstDropdown },
  {
    name: "Transitions Set",
    pass: firstDropdown
      ? getComputedStyle(firstDropdown).transition.includes("opacity")
      : false,
  },
];

checks.forEach((check) => {
  console.log(check.pass ? "✅" : "❌", check.name);
});

const allPassed = checks.every((c) => c.pass);

if (allPassed) {
  console.log("\n🎉 Everything looks good!");
  console.log("\nNext steps:");
  console.log("1. Click a menu item (Monetary Policy, Markets, etc.)");
  console.log("2. Watch for smooth slide-down animation");
  console.log("3. Or run: testAnimation()");
} else {
  console.log("\n⚠️  Some checks failed!");
  console.log("\nTroubleshooting:");
  console.log("1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)");
  console.log("2. Clear cache and reload");
  console.log("3. Rebuild Hugo: cd test && hugo --gc");
  console.log("4. Check browser console for errors");
}

console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log("\n💡 Quick Test: Type testAnimation() and press Enter\n");
