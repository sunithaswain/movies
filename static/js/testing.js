$(function() {
    $(".inputWrapper").mousedown(function() {
        var button = $(this);
        button.addClass('clicked');
        setTimeout(function(){
            button.removeClass('clicked');
        },50);
    });
});



        $(document).ready(function(){
 $('.fileInput').change(function(){
     var file_name = $(this).val();
     $(".prof-file").text(file_name);
     $('#place-holder p').css('display','none');
     $('.text-file textarea').css('display','none');
     $('.text-file').css('height','80px');
 });
});


$(document).ready(function(){
  $(".text p").click(function(){
    $(".upload-block").css("display","none");
    $(".upload-blockto").css("display","block");
  });
    $('.slideControl').slideControl();
    prettyPrint();
});


$(document).ready(function(){
    $(".text-file textarea").keyup(function(){
    var count=$(this).val().length;
     if (count >= 1){
    $("#place-holder").css("display","none");
    }else{
    $("#place-holder").css("display","block");
    }
});
});
