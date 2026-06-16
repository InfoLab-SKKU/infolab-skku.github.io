// Software & Datasets page — category filter
{
  const init = () => {
    const btns = document.querySelectorAll('.sw-filter-btn');
    const cards = document.querySelectorAll('.sw-repo-card');
    if (!btns.length || !cards.length) return;

    btns.forEach((btn) => {
      btn.addEventListener('click', () => {
        btns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        const cat = btn.dataset.cat;
        cards.forEach((card) => {
          card.style.display = (cat === 'all' || card.dataset.cat === cat) ? '' : 'none';
        });
      });
    });
  };

  window.addEventListener('load', init);
}
