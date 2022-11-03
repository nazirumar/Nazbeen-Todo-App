// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict';
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms).forEach((form) => {
      form.addEventListener('submit', (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  })();

function TodoTyped() {
  var typed = new Typed('#typed', {
    strings: ['Welcome  to <strong>Nazbeen</strong> Todo App', ' ', 'Add Your Todo List to make your life easie'],
    typeSpeed: 70,
    backSpeed: 0,
    fadeOut: true,
    loop: true
  });
5
}

const btnNew = document.getElementById('btn-new')
btnNew.onmouseover = () =>
{
  TodoTyped()
};
