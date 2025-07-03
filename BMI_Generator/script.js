const data=document.querySelector("form")
console.log(data);

data.addEventListener('submit',function(e){
    e.preventDefault();

    const height=document.querySelector('#height').value;
    const weight=document.querySelector('#weight').value;
    const results=document.querySelector('#results');
    
    if(height=='' || weight==''){
        results.innerHTML="Please Enter height and weight first";
    }
    else{
        const BMI=(weight/(height*height/10000)).toFixed(2);
        results.innerHTML=`<span>BMI = ${BMI}</span>`
    }

})