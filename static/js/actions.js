function myFunction () {
  
  var select_value = document.getElementById("languages_id").value;
  //alert(event.target.id);
  console.log(select_value);   



    if (select_value!="Select Language")
        {
        $.ajax({
                type:"GET",
                url:"/languages/",
                data:{"lan":select_value},
                success:function(data)
                {
                    console.log("success");
                }
            });

        }
    else
    {
        alert("not updated");   
    }

 

}
