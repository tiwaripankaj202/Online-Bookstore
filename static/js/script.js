document.addEventListener('DOMContentLoaded', function () {
    const root = document.documentElement;
    const themeToggle = document.querySelector('.theme-toggle');
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('#main-nav');

    function applyTheme(theme, persist) {
        root.dataset.theme = theme;
        if (themeToggle) {
            const nextTheme = theme === 'dark' ? 'light' : 'dark';
            themeToggle.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
            themeToggle.setAttribute('title', `Switch to ${nextTheme} theme`);
            themeToggle.setAttribute('aria-pressed', String(theme === 'light'));
            const icon = themeToggle.querySelector('[data-theme-icon]');
            if (icon) icon.textContent = theme === 'dark' ? '☼' : '☾';
        }
        if (persist) {
            try {
                localStorage.setItem('qq-theme', theme);
            } catch (error) {
                // Keep the selected theme for this page even if storage is unavailable.
            }
        }
    }

    applyTheme(root.dataset.theme === 'light' ? 'light' : 'dark', false);
    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
        });
    }

    function setMenuOpen(isOpen) {
        if (!menuToggle || !mainNav) return;
        mainNav.classList.toggle('is-open', isOpen);
        menuToggle.setAttribute('aria-expanded', String(isOpen));
        menuToggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
        const icon = menuToggle.querySelector('[aria-hidden="true"]');
        if (icon) icon.textContent = isOpen ? '×' : '☰';
    }

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function () {
            setMenuOpen(menuToggle.getAttribute('aria-expanded') !== 'true');
        });
        mainNav.addEventListener('click', function (event) {
            if (event.target.closest('a')) setMenuOpen(false);
        });
        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') {
                setMenuOpen(false);
                menuToggle.focus();
            }
        });
        window.addEventListener('resize', function () {
            if (window.matchMedia('(min-width: 761px)').matches) setMenuOpen(false);
        });
    }

    document.querySelectorAll('.flash').forEach(function (message) {
        const dismiss = function () {
            message.hidden = true;
        };
        const closeButton = message.querySelector('.flash-close');
        if (closeButton) closeButton.addEventListener('click', dismiss);
        setTimeout(dismiss, 3500);
    });

    document.querySelectorAll('.confirm-delete').forEach(function (button) {
        button.addEventListener('click', function (event) {
            const confirmed = window.confirm('Are you sure you want to delete this item?');
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    document.querySelectorAll('.validate-form').forEach(function (form) {
        form.addEventListener('submit', function (event) {
            const name = form.querySelector('input[name="name"]');
            const email = form.querySelector('input[name="email"]');
            const password = form.querySelector('input[name="password"]');

            if (name && name.value.trim().length < 2) {
                event.preventDefault();
                alert('Name must contain at least 2 characters.');
                return;
            }

            if (email && !email.value.includes('@')) {
                event.preventDefault();
                alert('Please enter a valid email address.');
                return;
            }

            if (password && password.value.length < 6) {
                event.preventDefault();
                alert('Password must contain at least 6 characters.');
            }
        });
    });
});
