window.onload = function() {


  let value =  fetch("${backend_api_gateway}/count",{

    method : "GET",
    mode : "cors",
  }).then(response=>response.json())
  .then(data=>{ document.getElementById('visitorCount').textContent = data; console.log(data); console.log(data);})


   

  };
