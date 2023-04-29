/* Initialize difficulty progress bar. */
(function() {
    const progressBars = document.getElementsByClassName('diff-bar');
    for (const bar of progressBars) {
        const percentage = bar.getAttribute('difficulty') * 10;
        bar.style['width'] = `${percentage}%`;
        bar.style['background-color'] = `color-mix(in srgb, #ff5050 ${percentage}%, #50ff50)`;
    }
})();
