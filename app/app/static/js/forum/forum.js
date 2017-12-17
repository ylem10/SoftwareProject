$(function () {
    commentClick();
    returnComment();
    cancel_A_Comment();
    deleteForum();
    addFroum();
    goForumDetail();
    editForumDetail();
});

//评论Click事件
function commentClick() {
    $('.comment input').click(function () {
        if (isLogin()) {
            $(this).css({
                width: '100%'
            });
            $(this).next().remove();
            $(this).parent().append('<input class="comment_submit"  type="button" value="提交"/>');
            $(this).parent().css({
                'padding-bottom': '30px'
            });
            addComment();
        }
    })
}

//回复评论弹出
function returnComment() {
    $('.comment_list li .feedback').click(function () {
        if (!$(this).parent().find('div').html()) {
            $(this).parent().append('<div><textarea placeholder="回复内容"></textarea><input class="confirm" type="button" value="确定"><input class="cancel" type="button" value="取消"></div>');
            showComment();
            cancelComment();
        }
        //去掉取消评论
        if ($(this).parent().find('.cancelCom').html()) {
            $(this).parent().find('.cancelCom').remove();
        }
    })
}

//显示评论内容
function showComment() {
    $('.comment_list li .confirm').click(function () {
        //把输入框去掉
        var comment = $(this).prev().val();
        if (comment != "") {
            $(this).parent().parent().after('<li><span class="feedback"><a>XX</a>&nbsp;回复&nbsp;<a>YY</a>：' + comment + '</span></li>');

            // $(this).parent().parent().parent().append('<li><span class="feedback"><a>XX</a>&nbsp;回复&nbsp;<a>YY</a>：' + comment + '</span></li>');
            $(this).parent().remove();
        }
        returnComment();
        cancel_A_Comment();
    })
}

//取消编辑评论
function cancelComment() {
    $('.comment_list li .cancel').click(function () {
        $(this).parent().remove();
    })
}

//取消评论
function cancel_A_Comment() {
    $('.comment_list li').mouseover(function () {
        if (!$(this).find('.cancelCom').html() && !$(this).find('div').html()) {
            $(this).append('<span class="cancelCom">取消评论</span>');
            cancelByClick();
        }
    });

    $('.comment_list li').mouseleave(function () {
        if ($(this).find('.cancelCom').html()) {
            $(this).find('.cancelCom').remove();
            cancelByClick();
        }
    })


}

function cancelByClick() {
    $('.cancelCom').click(function () {
        var comm_id = $(this).parent().find('.comm_id').text();
        var data = {'comm_id': comm_id}
        $.ajax({
            url: '/forum/delcomment',
            type: 'GET',
            data: data,
            dataType: 'json',
            success: function (res) {
                res = eval(res)
                if (res.ok) {
                    alert('删除成功');
                } else {
                    alert('删除失败！');
                }
            },
            error: function () {

            }

        });
        $(this).parent().remove();
    })
}

//添加评论
function addComment() {
    $('.comment_submit').click(function () {
        var vals = $(this).prev().val();
        var poster_name = $(this).parent().prev().prev().find('.poster_name').text();
        var post_id = $(this).parent().parent().find('.post_id').text();
        var comm_name = $('.username').text();
        var comm_content = $(this).prev().val();
        if (vals !== "") {
            $(this).parent().next().find('ul').append('<li><span class="feedback"><a>' + comm_name + '</a>&nbsp;回复&nbsp;<a>' + poster_name + '</a>：' + vals + '</span></li>');
            returnComment();
            cancel_A_Comment();
            $(this).prev().val('');
            $(this).parent().css({
                'padding-bottom': '0px'
            });
            $(this).remove();
        }
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
                res = eval(res)
                console.log(res.ok);

            }
        });
    })
}


function deleteForum() {
    $('.deleteForum').click(function () {
        var post_id = $(this).parent().prev().text();
        alert(post_id);
    })
}

//添加随笔
function addFroum() {
    $('.addForum').click(function () {
        if (isLogin()) {
            //跳转到商品添加随笔里面
            window.location.replace("/forum/goAddPost");
        }
    })

}


//查看论坛的帖子详情
function goForumDetail() {
    $('.content_top').click(function () {
        var post_id = $(this).parent().prev().prev().text();
        window.location.replace("/forum/goForumDetail?post_id=" + post_id);
    })
}


function deleteForum() {
    $('.deleteForum').click(function () {
        var data = {
            data: JSON.stringify({
                'post_id': $(this).parent().prev().text()
            })
        };
        $.ajax({
            url: '/forum/delUserForum',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (res) {
                res = eval(res);
                console.log(res.ok);
                if (res.ok == true) {
                    alert("删除成功！");
                } else if (res.ok == false) {
                    alert("删除失败！");
                }
            }
        });
        window.location.reload();
    })
}

function editForumDetail() {
    $('.edit').click(function () {
        var post_id = $(this).parent().prev().text();
        // alert(post_id);
        window.location.replace("/forum/show_info?post_id=" + post_id);
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