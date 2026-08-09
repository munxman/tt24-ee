/* SL Tervisekeskus — main.js  v1.0  DRAFT 2026-08-09
   Minimal JS: mobile nav, FAQ accordion, registration form intercept.
   No frameworks, no dependencies. */

(function () {
  'use strict';

  /* ── Mobile nav ─────────────────────────────────────── */
  var hamburger = document.getElementById('hamburger');
  var mobileNav = document.getElementById('mobile-nav');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', function () {
      var open = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', String(!open));
      mobileNav.classList.toggle('is-open', !open);
      document.body.style.overflow = open ? '' : 'hidden';
    });
    // Close on any link click inside
    mobileNav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileNav.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ── FAQ accordion ───────────────────────────────────── */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      if (!item) return;
      var wasOpen = item.classList.contains('is-open');
      // Close all
      document.querySelectorAll('.faq-item.is-open').forEach(function (el) {
        el.classList.remove('is-open');
        el.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
      });
      if (!wasOpen) {
        item.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ── Conditional fields (alaealise esindaja toggle) ─── */
  var esindajaToggle = document.getElementById('esindaja_toggle');
  var esindajaFields = document.getElementById('esindaja_fields');
  if (esindajaToggle && esindajaFields) {
    esindajaToggle.addEventListener('change', function () {
      esindajaFields.classList.toggle('is-shown', this.checked);
      esindajaFields.querySelectorAll('input').forEach(function (inp) {
        inp.required = esindajaToggle.checked;
      });
    });
  }

  /* ── Registration form intercept (preview mode) ──────── */
  var avForm = document.getElementById('avaldus-form');
  var avNotice = document.getElementById('avaldus-notice');

  if (avForm && avNotice) {
    avForm.addEventListener('submit', function (e) {
      e.preventDefault();

      var valid = true;

      // Required fields
      avForm.querySelectorAll('[required]').forEach(function (field) {
        var grp = field.closest('.form-group');
        var empty = field.type === 'checkbox' ? !field.checked : !field.value.trim();
        if (empty) {
          valid = false;
          if (grp) grp.classList.add('has-error');
        } else {
          if (grp) grp.classList.remove('has-error');
        }
      });

      // Isikukood: must be 11 digits
      var ikField = document.getElementById('isikukood');
      if (ikField && ikField.value) {
        var ik = ikField.value.replace(/\D/g, '');
        if (ik.length !== 11) {
          valid = false;
          var grp = ikField.closest('.form-group');
          if (grp) grp.classList.add('has-error');
        }
      }

      if (!valid) {
        var firstErr = avForm.querySelector('.has-error');
        if (firstErr) firstErr.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }

      // Preview success
      avForm.style.display = 'none';
      avNotice.style.display = 'block';
      avNotice.scrollIntoView({ behavior: 'smooth', block: 'center' });

      // GA4 event (fires only if gtag is loaded)
      if (typeof gtag === 'function') {
        gtag('event', 'avaldus_submit', { event_category: 'registration', event_label: 'preview_mode' });
      }
    });

    // Clear error on input
    avForm.querySelectorAll('.form-control').forEach(function (f) {
      f.addEventListener('input', function () {
        var grp = f.closest('.form-group');
        if (grp) grp.classList.remove('has-error');
      });
    });
  }

  /* ── GA4 event tracking helpers ─────────────────────── */
  function trackClick(selector, eventName, label) {
    document.querySelectorAll(selector).forEach(function (el) {
      el.addEventListener('click', function () {
        if (typeof gtag === 'function') {
          gtag('event', eventName, { event_category: 'engagement', event_label: label });
        }
      });
    });
  }
  trackClick('a[href*="eperearstikeskus"]', 'epak_click', 'e-perearstikeskus');
  trackClick('a[href^="tel:"]', 'phone_click', 'phone');
  trackClick('a[href*="valvekliinik"]', 'valvekliinik_click', 'after_hours');

})();
