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

  const heroMedia = document.querySelector('.hero-media');
  const heroVideo = document.querySelector('.hero-video');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const desktopVideo = window.matchMedia('(min-width: 641px)');

  const updateHeroVideo = () => {
    if (!heroMedia || !heroVideo) return;

    if (reducedMotion.matches || !desktopVideo.matches) {
      heroMedia.classList.remove('video-playing');
      heroVideo.pause();
      return;
    }

    if (!heroVideo.src) {
      heroVideo.src = heroVideo.dataset.src;
      heroVideo.load();
    }

    const playAttempt = heroVideo.play();
    if (playAttempt) {
      playAttempt.then(() => heroMedia.classList.add('video-playing')).catch(() => {
        heroMedia.classList.remove('video-playing');
      });
    }
  };

  heroVideo?.addEventListener('error', () => heroMedia?.classList.remove('video-playing'));
  reducedMotion.addEventListener('change', updateHeroVideo);
  desktopVideo.addEventListener('change', updateHeroVideo);
  updateHeroVideo();

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

  const instructorDialog = document.getElementById('instructor-dialog');
  const instructorContent = instructorDialog?.querySelector('[data-instructor-content]');
  const dialogClose = instructorDialog?.querySelector('[data-dialog-close]');

  document.querySelectorAll('[data-instructor]').forEach((button) => {
    button.addEventListener('click', () => {
      const template = document.getElementById(`instructor-${button.dataset.instructor}`);
      if (!instructorDialog || !instructorContent || !template) return;

      instructorContent.replaceChildren(template.content.cloneNode(true));
      document.body.classList.add('dialog-open');

      if (typeof instructorDialog.showModal === 'function') {
        instructorDialog.showModal();
      } else {
        instructorDialog.setAttribute('open', '');
      }
    });
  });

  const closeInstructorDialog = () => {
    if (!instructorDialog) return;
    if (typeof instructorDialog.close === 'function') instructorDialog.close();
    else instructorDialog.removeAttribute('open');
    document.body.classList.remove('dialog-open');
  };

  dialogClose?.addEventListener('click', closeInstructorDialog);
  instructorDialog?.addEventListener('click', (event) => {
    if (event.target === instructorDialog) closeInstructorDialog();
  });
  instructorDialog?.addEventListener('close', () => document.body.classList.remove('dialog-open'));
})();
