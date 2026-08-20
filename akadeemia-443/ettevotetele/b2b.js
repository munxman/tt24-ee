(() => {
  const form = document.querySelector('[data-enquiry-form]');
  if (!form) return;

  const status = form.querySelector('[data-form-status]');
  const email = form.elements.email;
  const phone = form.elements.phone;
  const replyMethods = form.querySelectorAll('input[name="replyMethod"]');
  const panels = form.querySelectorAll('[data-contact-panel]');

  const syncReplyMethod = () => {
    const method = form.elements.replyMethod.value;
    panels.forEach((panel) => {
      const active = panel.dataset.contactPanel === method;
      panel.hidden = !active;
      panel.querySelector('input').required = active;
    });
  };

  replyMethods.forEach((radio) => radio.addEventListener('change', syncReplyMethod));
  syncReplyMethod();

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    if (!form.reportValidity()) return;

    const data = new FormData(form);
    const topics = data.getAll('topics');
    const replyMethod = data.get('replyMethod') === 'phone' ? 'telefoni teel' : 'e-posti teel';
    const lines = [
      'Tere',
      '',
      'Soovin arutada ettevõttele sobivat enesekaitse- ja de-eskalatsioonikoolitust.',
      '',
      `Organisatsioon: ${data.get('organization') || ''}`,
      `Kontaktisik: ${data.get('contact') || ''}`,
      `E-post: ${data.get('email') || ''}`,
      `Telefon: ${data.get('phone') || 'ei lisatud'}`,
      `Soovitud vastamisviis: ${replyMethod}`,
      `Ligikaudne osalejate arv: ${data.get('participants') || 'täpsustamisel'}`,
      `Eelistatud ajastus: ${data.get('timing') || 'avatud'}`,
      '',
      'Olukorrad ja vajadus:',
      topics.length ? topics.map((topic) => `- ${topic}`).join('\n') : '- täpsustamisel',
      data.get('details') ? `\nLisainfo:\n${data.get('details')}` : '',
      '',
      'Parimate soovidega',
      data.get('contact') || ''
    ];

    const subject = `Ettevõttekoolituse päring: ${data.get('organization') || 'organisatsioon'}`;
    const href = `mailto:info@krav-maga.ee?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;

    status.textContent = 'Avame teie e-posti rakenduse koos ettevalmistatud kirjaga.';
    window.location.href = href;
  });
})();
