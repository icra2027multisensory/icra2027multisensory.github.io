(() => {
  const button = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if (!button || !nav) return;
  const closeMenu = () => {
    button.setAttribute('aria-expanded', 'false');
    nav.classList.remove('nav-open');
  };
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('nav-open', open);
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
  document.addEventListener('click', event => { if (!nav.contains(event.target) && !button.contains(event.target)) closeMenu(); });
})();
