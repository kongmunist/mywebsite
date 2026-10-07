// Keep video URLs out of the browser's fetch queue until they approach the viewport.
(() => {
  const videos = document.querySelectorAll('video.deferred-video');
  const load = (video) => {
    const sources = [video, ...video.querySelectorAll('source[data-src]')];
    sources.forEach((source) => {
      if (source.dataset.src) {
        source.src = source.dataset.src;
        delete source.dataset.src;
      }
    });
    video.load();
    if (video.autoplay) {
      const playback = video.play();
      if (playback) playback.catch(() => {});
    }
  };
  if (!('IntersectionObserver' in window)) {
    videos.forEach(load);
    return;
  }
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(({ target, isIntersecting }) => {
      if (isIntersecting) {
        observer.unobserve(target);
        load(target);
      }
    });
  }, { rootMargin: '300px 0px' });
  videos.forEach((video) => observer.observe(video));
})();
