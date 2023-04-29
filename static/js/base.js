/* Highlight the active link in the navigation bar. */
(function() {
    const url = location.href;
    const navigationLinks = document.getElementsByClassName('nav-link');
    for (const link of navigationLinks) {
        if (link.href == url) {
            link.classList.add('nav-link--active');
            break;
        }
    }
})();
