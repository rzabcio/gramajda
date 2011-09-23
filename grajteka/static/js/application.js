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

  var tabContainers = $('div.tab');
    
  $('ul.tabs a').click(function () {
	tabContainers.hide().filter(this.hash).show();
	$('ul.tabs a').parent("li").removeClass('active');
	$(this).parent("li").addClass('active');
	return false;
  }).filter(':first').click();


});

function boardgamesJsonToTable(data) {
	var items = [];
	$.each(data, function() {
		items.push('<tr>'
			+ '<td><a href=\"/boardgame/' + this.fields.meta + '/\">' + this.fields.meta + '</a></td>'
			+ '<td><a href=\"/user/' + this.fields.owner + '/\">' + this.fields.owner + '</a></td>'
			+ '<td><a href=\"/user/' + this.fields.patron + '/\">' + this.fields.patron + '</a></td>'
			+ '<td><a href=\"/user/' + this.fields.holder + '/\">' + this.fields.holder + '</a></td>'
			+ '</tr>');
	});
	return '<table class=\"zebra-striped\"><tbody><tr><th>Nazwa gry</th><th>Właściciel</th><th>Opiekun</th><th>Posiadający</th></tr>' + items + '</tbody></table>';
	//return '<table class=\"zebra-striped\"><tbody>' + items + '</tbody></table>';
}

