(() => {
  const menuButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');

  if (menuButton && nav) {
    menuButton.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(open));
    });

    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        menuButton.setAttribute('aria-expanded', 'false');
      });
    });
  }

  document.querySelectorAll('.faq-question').forEach((button) => {
    button.addEventListener('click', () => {
      const answer = document.getElementById(button.getAttribute('aria-controls'));
      const expanded = button.getAttribute('aria-expanded') === 'true';

      document.querySelectorAll('.faq-question[aria-expanded="true"]').forEach((other) => {
        if (other === button) return;
        other.setAttribute('aria-expanded', 'false');
        const otherAnswer = document.getElementById(other.getAttribute('aria-controls'));
        if (otherAnswer) otherAnswer.style.maxHeight = '0px';
      });

      button.setAttribute('aria-expanded', String(!expanded));
      if (answer) answer.style.maxHeight = expanded ? '0px' : `${answer.scrollHeight}px`;
    });
  });
})();
