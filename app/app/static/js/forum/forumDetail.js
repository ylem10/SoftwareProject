$(function () {
    pageTurn();
    jumpToPages();
    addCommentClick();
    gotoTop();
    gotoBottom();
});

//页面跳转
function pageTurn() {
    $('.page_num span').click(function () {
        $(this).parent().find('span').attr('class', "");
        $(this).attr('class', 'tp');
        var page_num = $(this).text();
        pageTurnByAjax(page_num);
    });

    $('.last_page').click(function () {
        $(this).parent().find('span').attr('class', "");
        $(this).prev().attr('class', 'tp')
        var page_num = $(this).prev().text();
        pageTurnByAjax(page_num);
    });
}


//页面跳转的ajax
function pageTurnByAjax(page_num) {
    var data = {
        data: JSON.stringify({
            'page_num': page_num,
            'post_id': $('.post_id').text()
        })
    };
    $.ajax({
        url: '/forum/commentPage',
        type: 'POST',
        data: data,
        dataType: 'json',
        success: function (res) {
            console.log(res);
            $('.comments').empty();
            for (var i = 0; i < res.length; i++) {
                $('.comments').append('<div class="comment">\n' +
                    '                    <div class="left">\n' +
                    '                        <div class="left_img"><img src=../../../static/images/' + res[i]['com_pic'] + '></div>\n' +
                    '                        <div class="name">' + res[i]['comt_commenter'] + '</div>\n' +
                    '                    </div>\n' +
                    '                    <div class="right">\n' +
                    '                        <div class="content_show"><a style="padding: 10px">' + res[i]['comt_content'] + '</a></div>\n' +
                    '                        <div class="time_show"> ' + res[i]['comt_time'] + '</div>\n' +
                    '                    </div>\n' +
                    '                </div>')
            }
        }
    });
}

//跳到第几页
function jumpToPages() {
    $('.jump_btn').click(function () {
        var totalPage = $('.totalPage').text();
        var page = $('.jumpPage').val();
        if (page == "") {
            alert('您还未输入！');
        } else if (page > totalPage) {
            alert('没有该页');
        } else {
            pageTurnByAjax(page);
        }

    })

}


//添加评论
function addComment() {
    var post_id = $('.post_id').text();
    var comm_name = $('.username').text();
    var comm_content = $('.body_txt').val();
    var data = {
        data: JSON.stringify({
            'comm_name': comm_name,
            'post_id': post_id,
            'comm_content': comm_content
        })
    };
    $.ajax({
        url: '/forum/addComment',
        type: 'POST',
        data: data,
        dataType: 'json',
        success: function (res) {
            res = eval(res);
            console.log(res.ok);
            if (res.ok == true) {
                window.location.reload();
                alert('添加成功！');

            } else {
                alert('添加失败！');
            }
        }
    });
}

function addCommentClick() {
    $('.upload').click(function () {
        if (isLogin()) {
            addComment();
        }
    })
}

//回到顶部
function gotoTop() {
    $('.return_top').click(function () {
        $('html,body').animate({scrollTop: 0}, 'slow');
    });
}


//点击回复
function gotoBottom() {
    $('#core_btn_reply').click(function () {
        $("html,body").animate({
            scrollTop: document.body.clientHeight
        }, 'slow');
    })

}

//判断是否登录
function isLogin() {
    if ($('.username').text() == "") {
        alert('您还未登录！');
        return false;
    }

    return true;
}