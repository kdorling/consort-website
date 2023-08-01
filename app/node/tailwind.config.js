/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../**/**/*.{html,js}", "../weather/templatetags/*.py",
    "./node_modules/tw-elements/src/js/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("tw-elements/dist/plugin.cjs"),
  ],
  darkMode: "class",
  theme: {
    fontFamily: {
      sans: ["Lexend", "sans-serif"],
      body: ["Lexend", "sans-serif"],
      mono: ["ui-monospace", "monospace"],
    },
  },
  corePlugins: {
    preflight: false,
  },
}

