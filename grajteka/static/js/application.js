$(document).ready(function(){

  // Google code prettify
  // ====================

  prettyPrint();

  // Dropdown example for topbar nav
  // ===============================

  $("body").bind("click", function (e) {
    $('.dropdown-toggle, .menu').parent("li").removeClass("open");
  });
  $(".dropdown-toggle, .menu").click(function (e) {
    var $li = $(this).parent("li").toggleClass('open');
    return false;
  });

  //${"a").click(function (e) {
//	var $li = $(this).parent("li");
  //});
  //
  //
  var tabContainers = $('div.tab');
    
  $('ul.tabs a').click(function () {
	tabContainers.hide().filter(this.hash).show();
	$('ul.tabs a').parent("li").removeClass('active');
	$(this).parent("li").addClass('active');
	return false;
  }).filter(':first').click();


});

