$(function () {
  setTimeout(function () {
    $.post({
      url: "/user",
      data: {name: "Casey", status: "cool"}
    });
  }, 3000);
});
