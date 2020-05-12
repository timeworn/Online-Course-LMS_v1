$(function() {
  console.log(location.pathname)
  $(`a[href^='${location.pathname}']`).addClass('active');
  $(`a[href^='${location.pathname}']`).parents('li:eq(0)').addClass('active');
});