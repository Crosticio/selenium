const footer = document.querySelector('footer')
window.scrollTo({top: window.scrollY + footer.getBoundingClientRect().y - (window.screen.height/3)})