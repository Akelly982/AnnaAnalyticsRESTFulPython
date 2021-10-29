$("#inputSubmit").click(function(e){
    e.preventDefault();
    //alert("inputSubmit btn hit");
    
    // find output container
    var outputContainer = document.getElementById("outputContainer");
    
    //find inputs 
    var num1 = document.getElementById("num1")
    var num2 = document.getElementById("num2")
    
    //data validation
    if(num1.value.length == 0 || num2.value.length == 0){
        alert('One or more fields was left empty');
        return
    }
    
    //send data to outputXX
    $.ajax({
        url:"http://127.0.0.1:5000/itemOutput1C",
        method:"POST",
        data : { x : num1.value , y : num2.value},  
        crossDomain: true,
        success : function(result){  //my result becomes my JSON // ARRAY
            if(result.isSuccessfull){
                outputContainer.innerHTML = result.htmlString;
            }else{

            }
            
        },    
        error: function (jqXhr, textStatus, errorMessage) {
            console.log("Error 1A input");
        }    
    });  
});