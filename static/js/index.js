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

let notecicle = document.getElementsByTagName ('note-cicle');

let reading = document.getElementById("id_is_reading").classList.add('notecicle');
let readigClass = document.querySelectorAll('.notecicle')
console.log(readigClass);

let todoCheck = document.querySelectorAll('todo-check');
console.log(todoCheck.value == true);

// console.log(reading.checked == false);
// if (reading.checked  == false) {
//   notecicle.style.backgroundColor='red'
// }
// else {

// }
