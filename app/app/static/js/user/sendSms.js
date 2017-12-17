 $(function () {
        sendSms();
        checkphone();
        checkSms();
        formSubmit();
    });

    function sendSms() {
        $('.sendSms').click(function () {
            if (checkPhoneByNormal($('.cellPhone')) == true) {
                var time = 60;
                sendSmsAjax();
                $('.sendSms').val(time + 's');
                $('.sendSms').attr("disabled", true);
                var count = setInterval(function () {
                    if (time > 0) {
                        time--;
                        $('.sendSms').val(time + 's');

                    } else {
                        clearInterval(count);
                        $('.sendSms').val("重新发送")
                        $('.sendSms').attr("disabled", false);
                    }
                }, 1000);

                $(this).parent().prev().find(".cellPhone").css({
                    "border-bottom": "1px solid #48aecb",
                    "background-color": " #fff"
                });
                $(this).parent().prev().find("a").text('');
            } else {
                $(this).parent().prev().find("a").text("还未输入手机号或者手机号输入不合法！");
                $(this).parent().prev().find(".cellPhone").css({
                    "border-bottom": "1px solid #f75234",
                    "background-color": "#fdf6f5",
                    "transition": 'border .8s'
                });
            }
        })
    }

    function sendSmsAjax() {
        var cellphone = $('.cellPhone').val();
        var data = {
            data: JSON.stringify({
                'cellphone': cellphone
            })
        };
        $.ajax({
            url: '/SendSms',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (res) {
                console.log(res);
                console.log(0)

            },
        })
    }

    //手机号blur事件
    function checkphone() {
        $('.cellPhone').blur(function () {
            checkPhoneByNormal($(this));
        });
    }

    //手机号验证
    function checkPhoneByNormal(root) {
        //alert(phoneRegex.test(phone));
        var phone = $('.cellPhone').val();
        var phoneRegex = /^1[34578]\d{9}$/;
        if (phoneRegex.test(phone)) {
            root.css({
                "border-bottom": "1px solid #48aecb",
                "background-color": " #fff"
            });
            root.next().text('');
            return true;
        } else {
            root.next().text('请输入正确的11位手机号！');
            root.css({
                "border-bottom": "1px solid #f75234",
                "background-color": "#fdf6f5",
                "transition": 'border .8s'
            });
            return false;
        }
    }



    //验证码非空检验
    function checkSMSByNormal(root) {
        //alert(phoneRegex.test(phone));
        var phone = $('.SmsCode').val();
        if (phone != "") {
            root.css({
                "border-bottom": "1px solid #48aecb",
                "background-color": " #fff"
            });
            root.next().next().text('');
            return true;
        } else {
            root.next().next().text('验证码不能为空！');
            root.css({
                "border-bottom": "1px solid #f75234",
                "background-color": "#fdf6f5",
                "transition": 'border .8s'
            });
            return false;
        }
    }

    //验证码blur事件
    function checkSms() {
        $('.SmsCode').blur(function () {
            checkSMSByNormal($(this));
        });
    }

     //表单提交事件--把验证码提交到服务器
    function formSubmit() {
        $('.submit').click(function () {
            if (checkPhoneByNormal($('.cellPhone')) && checkSMSByNormal($('.SmsCode'))) {
                var SmsCode = $('.SmsCode').val();
                var data = {
                    data: JSON.stringify({
                        'SmsCode': SmsCode
                    })
                };
                $.ajax({
                    url: '/user/checkSmsCode',
                    type: 'POST',
                    data: data,
                    dataType: 'json',
                    success: function (res) {
                        res = eval(res)
                        console.log(res.ok);
                        if (res.ok == false) {
                            alert("验证码输入错误！")
                        } else {
                            alert("成功");
                            window.location.replace("/user/modifyPwd?phone="+ $('.cellPhone').val());
                        }
                    }
                })

            }
            return false;
        })
    }