$(function () {
    titleBlur();
    pagBlur();
    save_modify();
    submitForm1()
});

//标题blur事件
function titleBlur() {
    $('.title').blur(function () {
        checkTitleByNormal($(this), '标题不能为空！');
    })
}

//验证标题
function checkTitleByNormal(root, content) {
    var title = root.val();
    if (title == "") {
        root.next().text(content);
        root.css({
            "border-bottom": "1px solid #f75234",
            "background-color": "#fdf6f5",
            "transition": 'border .8s'
        });
        return false;
    } else {
        root.css({
            "border-bottom": "1px solid #e5e5e5",
            "background-color": " #fff"
        });
        root.next().text('');
        return true;
    }
}


//验证正文内容
function pagBlur() {
    $('.pag').blur(function () {
        checkTitleByNormal($(this), '内容不能为空！');
    })
}

//提交表单
function submitForm1() {
    //表单校验
    $('.upload').click(function () {
            var post = $(this).parent().prev().text();
            var data = {
                data: JSON.stringify({
                    'post_id': $(this).parent().prev().text(),
                    'post_title': $('.title').val(),
                    'post_content': $('.pag').val(),
                    'pic': $('.preview').find('img').attr("src"),
                    'bool': 'add'
                })
            };
            $.ajax({
                url: '/forum/commit_article',
                type: 'POST',
                data: data,
                dataType: 'json',
                success: function (res) {
                    res = eval(res);
                    console.log(res.ok);
                    if (res.ok == true) {
                        alert("添加成功！");
                        // window.location.replace("/");
                    } else if (res.ok == false) {
                        alert("添加失败！");
                    }
                }
            });
            window.location.replace("/forum/gotoForum");
            return false;
        }
    )
}

//保存修改
function save_modify() {
    var post_id = GetQueryString("post_id");
    $('.modify').click(function () {
        var data = {
            data: JSON.stringify({
                'post_id': post_id,
                'post_title': $('.title').val(),
                'post_content': $('.pag').val(),
                'pic': '',
                'bool': 'edit'
            })
        };
        $.ajax({
            url: '/forum/commit_article',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (res) {
                res = eval(res);
                console.log(res.ok);
                if (res.ok == true) {
                    alert("修改成功！");
                    // window.location.replace("/");
                } else if (res.ok == false) {
                    alert("修改失败！");
                }
            }
        });
        window.location.replace("/forum/gotoForum");
        return false;
    })
}

//获取URL参数
function GetQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null)
        return unescape(r[2]);
    return null;
}
