// Language toggle for Auto Bazar Syria
// Shared across all pages.
// Visibility of .lang-en / .lang-ar is handled purely in CSS via the
// <html lang> attribute, which an inline head script sets before first
// paint — so there is no layout shift and nothing to hide per-element here.

function setLang(lang) {
  localStorage.setItem('lang', lang);
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';

  // Localized title (homepage only — other pages keep their own titles)
  if (location.pathname === '/' || location.pathname === '/index.html') {
    document.title = lang === 'ar'
      ? 'سيارات وعقارات وتأجير سيارات في سوريا | أوتو بازار - Auto Bazar'
      : 'Cars, Real Estate & Car Rentals in Syria | Auto Bazar';
  }
}

function toggleLang() {
  const current = localStorage.getItem('lang') || 'ar';
  setLang(current === 'en' ? 'ar' : 'en');
}

// Apply saved language on load (lang/dir were already set pre-paint by the
// inline head script; this syncs storage and the localized title).
setLang(document.documentElement.lang === 'en' ? 'en' : 'ar');
