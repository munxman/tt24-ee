(() => {
  const form = document.querySelector('[data-enquiry-form]');
  if (!form) return;

  const status = form.querySelector('[data-form-status]');

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    if (!form.reportValidity()) return;

    const data = new FormData(form);
    const lines = [
      'Tere',
      '',
      'Soovin arutada ettevõttele sobivat enesekaitse- ja de-eskalatsioonikoolitust.',
      '',
      `Organisatsioon: ${data.get('organization') || ''}`,
      `Kontaktisik: ${data.get('contact') || ''}`,
      `E-post: ${data.get('email') || ''}`,
      `Telefon: ${data.get('phone') || 'ei lisatud'}`,
      `Ligikaudne osalejate arv: ${data.get('participants') || 'täpsustamisel'}`,
      `Eelistatud ajastus: ${data.get('timing') || 'avatud'}`,
      '',
      'Olukorrad ja vajadus:',
      data.get('situations') || '',
      '',
      'Parimate soovidega',
      data.get('contact') || ''
    ];

    const subject = `Ettevõttekoolituse päring: ${data.get('organization') || 'organisatsioon'}`;
    const href = `mailto:info@krav-maga.ee?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;

    status.textContent = 'Avame sinu e-posti rakenduse koos ettevalmistatud kirjaga.';
    window.location.href = href;
  });
})();
