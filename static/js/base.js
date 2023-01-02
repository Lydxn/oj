// Highlight the active link in the navigation bar.
(function() {
    const url = location.href;
    const navigationButtons = document.getElementsByClassName('nav-bar__button');
    for (const button of navigationButtons) {
        if (button.href == url) {
            const buttonIcon = button.getElementsByClassName('nav-bar__icon')[0];
            button.classList.add('nav-bar__button--active');
            buttonIcon.classList.add('nav-bar__icon--active');
            break;
        }
    }
})();
