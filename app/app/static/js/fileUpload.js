$(function () {
    fileText();
    submitPic();
});

//图片上传
function submitPic() {
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

//验证图片上传是否合法
function fileText() {
    $(".uploadCom").on("change", "input[type='file']", function () {
        $('.picValid').text("");
        var filePath = $(this).val();
        if (filePath.indexOf("jpg") != -1 || filePath.indexOf("png") != -1 || filePath.indexOf("xls") != -1) {
            $('.preview').find('a').remove();
            $('.preview').append('<a href="/downloadFile" style="left: 50px" class="urls">' + filePath + '</a>');
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
        $(".urls").before('<img class="url" src=' + res + '>');
        alert('上传成功');
        $('.submit').attr("class", "edit cancel");
        $('.edit').val('点此处取消');
        res = res.slice(1);
        $('.preview').find('a').attr('href', '/downloadFile?filename=' + res)
    }).fail(function (res) {
        alert("上传失败！");
    });
}


//取消上传
function cancelUpload() {

}


//文件下载
// function fileDownload(filename) {
//     var data = {
//         data: JSON.stringify({
//             'url': filename,
//         })
//     };
//
//     $.ajax({
//         url: '/downloadFile',
//         type: 'POST',
//         data: data,
//         dataType: 'json',
//         success: function (res) {
//             res = eval(res);
//             console.log(res.ok);
//             if (res.ok == true) {
//                 root.css({
//                     "border-bottom": "1px solid #48aecb",
//                     "background-color": " #fff"
//                 });
//                 root.next().text('');
//             } else {
//                 root.next().text('用户不存在！');
//                 root.css({
//                     "border-bottom": "1px solid #f75234",
//                     "background-color": "#fdf6f5",
//                     "transition": 'border .8s'
//                 });
//             }
//         }
//     })
// }

