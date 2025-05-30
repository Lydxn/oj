/* Copy the sample input/output to the clipboard. */
(function() {
    const icons = document.getElementsByClassName('sample-copy-icon');
    for (const icon of icons) {
        icon.addEventListener('click', () => {
            // Copy to clipboard
            navigator.clipboard.writeText(
                icon.closest('.sample-box')
                    .getElementsByClassName('sample-content')[0]
                    .textContent
            );

            const msg = icon.parentElement.getElementsByClassName('sample-copy-msg')[0];

            // Unhide "Copied!" text
            msg.style.opacity = 2;

            clearInterval(icon.copyInterval);
            icon.copyInterval = setInterval(() => {
                if (msg.style.opacity <= 0)
                    clearInterval(icon.copyInterval);
                msg.style.opacity -= 0.1;
            }, 50);
        });
    }
})();
