$(function() {
  $("body").append(
    '<div class="lin-mask">\
        <div class="lin-alert">\
            <p><span class="iconfont icon-icon delete"></span></p>\
            <div class="lin-info">\
                <span class="iconfont icon-chenggong"></span>\
                <p class="alert-info"></p>\
            </div>\
            <div class="lin-con">\
            </div>\
        </div>\
    </div>'
  );
});

//包装器函数
(function($) {
  //定义一个according的插件名
  $.fn.according = function(options) {
    var settings = $.extend({}, { open: false }, options);
    return this.each(function() {
      var dts = $(this).children("dt");
      dts.click(onClick);
      dts.each(reset);
    });

    function onClick() {
      $(this)
        .siblings("dt")
        .each(hide);
      $(this)
        .next()
        .slideDown("fast");
      return false;
    }

    function hide() {
      $(this)
        .next()
        .slideUp("fast");
    }

    function reset() {
      $(this).next.hide();
    }
  };
})(jQuery);

//弹出框插件
$.extend({
  Myalert: function(data) {
    $(".lin-mask").css({
      height: "100%"
    });
    //判断是哪一种类型的弹出框
    if (data.type == "wanning") {
      $(".lin-con")
        .empty()
        .append('<a class="lin-cancel confirm wanning">确定</a>');
      $(".lin-info span").attr("class", "iconfont icon-jinggao wanning");
      $(".lin-info p").attr("class", "alert-info wanning");
      $(".lin-con").removeClass("lin-con-confirm");
    } else if (data.type == "success") {
      $(".lin-con")
        .empty()
        .append('<a class="confirm lin-sure success">确定</a>');
      $(".lin-info span").attr("class", "iconfont icon-chenggong success");
      $(".lin-info p").attr("class", "alert-info success");
      $(".lin-con").removeClass("lin-con-confirm");
    } else if (data.type == "confirm") {
      $(".lin-info span").attr("class", "iconfont icon-icon-test lin-confirm");
      $(".lin-info p").attr("class", "alert-info lin-confirm");
      $(".lin-con")
        .empty()
        .append(
          '<input type="button" class="lin-confirm delete lin-sure" value="确定">\
           <input type="button" class="lin-cancel wanning delete" value="取消">\
           '
        );
      $(".lin-con").addClass("lin-con-confirm");
    }

    //提示信息
    $(".lin-alert .alert-info").text(data.value);
    
    //弹出框下滑出现
    $(".lin-alert").css({
      margin: "150px auto",
      transition: "margin " + data.speed + "s",
      "-webkit-transition": "margin " + data.speed + "s",
      "-moz-transition": "margin " + data.speed + "s"
    });

    //点击叉弹出框消失
    $(".lin-alert .delete").click(function() {
      $(this)
        .parent()
        .parent()
        .css({
          margin: "-1500px auto"
        });
      $(".lin-mask").css({
        height: 0
      });
    });

    //点击确定弹出框消失
    $(".confirm").click(function() {
      $(this)
        .parent()
        .parent()
        .css({
          margin: "-1500px auto"
        });

      $(".lin-mask").css({
        height: 0
      });
    });

    //点击确定调用回调函数
    $(".lin-sure").click(function() {
      if (
        typeof data.confirm != "undefined" &&
        typeof data.confirm == "function"
      ) {
        data.confirm();
      }
    });

    $(".lin-cancel").click(function() {
      if (
        typeof data.cancel != "undefined" &&
        typeof data.cancel == "function"
      ) {
        data.cancel();
      }
    });
  }
});
