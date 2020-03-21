(function($) {

  //   /**
  //   * Copyright 2012, Digital Fusion
  //   * Licensed under the MIT license.
  //   * http://teamdf.com/jquery-plugins/license/
  //   *
  //   * @author Sam Sehnert
  //   * @desc A small plugin that checks whether elements are within
  //   *     the user visible viewport of a web browser.
  //   *     only accounts for vertical position, not horizontal.
  //   */

  $.fn.visible = function(partial) {

    var $t = $(this),
      $w = $(window),
      viewTop = $w.scrollTop(),
      viewBottom = viewTop + $w.height(),
      _top = $t.offset().top,
      _bottom = _top + $t.height(),
      compareTop = partial === true ? _bottom : _top,
      compareBottom = partial === true ? _top : _bottom;

    return ((compareBottom <= viewBottom) && (compareTop >= viewTop));

  };

})(jQuery);

var prevScrollpos = window.pageYOffset;

$(window).scroll(function(event) {

  $(".jpt-text").each(function(i, el) {
    var el = $(el);
    if (el.visible(true)) {
      el.addClass("animation-target");
    }
  });

  var currentScrollPos = window.pageYOffset;
  if (currentScrollPos == 0) {
    $("#navbar").css("top", "0px").css("background-color", "transparent");
  }
  else if (prevScrollpos > currentScrollPos) {
    $("#navbar").css("top", "0px").css("background-color", "#111111");
  }
  else {
    $("#navbar").css("top", "-90px");
  }
  prevScrollpos = currentScrollPos;


});
// -----------------------------------------

// Wrap every letter in a span
var textWrapper = document.querySelector('.jpt-promo');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({ loop: true })
  .add({
    targets: '.jpt-promo',
    translateX: [40, 0],
    translateZ: 0,
    opacity: [0, 1],
    easing: "easeInExpo",
    duration: 1200,
    delay: 100,
  }).add({
    targets: '.jpt-promo',
    translateX: [0, -30],
    opacity: [1, 0],
    easing: "easeOutExpo",
    duration: 1100,
    delay: 600,
  });

// -----------------------------------------


anime.timeline({ loop: true })
  .add({
    targets: '.circle-sm',
    opacity: [0, 1],
    easing: "easeInCirc",
    duration: 300,
  }).add({
    targets: '.circle-md',
    opacity: [0, 1],
    easing: "easeInCirc",
    duration: 300,
  }).add({
    targets: '.circle-lg',
    opacity: [0, 1],
    easing: "easeInCirc",
    duration: 300,
  }).add({
    targets: '.circle-xl',
    opacity: [0, 1],
    easing: "easeInCirc",
    duration: 300,
  }).add({
    targets: '.circle-sm',
    opacity: [1, 0],
    easing: "easeOutCirc",
    duration: 200,
    delay: 500,
  }).add({
    targets: '.circle-md',
    opacity: [1, 0],
    easing: "easeOutCirc",
    duration: 200,
  }).add({
    targets: '.circle-lg',
    opacity: [1, 0],
    easing: "easeOutCirc",
    duration: 200,
  }).add({
    targets: '.circle-xl',
    opacity: [1, 0],
    easing: "easeOutCirc",
    duration: 200,
  });


$(document).ready(function() {
  $(function() {
    $('[data-toggle="tooltip"]').tooltip()
  })
});
