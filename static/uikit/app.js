// // Invoke Functions Call on Document Loaded
 document.addEventListener('DOMContentLoaded', function () {
   hljs.highlightAll();
 });

//  let alertWrapper = document.querySelector('.alert')
//  let alertClose = document.querySelectorAll('.alert__close')


//  if (alertWrapper){
//    alertClose.addEventListener('click', () =>
//     alertWrapper.style.display = 'none'
//    )
//  }

 document.querySelectorAll('.alert__close').forEach(element => {
   element.addEventListener('click', () => {
     document.querySelectorAll('.alert').forEach(alert => {
       alert.style.display = 'none';
     });
   });
 });