$(function () {
    checkPwd();
    submitForm();
});

//密码长度检验
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

function checkPwd2(root) {
    var pass1 = $('.password1').val();
    var pass2 = $('.password2').val();
    if (pass1 != pass2) {
        root.next().text('两次输入的密码不一致！');
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

//密码blur事件
function checkPwd() {
    $('.password1').blur(function () {
        checkPwdByNormal($(this));
    });
    $('.password2').blur(function () {
        checkPwdByNormal($(this));
        //继续判断两个密码是否一样
        checkPwd2($(this));
    });
}


//表单提交

function submitForm() {
    //表单校验
    $('.submit').click(function () {
            var GET = $.urlGet(); //获取URL的Get参数
            var phone = GET['phone']; //取得id的值
            var checkpwd1 = checkPwdByNormal($('.password1'));
            var checkpwd2_1 = checkPwdByNormal($('.password2'));
            var checkpwd2_2 = checkPwd2($('.password2'));
            if (checkpwd1 && checkpwd2_1 && checkpwd2_2) {
                var data = {
                    data: JSON.stringify({
                        'new_password': $('.password1').val(),
                        'phone': phone
                    })
                };
                $.ajax({
                    url: '/user/modifyPwd2',
                    type: 'POST',
                    data: data,
                    dataType: 'json',
                    success: function (res) {
                        res = eval(res)
                        console.log(res.ok);
                        if (res.ok == false) {
                            alert("修改失败！")
                        } else {
                            alert("修改成功！");
                            window.location.replace("/user/login");
                        }
                    }
                });

            }
            return false;
        }
    )

}

(function ($) {
    $.extend({
        urlGet: function () {
            var aQuery = window.location.href.split("?");  //取得Get参数
            var aGET = new Array();
            if (aQuery.length > 1) {
                var aBuf = aQuery[1].split("&");
                for (var i = 0, iLoop = aBuf.length; i < iLoop; i++) {
                    var aTmp = aBuf[i].split("=");  //分离key与Value
                    aGET[aTmp[0]] = aTmp[1];
                }
            }
            return aGET;
        }
    })
})(jQuery);
