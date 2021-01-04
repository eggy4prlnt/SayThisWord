$(document).ready(function () {
    $("#process").submit(function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "/process/",
            headers:{
                "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
            },
            data: {
              'word': $('#word').val() // from form
            },
            success: function (res) {
            //   console.log();
              var audio = $("#player");
              $("#mp3_src").attr("src", res.data);
              audio[0].pause();
              audio[0].load();//suspends and restores all audio element

              audio[0].oncanplaythrough = audio[0].play();
            }
          });

        return false;
    })
})