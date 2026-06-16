{
    const onLoad = () => {
      const carousel = document.querySelector('.carousel');
      if (!carousel) return;
      
      const wrapper = document.querySelector('.carousel-wrapper');
      const items = carousel.querySelectorAll('.carousel-item');
      const prevButton = document.querySelector('.carousel-control.prev');
      const nextButton = document.querySelector('.carousel-control.next');
      const indicators = document.querySelectorAll('.carousel-indicator');
      
      // Calculate total width and item dimensions
      const itemWidth = items[0].offsetWidth;
      const itemMargin = parseInt(window.getComputedStyle(items[0]).marginLeft) + 
                         parseInt(window.getComputedStyle(items[0]).marginRight);
      const itemTotalWidth = itemWidth + itemMargin;
      
      // Calculate how many items can be visible at once
      const wrapperWidth = wrapper.offsetWidth;
      const visibleItems = Math.floor(wrapperWidth / itemTotalWidth);
      
      // Initialize current position and total count
      let currentIndex = 0;
      const maxIndex = Math.max(0, items.length - visibleItems);
      let autoplayInterval;
      
      // Set first indicator as active
      if (indicators.length > 0) {
        indicators[0].classList.add('active');
      }
      
      // Function to update carousel position
      function updateCarousel(index) {
        // When reaching beyond the last item, loop back to the beginning
        if (index > maxIndex) index = 0;
        // When going before first item, loop to the end
        if (index < 0) index = maxIndex;
        
        currentIndex = index;
        const translateX = -currentIndex * itemTotalWidth;
        carousel.style.transform = `translateX(${translateX}px)`;
        
        // Update active indicator
        indicators.forEach((indicator, i) => {
          if (i === currentIndex) {
            indicator.classList.add('active');
          } else {
            indicator.classList.remove('active');
          }
        });
        
        // Since we now allow looping, buttons should always be active
        if (prevButton) {
          prevButton.style.opacity = "1";
        }
        if (nextButton) {
          nextButton.style.opacity = "1";
        }
      }
  
      // Click events for controls
      if (prevButton) {
        prevButton.addEventListener('click', () => {
          resetAutoplay();
          updateCarousel(currentIndex - 1);
        });
      }
  
      if (nextButton) {
        nextButton.addEventListener('click', () => {
          resetAutoplay();
          updateCarousel(currentIndex + 1);
        });
      }
      
      // Initialize
      updateCarousel(0);
      
      // Click events for controls
      if (prevButton) {
        prevButton.addEventListener('click', () => {
          if (currentIndex > 0) {
            resetAutoplay();
            updateCarousel(currentIndex - 1);
          }
        });
      }
      
      if (nextButton) {
        nextButton.addEventListener('click', () => {
          if (currentIndex < maxIndex) {
            resetAutoplay();
            updateCarousel(currentIndex + 1);
          }
        });
      }
      
      // Click events for indicators
      indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
          resetAutoplay();
          updateCarousel(index);
        });
      });
      
      // Touch support
      let touchStartX = 0;
      let touchEndX = 0;
      
      const handleTouchStart = (e) => {
        touchStartX = e.touches[0].clientX;
      };
      
      const handleTouchEnd = (e) => {
        touchEndX = e.changedTouches[0].clientX;
        handleSwipe();
      };
      
      const handleSwipe = () => {
        const swipeThreshold = 50;
        if (touchStartX - touchEndX > swipeThreshold && currentIndex < maxIndex) {
          // Swipe left
          resetAutoplay();
          updateCarousel(currentIndex + 1);
        } else if (touchEndX - touchStartX > swipeThreshold && currentIndex > 0) {
          // Swipe right
          resetAutoplay();
          updateCarousel(currentIndex - 1);
        }
      };
      
      carousel.addEventListener('touchstart', handleTouchStart);
      carousel.addEventListener('touchend', handleTouchEnd);
      
      // Autoplay
      const startAutoplay = () => {
        autoplayInterval = setInterval(() => {
          // Loop back to beginning if we reach the end
          const nextIndex = currentIndex < maxIndex ? currentIndex + 1 : 0;
          updateCarousel(nextIndex);
        }, 2000);
      };
      
      const resetAutoplay = () => {
        clearInterval(autoplayInterval);
        startAutoplay();
      };
      
      // Start autoplay when the page loads
      startAutoplay();
      
      // Handle window resize
      window.addEventListener('resize', debounce(() => {
        // Recalculate visible items
        const newWrapperWidth = wrapper.offsetWidth;
        const newVisibleItems = Math.floor(newWrapperWidth / itemTotalWidth);
        const newMaxIndex = Math.max(0, items.length - newVisibleItems);
        
        // Adjust current index if needed
        let newIndex = currentIndex;
        if (newIndex > newMaxIndex) newIndex = newMaxIndex;
        
        // Update carousel
        updateCarousel(newIndex);
      }, 250));
      
      // Utility function for debouncing
      function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
          const later = () => {
            clearTimeout(timeout);
            func(...args);
          };
          clearTimeout(timeout);
          timeout = setTimeout(later, wait);
        };
      }
      
      // Pause autoplay when hovering over the carousel
      wrapper.addEventListener('mouseenter', () => clearInterval(autoplayInterval));
      wrapper.addEventListener('mouseleave', startAutoplay);
    };
    
    // After page loads
    window.addEventListener('load', onLoad);
  }