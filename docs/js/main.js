// Lidice's Cleaning Services - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    var mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    var mobileMenu = document.querySelector('.mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');

            var spans = mobileMenuBtn.querySelectorAll('span');
            if (mobileMenu.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
            } else {
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
            }
        });

        mobileMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
            });
        });
    }

    // Save language preference
    var langSwitch = document.querySelector('.lang-switch');
    if (langSwitch) {
        langSwitch.addEventListener('click', function() {
            var href = this.getAttribute('href');
            var lang = href.includes('/sv/') ? 'sv' : 'en';
            localStorage.setItem('lidice-lang', lang);
        });
    }

    var htmlLang = document.documentElement.lang;
    if (htmlLang === 'en' || htmlLang === 'sv') {
        localStorage.setItem('lidice-lang', htmlLang);
    }

    // Quote Form Handling
    var quoteForm = document.getElementById('quote-form');
    var successMessage = document.getElementById('form-success');
    var errorMessage = document.getElementById('form-error');

    if (quoteForm) {
        quoteForm.addEventListener('submit', function(e) {
            e.preventDefault();

            var submitBtn = quoteForm.querySelector('button[type="submit"]');
            var originalText = submitBtn.textContent;
            submitBtn.textContent = '...';
            submitBtn.disabled = true;

            if (successMessage) successMessage.style.display = 'none';
            if (errorMessage) errorMessage.style.display = 'none';

            var formData = new FormData(quoteForm);

            fetch(quoteForm.action, {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            })
            .then(function(response) {
                if (response.ok) {
                    quoteForm.reset();
                    if (successMessage) successMessage.style.display = 'block';
                    quoteForm.style.display = 'none';
                } else {
                    throw new Error('Form submission failed');
                }
            })
            .catch(function(error) {
                console.error('Error:', error);
                if (errorMessage) errorMessage.style.display = 'block';
            })
            .finally(function() {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            });
        });
    }

    // Header scroll effect
    var header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.08)';
            } else {
                header.style.boxShadow = '';
            }
        });
    }
});
