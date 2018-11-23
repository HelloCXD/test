

$(function(){

    // 用户名
    $('#exampleInputEmail1').blur(function () {
        // var re_tel = /^1[3|5|7|8]\d{9}$/;
        // console.log(re_tel)
        // flag = re_tel.test($('#pel1').val())
        var username = $(this).val()
        if(username == ""){
            // console.log(1)
            $("#name-err1").show();
            $("#name-err2").hide();
            $("#name-err3").hide();
        }
        // else if(re_tel.test($(this).val())){
        //     // console.log(2)
        //     $.get('/checkin/', {'pel':$(this).val()}, function (response) {
        //         console.log(response)
        //         if (response.status == -1){ // 不可用
        //             $("#tel-err1").hide();
        //             $("#tel-err2").hide();
        //             $("#tel-err3").show();
        //         }
        //         else {
        //             // a=1
        //             $("#tel-err1").hide();
        //             $("#tel-err2").hide();
        //             $("#tel-err3").hide();
        //             $("#btn1").replaceWith("<input id='btn1' type='submit' value='立即注册' class='enter'/>")
        //
        //         }
        //
        //
        //     })
        // }

        else {
            if (username.length < 6 || username.length > 16){
                // console.log(3)
                $("#name-err1").hide();
                $("#name-err2").show();
                $("#name-err3").hide();
            }
            else {
                $.get('/checkin/', {'username': username}, function (response) {
                    console.log(response)
                    if (response.status == -1) { // 不可用
                        $("#name-err1").hide();
                        $("#name-err2").hide();
                        $("#name-err3").show();
                    }
                    else {   // 可用
                        // a=1
                        $("#name-err1").hide();
                        $("#name-err2").hide();
                        $("#name-err3").hide();
                        $("#btn1").replaceWith("<input id='btn1' type='submit' value='立即注册' class='enter'/>")

                    }


                })
            }

        }
    })

    //注册---密码匹配  :6～12位即可
    $('#password').blur(function () {
        var password = $('#password').val()

        // console.log(password)

        if (password.length >= 6) {
            $('#password-err').hide()
            $("#btn1").replaceWith("<input id='btn1' type='submit' value='立即注册' class='enter'/>")
        } else {
            // b = 1
            $('#password-err').show()
            $("#btn1").replaceWith("<input id='btn1' type='button' value='立即注册' class='enter'/>")
        }
    })

    //注册---两个密码匹配是否相等
    $('#password1').blur(function () {
        if( $('#password').val()==$('#password1').val()){
            // c = 1
            $('#password1-err').hide()
            $("#btn1").replaceWith("<input id='btn1' type='submit' value='立即注册' class='enter'/>")
            // $("#btn1").replaceWith("<div class='btn btn-primary'>注册</div>")
        }else {
            $('#password1-err').show()
            $("#btn1").replaceWith("<input id='btn1' type='button' value='立即注册' class='enter'/>")
        }

    })

    // 邮箱验证
    $('#mail').blur(function () {
        var mail = $('#mail').val()

        // console.log(password)

        if (mail.length == 3) {
            $('#mail-err').hide()
            $("#btn1").replaceWith("<input id='btn1' type='submit' value='立即注册' class='enter'/>")
        } else {
            // b = 1
            $('#mail-err').show()
            $("#btn1").replaceWith("<input id='btn1' type='button' value='立即注册' class='enter'/>")
        }
    })

	
})