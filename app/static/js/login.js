
 $(function(){
     //账户名
	$('#exampleInputEmail1').on("blur",function(){

        //验证是否为空，电话和邮箱，或都不是
        var username = $(this).val();
        // var reg_user_email = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9_\.\-]+\.[a-zA-Z]+$/;
        if(username == ""){ //为空
            $("#name-err1").show();
            $("#name-err2").hide();

            // $(".code2").hide();
            // $(".phone_code").hide();
        }
        else{// 不为空
            if (username.length < 6 || username.length > 16){
                // console.log(3)
                $("#name-err1").hide();
                $("#name-err2").show();
            }
            else {
                $("#name-err1").hide();
                $("#name-err2").hide();
            }


        }
	})




//     var re_tel = /^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/
//     $('#pel1').blur(function () {
//         console.log(12)
//         flag = re_tel.test($('#pel1').val())
//         // var tel = $(this).val()
//         console.log(flag)
//         //通过
//         // var $li = $('<span id="tel-err">输入手机号码格式不对</span>').appendTo($mygoods)
//         if(flag){
//             $('#tel-err').hide()
//             $("#btn1").replaceWith("<input id='btn1' type='submit' value='立即登录' class='enter'/>")
//         }else{
//             $('#tel-err').show()
//             $("#btn1").replaceWith("<input id='btn1' type='button' value='立即登录' class='enter'/>")
//         }
//     })
//
//     //注册---密码匹配  :6～12位即可
//     $('#pwd1').blur(function () {
//         var password = $('#pwd1').val()
//
//         console.log(password)
//
//         if ((password.length >= 1 && password.length < 6) || password.length > 12) {
//             $('#password-err').show()
//             $("#btn1").replaceWith("<input id='btn1' type='button' value='立即登录' class='enter'/>")
//         } else {
//             $('#password-err').hide()
//             $("#btn1").replaceWith("<input id='btn1' type='submit' value='立即登录' class='enter'/>")
//         }
//     })
//
//
//
 })