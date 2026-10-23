(() => {
  document.documentElement.classList.add('js');
  const button = document.querySelector('.menu-toggle');
  const links = document.querySelector('.nav-links');
  if (!button || !links) return;

  const closeMenu = () => {
    button.setAttribute('aria-expanded', 'false');
    links.classList.remove('is-open');
  };
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    links.classList.toggle('is-open', open);
  });
  links.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') closeMenu();
  });
})();
