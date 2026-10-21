// Keep the original banner image maps aligned with responsive image variants.
document.querySelectorAll('.matharena-post img[usemap]').forEach((image) => {
  const map = document.getElementsByName(image.useMap.slice(1))[0];
  if (!map) return;
  const areas = Array.from(map.querySelectorAll('area'), (area) => ({
    area,
    coordinates: area.coords.split(',').map(Number),
  }));
  const resize = () => {
    const originalWidth = Number(image.getAttribute('width')) || image.naturalWidth;
    const originalHeight = Number(image.getAttribute('height')) || image.naturalHeight;
    if (!originalWidth || !originalHeight) return;
    const scaleX = image.clientWidth / originalWidth;
    const scaleY = image.clientHeight / originalHeight;
    areas.forEach(({ area, coordinates }) => {
      area.coords = coordinates.map((value, index) =>
        Math.round(value * (index % 2 ? scaleY : scaleX))).join(',');
    });
  };
  image.addEventListener('load', resize);
  new ResizeObserver(resize).observe(image);
  resize();
});
