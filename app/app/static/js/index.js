$(function () {
    LRClose();
    buttonClick();
    fileText();
    submitExcl();
});

//闭合
function LRClose() {
    $('.data_left').css({
        left: '0'
    })
    $('.data_right').css({
        right: '0'
    })
}

//打开
function LROpen() {
    $('.data_left').css({
        left: '-500px'
    })
    $('.data_right').css({
        right: '-500px'
    })
}

function buttonClick() {
    $('.center_button_left').click(function () {
        LROpen();
    });

    $('.center_button_right').click(function () {
        LROpen();
    })
}


//验证图片上传是否合法
function fileText() {
    $(".uploadCom").on("change", "input[type='file']", function () {
        $('.picValid').text("");
        var filePath = $(this).val();
        if (filePath.indexOf("xls") != -1) {
            $('.preview').find('a').remove();
            $('.preview').append('<a href="/downloadFile" style="left: 50px" class="urls">' + filePath + '</a>');
            $('.submit').css({
                display: 'block'
            });
            $('.result').css({
                display: 'none'
            });
        } else {
            alert("文件格式不支持");
        }
    })
}

function FileUpload() {
    var formData = new FormData();
    formData.append('file', $('#fileupload')[0].files[0]);
    $.ajax({
        url: '/upload',
        type: 'POST',
        cache: false,
        data: formData,
        processData: false,
        contentType: false
    }).done(function (res) {
        $('.preview').find('img').remove();
        $(".urls").before('<img style="display: none" class="url" src=' + res + '>');
        alert('上传成功');
        $('.submit').css({
            display: 'none'
        });
        $('.result').css({
            display: 'block'
        });
        res = res.slice(1);
        $('.preview').find('a').attr('href', '/downloadFile?filename=' + res)
        resultPreview();
    }).fail(function (res) {
        alert("上传失败！");
    });
}

function submitExcl() {
    $('.submit').click(function () {
        var url = $('.preview').text();
        if (url == "") {
            alert("还未选择文件");
        } else {
            //上传文件
            FileUpload();
        }
    });
}


function resultPreview() {
    $('.result').click(function () {
        var exclUrl = $('.preview').find('img').attr('src');
        window.open('/dataAnalyze?filename=' + exclUrl)
    })
}
