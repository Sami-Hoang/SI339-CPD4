// BUTTON TO SHOW MORE OR LESS PHOTOS IN GALLERY 
function showMorePhotos() {
    const gallery = document.querySelector('#gallery');
    const button = document.querySelector('.ShowMoreButton');
    
    // Toggle visibility of additional photos
    const hiddenPhotos = gallery.querySelectorAll('a:nth-child(n+9)');
    
    if (hiddenPhotos[0].style.display === 'none' || !hiddenPhotos[0].style.display) {
        hiddenPhotos.forEach(photo => {
            photo.style.display = 'block';
        });
        button.textContent = 'Show Less Photos'; // Update button text
    } else {
        hiddenPhotos.forEach(photo => {
            photo.style.display = 'none';
        });
        button.textContent = 'See More Photos'; // Revert button text
    }
}

// HIDE IMAGES IF NOT FOUND
document.querySelectorAll('img').forEach(img => {
    img.onerror = function() {
      this.onerror = null; // Prevents infinite loop if the default image is missing
      this.style.display = 'none'; // Hide the image if not found
    };
  });


// ADDITIONAL LIGHTBOX

  lightbox.option({
      'resizeDuration': 200,
      'wrapAround': true,
      'positionFromTop': 50
  });


// CUSTOMIZED GREETING MESSAGE
  let nm = prompt("What is your name?");
  if (nm) {
      document.querySelector('h1').innerHTML = "Hi " + nm + "! Welcome to the Ann Arbor Skyline Athletes Page!";
  }