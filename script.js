window.onload = function() {


  let value =  fetch("${backend_api_gateway}/count",{

   method : "GET",
   mode : "cors",
  

   }).then(response=>response.json())
   .then(data=>{ document.getElementById("replace").innerHTML = ", and this resume has been accessed "+data+" times"; console.log(data); })


   

  };