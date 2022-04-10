
function addRowCount(tableAttr) {
    $(tableAttr).each(function(){
        $('th:first-child, thead td:first-child', this).each(function(){
            var tag = $(this).prop('tagName');
            $(this).before('<'+tag+'>#</'+tag+'>');
        });
        $('td:first-child', this).each(function(i){
            $(this).before('<td>'+(i+1)+'</td>');
        });
    });
}
addRowCount('.js-serial');



