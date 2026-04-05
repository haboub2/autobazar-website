/**
 * Auto Bazar Syria — Shared Theme & Lang JS
 */

// ========================
// THEME (Light / Dark)
// ========================
(function () {
  const PREF_KEY = 'ab-theme';
  const saved = localStorage.getItem(PREF_KEY);
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', theme);
})();

function getTheme() {
  return document.documentElement.getAttribute('data-theme') || 'light';
}

function setTheme(theme) {
  document.documentElement.classList.add('theme-transition');
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('ab-theme', theme);
  updateThemeIcon();
  setTimeout(() => document.documentElement.classList.remove('theme-transition'), 400);
}

function toggleTheme() {
  setTheme(getTheme() === 'dark' ? 'light' : 'dark');
}

function updateThemeIcon() {
  const btn = document.getElementById('theme-toggle-btn');
  if (!btn) return;
  btn.innerHTML = getTheme() === 'dark'
    ? `<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><path stroke-linecap="round" d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>`
    : `<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>`;
  btn.title = getTheme() === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
}

document.addEventListener('DOMContentLoaded', updateThemeIcon);

// ========================
// MOBILE MENU
// ========================
function toggleMenu() {
  const ham = document.querySelector('.hamburger');
  const menu = document.querySelector('.mobile-menu');
  if (ham) ham.classList.toggle('active');
  if (menu) menu.classList.toggle('open');
}

// ========================
// ACCORDION (Support FAQ)
// ========================
function toggleAccordion(btn) {
  const item = btn.closest('.accordion-item');
  const content = item.querySelector('.accordion-content');
  const icon = btn.querySelector('.accordion-icon');
  const isOpen = content.classList.contains('open');

  // Close all open items first
  document.querySelectorAll('.accordion-content.open').forEach(function (c) {
    c.classList.remove('open');
    var parentIcon = c.closest('.accordion-item').querySelector('.accordion-icon');
    if (parentIcon) parentIcon.classList.remove('rotated');
  });

  if (!isOpen) {
    content.classList.add('open');
    if (icon) icon.classList.add('rotated');
  }
}

// ========================
// FADE-IN OBSERVER
// ========================
document.addEventListener('DOMContentLoaded', function () {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
    });
  }, { threshold: 0.08 });

  document.querySelectorAll('.fade-in').forEach(el => io.observe(el));

  // Immediately show in-viewport items
  requestAnimationFrame(() => {
    document.querySelectorAll('.fade-in').forEach(el => {
      if (el.getBoundingClientRect().top < window.innerHeight + 60)
        el.classList.add('visible');
    });
  });
});
