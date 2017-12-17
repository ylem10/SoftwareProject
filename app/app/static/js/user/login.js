$(function () {
    checkUsername();
    checkPwd();
    checkValidCode();
    submitForm();
    validClick();
});

//用户名校验
function checkUsernameByNormal(root) {
    var username = $('.username').val();
    if (isNaN(username)) {
        root.css({
            "border-bottom": "1px solid #48aecb",
            "background-color": " #fff"
        });
        root.next().text('');
        return true;
    } else if (username == '') {
        root.next().text('用户名不能为空！');
        root.css({
            "border-bottom": "1px solid #f75234",
            "background-color": "#fdf6f5",
            "transition": 'border .8s'
        });
        return false;
    } else {
        root.next().text('用户名不能为纯数字！');
        root.css({
            "border-bottom": "1px solid #f75234",
            "background-color": "#fdf6f5",
            "transition": 'border .8s'
        });
        return false;
    }
}

//为检验用户名提供blur事件
function checkUsername() {
    $('.username').blur(function () {
        checkUsernameByNormal($(this));
        userExist($(this))
    });
}

//密码校验
function checkPwdByNormal(root) {
    var pass = root.val();
    if (pass == "") {
        root.next().text('密码不能为空！');
        root.css({
            "border-bottom": "1px solid #f75234",
            "background-color": "#fdf6f5",
            "transition": 'border .8s'
        });
        return false;
    } else if (pass.length > 12) {
        root.next().text('密码长度不能大于12位！');
        root.css({
            "border-bottom": "1px solid #f75234",
            "background-color": "#fdf6f5",
            "transition": 'border .8s'
        });
        return false;
    } else if (pass.length < 6) {
        root.next().text('密码长度不能小于6位！！');
        root.css({
            "border-bottom": "1px solid #f75234",
            "background-color": "#fdf6f5",
            "transition": 'border .8s'
        });
        return false;
    } else {
        root.css({
            "border-bottom": "1px solid #48aecb",
            "background-color": " #fff"
        });
        root.next().text('');
        return true;
    }


}

//密码校验
function checkPwd() {
    $('.password').blur(function () {
        checkPwdByNormal($(this));
    });
}

//验证码校验
function checkValidCodeByNormal(root) {
    var validCode = root.val();
    if (validCode == "") {
        root.next().next().text('验证码不能为空！');
        root.css({
            "border-bottom": "1px solid #f75234",
            "background-color": "#fdf6f5",
            "transition": 'border .8s'
        });
        return false;
    } else {
        root.css({
            "border-bottom": "1px solid #48aecb",
            "background-color": " #fff"
        });
        root.next().next().text('');
        return true;
    }

}

function checkValidCode() {
    $('.validCode').blur(function () {
        checkValidCodeByNormal($(this))
    })
}

//提交表单
function submitForm() {
    //表单校验
    $('.submit').click(function () {
            var checkUserName = checkUsernameByNormal($('.username'));
            var checkPwd = checkPwdByNormal($('.password'));
            var checkValid = checkValidCodeByNormal($('.validCode'));
            var d = new Date()
            if (checkUserName && checkPwd && checkValid) {
                var data = {
                    data: JSON.stringify({
                        'username': $('.username').val(),
                        'password': $('.password').val(),
                        'validCode': $('.validCode').val()
                    })
                };
                $.ajax({
                    url: '/user/loginCheck',
                    type: 'POST',
                    data: data,
                    dataType: 'json',
                    success: function (res) {
                        res = eval(res)
                        console.log(res.ok);
                        if (res.ok == true) {
                            $.Myalert({
                                type: 'success', //消息类型
                                value: '登录成功！!', //消息内容
                                speed: '0.3', //滑动速度（以秒为单位）
                                confirm: function () {
                                    window.location.replace("/");
                                }
                            });

                        } else if (res.ok == "validError") {
                             $.Myalert({
                                type: 'wanning', //消息类型
                                value: '验证码输入错误！！!', //消息内容
                                speed: '0.3', //滑动速度（以秒为单位）
                                confirm: function () {
                                    window.location.replace("/");
                                }
                            });
                            $('.identifyCode').attr("src", '/VerifyCode?time=' + d.getTime())
                        } else if (res.ok == "pwdError") {
                            $.Myalert({
                                type: 'wanning', //消息类型
                                value: '密码输入错误！！!', //消息内容
                                speed: '0.3', //滑动速度（以秒为单位）
                                confirm: function () {
                                    window.location.replace("/");
                                }
                            });
                            $('.identifyCode').attr("src", '/VerifyCode?time=' + d.getTime())
                        }
                    }
                });

            }
            return false;
        }
    )

}


//点击更换验证码
function validClick() {
    $('.identifyCode').click(function () {
        var d = new Date()
        $(this).attr("src", '/VerifyCode?time=' + d.getTime());
    })
}


//判断该用户是否存在，给后台发送用户名
function userExist(root) {
    var data = {
        data: JSON.stringify({
            'username': $('.username').val()
        })
    };

    $.ajax({
        url: '/user/checkUsernameExist',
        type: 'POST',
        data: data,
        dataType: 'json',
        success: function (res) {
            res = eval(res)
            console.log(res.ok);
            if (res.ok == true) {
                root.css({
                    "border-bottom": "1px solid #48aecb",
                    "background-color": " #fff"
                });
                root.next().text('');
            } else {
                root.next().text('用户不存在！');
                root.css({
                    "border-bottom": "1px solid #f75234",
                    "background-color": "#fdf6f5",
                    "transition": 'border .8s'
                });
            }
        }
    })
}