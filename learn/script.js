const buttons=document.querySelectorAll(".color")
const body=document.querySelector("body")
buttons.forEach(function (button){
     button.addEventListener('mouseenter',function(e){
            body.style.backgroundColor=e.target.id;
     })
     button.addEventListener('mouseleave',function(e){
        body.style.backgroundColor='white';
     })
})

