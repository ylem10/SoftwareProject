$(function () {
    submitForm();
});


//提交表单
function submitForm() {
    //表单校验
    $('.input').click(function () {
                var data = {
                    data: JSON.stringify({
                        'user_Nick_name': $('.Nick_name').val(),
                        'user_Email': $('.Email').val()
                    })
                };
                $.ajax({
                    url: '/user/checkUserInfo',
                    type: 'POST',
                    data: data,
                    dataType: 'json',
                    success: function (res) {
                        res = eval(res);
                        console.log(res.ok);
                        if (res.ok == true) {
                            alert("修改成功！");
                            // window.location.replace("/");
                        }  else if (res.ok == false) {
                            alert("bug");
                        }
                    }
                });
            return false;
        }
    )
}



