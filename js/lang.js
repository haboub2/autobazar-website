// Language toggle for Auto Bazar Syria
// Shared across all pages

function initLang() {
  const saved = localStorage.getItem('lang') || 'en';
  setLang(saved);
}

function setLang(lang) {
  localStorage.setItem('lang', lang);
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';

  document.querySelectorAll('.lang-en').forEach(el => {
    el.style.display = lang === 'en' ? '' : 'none';
  });
  document.querySelectorAll('.lang-ar').forEach(el => {
    el.style.display = lang === 'ar' ? '' : 'none';
  });

  // Update toggle button text - Handled by CSS to prevent duplication
  // document.querySelectorAll('.lang-toggle').forEach(btn => {
  //   btn.textContent = lang === 'en' ? 'عربي' : 'EN';
  // });


  // Update font
  document.body.style.fontFamily = lang === 'ar'
    ? "'Noto Sans Arabic', 'Inter', sans-serif"
    : "'Inter', sans-serif";

  document.title = lang === 'ar'
    ? 'أوتو بازار | سيارات للبيع في سوريا - سوق السيارات الأول'
    : 'Auto Bazar | Cars for Sale in Syria - #1 Car Marketplace';
}

function toggleLang() {
  const current = localStorage.getItem('lang') || 'en';
  setLang(current === 'en' ? 'ar' : 'en');
}

document.addEventListener('DOMContentLoaded', initLang);
