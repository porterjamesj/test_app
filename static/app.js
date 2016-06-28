$(function () {
  setTimeout(function () {
    $.post({
      url: "/users",
      data: {name: "Casey", status: "cool"}
    });
  }, 3000);
});
