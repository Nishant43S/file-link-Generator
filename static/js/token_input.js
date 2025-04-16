// Initialize Swiper slider
const slider = document.getElementById('slider');
const totalImages = slider.children.length;
let currentIndex = 0;

function updateSlider() {
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalImages;
    updateSlider();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + totalImages) % totalImages;
    updateSlider();
}

// Animate from image 1 to 2 automatically only once
setTimeout(() => {
    currentIndex = 1;
    updateSlider();
}, 2000); // 2 seconds after load